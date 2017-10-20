# ud036_StarterCode
Source code for a Movie Trailer website.

## Introduction

This programs contained in this repo will display movie information for several popular movies. This information displayed includes the movie title, a brief summary, poster image and trailer for the film. The movies to be displayed are generated from the entertainment_center_chris.py file. This file can be altered by the user and run inorder to display movies of their choice. 

## Download 

Download and unzip the file to a local directory. 

## Movie Class

The media.py file contains the Movie class, this class takes inputs: Title, Storyline, Poster Image URL, Trailer's Youtube URL. The entertainment_center_chris.py program uses this class to build objects that are utilized by the fresh_tomatoes.py program. 

## Updating Movies

In order to update the movies listed on the Movie Trailer website, the user will need to create a program similar to entertainment_center_chris.py. This program can be used as a template. The key aspects of this program show how to create movie objects and then run the fresh_tomatoes.py program with the movies they want displayed. Notice at the bottom of the entertainment_center_chris.py file, we have a line fresh_tomatoes.open_movies_page(movies), this is what calls the fresh_tomatoes program and tells it to open a movie page based on the movies provided. You will need to update the array of movies to contain the objects created earlier in the file. 

When creating new objects you will want to name your object after the title of the movie, using all lowercase letters. This should be set equal to media.Movie("Movie Title", "Description", "Movie Poster URL", "Youtube Trailer URL"). See example below.  

`fight_club = media.Movie("Fight Club",
                          "An insomniac office worker, looking for a way to change his life, crosses paths with a devil-may-care soap maker, forming an underground fight club that evolves into something much, much more.",
                          "https://upload.wikimedia.org/wikipedia/en/f/fc/Fight_Club_poster.jpg",
                          "https://www.youtube.com/watch?v=SUXWAEX2jlg")`


