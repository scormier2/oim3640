# Input Validation — get_float_input() wraps every user input in a try/except block. If someone types "abc" or a nonsense number, it shows a warning and re-prompts instead of crashing.

# Organized Functions — The code is split into clean, single-purpose functions:

# get_float_input() – validated input
## Calculate_weight_loss() – all the math
## display_results() – formatted output
## run_calculator() – ties input + calc + display together
## show_menu() / show_info() – UI helpers
## main() – the loop controller

## Menu — Users see a 3-option menu every cycle: run a calculation, read an explanation of the formulas, or quit.

# Loop — The whole program runs in a while True loop inside main(), so users can calculate as many plans as they want without restarting. It only exits cleanly when they choose option 3.

# ============================================================
# Weight Loss Planning Calculator - Milestone 2
# Features: Input validation, organized functions, menu, loop
# ============================================================

def get_float_input(prompt, min_val=1, max_val=2000):
    """Prompt the user for a float and validate the input."""
    while True:
        try:
            value = float(input(prompt))
            if value < min_val or value > max_val:
                print(f"  ⚠  Please enter a value between {min_val} and {max_val}.")
            else:
                return value
        except ValueError:
            print("  ⚠  Invalid input. Please enter a number (e.g. 185 or 150.5).")


def calculate_weight_loss(current_weight, goal_weight):
    """Return pounds to lose, Number of weeks to loss weight Normal and ambitious, and daily calories."""
    pounds_to_lose = current_weight - goal_weight
    weeks_normal   = pounds_to_lose / 1          # 1 lb/week
    weeks_ambitious = pounds_to_lose / 2         # 2 lbs/week
    daily_calories = goal_weight * 12
    return pounds_to_lose, weeks_normal, weeks_ambitious, daily_calories


def display_results(current, goal, pounds, weeks1, weeks2, calories):
    """Print the results in a clean, readable format."""
    print("\n" + "=" * 45)
    print("        📋  YOUR WEIGHT LOSS PLAN")
    print("=" * 45)
    print(f"  Current weight      : {current:.1f} lbs")
    print(f"  Goal weight         : {goal:.1f} lbs")
    print(f"  Pounds to lose      : {pounds:.1f} lbs")
    print("-" * 45)
    print(f"  Normal pace (1 lb/week)   → {weeks1:.1f} weeks")
    print(f"  Ambitious pace (2 lbs/wk) → {weeks2:.1f} weeks")
    print("-" * 45)
    print(f"  Recommended daily calories: {calories:.0f} cal/day")
    print("=" * 45 + "\n")


def run_calculator():
    """Collect input and run the weight loss calculation."""
    print("\n--- Weight Loss Calculator ---")
    current = get_float_input("  Enter your current weight (lbs): ", min_val=50, max_val=2000)
    goal    = get_float_input("  Enter your goal weight (lbs)   : ", min_val=50, max_val=2000)

    if goal >= current:
        print("\n  ⚠  Your goal weight must be less than your current weight.\n")
        return

    pounds, weeks1, weeks2, calories = calculate_weight_loss(current, goal)
    display_results(current, goal, pounds, weeks1, weeks2, calories)


def show_menu():
    """Display the main menu and return the user's choice."""
    print("╔════════════════════════════════════╗")
    print("║   Weight Loss Planning Calculator  ║")
    print("╠════════════════════════════════════╣")
    print("║  1. Calculate my weight loss plan  ║")
    print("║  2. What do these numbers mean?    ║")
    print("║  3. Quit                           ║")
    print("╚════════════════════════════════════╝")
    return input("  Choose an option (1-3): ").strip()


def show_info():
    """Print a short explanation of the formulas used."""
    print("\n" + "-" * 45)
    print("  ℹ  How the numbers are calculated:")
    print("  • Pounds to lose  = current weight − goal weight")
    print("  • Normal weeks    = pounds ÷ 1  (1 lb lost/week)")
    print("  • Ambitious weeks = pounds ÷ 2  (2 lbs lost/week)")
    print("  • Daily calories  = goal weight × 12")
    print("    (A simple maintenance-level estimate)")
    print("-" * 45 + "\n")


def main():
    """Main loop — keeps running until the user quits."""
    print("\nWelcome to the Weight Loss Planning Calculator!")

    while True:
        choice = show_menu()

        if choice == "1":
            run_calculator()
        elif choice == "2":
            show_info()
        elif choice == "3":
            print("\n  Goodbye! Stay consistent and you'll reach your goal! 💪\n")
            break
        else:
            print("\n  ⚠  Please enter 1, 2, or 3.\n")


# ── Entry point ──────────────────────────────────────────────
if __name__ == "__main__":
    main()