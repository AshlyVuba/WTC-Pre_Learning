def main():
    grocery_list = []

    print("Enter grocery items (Ctrl+D to stop):")
    try:
        while True:
            user_input = input().strip().lower()
            if user_input:
                grocery_list.append(user_input)
    except EOFError:
        pass

    print("\nGrocery List:")
    for item in sorted(set(grocery_list)):
        count = grocery_list.count(item)
        print(f"{count} {item.upper()}")

main()