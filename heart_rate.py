age = int(input("Please enter your age: "))

highest_rate = 220 - age
slowest = highest_rate * 0.65
fastest = highest_rate * 0.85

print(f"When you exercise to strengthen your heart, you should keep your heart rate between {slowest:.0f} and {fastest:.0f} beats per minute.")