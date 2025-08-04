from pyfiglet import Figlet
import sys
import random


def main():
    figlet = Figlet()
    fonts = figlet.getFonts()

    if len(sys.argv) == 1:
        font = random.choice(fonts)
    elif len(sys.argv) == 3 and sys.argv[1] in ["-f", "--font"]:
        font = sys.argv[2]
        if font not in fonts:
            sys.exit("Error: Invalid font name")
    else:
        sys.exit("Usage: python figlet.py [-f fontname]")
    figlet.setFont(font=font)
    user_input = input("Input:")
    print(figlet.renderText(user_input))


if __name__ == "__main__":
    main()
