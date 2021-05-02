from collections import Counter

def create_movie(title: str, genre: str, rating: float):
    if not title or not genre or not rating:
        return None
    return { "title":title, "genre":genre, "rating":rating }

def add_to_watched(user_data: dict, movie: dict):
    user_data["watched"].append(movie)
    return user_data

def add_to_watchlist(user_data: dict, movie: dict):
    user_data["watchlist"].append(movie)
    return user_data

def watch_movie(user_data: dict, title: str):
    watchlist_movie = first_movie_with_title(user_data["watchlist"], title)
    if (watchlist_movie):
        user_data["watched"].append(watchlist_movie)
        user_data["watchlist"].remove(watchlist_movie)
    return user_data

def first_movie_with_title(movies: list, title: str):
    does_movie_match_title = lambda movie: movie["title"] == title
    return next(filter(does_movie_match_title, movies), None)

def get_watched_avg_rating(user_data: dict):
    if not user_data["watched"]:
        return 0.0
    ratings = list(map(lambda movie: movie["rating"], user_data["watched"]))
    return sum(ratings) / len(ratings)

def get_most_watched_genre(user_data: dict):
    if not user_data["watched"]:
        return None
    genres = list(map(lambda movie: movie["genre"], user_data["watched"]))
    genre_counts = dict(Counter(genres))
    return max(genre_counts, key=genre_counts.get)

def get_unique_watched(user_data: dict):
    friends_watched = get_friends_watched_set(user_data["friends"])
    unique_movies = filter(lambda movie: movie not in friends_watched, user_data["watched"])
    return list(unique_movies)

# returns a list since the movie dicts are not hashable
def get_friends_watched_set(friends: list):
    watched = list(iter_friends_watched(friends))
    watched_set = {movie["title"]: movie for movie in watched}.values()
    return list(watched_set)

def iter_friends_watched(friends: list):
    for friend in friends:
        for movie in friend["watched"]:
            yield movie

def get_friends_unique_watched(user_data: dict):
    friends_watched = get_friends_watched_set(user_data["friends"])
    unique_movies = filter(lambda movie: movie not in user_data["watched"], friends_watched)
    return list(unique_movies)

def get_available_recs(user_data: dict):
    friends_unique_watched = get_friends_unique_watched(user_data)
    watchable = filter(lambda movie: movie["host"] in user_data["subscriptions"], friends_unique_watched)
    return list(watchable)

def get_new_rec_by_genre(user_data: dict):
    fav_genre = get_most_watched_genre(user_data)
    friends_unique_watched = get_friends_unique_watched(user_data)
    new_recs = filter(lambda movie: movie["genre"] == fav_genre, friends_unique_watched)
    return list(new_recs)

def get_rec_from_favorites(user_data: dict):
    friends_watched = get_friends_watched_set(user_data["friends"])
    fav_recs = filter(lambda movie: movie not in friends_watched, user_data["favorites"])
    return list(fav_recs)