from fractions import Fraction
def main():
    while True:
        user_input = input("Fraction:")
        valid_chars = "0123456789/-"
        if any(ch not in valid_chars for ch in user_input):
            print("Invalid characters detected. Use digits and one '/'.")
            continue
        if user_input.count('/') != 1:
            print("Invalid input. Please enter a proper fraction like 3/4.")
            continue
        try:
            fraction = Fraction(user_input)
            if fraction.denominator == 0:
                print("Denominator can't be zero")
                continue

            if fraction < 0:
                print("Fraction can't be negative")
                continue

            if fraction.numerator >= fraction.denominator:
                print("Numerator can't be greater than Denominator")
                continue

            if fraction.numerator <= fraction.denominator:
                percentage = float(fraction) * 100
                if percentage <= 1:
                    print("E")
                elif percentage >= 99:
                    print("F")
                else:
                    print(f"Percentage:{round(percentage)}%")
                break

        except ValueError:
            print("Numerator can't be greater than Denominator")
        except ZeroDivisionError:
            print("Denominator can't be zero")


main()
