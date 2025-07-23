def greeting():
    greeting = input("Enter a Greeting:").strip().lower()
    if greeting.startswith("hello"):
        return "$0"
    if greeting.startswith("h"):
        return "$20"
    else:
        return "$100"

print(greeting())