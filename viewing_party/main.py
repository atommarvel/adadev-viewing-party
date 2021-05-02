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
    ratings = [movie["rating"] for movie in user_data["watched"]]
    return sum(ratings) / len(ratings)

def get_most_watched_genre(user_data: dict):
    if not user_data["watched"]:
        return None
    genres = [movie["genre"] for movie in user_data["watched"]]
    genre_counts = dict(Counter(genres))
    return max(genre_counts, key=genre_counts.get)

def get_unique_watched(user_data: dict):
    friends_watched = get_friends_watched_set(user_data)
    is_movie_unwatched_by_friends = lambda movie: movie not in friends_watched
    unique_movies = filter(is_movie_unwatched_by_friends, user_data["watched"])
    return list(unique_movies)

# returns a list since the movie dicts are not hashable
def get_friends_watched_set(user_data: dict):
    return list(iter_users_watched_unique(user_data["friends"]))

# a generator that iterates through every movie that every given user has watched but only yields movies with unique titles
def iter_users_watched_unique(users: list):
    yielded_titles = set()
    for user in users:
        for movie in user["watched"]:
            if (movie["title"] not in yielded_titles):
                yielded_titles.add(movie["title"])
                yield movie

def get_friends_unique_watched(user_data: dict):
    is_movie_unwatched_by_user = lambda movie: movie not in user_data["watched"]
    unique_movies = filter(is_movie_unwatched_by_user, iter_users_watched_unique(user_data["friends"]))
    return list(unique_movies)

def get_available_recs(user_data: dict):
    friends_unique_watched = get_friends_unique_watched(user_data)
    is_movie_available_in_user_subscriptions = lambda movie: movie["host"] in user_data["subscriptions"]
    watchable = filter(is_movie_available_in_user_subscriptions, friends_unique_watched)
    return list(watchable)

def get_new_rec_by_genre(user_data: dict):
    fav_genre = get_most_watched_genre(user_data)
    friends_unique_watched = get_friends_unique_watched(user_data)
    is_movie_in_users_fav_genre = lambda movie: movie["genre"] == fav_genre
    new_recs = filter(is_movie_in_users_fav_genre, friends_unique_watched)
    return list(new_recs)

def get_rec_from_favorites(user_data: dict):
    friends_watched = get_friends_watched_set(user_data)
    is_movie_unwatched_by_friends = lambda movie: movie not in friends_watched
    fav_recs = filter(is_movie_unwatched_by_friends, user_data["favorites"])
    return list(fav_recs)