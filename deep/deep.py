def deep():
    answer = input("What is the Answer to the Great Questions of Life, the Universe, and Everything? ")
    answer = answer.lower()
    if answer == "42" or answer == "forty-two" or answer == "forty two":
        return "Yes"
    else:
        return "No"
    
deep()