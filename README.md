# Movie Trailer Website

The Movie Trailer Website displays box art imagery of my favorite movies.  By selecting one of the movie posters shown, the corresponding movie's trailer will be played in a separate pop-up window.  In addition, if the viewer likes the movie trailer, there is a web link underneath the movie title, which leads to the Amazon online store where the movie's DVD can be purchased.

## Prerequisites

The Movie Trailer Website consists of three Python files: fresh_tomatoes.py, media.py and entertainment_center.py.  In order for the website to operate properly, all three files must reside in the same directory on your computer.  The required Python files can be downloaded [here](https://github.com/pp7998/Movie_Trailer_Website).

## Python Files

#### fresh_tomatoes.py

This file contains starter code provided by Udacity to generate the HTML needed to display box art imagery for movies.  This is done via the **_open\__movies\__page()_** function, which accepts a list of the desired movies contained within  **entertainment_center.py**.  The starter code was slightly altered to create a link to the Amazon store for an option to purchase the movie DVD.

#### media.py

**_class Movie_** is created in this module and provides a way to store movie related information.  Currently, the movie information stored contains the title, the storyline and URL links to the movie poster, Youtube trailer and Amazon DVD.  The module can be further modified with any other related information for the movie.

#### entertainment_center.py

Two main tasks are executed within this file: creation of an instance of **_class Movie_** to store information for each favorite movie and a function call to **_open\__movies\__page()_** within **fresh_tomatoes.py** to generate the Movie Trailer Website HTML file.  

## Running the Application

It is expected that the user has Python installed.  If not already installed, Python can be downloaded [here](https://www.python.org).  As mentioned previously, all three Python files must reside in the same directory.  The application can be run using either the command line or the Python GUI.

Command Line:
1. Download Movie Website Project [here](https://github.com/pp7998/Movie_Trailer_Website).
2. Extract downloaded zip to a folder location on your local drive.
3. Open a terminal window and navigate to the folder location (i.e, **cd Movie_Trailer_Website-master**).
4. Type **python entertainment_center.py**.

GUI:
1. Download Movie Website Project [here](https://github.com/pp7998/Movie_Trailer_Website).
2. Extract downloaded zip to a folder location on your local drive.
3. Start IDLE (Python GUI).
4. Open **entertainment_center.py** in IDLE (File, Open and navigate to folder location).
5. In the menu bar, click on Run-->Run Module or press F5 on your keyboard.
