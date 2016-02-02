__author__ = 'Walters954'

# Maps or dictionaries

favoriteMovies = {'Lego Movie': 10, 'Interstellar': 10, 'Memento': 10}

favoriteMovies['Lego Movie'] = 8
favoriteMovies['The Dark Knight'] = 10
favoriteMovies['The Grand Budapest Hotel'] = 10
favoriteMovies['Moonrise Kingdom'] = 10
favoriteMovies['Kung Fury'] = 1

del favoriteMovies['Moonrise Kingdom']
print(favoriteMovies)
# print(len(favoriteMovies))

if 'Moonrise Kingdom' in favoriteMovies:
    print('Moonrise Kingdom was a great movie 10 out of 10')
else:
    print('Are you a fool?')

if 'The Grand Budapest Hotel' not in favoriteMovies:
    print('Grand Budapest Hotel should be at the top of this movie list')
else:
    print('You need have made a wise decision')

for movie, rating in favoriteMovies.items():
    if rating <= 8:
        print(movie + ' this was a bad movie')
    else:
        print('%s is a great movie and the rating is %i' % (movie, rating))
