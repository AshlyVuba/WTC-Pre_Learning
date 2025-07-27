def main():
    camelCase = input("Enter a camelCase name:").strip()

    snake_case = ''
    for char in camelCase:
        if char.isupper():
            snake_case += '_' + char.lower()
        else:
            snake_case += char
    print("camelCase:", camelCase)
    print("snake_case:", snake_case)

main()
