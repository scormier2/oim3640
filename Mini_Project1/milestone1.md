# Protoype
# ___________________________________________________________________________________________

# Goal:Build the most basic version of a weight loss calculator.

# Step-by-step flow:
1)Ask the user for their current weight
2)Ask the user for their goal weight
3)Calculate total pounds to lose
4)current weight − goal weight
5)Calculate number weeks to lose weight
6)Weight divided by lose pounds (1 Ib or 2 Ib per week)
7)Calculate calories to eat a day
8)goal weight times 12 is daily calories

9)Display the results

10)Done

# Outline:

    - Pounds to lose
    - Weeks (1 lb/week)
    - Weeks (2 lbs/week)
    - Daily calorie estimate

# Goal:
 - Program runs
 - Takes user input
 - Uses at least one function

 # Simple Weight Loss Planner

# Ask for input
current = float(input("Current weight (lbs): "))
goal = float(input("Goal weight (lbs): "))

# Calculate pounds to lose
loss = current - goal

# Calculate weeks
weeks1 = loss
weeks2 = loss / 2

# Calculate daily calories
calories = goal * 12

# Show results
print("Pounds to lose:", loss)
print("Weeks (1 lb per week):", weeks1)
print("Weeks (2 lbs per week):", weeks2)
print("Daily calories:", calories)