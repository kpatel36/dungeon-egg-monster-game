#!/usr/bin/env python
# coding: utf-8

# 1. starting position = (0,0) or (2,2)
# 2. use up, down, left, right to move around board
# 3
# 
# "build walls at sides of board"
# if player_location == (x,0) and they try to go up -> not allowed
# if player_location == (x,4) and they try to go down -> not allowed
# if player_location == (0,x) and they try to go left -> not allowed
# if player_location == (3,x) and they try to go right -> not allowed 
# 
# except for door - once all eggs have been found 
# 
# while basket_on_board = True:
# 
# "find a mushroom to be invisible/immune to monster for 4 moves"
#     - will need a moves countdown "you have x amount of moves left with the cloak"
#     
#     
#  
# 
# KEY MOMENTS IN GAME
# 1. find basket first
# 	- start with basket on the board
# 	- while True = basket on board
# 	- while false = basket NOT on board, eggs can appear
# 2. once basket is found, eggs can appear on the board for player to gather
# 	- initiatte function to randomly allocate eggs onto places on board
# 3. player must gather all 3 eggs to exit door
# 4. can get "killed by monster"
# 	@ (3,4) 'uh-oh - you've been found!' - break out of loop
# 5. how to loop to start over
# 
# 
# def basket_found(basket_on_board):
# 
# 
# 1. create for loop to print out board in 5x5
# 
# 
# - what attributes and behaviors a player and monster would need?
# - behavior would be movement
# 
# - attributes for player class (b.c theyll need to interact with player and eggs) - includes names (baskets, eggs)
# 
# 

# In[ ]:


CELLS = [
    (0,0),(1,0),(2,0),(3,0),(4,0),
    (0,1),(1,1),(2,1),(3,1),(4,1),
    (0,2),(1,2),(2,2),(3,2),(4,2),
    (0,3),(1,3),(2,3),(3,3),(4,3),
    (0,4),(1,4),(2,4),(3,4),(4,4),]
col_0 = []
col_1 = []
col_2 = []
col_3 = []
col_4 = []
#print (col0, col1, col2, col3, col4)
for i in CELLS:
    if i[0] == 0:
        col_0.append(i)
    elif i[0] == 1:
        col_1.append(i)
    elif i[0] == 2: 
        col_2.append(i)
    elif i[0] == 3:
        col_3.append(i)
    elif i[0] == 4: 
        col_4.append(i)
columns =[col_0, col_1, col_2, col_3, col_4]

row_0 = []
row_1 = []
row_2 = []
row_3 = []
row_4 = []
for i in CELLS:
    if i[1] == 0:
        row_0.append(i)
    elif i[1] == 1:
        row_1.append(i)
    elif i[0] == 2: 
        row_2.append(i)
    elif i[1] == 3:
        row_3.append(i)
    elif i[1] == 4: 
        row_4.append(i)
rows =[row_0, row_1, row_2, row_3, row_4]

#for x in rows:
#    for tuple in x:
#        print ('SQUARE')
#print(board)


# In[3]:


# from IPython.display import clear_output
class Game:
    def __init__(self):
        self.CELLS = CELLS
    
    def drawMap(self):
    #    for cell in self.CELLS:
        pass
    
class Token:
    def __init__(self):
        self.basket_on_board = basket_on_board
        self.eggs_on_board = 3
        
    
class Player(Token):
    # start at (2,2) or (0,0)?
    pass

class Monster(Token):
    # once you figure out game, import random to generate random locations for eggs 
    pass

class Egg(Token):
    # how to make appear only once basket is picked up?
    ## while loop? while basket_on_board = True, eggs =0; once basket_on_board=False, eg
    # once you figure out game, import random to generate random locations for eggs 
    pass

    #def add_eggs():
        #self.eggs_on_board = 3
#player_location

#game_start:
#     player_location = (0,0)
#     basket_location = (0,1)

