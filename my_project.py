#RANDOM PICKER FOR ANIMEs TO BINGE

#import random
from random import choice

#create a list of animes that i want to watch
#sort the animes as nested lists and add other sub genres
anime = [['one piece', 'adventure', 'long', 'series'], ['fairy tail', 'fantasy', 'long', 'series'], ['black clover', 'fantasy', 'long', 'series'], ['anohana', 'drama', 'short', 'movie']]


#ask for user input on what type he want to watch (movie or series)
print('What do you want to watch a movie or a series?')
movieSeries = input()
list = []

#if movie get the index of nested movie list else get the series one
for type in anime:
    if type[3] == movieSeries:
        not list.append(type[0])    
#ask user about their mood


#get the index of a nested list depending on mood
#print the ANIME!
