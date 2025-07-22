def convert(str):
    str = input("Enter a greeting: Hello :), or Goodbye :( : ")
    if "Hello :) Goodbye :(":
        return "Hello 🙂 Goodbye 🙁"
    elif "Hello :)" in str:
        return "Hello 🙂"
    elif "Goodbye :(" in str:
        return "Goodbye 🙁"
    else:
        return "Invalid Greeting"
print(convert(str))