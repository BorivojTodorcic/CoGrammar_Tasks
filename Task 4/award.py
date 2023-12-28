"""
Practical Task 1
"""


swimming = int(input("What was your completion time (in minutes) for the swimming race?: "))
cycling = int(input("What was your completion time (in minutes) for the cycling race?: "))
running = int(input("What was your completion time (in minutes) for the running race?: "))


total_time = swimming + cycling + running


if total_time <= 0:
    print("Please re-check your completion times and try again.")
elif total_time <= 100:
    print(f"You completed the triathlon in {total_time} minutes.\nYou have been awarded the Provincial Colours!")
elif total_time <= 105:
    print(f"You completed the triathlon in {total_time} minutes.\nYou have been awarded the Provincial Half Colours!")
elif total_time <= 110:
    print(f"You completed the triathlon in {total_time} minutes.\nYou have been awarded the Provincial Scroll!")
else:
    print(f"You completed the triathlon in {total_time} minutes.\nYou haven't been given an award.")

