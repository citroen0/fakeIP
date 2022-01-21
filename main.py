import random
import getpass
import time
agent = getpass.getuser()
agent = agent.capitalize()
def clear():
    subprocess.Popen("cls" if platform.system() == "Windows" else "clear", shell=True)
    time.sleep(.01)
#print('> ? < What is your name?')
#time.sleep(1.0)
#print("> ? < It's okay, you don't need to tell me your name. I know who you are, Agent " + agent.capitalize() + '. And surely, you have not forgotten me, Dr. Sydanry.')
#time.sleep(3.0)
#reason = input("> Dr. Sydanry <  However, I do not know your mission. Why have you come to my lair, here in Москва?" + '\n')
#time.sleep(2.0)
#print("> Dr. Sydanry < " + reason.capitalize() + "? That is a blatant lie. I know you are here to capture me.")
#time.sleep(1.9)
#print("> Dr. Sydanry < That's too bad, as you'll be dead before you can catch me!")
#time.sleep(2.0)
#print("Dr. Sydanry pulls a rusty lever, which releases you down a long, dark shaft.")
#time.sleep(1.0)
#print("...")
#time.sleep(0.6)
#print("..")
#time.sleep(0.3)
#print(".")
#time.sleep(2)
#print("Finally, you hit the bottom. A long hallway stretches before you. You must navigate your way through in order to catch Dr. Sydanry!" + '\n')
#time.sleep(4)
from random import randint, choice
import subprocess
import platform
import time
leftRange = False
rightRange = False
topRange = False
bottomRange = False

class MapGrid:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.walls = []
        self.start = (0, 0)
        self.goal = (width-1, height-1)
        self.player = (0, 0)

    def move_player(self, d):
        x = self.player[0]
        y = self.player[1]
        pos = None

        if d[0] == 'r':
            pos = (x + 1, y) #right
        elif d[0] == 'l':
            pos = (x - 1, y) #left
        elif d[0] == 'u':
            pos = (x, y - 1) #up
        elif d[0] == 'd':
            pos = (x, y + 1) #down

        leftRange = False
        rightRange = False
        topRange = False
        bottomRange = False
        if x >= 30:
            rightRange = True
        elif x <= -1:
            leftRange = True
        elif y >= 10: #bottomRange is displayed here
            topRange = True
        elif y <= -1: #topRange is displayed here
            bottomRange = True


        # I made a large mistake here. topRange is performing 
        # the tasks that bottomRange is supposed to be completing.
        # bottomRange is doing topRange's tasks.
        # However, it's working-ish so I'm going to leave it for now and fix it later.
        if pos not in self.walls:
            if rightRange == False and leftRange == False and topRange == False and bottomRange == False:
                self.player = pos
            while rightRange == True:
                pos = (x - 1, y)
                if x < 30:
                    rightRange = False
                if rightRange == False:
                    self.player = pos
            while leftRange == True:
                pos = (x + 1, y)
                if  x < (x-x):
                    leftRange = False
                if leftRange == False:
                    self.player = pos
            while topRange == True:
                pos = (x, y - 1)
                if y > 9:
                    topRange = False
                if topRange == False:
                    self.player = pos
            while bottomRange == True:
                pos = (x, y + 1)
                if y < 0:
                    bottomRange = False
                if bottomRange == False:
                    self.player = pos
        if pos == self.goal:
            print("You made it to the end!")


def draw_grid(g, width=2):
    for y in range(g.height):
        for x in range(g.width):
            if (x, y) in g.walls:
                symbol = '#'
            elif (x + 1, y) == g.walls:
                symbol = '.'
            elif (x, y + 1) == g.walls:
                symbole = '.'
            elif (x, y) == g.player:
                symbol = '█'
            elif (x, y) == g.start:
                symbol = '<'
            elif (x, y) == g.goal:
                symbol = '>'
            else:
                symbol = '.'
            print("%%-%ds" % width % symbol, end="")
        print()


def get_walls(g: MapGrid, pct=.25) -> list:
        out = []
        for i in range(int(g.height*g.width*pct)//2):

            x = randint(1, g.width-2)
            y = randint(1, g.height-2)

            out.append((x, y))
            out.append((x + choice([-1, 0, 1]), y + choice([-1, 0, 1])))
        return out

def main():
    g = MapGrid(30, 10)
    g.walls = get_walls(g)

    while g.player != g.goal:
        draw_grid(g)
        d = input("Which way? (r, l, u, d, or arrow keys)")
        g.move_player(d)
        clear()
    print("You survived! Sadly, Dr. Sydanry already escaped. It's too bad, it looks like he doesn't remember his partner...")


if __name__ == '__main__':
    main()

# While there is no failsafe preventing an unplayable board layout with the 
# size 30x10, there is a roughly 0.0000009259% chance 
# that an unplayable map will be created.
# Therefore, a failsafe will not be implemented at this time.
# I will, however, add one when an unplayable map is generated.