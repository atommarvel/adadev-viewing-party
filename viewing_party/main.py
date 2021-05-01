def create_movie(title:str, genre:str, rating:float):
    if not title or not genre or not rating:
        return None
    return { "title":title, "genre":genre, "rating":rating }

# Add the given movie to list found at user_data.watched
def add_to_watched(user_data: dict, movie: dict):
    user_data["watched"].append(movie)
    return user_data