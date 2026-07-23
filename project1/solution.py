# Project 1 — Temperature Converter
# Author: Gul İfdal
# Date:   March 31, 2026
#
# Instructions:
#   1. Read the README.md in this folder first.
#   2. Fill in the missing lines below.
#   3. Test with: 0°C → 32°F | 100°C → 212°F | -40°C → -40°F

# ── Your solution goes here ───────────────────────────────────────────────────


celsius = float(input("Enter temperature in Celsius: "))


fahrenheit = (celsius * 9 / 5) + 32


print(f"{celsius}°C is equal to {fahrenheit:.2f}°F")

# ── Bonus (optional) ─────────────────────────────────────────────────────────
# Add a direction menu (C→F or F→C)

print("\nWould you like to do another conversion?")
print("1: Celsius to Fahrenheit")
print("2: Fahrenheit to Celsius")
choice = input("Your choice (1 or 2): ")

if choice == "1":
    c = float(input("Enter Celsius: "))
    f = (c * 9/5) + 32
    print(f"Result: {f} Fahrenheit")
elif choice == "2":
    f = float(input("Enter Fahrenheit: "))
    c = (f - 32) * 5/9
    print(f"Result: {c} Celsius")
else:
    print("Invalid choice!")
