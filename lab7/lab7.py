import random


def box1(blue=2, white=3, trials=10000):
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


# print(box1())


def box2(blue=2, white=3, trials=10000):
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


# print(box2())


def prob_integers(digits=3, value=6):
    count = 0
    for i in range(10000):
        temp = ""
        for i in range(digits):
            temp += str(random.randint(0, 9))

        if int(temp) % value == 0:
            count += 1

    return count / 10000


# print(prob_integers())
# print(prob_integers(4, 7))


def tourament(wins_a=2, wins_b=0):
    if wins_a == 4 or wins_b == 4:
        print(list([wins_a, wins_b]))
        return 1
    return tourament(wins_a + 1, wins_b) + tourament(wins_a, wins_b + 1)

# print(tourament())
