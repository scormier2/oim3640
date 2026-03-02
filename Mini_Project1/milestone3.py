# Weight Loss Planning Calculator - Milestone 3
# ============================================================
#
# so for milestone 3 the big goal was basically to make this
# thing actually feel GOOD to use, not just functional.
#
# like milestone 2 was solid — it worked, it validated input,
# it had a menu and a loop. but it felt kind of plain and robotic.
# you'd run it and it would just... spit numbers at you. no vibe.
#
# milestone 3 is where we gave it some personality 🎉
#
# the welcome screen now hits you with:
#   🎯 "Your transformation journey starts RIGHT NOW."
# instead of just "welcome to the calculator" lol
#
# the menu has emojis on every option — the rocket 🚀, the
# thinking face 🤔, the wave 👋 — so it feels more like an
# app and less like a school assignment
#
# the results screen is where it really pops off. instead of
# a dry table of numbers you get:
#
#   🏆  YOUR PERSONALIZED WEIGHT LOSS PLAN
#   💥  Total pounds to crush: 35.0 lbs
#   🐢  Steady pace  →  35.0 weeks
#   🚀  Beast mode   →  17.5 weeks
#   🥗  Daily calorie target: 1800 cal/day
#   💪🔥 YOU'VE GOT THIS. Every day counts!
#
# even the error messages are encouraging now — if you type
# letters instead of a number it says "Oops! you got this!"
# instead of just "invalid input." small thing but it matters
#
# the help screen also got some flavor — stuff like
#   ⛰️  "That's the mountain you're going to climb!"
#   🔥  "Respect the grind!"
#   🥗  "Feed your future self, not your current one."
#
# and the quit message? chef's kiss:
#   🏆  "Stay consistent, stay hungry, stay UNSTOPPABLE!"
#
# same exact code structure as m2 — same functions, same logic,
# same loop. we just made the text actually encourages 🔥



def get_float_input(prompt, min_val=1, max_val=2000):
    """Prompt the user for a float and validate the input."""
    while True:
        try:
            value = float(input(prompt))
            if value < min_val or value > max_val:
                print(f"  ⚠️  Hmm, that doesn't seem right! Please enter a value between {min_val} and {max_val}.")
            else:
                return value
        except ValueError:
            print("  ⚠️  Oops! That's not a number. Try something like 185 or 150.5 — you got this!")


def calculate_weight_loss(current_weight, goal_weight):
    """Return pounds to lose, weeks for each pace, and daily calories."""
    pounds_to_lose  = current_weight - goal_weight
    weeks_normal    = pounds_to_lose / 1          # 1 lb/week
    weeks_ambitious = pounds_to_lose / 2          # 2 lbs/week
    daily_calories  = goal_weight * 12
    return pounds_to_lose, weeks_normal, weeks_ambitious, daily_calories


def display_results(current, goal, pounds, weeks1, weeks2, calories):
    """Print the results in a clean, readable format."""
    print("\n" + "=" * 45)
    print("   🏆  YOUR PERSONALIZED WEIGHT LOSS PLAN")
    print("=" * 45)
    print(f"  Starting weight      : {current:.1f} lbs")
    print(f"  Dream goal weight    : {goal:.1f} lbs")
    print(f"  Total pounds to crush: {pounds:.1f} lbs  💥")
    print("-" * 45)
    print(f"  🐢  Steady pace (1 lb/week)  → {weeks1:.1f} weeks")
    print(f"  🚀  Beast mode  (2 lbs/week) → {weeks2:.1f} weeks")
    print("-" * 45)
    print(f"  🥗  Daily calorie target     : {calories:.0f} cal/day")
    print("=" * 45)
    print("  YOU'VE GOT THIS. Every day counts! 💪🔥")
    print("=" * 45 + "\n")


def run_calculator():
    """Collect input and run the weight loss calculation."""
    print("\n🌟 Let's build YOUR weight loss plan! 🌟")
    current = get_float_input("  What's your current weight (lbs)? ", min_val=50, max_val=2000)
    goal    = get_float_input("  What's your goal weight (lbs)?    ", min_val=50, max_val=2000)

    if goal >= current:
        print("\n  ⚠️  Whoops! Your goal weight needs to be LESS than your current weight.")
        print("      Dream bigger — you can do it! Try again. 💫\n")
        return

    pounds, weeks1, weeks2, calories = calculate_weight_loss(current, goal)
    display_results(current, goal, pounds, weeks1, weeks2, calories)


def show_menu():
    """Display the main menu and return the user's choice."""
    print("╔══════════════════════════════════════╗")
    print("║  💪 Weight Loss Planning Calculator ║")
    print("╠══════════════════════════════════════╣")
    print("║  1. Build my weight loss plan! 🚀   ║")
    print("║  2. How do these numbers work? 🤔   ║")
    print("║  3. Quit                       👋   ║")
    print("╚══════════════════════════════════════╝")
    return input("  Your choice (1-3): ").strip()


def show_info():
    """Print a short explanation of the formulas used."""
    print("\n" + "-" * 45)
    print("  🧠  HERE'S THE SCIENCE BEHIND YOUR PLAN:")
    print("-" * 45)
    print("  • Pounds to lose   = current weight - goal weight")
    print("    (That's the mountain you're going to climb! ⛰️)")
    print()
    print("  • Steady weeks     = pounds / 1  (1 lb/week)")
    print("    Slow and steady wins the race — and keeps it off!")
    print()
    print("  • Beast mode weeks = pounds / 2  (2 lbs/week)")
    print("    Max recommended pace — respect the grind! 🔥")
    print()
    print("  • Daily calories   = goal weight x 12")
    print("    Feed your future self, not your current one. 🥗")
    print("-" * 45 + "\n")


def main():
    """Main loop — keeps running until the user quits."""
    print("\n🎯 Welcome to the Weight Loss Planning Calculator! 🎯")
    print("   Your transformation journey starts RIGHT NOW.\n")

    while True:
        choice = show_menu()

        if choice == "1":
            run_calculator()
        elif choice == "2":
            show_info()
        elif choice == "3":
            print("\n  👋 See you on the other side of your goal!")
            print("     Stay consistent, stay hungry, stay UNSTOPPABLE! 🏆\n")
            break
        else:
            print("\n  ⚠️  Please enter 1, 2, or 3 — so close! Try again. 😄\n")


# ── Entry point ──────────────────────────────────────────────
if __name__ == "__main__":
    main()