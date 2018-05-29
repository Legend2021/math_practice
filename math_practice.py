'''
Collection of Math Functions
'''

import matplotlib.pyplot as plt
#ALL EVEN NUMBERS

#Function: 2n
def even_to_nth(num):
    
    even_series = []
    [even_series.append(2*i) for i in range(1,num +1)]
    print(f'\nEven to Nth term \n {even_series}')

def odd_to_nth(num):
    odd_series = []
    [odd_series.append((2*i)-1) for i in range(1,num+1)]
    print(f'\nOdd to Nth term \n {odd_series}')
    
def make_matrix(row_,col_):
    mat = []
    [[mat.append([]),[[mat[j].append([])] for i in range(col_)]] for j in range(row_)]
    return mat

#TODO: FINISH
def warnsdorffs_rule(row_ ,col_, pos_x, pos_y):
    #SET UP THE RULES THAT MUST BE FOLLOWED
    # Move to the point with the least amount of available moves
    
    knight_moves = [(1,2),(1,-2),
                    (2,1),(2,-1),
                    (-1,2),(-1,-2),
                    (-2,1),(-2,-1)]
            
    board = make_matrix(row_,col_)
    #[print(knight_moves[i][0] + knight_moves[i][1]) for i in range(len(knight_moves))]
    #[board.append([]) for i in range(row_)]
    
    #[[board.append([]),[[board[j].append([])] for i in range(col_)]] for j in range(row_)]
    
    board[pos_x][pos_y].append(1)
    
    #[[board[pos_x - x][pos_y - y].append(0)] for (x,y) in knight_moves]
    [print(f'{board[i]}') for i in range(row_)]
    

changes = []

#TODO: (DONE) FIX THE LIST CREATIONa
def foxes_rabbits(
        prey_population_,
        pred_population_,
        generations = [],
        no_generations = False,
        generation_count = 100,
        prey_growth = 0.04,
        prey_factor = 0.0004,
        pred_diminish = 0.08,
        feed_rate = 0.0001
        ,phase_ = 0):
    
    pred_population = pred_population_
    prey_population = prey_population_
    prey_change = (prey_population_)*(prey_growth - (pred_population_*prey_factor))
    pred_change = (pred_population_)*((-pred_diminish) + (prey_population_*feed_rate))
    pred_population += pred_change
    prey_population += prey_change
    
    
    #[generation.append((pred_population,prey_population)) for i in range(generations)]
    #recursive?
    n = phase_ + 1
    if (n < generation_count or no_generations) and (pred_population > 0 and prey_population > 0):
        #print(f'{n}:\n PREY: {prey_population}\n PRED: {pred_population}')
        foxes_rabbits(
                prey_population, 
                pred_population,
                generations = generations,
                no_generations = no_generations,
                generation_count = generation_count,
                prey_growth = prey_growth,
                prey_factor = prey_factor,
                pred_diminish = pred_diminish,
                feed_rate = feed_rate,
                phase_ = n)
        generations.append((prey_population, pred_population))
        if n == 1:
            generations.append((prey_population_, pred_population_))
        #pred_population += pred_change
        #prey_population += prey_change
        #print(phase_)
    else:
        generations.append((prey_population, pred_population))
        #print(phase_)
        return True#(prey_population, pred_population)
    
    return True
        
    
    
#even_to_nth(4)
#odd_to_nth(4)
#warnsdorffs_rule(5,5,2,2)
foxes_rabbits(6000,80, no_generations = True,generation_count = 100,generations = changes)
#[print(test[i]) for i in range(len(test))]
#[print(f'phase {i}: {testing[i]}') for i in range(50)]
changes.reverse()
[print(f'phase {i}: {changes[i]}') for i in range(len(changes))]
test = make_matrix(3,4)

[print(f'{test[i]}') for i in range(len(test))]
