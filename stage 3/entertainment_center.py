import fresh_tomatoes
import media

toy_story = media.Movie("Toy Story", "A story of a boy and his toys that come to life", "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg", "https://www.youtube.com/watch?v=vwyZH85NQC4")

#print(toy_story.storyline)


avatar = media.Movie("Avatar", "A marine on an alien planet", "https://upload.wikimedia.org/wikipedia/id/b/b0/Avatar-Teaser-Poster.jpg", "https://www.youtube.com/watch?v=5PSNL1qE6VY")

#print(avatar.storyline)
#avatar.show_trailer()

warcraft = media.Movie("Warcraft", "A story from a famous game, World of Warcraft","https://upload.wikimedia.org/wikipedia/en/5/56/Warcraft_Teaser_Poster.jpg", "https://www.youtube.com/watch?v=2Rxoz13Bthc")

#warcraft.show_trailer()

movies = [toy_story, avatar, warcraft]
#fresh_tomatoes.open_movies_page(movies)
#print(media.Movie.VALID_RATINGS)


print(media.Movie.__doc__)
print(media.Movie.__name__)
print(media.Movie.__module__)










