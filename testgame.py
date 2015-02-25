import scoringsystem

"""
Test cases for tenth frame outcomes
"""

player_list = []

michael = scoringsystem.PlayerScore("Michael")
player_list.append(michael)

lindsay = scoringsystem.PlayerScore("Lindsay")
player_list.append(lindsay)

gob = scoringsystem.PlayerScore("Gob")
player_list.append(gob)

buster = scoringsystem.PlayerScore("Buster")
player_list.append(buster)

tobias = scoringsystem.PlayerScore("Tobias")
player_list.append(tobias)

lucille = scoringsystem.PlayerScore("Lucille")
player_list.append(lucille)

#Fill up bowling score lists
for i in range(21):
    michael.throws[i]   = 0
    gob.throws[i]       = 2
    lindsay.throws[i]   = 3
    tobias.throws[i]    = 4
    buster.throws[i]    = 5 
    lucille.throws[i]   = 10

#Test last frame output  
michael.throws[18] = 9
michael.throws[19] = 1
michael.throws[20] = 6

gob.throws[18] = 3
gob.throws[19] = 7
gob.throws[20] = 10
  
lindsay.throws[18] = 10
lindsay.throws[19] = 5
lindsay.throws[20] = 1
  
tobias.throws[18] = 10
tobias.throws[19] = 6
tobias.throws[20] = 4
  
buster.throws[18] = 10
buster.throws[19] = 10
buster.throws[20] = 3
  
lucille.throws[18] = 10
lucille.throws[19] = 10
lucille.throws[20] = 10
  
#Prints from the list of players, and passes maximum length of name (unused)
scoringsystem.print_scores(player_list)
print

scoringsystem.register()