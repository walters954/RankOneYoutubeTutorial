__author__ = 'Walters954'


########## classes ###############
class Movie:
    def __init__(self, title, year):
        self.__title = title
        self.year = year
        self.rating = 0

    def set_title(self, title):
        self.__title = title

    def get_title(self):
        return self.__title


movie_good = Movie('Lego Movie', 2014)
movie_bad = Movie('Sharknado', 1814)
movie_good.year = 1512
movie_bad.rating = 1
movie_good.set_title('Man of Steel')
print(movie_good.get_title(), movie_good.year, movie_good.rating)
print(movie_bad.get_title(), movie_bad.rating)
