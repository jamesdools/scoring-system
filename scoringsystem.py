# Bowling Scoring System for a technical assessment
# Programmed by James Dooley
import re
import sys

class PlayerScore(object):
    
    def __init__(self, name):
        self.name = name
        self.throws = [-1] * 21 #list holding each throw (plus bonus)
        self.frames = [0] * 10
        
    def __repr__(self):
        return "%s's score is %d" % (self.name, self.get_score())
    
    def reset(self): #used when wanted to play again
        self.throws = [-1] * 21
        self.frames = [0] * 10
        
    def get_score(self):
        score = 0    
        
        for i in xrange(0,20,2):
            
            frame_score = 0
            first_throw = self.throws[i]
            second_throw = self.throws[i+1]
                
            if i != 18: #If not in last frame
                
                if(first_throw == 10):
                    frame_score += 10
                    frame_score += self.strike_bonus(i)
                    
                elif(first_throw + second_throw == 10):
                    frame_score += 10 + self.spare_bonus(i)
                    
                else:
                    if(first_throw != -1 and second_throw != -1):
                        frame_score += first_throw + second_throw
            
            else: #If iterated to the last frame
                bonus_throw = self.throws[i+2]
                
                #If all ten knocked down in one or two goes, get bonus throw
                if(first_throw == 10 or first_throw + second_throw == 10):
                    frame_score += first_throw + second_throw + bonus_throw
                else:
                    if(first_throw != -1 and second_throw != -1):
                        frame_score += first_throw + second_throw
            
            #Add total score and frame score list            
            score += frame_score
            self.frames[i/2] = score     
            
        return score
        
    #Strike score at current frame
    def strike_bonus(self,throw_index):
        bonus_points = bonus_throws = 0
        hop = 1
        
        while bonus_throws < 2: #Next two throws from strike
            if throw_index + hop > 20: #Stops rolling off end of list
                return 0   
            if self.throws[throw_index+hop] == -1:
                hop += 1
            else:
                bonus_points += self.throws[throw_index+hop]
                bonus_throws += 1
                hop += 1 
                
        return bonus_points
    
    #Strike score at current frame
    def spare_bonus(self,throw_index):
        bonus_points = bonus_throws = 0
        hop = 2
        
        while bonus_throws < 1: #Next throw from spare
            if throw_index + hop > 20: #Stops rolling off end of list
                return 0
            if self.throws[throw_index+hop] == -1:
                hop += 1
            else:
                bonus_points += self.throws[throw_index+hop]
                bonus_throws += 1
                
        return bonus_points
        #End of class               

def print_scores(player_list):
    
    header = '{0:<10}|{1:^3}|{2:^3}|{3:^3}|{4:^3}|{5:^3}|{6:^3}|{7:^3}|{8:^3}|{9:^3}|{10:>3}| {11:>5}'\
    .format('Player', 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'Total') 
    head_width = len(header)
    
    print '\n', header
    
    for player in player_list:
        
        player.get_score()
        print '-' * head_width
        
        print ('{0:<10}|{1:>3}|{2:>3}|{3:>3}|{4:>3}|{5:>3}|{6:>3}|{7:>3}|{8:>3}|{9:>3}|{10:>3}| {11:>5}'
        .format(player.name[:10], symbol(player,0), symbol(player,2), symbol(player,4), symbol(player,6), symbol(player,8)
        ,symbol(player,10), symbol(player,12), symbol(player,14), symbol(player,16), symbol(player,18), ''))
       
        print ('{0:<10}|{1:>3}|{2:>3}|{3:>3}|{4:>3}|{5:>3}|{6:>3}|{7:>3}|{8:>3}|{9:>3}|{10:>3}| {11:>5}'
        .format('', frame_check(player,0), frame_check(player,1), frame_check(player,2), frame_check(player,3), frame_check(player,4)
        ,frame_check(player,5), frame_check(player,6), frame_check(player,7), frame_check(player,8), frame_check(player,9), player.get_score()))    

#For printing, checks whether frame has been played first        
def frame_check(player,frame_index):
    if player.throws[frame_index*2] == -1:
        return ''
    else:
        return player.frames[frame_index]
        
#For printing scores, returns suitable symbols for X, /, -
def symbol(player,throw_index):
    out = ''
    first = player.throws[throw_index]
    second = player.throws[throw_index+1]
    
    #If not printing for the last frame
    if throw_index != 18:

        if first == 10:
            out = 'X'
        elif first + second == 10:
            out = '%s %s' % (str(first), '/')
        else:
            out = '%s %s' % (str(first), str(second))
    
    #When printing for the last frame
    else:
        bonus = player.throws[throw_index+2]
        
        if first == 10:
            if second == 10:
                if bonus == 10:
                    out = 'XXX'
                else:
                    out = 'XX%s' % (str(bonus))
                    
            elif second + bonus == 10:
                out = 'X%s/' % (str(second))
            else:
                out = 'X%s%s' % (str(second),str(bonus))
        
        elif first + second == 10:
            if bonus == 10:
                out = '%s/X' % (str(first))
            else:
                out = '%s/%s' % (str(first),str(bonus))
        
        #If no spares or strikes rolled
        else:
            out = '%s %s' % (str(first), str(second))
            
    out = out.replace('0','-')
    out = out.replace('-1','') #Hides skipped throws (eg. after strike)
    
    return out
    #end of Class