#class Basket(Token):
basket_location = (0,0)
def eggs_onto_board():
    #egg counter += "you have x amount of eggs in your basket and y amount to go to find the door"
    print ('eggs_onto_board is working')
    eggs_on_board = 3
    egg1 = (2, 0)
    egg2 = (3, 0)
    egg3 = (4, 0)
    egg_location_set = (egg1, egg2, egg3)
    while len(egg_location_set) > 0:
        if player_location == egg1:
            print('congrats! you\'ve found egg 1!')
            egg_location_set.remove(egg1)
            print(len(egg_location_set))
        elif player_location == egg2:
            print('congrats! you\'ve found egg 2!')
            egg_location_set.remove(egg2)
            print(len(egg_location_set))
        elif player_location == egg3:
            print('congrats! you\'ve found egg 3!')
            egg_location_set.remove(egg3)
            print(len(egg_location_set))
    else:
        print ('all eggs gone or somethings wrong')
#    return egg1 egg2 egg3 egg_location_set

def basket_pickup():
    basket_on_board = 1
    if player_location == basket_location:
        basket_on_board = 0
        print('You\'ve found your basket! Now collect the eggs')
        print ('activate the eggs')
        print ('also activate the monster')
    else:
        print ('somethings wrong')
    return basket_on_board
    
row_location = 1
column_location = 1
player_location = (row_location, column_location)

class Door(Token):
    #put against a wall - maybe @ (2,4)
    
    pass
#game_instance = Game()


egg1 = (2, 0)
egg2 = (3, 0)
egg3 = (4, 0)
egg_location_set = (egg1, egg2, egg3)
while len(egg_location_set) > 0:
    if player_location == egg1:
        print('congrats! you\'ve found egg 1!')
        egg_location_set.remove(egg1)
        print(len(egg_location_set))
    elif player_location == egg2:
        print('congrats! you\'ve found egg 2!')
        egg_location_set.remove(egg2)
        print(len(egg_location_set))
    elif player_location == egg3:
        print('congrats! you\'ve found egg 3!')
        egg_location_set.remove(egg3)
        print(len(egg_location_set))
else:
    print ('all eggs gone or somethings wrong')




#directions - could implement a while loop instead: "while i < 4" or "while i > 0 "? but is it needed\
game_in_play = True
while game_in_play:
    print (f'Starting Location: {player_location}')
#    print(basket_on_board)
    direction = (input('what direction would you like to go? \n')).lower()
#    if player_location == basket_location:
#        print('basket_pickup')
#    else:
#       continue
    #def player_movement():    
#     if basket_on_board == 1:
#         print ('basket still on board')
#     elif basket_on_board == 0:
#         print ('eggs on board')
#         print ('monster needs to go on board')
    if direction == 'up':
        if row_location == 0:
            print ('Sorry yov\'ve hit the upper wall of the room. Pick another direction')
            print (f' Current Location: {player_location}')
        else:
            row_location = row_location - 1
            player_location = (row_location, column_location)
            print ('you\'ve moved one space up')
            print (player_location)
            if player_location == basket_location:
                basket_pickup()
    elif direction == 'down':
        if row_location == 4:
            print ('Sorry yov\'ve hit the bottom wall of the room. Pick another direction')
            print (f' Current Location: {player_location}')
        else: 
            row_location = row_location + 1
            player_location = (row_location, column_location)
            print ('you\'ve moved one space down')
            print (player_location)
            if player_location == basket_location:
                basket_pickup()
    elif direction == 'left':
        if column_location == 0:
            print ('Sorry yov\'ve hit the left wall of the room. Pick another direction')
            print (f' Current Location: {player_location}')
        else: 
            column_location = column_location - 1
            player_location = (row_location, column_location)
            print ('you\'ve moved one space to the left')
            print (player_location)
            if player_location == basket_location:
                basket_pickup()            
    elif direction == 'right':
        if column_location == 4:
            print ('Sorry yov\'ve hit the right wall of the room. Pick another direction')
            print (f' Current Location: {player_location}')
        else: 
            column_location = column_location + 1
            player_location = (row_location, column_location)
            print ('you\'ve moved one space to the right')
            print (player_location)
            if player_location == basket_location:
                basket_pickup()
#    return column_location, row_location, player_location
else:
    print('game over')


# In[ ]:




