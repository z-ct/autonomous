import numpy as np
import time
class Car:
    def __init__(self, id, bid, budget):
        self.id = id
        self.bid = bid
        self.budget = budget
        self.ledger = 0

    def compCar(self, other):
        #self wins
        time.sleep(1)
        print(' *** car ', self.id, ' and car ', other.id, ' are bidding ***')
        print('car ', self.id, ' bids ', self.bid)
        print('car ', other.id, 'bids ', other.bid)
        if self.bid > other.bid:
            self.budget -= other.bid
            self.ledger -= other.bid
            print(' ===> car', self.id, 'wins!')
            print('\n')
            return self
        #other wins
        elif other.bid > self.bid:
            other.budget -= self.bid
            other.ledger -= self.bid
            print(' ===> car', other.id, 'wins!')
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
            except:
                left = ' '
            try:
                right = str(self.road[i][1].id)
            except:
                right = ' '
            if len(right) == 1:
                right = ' ' + right
            if len(left) == 1:
                left = ' ' + left
            print('||',left,'|', right, '||')


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
        # print('***********')
    if not leftOpen:
        road.road[0][0] = None
    else:
        road.road[0][1] = None
    # road.printRoad()

def main():
    road_length=20
    testRoad = Road(road_length, 2)
    testRoad.road[0][0] = Car(0, np.random.uniform(low=1.0, high = 10.0), 50)
    counter = 1
    for i in range(1,road_length):
        testRoad.road[i][0] = Car(counter, np.random.uniform(low=1.0, high = 10.0), 50)
        testRoad.road[i][1] = Car(counter+1, np.random.uniform(low=1.0, high = 10.0), 50)
        counter += 2

    print("Road intial state")
    print("=================")

    testRoad.printRoad()

    print('\n')
    
    while(True):
        runProg(testRoad)
        time.sleep(2)



if __name__ == "__main__":
    main()

