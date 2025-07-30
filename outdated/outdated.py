def main():
    months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]
    while True:
        try:
            user_input = input("Date: ").strip()

            if "/" in user_input:
                month, day, year = user_input.split("/")
                month = int(month)
                day = int(day)
                year = int(year)
                if 1 <= month <= 12 and 1 <= day <= 31:
                    print(f"{year:04}-{month:02}-{day:02}")
                    break

            elif "," in user_input:
                month_name, rest = user_input.split(" ", 1)
                day, year = rest.replace(",", "").split()
                if month_name in months:
                    month = months.index(month_name) + 1
                    day = int(day)
                    year = int(year)
                    if 1 <= day <= 31:
                        print(f"{year:04}-{month:02}-{day:02}")
                        break

        except (ValueError, IndexError):
            pass
main()
