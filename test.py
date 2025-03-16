import os
import time
0.04



def animation():
    x=0
    for _ in range(3):
        for _ in range(25):
            animation = open(f"frame{x}.txt","r", encoding="utf-8").read()
            x=x+1
            print(animation)
            time.sleep(0.04)
            os.system("cls")
        x=0

animation()