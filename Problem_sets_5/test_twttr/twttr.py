def main():
    user_input = input("Input: ")
    result = shorten(user_input)
    print("Output:", result)

def shorten(word):
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    return ''.join(letter for letter in word if letter not in vowels)

if __name__ == "__main__":
    main()
