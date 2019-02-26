import random


#1
def box1(blue=2, white=3, trials=10000):
    """
    blue = 2\n
    white = 3\n
    trials = 10000\n
    return 3 prob:\n
    1.the first ball is blue and the second is white\n
    2.both balls are white\n
    3.second ball is blue
    """
    balls = []
    for i in range(blue):
        balls.append('blue')
    for i in range(white):
        balls.append('white')

    count1 = 0
    count2 = 0
    count3 = 0
    for i in range(trials):
        b1 = random.choice(balls)
        b2 = random.choice(balls)

        if b1 is 'blue' and b2 is 'white':
            count1 += 1
        elif b1 is 'white' and b2 is 'white':
            count2 += 1
        elif b2 is "blue":
            count3 += 1

    return count1 / trials, count2 / trials, count3 / trials

print(box1())


#2
def box2(blue=2, white=3, trials=10000):
    """
    blue = 2\n
    white = 3\n
    trials = 10000\n
    after the first ball drawn, it not returned to the box\n
    return 3 prob:\n
    1.the first ball is blue and the second is white\n
    2.both balls are white\n
    3.second ball is blue
    """
    count1 = 0
    count2 = 0
    count3 = 0
    for i in range(trials):
        balls = []
        for i in range(blue):
            balls.append('blue')
        for i in range(white):
            balls.append('white')

        b1 = random.choice(balls)
        balls.remove(b1)
        b2 = random.choice(balls)

        if b1 is 'blue' and b2 is 'white':
            count1 += 1
        elif b1 is 'white' and b2 is 'white':
            count2 += 1
        elif b2 is 'blue':
            count3 += 1

    return count1 / trials, count2 / trials, count3 / trials

print(box2())


#3
def prob_integers(digits=3, value=6):
    """
    digits - the number of digits in an positive integer\n
    value - common divisor\n
    return a prob that random chosen positive d-digit int is a multiple of v\n
    prob_integers(3, 6)\n
    prob_integers(4, 7)
    """
    count = 0
    for i in range(10000):
        temp = ""
        for i in range(digits):
            temp += str(random.randint(0, 9))

        if int(temp) % value == 0:
            count += 1

    return count / 10000

print(prob_integers())
print(prob_integers(4, 7))


#4
def tourament(wins_a=2, wins_b=0):
    """
    win_a - the number of games team A won\n
    win_b - the number of games team B won\n
    return the number of ways the tourament can be completed
    """
    if wins_a == 4 or wins_b == 4:
        # print(list([wins_a, wins_b]))
        return 1
    return tourament(wins_a + 1, wins_b) + tourament(wins_a, wins_b + 1)

print(tourament())
