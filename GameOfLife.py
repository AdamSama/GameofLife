'''
Name: game of life

@author: Yuexiang Liao


'''
import os
def game_of_life(file):
    life = open(file,'r')
    big_string = life.read()
    new_list=[]
    new_str_list=[]
    '''
    Because string is immutable, I put all the character
    from the string into a list called new_str_list
    '''
    line_list = big_string.split(os.linesep)
    for x in range(22):
        new_str_list.append('-')
    new_list.append(new_str_list)
    for line in line_list:     # add the the initial '-', the content and the last '-'s on each line
        new_str_list=[]
        new_str_list.append('-')
        for each in line:
            if each == '*':
                new_str_list.append(each)
            else:
                new_str_list.append('-')
        if len(line)<20:
            for x in range(len(line),20):
                new_str_list.append('-')
        new_str_list.append('-')
        new_list.append(new_str_list)
        '''
        In case we don't have file with 10 rows, we
        add rows into the file
        '''
    if len(line_list) < 10:
        for x in range(len(line_list),11):
            new_str_list=[]
            for x in range(22):
                new_str_list.append('-')
            new_list.append(new_str_list)

    return new_list

def number_of_living_around(row,col,line_list):
    num=0
    '''
    Here we decide how many neighbors are alive in the position r and c
    and we have to make sure the postion is not on the edge
    '''
    if (row in range(1,11)) and (col in range(1,21)):
        for i in range(row-1,row+2):
            for j in range(col-1,col+2):
                if line_list[i][j]=="*":
                    num+=1
    return num

def live_or_dead_in_next_generation(i,j,line_list):
    live_or_dead = False     
    if number_of_living_around(i,j,line_list) in range(3,5) and line_list[i][j]=='*':
        live_or_dead = True
    elif number_of_living_around(i,j,line_list) == 3 and line_list[i][j]!=' ':
        live_or_dead = True
    return live_or_dead #return whether the cell will live in the next generation

def next_generation_list(line_list):
    new_list=[]
    new_str_list=[]
    '''
    I create a new big list to hold next generation.
    And use the list new_str_list to hold the string as well.
    '''
    for x in range(22):
        new_str_list.append('-')
    new_list.append(new_str_list)
    for i in range(1,len(line_list)-1):
        new_str_list=['-']
        for j in range(1,len(line_list[i])-1):
            if live_or_dead_in_next_generation(i,j,line_list):
                new_str_list.append('*')
            else:
                new_str_list.append('-')
        new_str_list.append('-')
        new_list.append(new_str_list)
    new_str_list=[]
    for x in range(22):
        new_str_list.append('-')
    new_list.append(new_str_list)
    return new_list

def main(infile):
    '''This is the main function to run the program.
    '''
    life_line = game_of_life(infile)
    new_life=[]
    new_str=''
    for x in range(11):
        print("Generation "+str(x)+":"+'\n')
        for i in range(1,11):
            for j in range(1,21):
                new_str+=life_line[i][j]
            print(new_str)
            new_str=''
            print('\n')
        life_line = next_generation_list(life_line)
        print('\n'+"================================"+'\n')
if __name__ == 'main':  
    main("life.txt")
#number_of_living_around(2,2,game_of_life('life.txt'))
#game_of_life('life.txt')
#next_generation_list(game_of_life('life.txt'))


    
    
    
    
