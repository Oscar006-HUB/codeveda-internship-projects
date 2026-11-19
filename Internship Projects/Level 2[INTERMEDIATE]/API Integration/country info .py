import requests

# the base url for the api i am using
BASE_URL = "https://restcountries.com/v3.1/name/"


def get_country_info(country_name):
    try:
        #making the get request to the api
        url = BASE_URL + country_name
        response = requests.get(url)

        # check if country was not found
        if response.status_code == 404:
            print(f"\nError: '{country_name}' was not found.")
            print("Please check the spelling and try again.")
            return

        # check for other bad responses
        if response.status_code != 200:
            print(f"\nError: Something went wrong. Status code: {response.status_code}")
            return

        #parse the json response
        data = response.json()

        # the api returns a list, we take the first result
        country = data[0]

        # pulling out the info i need
        name       = country["name"]["common"]
        official   = country["name"]["official"]
        capital    = country.get("capital", ["N/A"])[0]
        region     = country.get("region", "N/A")
        subregion  = country.get("subregion", "N/A")
        population = country.get("population", 0)
        area       = country.get("area", 0)
        flag       = country.get("flag", "")

        # getting currencies
        currencies = country.get("currencies", {})
        if currencies:
            currency_list = []
            for code, value in currencies.items():
                curr_name   = value["name"]
                curr_symbol = value["symbol"]
                currency_list.append(f"{curr_name} ({curr_symbol})")
            currency_str = ", ".join(currency_list)
        else:
            currency_str = "N/A"

        # getting languages
        languages = country.get("languages", {})
        if languages:
            lang_list = []
            for code, lang in languages.items():
                lang_list.append(lang)
            language_str = ", ".join(lang_list)
        else:
            language_str = "N/A"

        # display the results
        print("\n" + "=" * 45)
        print(f"  {flag}  {name}")
        print("=" * 45)
        print(f"  Official Name : {official}")
        print(f"  Capital       : {capital}")
        print(f"  Region        : {region}")
        print(f"  Sub Region    : {subregion}")
        print(f"  Population    : {population:,}")
        print(f"  Area          : {area:,} km2")
        print(f"  Currency      : {currency_str}")
        print(f"  Languages     : {language_str}")
        print("=" * 45)

    except requests.exceptions.ConnectionError:
        print("\nError: No internet connection.")
        print("Please check your network and try again.")

    except requests.exceptions.Timeout:
        print("\nError: The request took too long.")
        print("Try again after a few seconds.")

    except ValueError:
        # this handles cases where the response is not valid json
        print("\nError: Could not read the server response.")

    except Exception as e:
        # catching any other unexpected errors
        print(f"\nSomething unexpected happened: {e}")


def main():
    print("\n" + "=" * 45)
    print("       COUNTRY INFO LOOKUP")
    print("=" * 45)

    while True:
        print("\nWhat do you want to do?")
        print("1. Search for a country")
        print("2. Exit")

        choice = input("\nEnter your choice (1 or 2): ")

        if choice == "1":
            country_name = input("Enter the country name: ")

            # make sure user actually typed something
            if not country_name:
                print("Error: You did not enter a country name.")
            else:
                get_country_info(country_name)

        elif choice == "2":
            print("\nGoodbye!")
            break

        else:
            print("Error: Please enter 1 or 2 only.")


if __name__ == "__main__":
    main()