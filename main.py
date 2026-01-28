from dotenv import load_dotenv
from colorama import Style
from fpdf import FPDF
import requests
import calendar
import time
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
            `success` -> `success` -> This color means that the task went good.
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
            case "success":
                Color = f"\x1b[38;2;0;255;0m"
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

class coordinate:
    def __init__(self, longitude: float, latitude: float) -> None:
        self.x: float = longitude
        self.y: float = latitude
    
    #region getters
    def get_full_cordinate(self) -> tuple[float, float]:
        return (self.x, self.y)

    def get_longitude(self) -> float:
        return self.x
    
    def get_latitude(self) -> float:
        return self.y
    #endregion

    #region setters
    def set_longitude(self, longitude: float) -> None:
        self.x = longitude
    
    def set_latitude(self, latitude: float) -> None:
        self.y = latitude
    
    def set_cordinate(self, longitude: float, latitude: float) -> None:
        self.x = longitude
        self.y = latitude
    #endregion

    def __str__(self) -> str:
        return f"{self.x},{self.y}"

class date:
    def __init__(self, year: int, month: int, day: int) -> None:
        self.year: int = year
        self.month: int = month
        self.day: int = day
    
    #region getters
    def get_year(self) -> int:
        return self.year
    
    def get_month(self) -> int:
        return self.month
    
    def get_day(self) -> int:
        return self.day
    
    def get_last_day_of_month(self) -> int:
        return calendar.monthrange(self.year, self.month)[1]
    #endregion

    #region setters
    def set_year(self, year: int) -> None:
        self.year = year
    
    def set_month(self, month: int) -> None:
        self.month = month
    
    def set_day(self, day: int) -> None:
        self.day = day
    #endregion

    def __str__(self) -> str:
        return f"{self.year}-{self.month}-{self.day}"

def timer(func):
    def wrapper(*args, **kwargs):
        start: float = time.time()
        result = func(*args, **kwargs)
        end: float = time.time()
        print(f"Took {end-start:.8f} second\n\n")
        return result
    return wrapper

@timer
def ask_for_cordinate() -> coordinate | None:
    try:
        lon: float = float(input(ConsolColor.PreSetUpColoredTextLine("Enter longitude: ", "s_color")))
        lat: float = float(input(ConsolColor.PreSetUpColoredTextLine("Enter latitude: ", "s_color")))

    except ValueError:
        print(ConsolColor.PreSetUpColoredTextLine("Invalid input. Please enter numeric values for longitude and latitude.", "danger"))
        return None

    else:
        print(ConsolColor.PreSetUpColoredTextLine("Cordinate successfully created.", "success"))
        return coordinate(lon, lat)

    finally:
        print(ConsolColor.PreSetUpColoredTextLine("Cordinate input attempt completed.", "info"))

@timer
def ask_for_date() -> date | None:
    try:
        year: int = int(input(ConsolColor.PreSetUpColoredTextLine("Enter year (e.g., 2026): ", "s_color")))
        month: int = int(input(ConsolColor.PreSetUpColoredTextLine("Enter month (1-12): ", "s_color")))
        day: int = int(input(ConsolColor.PreSetUpColoredTextLine(f"Enter day (1-{calendar.monthrange(year, month)[1]}): ", "s_color")))

        if month < 1 or month > 12:
            raise ValueError("Month must be between 1 and 12.")

        if day < 1 or day > calendar.monthrange(year, month)[1]:
            raise ValueError(f"Day must be between 1 and {calendar.monthrange(year, month)[1]} for month {month}.")

    except ValueError as ve:
        print(ConsolColor.PreSetUpColoredTextLine(f"Invalid input: {ve}", "danger"))
        return None

    else:
        print(ConsolColor.PreSetUpColoredTextLine("Date successfully created.", "success"))
        return date(year, month, day)

    finally:
        print(ConsolColor.PreSetUpColoredTextLine("Date input attempt completed.", "info"))

@timer
def ask_for_unitGroup():
    try:
        unit_group: str = input(ConsolColor.PreSetUpColoredTextLine("Enter the unit group (metric/imperial): ", "s_color")).strip().lower()

        if unit_group not in ["metric", "imperial"]:
            raise ValueError("Unit group must be metric or imperial.")

    except ValueError as ve:
        print(ConsolColor.PreSetUpColoredTextLine(f"Invalid input: {ve}", "danger"))
        return None

    else:
        print(ConsolColor.PreSetUpColoredTextLine("Unit group is successfully created.", "success"))
        return unit_group

    finally:
        print(ConsolColor.PreSetUpColoredTextLine("Unit group input attempt completed.", "info"))

