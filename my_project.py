#RANDOM PICKER FOR ANIMEs TO BINGE

#import random
from random import choice

#create a list of animes that i want to watch
#sort the animes as nested lists and add other sub genres
anime = [['one piece', 'adventure', 'long', 'series'], ['fairy tail', 'fantasy', 'long', 'series'], ['black clover', 'fantasy', 'long', 'series'], ['anohana', 'drama', 'short', 'movie']]


#ask for user input on what type he want to watch (movie or series)
print('What do you want to watch a movie or a series?')
movieSeries = input()
list_type = []
list_genre = []
#if movie get the index of nested movie list else get the series one
for type in anime:
    if type[3] == movieSeries:
        list_type.append(type[0])    

#ask user about the genre they want
print('What genre do you want?')
genre = input()

#get the index of a nested list depending on mood
for type1 in anime:
    if type1[1] == genre:
        if type1[0] in list_type:
            list_genre.append(type1[0])
            

#print the ANIME!
print(list2)