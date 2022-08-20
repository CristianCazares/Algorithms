import os
os.system("clear||cls")

activities = [(0, 6), (1, 4), (2, 14), (3, 5), (4, 5), (5, 7), (5, 9), (6, 10), (8, 11), (8, 12), (12, 16)]

def isFeasible(selectedActs, newActIndex):
    #Algorithm to check if the time is overlapping:
    for act in selectedActs:
        earlierAct, laterAct = 0 , 0
        #look for the activity that starts first (earlierAct)
        if act[0] < activities[newActIndex][0]:
            earlierAct = act
            laterAct = activities[newActIndex]
        else:
            earlierAct = activities[newActIndex]
            laterAct = act
        
        #Chek if the one that started first, finished after the laterAct
        if earlierAct[1] >= laterAct[1]:
            activities[newActIndex] = None
            return False
    return True

def select(acts):
    #Algorithm to look for the activity with the least duration
    minAct = (float(0), float("inf"))
    minActPos = float("-inf")
    for i in range(len(acts)):
        if acts[i]:
            if acts[i][1] - acts[i][0] < minAct[1] - minAct[0]:
                minAct = acts[i]
                minActPos = i
    return minActPos
        
def checkNoneArray(arr):
    for i in arr:
        if i != None:
            return False
    return True

def greedy(acts):
    #GREEDY solution to get all non-overlapping activities with the minimun duration
    ResultActivitiesDurations = []
    ResultActivitiesIndex = []
    while not checkNoneArray(acts):
        x = select(acts)
        if isFeasible(ResultActivitiesDurations, x):
            ResultActivitiesDurations.append(acts[x])
            ResultActivitiesIndex.append(x)
            acts[x] = None

    return ResultActivitiesIndex, ResultActivitiesDurations

def main():
    
    results = greedy(activities)
    print("The activities with the least non-overlapping duration are:")
    for (i, act) in zip(results[0], results[1]):
        print(f'Activitie {i + 1}: {act[1] - act[0]} seconds ({act[0]}s to {act[1]}s)')

main()