def register():
    
    print "Welcome to Dools Bowling!"
    
    #Reading user input for the number of players
    prompt = raw_input("Please enter the number of players: ")
    while not(prompt.isdigit() and int(prompt) > 0 and int(prompt) < 7):
        prompt = raw_input("Invalid. Please enter between 1 and 6 players: ")
    number_of_players = int(prompt)
    
    #Create list of players
    player_list = []
            
    for i in range(number_of_players):
        name = (raw_input("Name of Player "+str(i+1)+ ": "))
        while (len(name) < 1 or len(name) >= 20 or re.match(r'[\d]', name)):
            name = str(raw_input("Invalid name. 20 character limit (no numbers). Name of Player "+str(i+1)+": "))
            
        player_list.append(PlayerScore(name))
    
    name_width = 0 #for scoreboard printing
    for p in player_list:
        name_width = max(name_width,len(p.name))
    
    play_game(player_list)


def play_game(player_list):
    
    #Checks that no more than 6 players are passed through    
    if len(player_list) > 6:
        player_list = player_list[:6]
    
    for p in player_list:
        p.reset()        
    #-----------------------
    #Game loop starts
    print_scores(player_list)
    
    for turn in range(10):
        
        for player in player_list:
            
            first = second = bonus = 0
            
            print "\n" + player.name + "'s turn"
            
            first_input = (raw_input("Enter first throw score: "))    
            while not(first_input.isdigit() and int(first_input) >= 0 and int(first_input) <= 10):
                first_input = (raw_input("Invalid. Please enter between 0 and 10: "))
            
            #Add first to score array       
            first = int(first_input)
            player.throws[turn*2] = first
            
            #Unless the last frame, strike ends the frame. If not a strike, ask for the second ball
            if first != 10 or turn == 9:
                second_input = (raw_input("Enter second throw score: "))
                
                #If strike on last frame, reset pins
                if turn == 9 and first == 10:
                    while not(second_input.isdigit() and int(second_input) >= 0 and int(second_input) <= 10):
                        second_input = (raw_input("Invalid. Please enter between 0 and 10: "))
                
                else:
                    while not(second_input.isdigit() and int(second_input) >= 0 and int(second_input) <= 10 - first):
                        second_input = (raw_input("Invalid. Please enter between 0 and " + str(10-first) + ": "))
                        
                #Add second to score array
                second = int(second_input)
                player.throws[turn*2+1] = second
             
            #Determines whether user gets the tenth frame bonus throw    
            if turn == 9 and first == 10 or turn == 9 and first + second == 10:
                bonus_input = (raw_input("Enter final bonus throw score: "))
                
                if first + second == 10 or second == 10:
                    while not(bonus_input.isdigit() and int(bonus_input) >= 0 and int(bonus_input) <= 10):
                        bonus_input = (raw_input("Invalid. Please enter between 0 and 10: "))
                
                else: #if not all ten pins are up
                    while not(bonus_input.isdigit() and int(bonus_input) >= 0 and int(bonus_input) <= 10 - second):
                        bonus_input = (raw_input("Invalid. Please enter between 0 and " + str(10-first) + ": "))        
                                    
                #Add bonus to score array
                bonus = int(bonus_input)
                player.throws[turn*2+2] = bonus
                
            #refresh scoreboard for next frame/player
            print_scores(player_list)

    #Game loop ends
    #-----------------------
    winner = ""
    top_score = 0
    for p in player_list:
        temp = p.get_score()
        if temp > top_score:
            top_score = temp
            winner = p.name    
    
    print "\n"+winner+" wins!"
    
    save = raw_input("Would you like to save this scoresheet? (Y or N): ")
    while not(save.upper() == 'Y' or save.upper() == 'N'):
        save = raw_input("Unrecognised. Please enter 'Y' for Yes or 'N' for no: ")
    if save.upper() == 'Y':
        save_scoresheet(player_list)
    
    again = raw_input("Would you like to play again? (Y or N): ")
    while not(again.upper() == 'Y' or again.upper() == 'N'):
        again = raw_input("Unrecognised. Please enter 'Y' for Yes or 'N' for no: ")
    if again.upper() == 'Y':
        play_game(player_list)
    elif again.upper() == 'N':
        print "Session finished. Come back again soon!"   
    #----------------------

#Saves final score sheet to text file, kludgy redirect
def save_scoresheet(player_list):
    default_std = sys.stdout
    f = open("scoresheet.txt","w")
    sys.stdout = f
    print_scores(player_list)    
    sys.stdout = default_std
    f.close()

if __name__ == '__main__':
    register()