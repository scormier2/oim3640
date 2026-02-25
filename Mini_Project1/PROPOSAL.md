# My Project Proposal
# ____________________________________________________

# What I'm building:
 A weight loss planning calculator that helps users estimate:
 - Total pounds to lose
 - How many weeks it will realistically take
 - Recommended daily calorie intake to reach their goal

# Why I chose this:
-When I (or my friends) want to lose weight, it can be confusing to figure out:
# 1. How much weight we actually need to lose
# 2. How long it will realistically take
# 3. How many calories we should eat daily to reach that goal safely

 There’s a lot of random advice online, but not clear math-based guidance.
 This project will make weight loss into simple, understandable calculations.

# Core features:
 - Calculate total pounds to lose (current_weight - goal_weight)
 - Estimate timeframe in weeks based on 1–2 lbs per week
 - Calculate suggested daily calorie intake based on goal weight
 - Provide both conservative (1 lb/week) and faster (2 lbs/week) timelines
 - Include input validation to prevent unrealistic or unhealthy goals

# What I don’t know yet:
 - How to calculate calories more accurately using height, age,
   and activity level (BMR/TDEE formulas)

 - How to ensure calorie recommendations are medically safe

 - How to handle edge cases (goal weight > current weight,
   negative inputs, unrealistic targets, etc.)

 - Whether to include warnings for extreme weight loss goals

 - Whether to build it as a CLI program or simple web app