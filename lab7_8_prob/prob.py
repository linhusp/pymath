import random
import time


def table(p1, p2, trials):
    t = []
    for i in range(trials):
        a = random.randint(1, p1 + p2)
        b = random.randint(1, p1 + p2)
        t.append([a, b])
    return t


def prob_draw(first, second, table, trials):
    count = 0
    for i in table:
        if i[0] in first and i[1] in second:
            count += 1
    return float(count) / trials


balls_table = table(2, 3, 10000)
blue = [1, 2]
white = [3, 4, 5]
trials = 10000
start_time = time.time()
print("prob [blue, white]: %s" % prob_draw(blue, white, balls_table, trials))
print("prob [white, white]: %s" % prob_draw(white, white, balls_table, trials))
print("prob [all, blue]: %s" % prob_draw(blue + white, blue, balls_table, trials))
print(time.time() - start_time)
