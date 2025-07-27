def main(): 
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    user_input = input("Input: ")

    output = ''.join(letter for letter in user_input if letter not in vowels)
    print("Output:", output)

main()
