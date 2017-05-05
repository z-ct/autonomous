import numpy as np
import time
from termcolor import colored

def calcBid(TL, TE, TB, RB, SSS):
    alpha1 = .65
    alpha2 = .1
    alpha3 = .25
    bid = 0
    if TL <= TE:
        return bid
    else:
        bid = ((alpha1*((TL - TE)/TL) + alpha2*(RB/TB) + alpha3*(SSS))/(alpha1 + alpha2 + alpha3))*RB
        return bid

class Car:
    def __init__(self, id, TL, TE, TB, RB, SSS):
        self.id = id
        self.TL = TL
        self.TE = TE
        self.TB = TB
        self.budget = RB
        self.SSS = SSS
        self.bid = calcBid(TL, TE, TB, RB, SSS)
        self.ledger = 0
        self.color = 'white'

    def compCar(self, other):
        #recalculate bids
        self.bid = calcBid(self.TL, self.TE, self.TB, self.budget, self.SSS)
        other.bid = calcBid(other.TL, other.TE, other.TB, other.budget, other.SSS)

        #self wins
        time.sleep(1)
        print(' *** car ', self.id, ' and car ', other.id, ' are bidding ***')
        print('car ', self.id, ' bids ', self.bid)
        print('car ', other.id, 'bids ', other.bid)
        if self.bid > other.bid:
            self.budget -= other.bid
            self.ledger -= other.bid
            self.color = 'green'
            string = ' ===> car ' + str(self.id) + ' wins!'
            print(colored(string, 'green'))
            string = ' ===> car ' + str(self.id) + ' pays: ' + str(other.bid)
            print(colored(string, 'green'))
            string = ' ===> car ' + str(self.id) + ' remaining budget is: ' + str(self.budget)
            print(colored(string, 'green'))
            print('\n')
            return self
        #other wins
        elif other.bid > self.bid:
            other.budget -= self.bid
            other.ledger -= self.bid
            other.color = 'green'
            string = ' ===> car ' + str(other.id) + ' wins!'
            print(colored(string, 'green'))
            string = ' ===> car ' + str(other.id) + ' pays: ' + str(self.bid)
            print(colored(string, 'green'))
            string = ' ===> car ' + str(other.id) + ' remaining budget is: ' + str(other.budget)
            print(colored(string, 'green'))
            print('\n')
            return other

class Road:
    def __init__(self, length, lanes):
        self.road = [[None for x in range(lanes)] for y in range(length)]
        self.length = length
        self.lanes = lanes

    def generate(self, nCars):
        idx = 0
        while idx < nCars:
            car = Car(idx, np.random.uniform(low=1.0, high = 10.0), 50)
            i, j = np.random.randint(low=0, high=self.length), np.random.randint(low=0, high=self.lanes)
            if self.road[i][j] is None:
                self.road[i][j] = car
                idx += 1
        print(self.road)

    def printRoad(self):
        for i in range(self.length):
            try:
                left = str(self.road[i][0].id)
                leftColor = self.road[i][0].color
            except:
                left = ' '
                leftColor = 'white'
            try:
                right = str(self.road[i][1].id)
                rightColor = self.road[i][1].color
            except:
                right = ' '
                rightColor = 'white'
            if len(right) == 1:
                right = ' ' + right
            if len(left) == 1:
                left = ' ' + left
            print('||',colored(left,leftColor),'|', colored(right,rightColor), '||')

            #reset colors
            if leftColor != 'white':
                self.road[i][0].color = 'white'
            if rightColor != 'white':
                self.road[i][1].color = 'white'

def runProg(road):
    leftOpen = False
    if road.road[0][0] is None:
            leftOpen = True
    for i in range(1, road.length):

        #check if both lanes are occupied
        if road.road[i][0] is not None and road.road[i][1] is not None:
            tempIDleft = road.road[i][0].id
            tempIDright = road.road[i][1].id
            winner = road.road[i][0].compCar(road.road[i][1])
            if winner.id == tempIDleft:
                #left car won make the position None
                road.road[i][0] = None
            else:
                #right car won make the position None
                road.road[i][1] = None


            #check if there is a car in the way in left lane and right lane open
            if road.road[i-1][0] is not None and road.road[i-1][1] is None:
                #move winner to the lane up 1 and to the right
                road.road[i-1][1] = winner
            #check if there is a car in the way in left lane and right lane open
            elif road.road[i-1][0] is None and road.road[i-1][1] is not None:
                #move winner to the lane up 1 and to the left
                road.road[i-1][0] = winner
        road.printRoad()
        print('\n')
    if not leftOpen:
        road.road[0][0] = None
    else:
        road.road[0][1] = None

def main():
    #TL, TE, TB, RB, SSS
    timeLeft = input("Type in your ETA: ")
    timeEvent = input("Type in the time until the event: ")
    totBudget = input("Type in the budget for the month: ")
    remBudget = input("Type in the remaining budget for the month: ")
    aggression = input("Type in the aggression: ")
    symbiote = input("Type in the Symbiote Stress Score: ")
    print('ALL PARAMETERS ACCEPTED')
    print('\n')
    print('\n')
    print('\n')
    print('\n')
    print('\n')

    road_length=20
    testRoad = Road(road_length, 2)
    testRoad.road[0][0] = Car(0, 6, 5, 100, 100, np.random.uniform(low=0.0, high = 1.0))
    counter = 1
    for i in range(1,road_length):
        testRoad.road[i][0] = Car(counter, 6, 5, 100, 100, np.random.uniform(low=0.0, high = 1.0))
        testRoad.road[i][1] = Car(counter+1, 6, 5, 100, 100, np.random.uniform(low=0.0, high = 1.0))
        counter += 2

    #set car 5 to something interesting
    testRoad.road[3][0] = Car('M', float(timeLeft), float(timeEvent), float(totBudget), float(remBudget), float(symbiote))


    print("Road intial state")
    print("=================")

    testRoad.printRoad()

    print('\n')

    while(True):
        runProg(testRoad)
        time.sleep(2)


if __name__ == "__main__":
    main()
