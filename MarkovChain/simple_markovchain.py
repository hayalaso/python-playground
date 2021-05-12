import numpy as np
import random as rm

# The state space
states = ['Sleep','Icecream','Run']

# Possible transitions: 3x3
transitionName = [['SS','SI','SR'],
                  ['IS','II','IR'],
                  ['RS','RI','RR']]

# Transition Matrix
transitionMatrix = [[0.2,0.2,0.6],
                    [0.2,0.1,0.7],
                    [0.1,0.3,0.6]]

assert sum(transitionMatrix[0])+sum(transitionMatrix[1])+sum(transitionMatrix[2])==3,"Transition matrix is not normalized"

# Create a MC to forecast state/mood after N days

def activity_forecast(days):

    # Choose starting day:
    activityToday = 'Sleep'
    activityList = [activityToday]

    i = 0
    prob = 1.0

    while i!=days:
        if activityToday == 'Sleep':
            pchange = transitionMatrix[0]
            change = np.random.choice(transitionName[0],p=pchange)
            if change == 'SS':
                prob *=pchange[0]
                activityList.append('Sleep')
                pass
            elif change == 'SI':
                prob *= pchange[1]
                activityList.append('Icecream')
                activityToday = 'Icecream'
            else:
                prob *= pchange[2]
                activityList.append('Run')
                activityToday = 'Run'
        elif activityToday == 'Icecream':
            pchange = transitionMatrix[1]
            change = np.random.choice(transitionName[1],p=pchange)
            if change == 'IS':
                prob *=pchange[0]
                activityList.append('Sleep')
                activityToday = 'Sleep'
            elif change == 'II':
                prob *= pchange[1]
                activityList.append('Icecream')
                pass
            else:
                prob *= pchange[2]
                activityList.append('Run')
                activityToday = 'Run'
        elif activityToday == 'Run':
            pchange = transitionMatrix[2]
            change = np.random.choice(transitionName[2],p=pchange)
            if change == 'RS':
                prob *=pchange[0]
                activityList.append('Sleep')
                activityToday = 'Sleep'
            elif change == 'RI':
                prob *= pchange[1]
                activityList.append('Icecream')
                activityToday = 'Icecream'
            else:
                prob *= pchange[2]
                activityList.append('Run')
                pass
        i+=1

    return activityList

list_Activity = []
count = 0
# Do simulation
for i in range(100000):
    sim = activity_forecast(2)
    #print(len(sim))
    if sim[2] == 'Run':
        count +=1
    list_Activity.append(sim)

print("Probability of starting in state 'Sleep' and ending at state 'Run': {}".format(count/100000))
    

