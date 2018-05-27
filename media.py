import webbrowser


class Movie():
    """This class provides a way to store movie related information.

    Attributes:
        movie_title: a string that describes the title of the movie.
        movie_storyline: a string that describes and shortens the movie story.
        poster_image: a string, URL location of the poster image.
        trailer_youtube: a string, URL location of the trailer on
        youtube website.
        movie_rating: can be one of three
        valid ratings = ["G","PG","PG-13","R"].
        movie category: is the type of movie; horror, science fiction ...
        movie director: the name of the director.
        movie duration: must be in minutes.
    """

    def __init__(self, movie_title, movie_storyline, poster_image,
                 trailer_youtube, movie_rating, movie_category,
                 movie_director, movie_duration):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
        self.rating = movie_rating
        self.category = movie_category
        self.director = movie_director
        self.duration = movie_duration

    def show_info(self):
        """ it will take instances of class and print the information of it"""
        print ("Title: " + self.title)
        print ("Duration: " + self.duration)
        print ("Storyline: " + self.storyline)
        print ("Category: " + self.category)
        print ("Director: " + self.director)
        print ("Rating: " + self.rating)

    def show_trailer(self):
        """This function is used to open the trailer
        of instance in web browser"""
        webbrowser.open(self.trailer_youtube_url)
