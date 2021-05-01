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
    predicate = lambda movie: movie["title"] == title
    return next(filter(predicate, movies), None)