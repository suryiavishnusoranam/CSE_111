import math 
from datetime import datetime

w = float(input("Enter the width of the tire in mm: "))
a = float(input("Enter the aspect ratio of the tire: "))
d = float(input("Enter the diameter of the wheel in inches: "))
date_for_today = datetime.now()
v = math.pi * w ** 2 * a * (w * a + (2540 * d)) / 10000000000

print(f"The approximate volume is {v:.2f} liters")

with open("volumes.txt", "at") as volumes_files:
    print(f"{date_for_today:%Y-%m-%d}, {w:.0f}, {a:.0f}, {d:.0f}, {v:.2f}", file=volumes_files)

