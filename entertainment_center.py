import fresh_tomatoes
import media
#import re

# Six instances of the class Movie from within the module media, each instance representing one of my favorite movies.

notting_hill = media.Movie("Notting Hill", "The owner of a bookstore develops a romantic, but tumultuous relationship with a famous actress", "https://vignette.wikia.nocookie.net/scratchpad/images/1/1e/Notting_Hill_%281999%29_Poster.png/revision/latest?cb=20171121022311", "https://www.youtube.com/watch?v=4RI0QvaGoiI", "https://www.amazon.com/Notting-Collectors-Universal-Studios-Michell/dp/B01GWCG922/ref=sr_1_1?ie=UTF8&qid=1541794824&sr=8-1&keywords=notting+hill+dvd")
blue_streak = media.Movie("Blue Streak", "After serving his prison sentence, a jewel thief attempts to recover a hidden gem from inside a police station", "https://upload.wikimedia.org/wikipedia/en/a/ab/Blue_Streak_film_poster.jpg", "https://www.youtube.com/watch?v=kj5NHXDvKKM", "https://www.amazon.com/Blue-Streak-Crystal-Chappell/dp/B00003GPFT/ref=sr_1_3?ie=UTF8&qid=1541794960&sr=8-3&keywords=blue+streak+dvd")
usual_suspects = media.Movie("The Usual Suspects", "A con man tells an investigator the story of events leading up to a massacre on a docked ship", "https://i.redd.it/o7h3v0gonb101.jpg", "https://www.youtube.com/watch?v=oiXdPolca5w", "https://www.amazon.com/Usual-Suspects-Bryan-Singer/dp/B01M5JFHWP/ref=sr_1_1?ie=UTF8&qid=1541795022&sr=8-1&keywords=usual+suspects+dvd")
black_panther = media.Movie("Black Panther", "After the king dies, his son battles a new challenger for the right to lead the people of Wakanda into a new era", "https://vignette.wikia.nocookie.net/marvelcinematicuniverse/images/f/fa/Black_Panther_Poster_October_2017.jpg/revision/latest?cb=20171016144626", "https://www.youtube.com/watch?v=x02xX2dv6bQ", "https://www.amazon.com/Black-Panther-Chadwick-Boseman/dp/B079FLYB41/ref=sr_1_1?ie=UTF8&qid=1541795053&sr=8-1&keywords=black+panther+dvd")
sweet_home_alabama = media.Movie("Sweet Home Alabama", "A socialite returns home to finalize her divorce so she can then marry a politician", "https://vignette.wikia.nocookie.net/theflophouse/images/1/1e/Sweet-Home-Alabama.jpg/revision/latest?cb=20151212022112", "https://www.youtube.com/watch?v=BM89EgWx_Gs", "https://www.amazon.com/Sweet-Home-Alabama-Reese-Witherspoon/dp/B00007E2F5/ref=sr_1_1?ie=UTF8&qid=1541795096&sr=8-1&keywords=sweet+home+alabama+dvd")
matrix = media.Movie("The Matrix", "A computer programmer learns the true nature of reality and rebels against the machines that are in control", "https://vignette.wikia.nocookie.net/matrix/images/e/e6/The_matrix_poster.jpg/revision/latest?cb=20060806212624", "https://www.youtube.com/watch?v=vKQi3bBA1y8", "https://www.amazon.com/Matrix-Keanu-Reeves/dp/B00000K19E/ref=sr_1_3?ie=UTF8&qid=1541795131&sr=8-3&keywords=the+matrix+dvd")

# List of my favorite movies (instances of class Movie), used as input to the open_movies_page function witin the module fresh_tomatoes. 

movies = [notting_hill, blue_streak, usual_suspects, black_panther, sweet_home_alabama, matrix]

# Function call to create fresh_tomatoes webpage, which shows poster image of my favorite movies and can play movie's trailer.

fresh_tomatoes.open_movies_page(movies)

