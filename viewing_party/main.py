def create_movie(title, genre, rating):
    if not title or not genre or not rating:
        return None
    return { "title":title, "genre":genre, "rating":rating }