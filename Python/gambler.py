import stdio
import sys
import random

stake = int(sys.argv[1])
goal = int(sys.argv[2])
trials = int(sys.argv[3])

bets = 0
wins = 0
for t in range(trials):
	cash = stake 
	while(cash > 0) and (cash < goal):
		bets += 1
		if random.randrange(0,2) == 0:
			cash +=1
		else:
			cash -= 1
			#stdio.write(str(bets) + ' ')
	if cash == goal:
		wins += 1
		#stdio.write(str(wins) + 'win')
stdio.writeln(str(100 * wins // trials) + '% wins')
stdio.writeln('Avg # bets: ' + str(bets // trials))
