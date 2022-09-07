import time
import random

counter = 0
Not = True

while Not == True:
    time.sleep(0.0001)
    counter += 1
    d20one = random.randrange(1, 21)
    d20two = random.randrange(1, 21)
    if d20one + d20two == 40:
        if counter > 1:
            print("It took " + str(counter) + " rolls")
        else:
            print("It took " + str(counter) + " roll")
        counter = 0
