import webbrowser


class Movie():
    """This class provides a way to store movie related information

    The __init__ method may be documented in either the class level
    docstring, or as a docstring on the __init__ method itself.

    Either form is acceptable, but the two should not be mixed. Choose one
    convention to document the __init__ method and be consistent with it.

    Note:
        Do not include the `self` parameter in the ``Args`` section.

    Args:
        movie_title (str): Title of movie.
        movie_storyline (str): One-line summary of movie.
        poster_image (str): URL location of movie poster.
        trailer_youtube (str): URL location of movie trailer on YouTube.
        buy_movie (str): URL location of movie DVD on Amazon.

    Attributes:
	    title (str): Title of movie.
        storyline (str): One-line summary of movie.
        poster_image_url (str): URL location of movie poster.
        trailer_youtube_url (str): URL location of movie trailer on YouTube.
        buy_movie_url (str): URL location of movie DVD on Amazonself.
    """

    def __init__(self, movie_title, movie_storyline, poster_image,
                 trailer_youtube, buy_movie):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
        self.buy_movie_url = buy_movie
