import inflect

def main():
    p = inflect.engine()
    names = []

    try:
        while True:
            name = input("Name:").strip()
            names.append(name)
    except EOFError:
        print()

    everyone = p.join(names)
    print(f"Adieu, adieu, to {everyone}")

if __name__ == "__main__":
    main()
