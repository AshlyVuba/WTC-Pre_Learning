def deep():
    answer = input("What is the Answer to the Great Questions of Life, the Universe, and Everything?: ").lower().strip()
    if answer in ["42", "forty-two", "forty two"]:
        return "Yes"
    else:
        return "No"

print(deep())