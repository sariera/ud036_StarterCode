TITLE : Movie Trailer Website 
AUTHOR : Ali AlSariera
PYTHON VERSION : Python 2.7
PROJECT : A python file generating a html web page

Last update 5/25/2018

File contents: 
~ entertainment_center.py
~ media.py


About entertainment_Center.py:

	entertainment_center.py is a python applet that reads JSON data containing 
	information about several movies and converts that data into an HTML
	document that presents the titles, descriptions and poster images of
	the films in a responsive layout.

	Each title contains a link to the appropriate film's page on www.wekipedia.com
	and clicking the film poster launches a youtube player with the film's 
	theatrical trailer.


About media.py:

	Inside of it, start our Movie class with the following attributes:
        movie_title: a string that describes the title of the movie.
        movie_storyline: a string that describes and shortens the movie story.
        poster_image: a string, URL location of the poster image.
        trailer_youtube: a string, URL location of the trailer on youtube website.
        movie_rating: can be one of thre valid ratings = ["G","PG","PG-13","R"].
        movie category: is the type of movie; horror, science fiction ...
        movie director: the name of the director.
        movie duration: must be in minutes.


Instructions:

	Download files to a single directory and launch entertainment_center.py from
	the command line or running the program though a compiler, like IDLE.
