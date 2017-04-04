import sys
from operator import itemgetter

if len(sys.argv) < 4:
        print "Usage: python findtopbottom343.py <closest_3_users> <ratings_file> <films_file>"
        print "e.g: python findtopbottom343.py closest3users.txt u.data u.item"
        exit()

users = []
ratings = []
films = []
fh_output = open('topbottom343.txt', 'w')

with open(sys.argv[1]) as users_input:
        for line in users_input:
                users.append(line.split('|'))

with open(sys.argv[2]) as ratings_input:
        for line in ratings_input:
                ratings.append(line.split('\t'))

with open(sys.argv[3]) as films_input:
        for line in films_input:
                films.append(line.split('|'))
first_user_ratings = []
second_user_ratings = []
third_user_ratings = []

i = 0
for user in users:
	i = i+1
	for rating in ratings:
		if (user[0] == rating[0]):
			if (i==1):
				first_user_ratings.append(rating)
			if (i==2):
				second_user_ratings.append(rating)
			if (i==3):
				third_user_ratings.append(rating)

first_user_ratings = sorted(first_user_ratings , key=itemgetter(2))
second_user_ratings = sorted(second_user_ratings , key=itemgetter(2))
third_user_ratings = sorted(third_user_ratings , key=itemgetter(2))

######## First user top and bottom films #########

first_user_bottom = []
first_user_top = []

for i in range(0,3):
	first_user_bottom.append(first_user_ratings[i]) 

for i in range(len(first_user_ratings)-3, len(first_user_ratings)):
	first_user_top.append(first_user_ratings[i])

film_first_bottom = []
for rat in first_user_bottom:
	film_first_bottom.append(rat[1])

film_first_top = []
for rat in first_user_top:
        film_first_top.append(rat[1])

fh_output.write('First User id: ' + first_user_ratings[0][0])
fh_output.write('\n******************\n')

fh_output.write('Top 3 films:')
fh_output.write('\n--------------\n')

for film in film_first_top:
	for movie in films:
		if (film == movie[0]):
			fh_output.write(movie[1] + '\n')

fh_output.write('--------------------------------------------\n')
fh_output.write('Bottom 3 films:')
fh_output.write('\n-----------------\n')

for film in film_first_bottom:
        for movie in films:
                if (film == movie[0]):
                        fh_output.write(movie[1] + '\n')

fh_output.write('*****************************************************\n')

######## Second user top and bottom films #########

second_user_bottom = []
second_user_top = []

for i in range(0,3):
        second_user_bottom.append(second_user_ratings[i])

for i in range(len(second_user_ratings)-3, len(second_user_ratings)):
        second_user_top.append(second_user_ratings[i])

film_second_bottom = []
for rat in second_user_bottom:
        film_second_bottom.append(rat[1])

film_second_top = []
for rat in second_user_top:
        film_second_top.append(rat[1])

fh_output.write('Second User id: ' + second_user_ratings[0][0])
fh_output.write('\n******************\n')

fh_output.write('Top 3 films:')
fh_output.write('\n--------------\n')

for film in film_second_top:
        for movie in films:
                if (film == movie[0]):
                        fh_output.write(movie[1] + '\n')

fh_output.write('--------------------------------------------\n')
fh_output.write('Bottom 3 films:')
fh_output.write('\n-----------------\n')

for film in film_second_bottom:
        for movie in films:
                if (film == movie[0]):
                        fh_output.write(movie[1] + '\n')

fh_output.write('*****************************************************\n')


######## Third user top and bottom films #########

third_user_bottom = []
third_user_top = []

for i in range(0,3):
        third_user_bottom.append(third_user_ratings[i])

for i in range(len(third_user_ratings)-3, len(third_user_ratings)):
        third_user_top.append(third_user_ratings[i])

film_third_bottom = []
for rat in third_user_bottom:
        film_third_bottom.append(rat[1])

film_third_top = []
for rat in third_user_top:
        film_third_top.append(rat[1])

fh_output.write('Third User id: ' + third_user_ratings[0][0])
fh_output.write('\n******************\n')

fh_output.write('Top 3 films:')
fh_output.write('\n--------------\n')

for film in film_third_top:
        for movie in films:
                if (film == movie[0]):
                        fh_output.write(movie[1] + '\n')

fh_output.write('--------------------------------------------\n')
fh_output.write('Bottom 3 films:')
fh_output.write('\n-----------------\n')

for film in film_third_bottom:
        for movie in films:
                if (film == movie[0]):
                        fh_output.write(movie[1] + '\n')

fh_output.write('*****************************************************\n')


