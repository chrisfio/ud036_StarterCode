import media
import fresh_tomatoes

# Creating several Movie objects inorder to display in fresh_tomatoes program
the_martian = media.Movie(
    "The Martian",
    "An astronaut becomes stranded on Mars after his team assume him dead, "
    "and must rely on his ingenuity to find a way to signal to Earth that he "
    "is alive.",
    "https://upload.wikimedia.org/wikipedia/en/c/cd/The_Martian_film_poster.jpg",  # NOQA
    "https://www.youtube.com/watch?v=ej3ioOneTy8")

inside_out = media.Movie(
    "Inside Out",
    "After young Riley is uprooted from her Midwest life and moved to San "
    "Francisco, her emotions - Joy, Fear, Anger, Disgust and Sadness - "
    "conflict on how best to navigate a new city, house, and school.",
    "https://upload.wikimedia.org/wikipedia/en/0/0a/Inside_Out_%282015_film%29_poster.jpg",  # NOQA
    "https://www.youtube.com/watch?v=yRUAzGQ3nSY")

ex_machina = media.Movie(
    "Ex Machina",
    "A young programmer is selected to participate in a ground-breaking "
    "experiment in synthetic intelligence by evaluating the human qualities "
    "of a breath-taking humanoid A.I.",
    "http://www.joblo.com/timthumb.php?src=/posters/images/full/ex-machina-large.jpg&h=600&q=100",  # NOQA
    "https://www.youtube.com/watch?v=XYGzRB4Pnq8")

the_big_short = media.Movie(
    "The Big Short",
    "Four denizens in the world of high-finance predict the credit and "
    "housing bubble collapse of the mid-2000s, and decide to take on the big "
    "banks for their greed and lack of foresight.",
    "https://upload.wikimedia.org/wikipedia/en/e/e3/The_Big_Short_teaser_poster.jpg",  # NOQA
    "https://www.youtube.com/watch?v=vgqG3ITMv1Q")

chappie = media.Movie(
    "CHAPPIE",
    "In the near future, crime is patrolled by a mechanized police force. "
    "When one police droid, Chappie, is stolen and given new programming, he "
    "becomes the first robot with the ability to think and feel for himself.",
    "https://upload.wikimedia.org/wikipedia/en/7/71/Chappie_poster.jpg",
    "https://www.youtube.com/watch?v=lyy7y0QOK-0")

the_big_lebowski = media.Movie(
    "The Big Lebowski",
    "'The Dude' Lebowski, mistaken for a millionaire Lebowski, seeks "
    "restitution for his ruined rug and enlists his bowling buddies to help "
    "get it.",
    "https://upload.wikimedia.org/wikipedia/en/3/35/Biglebowskiposter.jpg",
    "https://www.youtube.com/watch?v=cd-go0oBF4Y")

the_shawshank_redeption = media.Movie(
    "The Shawshank Redemption",
    "Two imprisoned men bond over a number of years, finding solace and "
    "eventual redemption through acts of common decency.",
    "https://upload.wikimedia.org/wikipedia/en/8/81/ShawshankRedemptionMoviePoster.jpg",  # NOQA
    "https://www.youtube.com/watch?v=6hB3S9bIaco")

the_dark_knight = media.Movie(
    "The Dark Knight",
    "When the menace known as the Joker emerges from his mysterious past, he "
    "wreaks havoc and chaos on the people of Gotham, the Dark Knight must "
    "accept one of the greatest psychological and physical tests of his "
    "ability to fight injustice.",
    "https://upload.wikimedia.org/wikipedia/en/8/8a/Dark_Knight.jpg",
    "https://www.youtube.com/watch?v=EXeTwQWrcwY")

fight_club = media.Movie(
    "Fight Club",
    "An insomniac office worker, looking for a way to change his life, "
    "crosses paths with a devil-may-care soap maker, forming an underground "
    "fight club that evolves into something much, much more.",
    "https://upload.wikimedia.org/wikipedia/en/f/fc/Fight_Club_poster.jpg",
    "https://www.youtube.com/watch?v=SUXWAEX2jlg")


# Create array of movies to be displayed by fresh_tomatoes.py program
movies = [
    the_martian,
    inside_out,
    ex_machina,
    the_big_short,
    chappie,
    the_big_lebowski,
    the_shawshank_redeption,
    the_dark_knight,
    fight_club]

# Call fresh_tomatoes.py to create website and display moveis
fresh_tomatoes.open_movies_page(movies)