@timer
def ask_for_weather_parameters():
    option_list: list[str] = ["datetime","temp","tempmax","tempmin","dew","humidity","precip","windgust","windspeed","cloudcover","solarradiation","solarenergy","uvindex","visibility"]
    print(ConsolColor.PreSetUpColoredTextLine("What do you need from the list:", "s_color"))
    for optionIndex in range(len(option_list)):
        print(ConsolColor.PreSetUpColoredTextLine(f"\t{optionIndex+1})- {option_list[optionIndex]}", "s_color"))
    print(ConsolColor.PreSetUpColoredTextLine("Type the numbers of the options you need separated by commas (e.g., 1,3,5) or type all if you need all. If you want to leave press enter.:", "s_color"))
    
    try:
        user_input: str = input(ConsolColor.PreSetUpColoredTextLine("?.: ", "s_color")).strip().lower()

        if user_input.lower() == "all":
            print(ConsolColor.PreSetUpColoredTextLine(f"Weather parameters is selected. ({user_input})", "success"))
            return option_list
        
        if user_input == "":
            raise ValueError("Parameters is empty.")
    except ValueError as ve:
        print(ConsolColor.PreSetUpColoredTextLine(f"Invalid input: {ve}", "danger"))
        return [""]

    else:
        try:
            selected_options: list[str] = []
            selected_indices: list[int] = [int(x.strip()) for x in user_input.split(",")]
            for index in selected_indices:
                if 1 <= index <= len(option_list):
                    selected_options.append(option_list[index - 1])
                else:
                    raise ValueError("Invalid input. Please enter valid option numbers separated by commas, 'all', or press enter to leave:")
        except ValueError as ve:
            print(ConsolColor.PreSetUpColoredTextLine(f"Invalid input: {ve}", "warning"))
            return [""]
        
        else:
            print(ConsolColor.PreSetUpColoredTextLine(f"Successful Weather parameters selection. ({user_input})", "success"))
            return selected_options

    finally:
        print(ConsolColor.PreSetUpColoredTextLine("Weather parameters input attempt completed.", "info"))

@timer
def load_environment_variables(file_path: str = ".env"):
    print(ConsolColor.PreSetUpColoredTextLine(f"Loading environment file: {file_path}", "i_tips"))
    try:
        load_dotenv(file_path)

    except Exception as e:
        print(ConsolColor.PreSetUpColoredTextLine(f"{file_path} could not load please make sure that the path is correct.","danger"))

    else:
        print(ConsolColor.PreSetUpColoredTextLine(f"{file_path} could load the path is correct.","success"))

    finally:
        print(ConsolColor.PreSetUpColoredTextLine(f"{file_path} file loading attempt completed.","s_color"))

@timer
def load_env_variable(variable_name: str) -> str:
    print(ConsolColor.PreSetUpColoredTextLine(f"Loading environment variables: {variable_name}", "i_tips"))
    env_variable: str
    try:
        env_variable = str(os.getenv(variable_name))

    except:
        print(ConsolColor.PreSetUpColoredTextLine(f"{variable_name} could not load please make sure that the name is correct.","danger"))
        return ""

    else:
        print(ConsolColor.PreSetUpColoredTextLine(f"{variable_name} could load.","success"))
        return env_variable

    finally:
        print(ConsolColor.PreSetUpColoredTextLine(f"{variable_name} variable loading attempt completed.","s_color"))

@timer
def create_json_log_file(data: dict):
    print(ConsolColor.PreSetUpColoredTextLine(f"Creating .json file for logging.", "i_tips"))

    try:
        with open("weather_data_response.json", "w") as file:
            file.write(str(data).replace('\'', '"'))
    
    except Exception as e:
        print(ConsolColor.PreSetUpColoredTextLine(f"File had problem: {e}","danger"))

    else:
        print(ConsolColor.PreSetUpColoredTextLine(f"File created successfully.", "success"))

    finally:
        print(ConsolColor.PreSetUpColoredTextLine(f"weather_data_response.json file creating attempt completed.","s_color"))

@timer
def fetch_api(cordinates = ask_for_cordinate(), start_date = ask_for_date(), end_date = ask_for_date(), unit_group = ask_for_unitGroup(), weather_params = ask_for_weather_parameters()) -> dict:
    load_environment_variables()
    url: str = f"{load_env_variable("API_URL")}{cordinates}/{start_date}/{end_date}?key={load_env_variable("API_KEY")}&include=days&unitGroup={unit_group}&elements={','.join(weather_params)}"
    print(ConsolColor.PreSetUpColoredTextLine(f"Asking the API for data.", "i_tips"))
    try:
        response = requests.get(url)

        if response.status_code != 200:
            raise Exception(f"API request failed with status code {response.status_code}")

    except Exception as e:
        print(ConsolColor.PreSetUpColoredTextLine(f"API request failed: {e}", "danger"))
        return {}

    else:
        print(ConsolColor.PreSetUpColoredTextLine(f"API responded successfully.", "success"))
        return response.json()

    finally:
        print(ConsolColor.PreSetUpColoredTextLine(f"API request attempt completed.","s_color"))

def main():
    while True:
        create_json_log_file(fetch_api())

        can_go = input(ConsolColor.PreSetUpColoredTextLine("Do you want to fech more data from the API? (yes | no)\n?.:", "s_color")).strip().lower()

        if can_go == "no":
            break


main()