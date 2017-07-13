import sys
import recommendations as rec

pref= rec.loadMovieLens()

top_movie = 'Braveheart (1995)'
bottom_movie = 'Amityville II: The Possession (1982)'

top_movies = rec.calculateSimilarItems(1, pref, 5)
bottom_movies = rec.calculateSimilarItems(0, pref, 5)

print 'Best Recommended movies to watch based on ' + top_movie + ':'
print '---------------------------------------------------------------'
for movie in top_movies[top_movie]:
    print movie[1]
print '++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++'
print 'Least Recommended movies to watch based on ' + top_movie + ':'
print '---------------------------------------------------------------'
for movie in bottom_movies[top_movie]:
    print movie[1]
print '++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++'
print 'Best Recommended movies to watch based on ' + bottom_movie + ':'
print '---------------------------------------------------------------'
for movie in top_movies[bottom_movie]:
    print movie[1]
print '++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++'
print 'Least Recommended movies to watch based on ' + bottom_movie + ':'
print '---------------------------------------------------------------'
for movie in bottom_movies[bottom_movie]:
    print movie[1]
print '++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++'

