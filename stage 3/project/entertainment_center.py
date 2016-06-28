#################################################
#
# This code stores the movie information and URL.
# The class Movie is created in media.py
# The class requires title, short storyline,
# poster URL and Youtube trailer URL.
# The list of the class instances are then sent
# to fresh_tomatoes.py where it creates a nice
# looking website.
#
#################################################

import fresh_tomatoes
import media

#List of Movies

toy_story = media.Movie("Toy Story", 
			"A story of a boy and his toys that come to life", 
			"https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg", 
			"https://www.youtube.com/watch?v=vwyZH85NQC4")

avatar = media.Movie("Avatar", 
			"A marine on an alien planet", 
			"https://upload.wikimedia.org/wikipedia/id/b/b0/Avatar-Teaser-Poster.jpg", 
			"https://www.youtube.com/watch?v=5PSNL1qE6VY")

warcraft = media.Movie("Warcraft", 
			"A story from a famous game, World of Warcraft",
			"https://upload.wikimedia.org/wikipedia/en/5/56/Warcraft_Teaser_Poster.jpg", 
			"https://www.youtube.com/watch?v=2Rxoz13Bthc")

moneyball = media.Movie("Moneyball", 
			"The story of Oakland A's general manager Billy Beane's successful"
			"attempt to put together a baseball club on a budget by employing "
			"computer-generated analysis to draft his players.",
			"http://t3.gstatic.com/images?q=tbn:ANd9GcR3eulLm1bZDjmHRNAhiliPPusnt9RNpYzwknPFCBe5ATOx-cCJ",
			"https://www.youtube.com/watch?v=-4QPVo0UIzc")

mebeforeyou = media.Movie("Me Before You", 
			"love between a caregiver and a wealthy young banker left paralyzed from an accident",
			"http://t3.gstatic.com/images?q=tbn:ANd9GcR-Pi0mGMztx_eCHb3f7BrSiL0Gy_YfMk0Ef6WUSPx2KZ135n-a", 
			"https://www.youtube.com/watch?v=H4pEn72mPeM") 

starwars = media.Movie("Star Wars: The Force Awakens", 
			"War in space between the First Order and the Resistance, thirty years after the defeat of the Galactic Empire",
			"https://upload.wikimedia.org/wikipedia/en/a/a2/Star_Wars_The_Force_Awakens_Theatrical_Poster.jpg",
			"https://www.youtube.com/watch?v=sGbxmsDFVnE")	


movies = [toy_story, avatar, warcraft, moneyball, mebeforeyou, starwars]
fresh_tomatoes.open_movies_page(movies)