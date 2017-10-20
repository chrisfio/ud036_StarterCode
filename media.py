import webbrowser

class Movie():

    #initialization for Movie, allows it to take in title, story, image url and tailer url    
    def __init__(self, title, movie_storyline, poster_image, trailer_youtube):
        self.title = title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
