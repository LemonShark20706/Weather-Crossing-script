from dotenv import load_dotenv
import requests
import calendar
import os
load_dotenv('.env')

def cordinates_to_string() -> str:
    """
    Asks for a longitude and latitude from the user and returns them as a formatted string.

    Returns:
        str: A string representation of the coordinates in the format. (x,y)
    """
    longitude:str = input("Enter the longitude: ")
    latitude:str = input("Enter the latitude: ")
    return f"{longitude},{latitude}"

def get_first_and_last_day_of_month(month: int, year: int) -> tuple:
    """
    Given a month and year, returns the first and last day of that month.

    Args:
        month (int): The month as an integer (1-12).
        year (int): The year as a four-digit integer.

    Returns:
        tuple: A tuple containing the first and last day of the month.
    """

    first_day:int = 1
    last_day = calendar.monthrange(year, month)[1]
    return (first_day, last_day)

def get_date_string() -> str:
    """
    Asks the user for a month and year, then returns a date string in the format YYYY-MM-DD to YYYY-MM-DD.
    """
    print("How much data do you want to fetch in time?\n1)- A year\n2)- A month\n3)- A day\n4)- Year to year range\n5)- Month to month range\n6)- Day to day range")
    while True:
        option: int = int(input("Choose an option (1-6): "))
        match option:
            case 1:
                print("Enter the year for which you want the data:")
                year: int = int(input("Year (e.g., 2026): "))
                start_date: str = f"{year}-01-01"
                end_date: str = f"{year}-12-31"
                return f"{start_date}/{end_date}"

            case 2:
                print("Enter the month and year for which you want the data:")
                month: int = int(input("Month (1-12): "))
                year: int = int(input("Year (e.g., 2026): "))
                if 1 <= month <= 12:
                    first_day, last_day = get_first_and_last_day_of_month(month, year)
                    start_date: str = f"{year}-{month:02d}-{first_day:02d}"
                    end_date: str = f"{year}-{month:02d}-{last_day:02d}"
                    return f"{start_date}/{end_date}"
                else:
                    print("Invalid month. Please enter a value between 1 and 12.")

            case 3:
                print("Enter the date for which you want the data:")
                year: int = int(input("Year (e.g., 2026): "))
                month: int = int(input("Month (1-12): "))
                day: int = int(input("Day (1-31): "))
                start_date: str = f"{year}-{month:02d}-{day:02d}"
                return start_date
            
            case 4:
                print("Enter the year range for which you want the data:")
                start_year: int = int(input("Start Year (e.g., 2026): "))
                end_year: int = int(input("End Year (e.g., 2026): "))
                start_date: str = f"{start_year}-01-01"
                end_date: str = f"{end_year}-12-31"
                print(f"Debug: start_date={start_date}, end_date={end_date}")
                return f"{start_date}/{end_date}"

            case 5:
                print("Enter the month range for which you want the data:")
                start_month: int = int(input("Start Month (1-12): "))
                start_year: int = int(input("Start Year (e.g., 2026): "))
                end_month: int = int(input("End Month (1-12): "))
                end_year: int = int(input("End Year (e.g., 2026): "))
                start_date: str = f"{start_year}-{start_month:02d}-01"
                end_date: str = f"{end_year}-{end_month:02d}-{get_first_and_last_day_of_month(end_month, end_year)[1]:02d}"
                print(f"Debug: start_date={start_date}, end_date={end_date}")
                return f"{start_date}/{end_date}"

            case 6:
                print("Enter the day range for which you want the data:")
                start_year: int = int(input("Start Year (e.g., 2026): "))
                start_month: int = int(input("Start Month (1-12): "))
                start_day: int = int(input("Start Day (1-31): "))
                end_year: int = int(input("End Year (e.g., 2026): "))
                end_month: int = int(input("End Month (1-12): "))
                end_day: int = int(input("End Day (1-31): "))
                start_date: str = f"{start_year}-{start_month:02d}-{start_day:02d}"
                end_date: str = f"{end_year}-{end_month:02d}-{end_day:02d}"
                print(f"Debug: start_date={start_date}, end_date={end_date}")
                return f"{start_date}/{end_date}"

            case _:
                print("Invalid option. Please choose a valid option (1-6).")

def fetch_api_url() -> str:
    """
    Fetches the API URL from environment variables.

    Returns:
        str: The API URL.
    """
    return f"{os.getenv('API_URL')}"

def fetch_api_key() -> str:
    """
    Fetches the API key from environment variables.

    Returns:
        str: The API key.
    """
    return f"{os.getenv('API_KEY')}"

def fecth_needed_infos() -> list[str]:
    """
    Fetches the necessary information from the user and environment variables.

    Returns:
        tuple: A tuple containing the coordinates string, API URL, and API key.
    """
    option_list: list[str] = ["datetime","temp","tempmax","tempmin","dew","humidity","precip","windgust","windspeed","cloudcover","solarradiation","solarenergy","uvindex","visibility"]
    print("What do you need from the list:")
    for optionIndex in range(len(option_list)):
        print(f"\t{optionIndex+1})- {option_list[optionIndex]}")
    print("Type the numbers of the options you need separated by commas (e.g., 1,3,5) or type all if you need all. If you want to leave press enter.:")
    
    user_input: str = input()
    if user_input.lower() == "all":
        return option_list
    elif user_input == "":
        return []
    else:
        try:
            selected_options: list[str] = []
            selected_indices: list[int] = [int(x.strip()) for x in user_input.split(",")]
            for index in selected_indices:
                if 1 <= index <= len(option_list):
                    selected_options.append(option_list[index - 1])
                else:
                    raise ValueError
            return selected_options
        except ValueError:
            print("Invalid input. Please enter valid option numbers separated by commas, 'all', or press enter to leave:")

    return [""]

def get_unitGroup() -> str | None:
    """
    Asks the user for their preferred unit group (metric or imperial).

    Returns:
        str: The unit group chosen by the user.
    """
    unit_group: str = input("Enter the unit group (metric/imperial): ").strip().lower()
    if unit_group in ["metric", "imperial"]:
        return unit_group
    else:
        print("Invalid input. Please enter 'metric' or 'imperial'.")

def fetch_api() -> dict:
    """
    Fetches data from the API based on user input and environment variables.
    """
    
    url: str = f"{fetch_api_url()}{cordinates_to_string()}/{get_date_string()}?key={fetch_api_key()}&include=days&unitGroup={get_unitGroup()}&elements={','.join(fecth_needed_infos())}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"API request failed with status code {response.status_code}")

def create_file_with_data(data: dict) -> None:
    """
    Creates a file and writes the provided data into it.

    Args:
        data (dict): The data to be written to the file.
    """
    with open("weather_data_response.json", "w") as file:
        file.write(str(data).replace('\'', '"'))

data = fetch_api()
create_file_with_data(data)