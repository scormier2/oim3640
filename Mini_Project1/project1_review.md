~Mini Project 1 code and check:
_________________________________________________________________________

# Did you use if __name__ == '__main__':? If not, add it!
# Did you use a list or dict? Where and why?
# If not, where could you? (e.g., storing results, counting, mapping inputs to outputs)
# Are your functions small and focused, or one giant block?
# Are your variable names clear to someone else?

# ✅ if __name__ == '__main__'
# Used correctly at the bottom as the entry point.


# ─── Lists or dicts used? ────────────────────
# Not explicitly, but the code would benefit from them.
# Good candidates:

# 1. A dict could map menu choices to functions,
#    replacing the if/elif chain in main():
menu_actions = {"1": run_calculator, "2": show_info}

# 2. A dict could store and return results from
#    calculate_weight_loss() instead of a 4-value tuple,
#    making the return value self-documenting:
return {
    "pounds_to_lose": ...,
    "weeks_normal": ...,
    "weeks_ambitious": ...,
    "daily_calories": ...,
}


# ✅ Are functions small and focused?
# Yes — this is one of the strongest aspects of the code.
# Each function does exactly one thing:
#   get_float_input     → validates
#   calculate_weight_loss → computes
#   display_results     → formats
# Nothing is crammed into a "god function."