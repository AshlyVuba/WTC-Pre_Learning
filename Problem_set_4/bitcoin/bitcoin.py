import sys
import requests

def main():
    if len(sys.argv) != 2:
        sys.exit("Missing command-line argument")

    try:
        amount = float(sys.argv[1])
    except ValueError:
        sys.exit("Command-line argument is not a number")

    try:
        response = requests.get(
            "https://api.coincap.io/v2/assets/bitcoin",
            headers={"Authorization": "Bearer YourApiKey"}  
        )
        response.raise_for_status()
        data = response.json()
        price = float(data["data"]["priceUsd"])
        total = amount * price
        print(f"${total:,.4f}")
    except requests.RequestException:
        sys.exit("Error fetching data from CoinCap")
    except (KeyError, TypeError, ValueError):
        sys.exit("Unexpected response format from API")

if __name__ == "__main__":
    main()
