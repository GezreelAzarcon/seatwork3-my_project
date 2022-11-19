#RANDOM PICKER FOR ANIMEs TO BINGE
#import random
from random import choice

#create a list of animes that i want to watch
#sort the animes as nested lists and add other sub genres
from animelist import anime #The list is in anotehr file now!

#add lists for sorting to a random anime
list_genre = []
list_length = []
list_type = []



#ask user about the genre they want
#design genre ui
print()
print('======================================')
print('||     WHAT GENRE DO YOU WANT?      ||')
print('||----------------------------------||')
print('||          Shounen --> 1           ||')
print('||           Drama --> 2            ||')        #design added!
print('||       Slice of Life --> 3        ||')
print('||          Sports --> 4            ||')
print('======================================')
print()

#add input validation
while True:
    genre = input('Type here: ')
    if genre == '1' or genre == '2' or genre == '3' or genre == '4':
        break
    else: 
        print('Wrong input! Try again!')
        continue

print()
if genre == '1':
    genre = 'shounen'
elif genre == '2':
    genre = 'drama'
elif genre == '3':
    genre = 'slice of life'
elif genre == '4':
    genre = 'sports'

#for loop condition for sorting the type of genre
for type1 in anime:
    if type1[1] == genre:
        if type1[0] not in list_genre:
            list_genre.append(type1[0])

print(list_genre) #for testing

#ask user if they want a short or long series
#design 2nd input ui
print('======================================')
print('||      DO YOU WANT TO WATCH A      ||')
print('||     "SHORT" OR "LONG" ANIME?     ||')
print('======================================')
print()

#add input validation
while True:
    length = input('Type short/long: ')
    length = length.lower()
    if length == 'short' or length == 'long':
        break
    else:
        print('Wrong input! Try again!')
        continue

print()

#for loop condition for sorting if you want a short or long series
for type2 in anime:
    if type2[2] == length:
        if type2[0] in list_genre:
            list_length.append(type2[0])

print(list_length) #for testing

#ask for user input on what type he want to watch (movie or series)
#design 3rd input ui
print('======================================')
print('||   WHAT DO YOU WANT TO WATCH A    ||')
print('||       SERIES OR A MOVIE?         ||')
print('======================================')
print()

#add input validation
while True:
    movieSeries = input('Type series/movie: ')
    movieSeries = movieSeries.lower()
    if movieSeries == 'series' or  movieSeries == 'movie':
        break
    else:
        print('Wring input! Try again!')
        continue

print()
#for loop condition to sort movie or series
for type3 in anime:
    if movieSeries in type3[3]:
        if type3[0] in list_length:
            list_type.append(type3[0])

#print the ANIME!
animelists = (list_type)
print('======================================')
print('||   THE ANIME YOU WILL WATCH IS... ||')
print('======================================')
print()
print(choice(animelists))
print('======================================')
print()