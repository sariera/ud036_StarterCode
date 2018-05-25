# This is main file where we create the instances of Movie class
# and run the file to view the movie website page

# we have to import media where class Movie is defined and fresh_tomatoes python files
import fresh_tomatoes
import media

# Each instance has 8 arguments: Title, story line, poster image, trailer url, rating, category, director, duration
alien_covenant = media.Movie("Alien: Covenant",
                        "The crew of a colony ship, bound for a remote planet, discover an uncharted paradise with a threat beyond their imagination,"
                        "and must attempt a harrowing escape.",
                        "https://upload.wikimedia.org/wikipedia/en/3/33/Alien_Covenant_Teaser_Poster.jpg",
                        "https://www.youtube.com/watch?v=H0VW6sg50Pk",
                        "R",
                        "Science fiction horror",
                        "Ridley Scott",
                        "123 Minutes")

avatar = media.Movie("Avatar","A marine on an alien planet",
                     "http://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
                     "http://www.youtube.com/watch?v=5PSNL1qE6VY",
                     "PG-13",
                     "Epic science fiction",
                     "James Cameron",
                     "162 Minutes")

okja = media.Movie("Okja",
                   "A young girl named Mija risks everything to prevent a powerful, multi-national company from kidnapping her best friend,"
                   "a massive animal named Okja",
                   "https://upload.wikimedia.org/wikipedia/en/f/f6/Okja.png",
                   "https://www.youtube.com/watch?v=AjCebKn4iic",
                   "R",
                   "Action-Adventure",
                   "Bong Joon-ho",
                   "120 Minutes")

gonegirl = media.Movie("Gone Girl",
                   "A sad story",
                   "http://upload.wikimedia.org/wikipedia/en/0/05/Gone_Girl_Poster.jpg",
                   "http://www.youtube.com/watch?v=Ym3LB0lOJ0o",
                   "R",
                   "Crime",
                   "David Fincher",
                   "149 Minutes")

avenger = media.Movie("Avenger",
                   "A story about superheroes",
                   "http://upload.wikimedia.org/wikipedia/en/3/37/Captain_America_The_First_Avenger_poster.jpg",
                   "http://www.youtube.com/watch?v=hIR8Ar-Z4hw",
                   "PG-13",
                   "Action",
                   "Joss Whedon",
                   "143 Minutes")

dark_knight = media.Movie("Dark knight rises",
                   "A story about batman",
                   "http://upload.wikimedia.org/wikipedia/en/8/83/Dark_knight_rises_poster.jpg",
                   "http://www.youtube.com/watch?v=g8evyE9TuYk",
                   "PG-13",
                   "Action",
                   "Christopher Nolan",
                   "165 Minutes")


# Creating a list of all instances
movies = [alien_covenant, avatar, okja, gonegirl, avenger, dark_knight]

# Calling open_movies_page function to create fresh_tomatoes.html file which contains a movie web page
fresh_tomatoes.open_movies_page(movies)
