from collections import Counter

def create_movie(title: str, genre: str, rating: float):
    if not title or not genre or not rating:
        return None
    return { "title":title, "genre":genre, "rating":rating }

# Add the given movie to list found at user_data.watched
def add_to_watched(user_data: dict, movie: dict):
    return append_to_user_data(user_data, movie, "watched")

def add_to_watchlist(user_data: dict, movie: dict):
    return append_to_user_data(user_data, movie, "watchlist")

def append_to_user_data(user_data: dict, movie: dict, key: str):
    user_data[key].append(movie)
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
    user_watched = user_data["watched"]
    friends_watched = list(iter_friends_watched(user_data["friends"]))
    unique_movies = filter(lambda movie: movie not in friends_watched, user_watched)
    return list(unique_movies)

def iter_friends_watched(friends: list):
    for friend in friends:
        for movie in friend["watched"]:
            yield movie