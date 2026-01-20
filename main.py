from dotenv import load_dotenv
from colorama import Style
import requests
import calendar
import os

class ConsolColor:
    @staticmethod
    def CustomColoredText(text : str, r : int, g : int, b : int) -> str:
        """
        Colors a given text to a given RGB color

        Args:
            szoveg (`str`): The text that you want to color.
            r (`int`): RGB color red.
            g (`int`): RGB color green.
            b (`int`): RGB color blue.

        Returns:
            `str`: Gives back the colored text.
        """
    
        color : str = f"\x1b[38;2;{r};{g};{b}m"
        coloredText : str = f"{color}{text}{Style.RESET_ALL}"
        return coloredText

    @staticmethod
    def PreSetUpColoredTextLine(text : str, textType : str) -> str:
        """
        Gives back a line of colored text with pre coded colors.

        Args:
            text (str): The text you want to color.
            textType (str): The color type.

        Returns:
            str: The colored text.

        ## Types
            `ni_tips` -> `not_important_tips` -> Tips that can be overlooked. It is a black color rgb(0,0,0).
            `i_tips` -> `important_tips` -> Tips that can make this process faster.
            `s_color` -> `system_color` -> The basic color that this code use.
            `is_color` -> `important_system_color` -> The system color that you sould look out for.
            `p_error` -> `possible_error` -> This colored message can lead to errors.
            `warning` -> `warning` -> This colored message is a warning.
            `danger` -> `danger` -> This colored message is a danger.
            `info` -> `information` -> This colored message is an information.
        """

        Color : str = ""
        match textType:
            case "ni_tips":
                Color = f"\x1b[38;2;0;0;0m"
            case "i_tips":
                Color = f"\x1b[38;2;150;150;150m"
            case "s_color":
                Color = f"\x1b[38;2;200;200;200m"
            case "is_color":
                Color = f"\x1b[38;2;255;255;255m"
            case "p_error":
                Color = f"\x1b[38;2;255;230;0m"
            case "warning":
                Color = f"\x1b[38;2;255;100;0m"
            case "danger":
                Color = f"\x1b[38;2;255;0;0m"
            case "info":
                Color = f"\x1b[38;2;0;0;255m"

        coloredText : str = f"{Color}{text}{Style.RESET_ALL}"
        return coloredText

    @staticmethod
    def PreSetUpColorStart(textType : str) -> str:
        """
        Gives back the start of colored line.

        Args:
            text (str): The text you want to color.
            textType (str): The color type.

        Returns:
            str: The colored text.

        ## Types
            `ni_tips` -> `not_important_tips` -> Tips that can be overlooked. It is a black color rgb(0,0,0).
            `i_tips` -> `important_tips` -> Tips that can make this process faster.
            `s_color` -> `system_color` -> The basic color that this code use.
            `is_color` -> `important_system_color` -> The system color that you sould look out for.
            `p_error` -> `possible_error` -> This colored message can lead to errors.
            `warning` -> `warning` -> This colored message is a warning.
            `danger` -> `danger` -> This colored message is a danger.
            `info` -> `information` -> This colored message is an information.
        """
    
        Color: str = ""
        match textType:
            case "ni_tips":
                Color = f"\x1b[38;2;0;0;0m"
            case "i_tips":
                Color = f"\x1b[38;2;150;150;150m"
            case "s_color":
                Color = f"\x1b[38;2;200;200;200m"
            case "is_color":
                Color = f"\x1b[38;2;255;255;255m"
            case "p_error":
                Color = f"\x1b[38;2;255;230;0m"
            case "warning":
                Color = f"\x1b[38;2;255;100;0m"
            case "danger":
                Color = f"\x1b[38;2;255;0;0m"
            case "info":
                Color = f"\x1b[38;2;0;0;255m"

        finalColor : str = f"{Color}"
        return finalColor

    @staticmethod
    def PreSetUpColorEnd() -> str:
        """
        Gives back the end of colored line.

        Returns:
            str: The end of colored text.
        """
        finalColorEnd = f"{Style.RESET_ALL}"
        return finalColorEnd    

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

def load_environment_variables() -> None:
    """
    Loads environment variables from a .env file.
    """
    load_dotenv('.env')

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
    load_environment_variables()
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

create_file_with_data(fetch_api())