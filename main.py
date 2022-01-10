import random
import time
print('Is this your IP?')
time.sleep(3)
r = 0
while r == 0:
    i1 = random.randint(0,255)
    i2 = random.randint(0,255)
    i3 = random.randint(0,255)
    i4 = random.randint(0,255)
    s1 = str(i1)
    s2 = str(i2)
    s3 = str(i3)
    s4 = str(i4)
    i = s1 + '.' + s2 + '.' + s3 + '.' + s4
    print(i)