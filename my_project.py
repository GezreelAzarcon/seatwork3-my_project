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
print('What genre do you want?')
genre = input()

#for loop condition for sorting the type of genre
for type1 in anime:
    if type1[1] == genre:
        if type1[0] not in list_genre:
            list_genre.append(type1[0])

#ask user if they want a short or long series
print('Do you want to watch a short or long series?')
length = input()

#for loop condition for sorting if you want a short or long series
for type2 in anime:
    if type2[2] == length:
        if type2[0] in list_genre:
            list_length.append(type2[0])
            
#ask for user input on what type he want to watch (movie or series)
print('What do you want to watch a movie or a series?')
movieSeries = input()

#for loop condition to sort movie or series
for type3 in anime:
    if movieSeries in type3[3]:
        if type3[0] in list_length:
            list_type.append(type3[0])





#print the ANIME!
print('blahblah')
print(list_type)