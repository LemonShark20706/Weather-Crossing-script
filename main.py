from dotenv import load_dotenv
from colorama import Style
import requests
import calendar
import os

from fpdf import FPDF

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

def cordinates_to_string() -> str | None:
    """
    Asks for a longitude and latitude from the user and returns them as a formatted string.

    Returns:
        str: A string representation of the coordinates in the format. (x,y)
    """
    try:
        longitude:float = float(input(ConsolColor.PreSetUpColoredTextLine("Enter the longitude: ", "info")))
        latitude:float = float(input(ConsolColor.PreSetUpColoredTextLine("Enter the latitude: ", "info")))
        return f"{longitude},{latitude}"
    except ValueError:
        print(ConsolColor.PreSetUpColoredTextLine("Invalid input. Please enter numeric values for longitude and latitude.", "warning"))

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
    print(ConsolColor.PreSetUpColoredTextLine("How much data do you want to fetch in time?\n1)- A year\n2)- A month\n3)- A day\n4)- Year to year range\n5)- Month to month range\n6)- Day to day range", "s_color"))
    while True:
        option: int = int(input(ConsolColor.PreSetUpColoredTextLine("Choose an option (1-6): ", "info")))
        match option:
            case 1:
                print(ConsolColor.PreSetUpColoredTextLine("Enter the year for which you want the data:", "s_color"))
                year: int = int(input(ConsolColor.PreSetUpColoredTextLine("Year (e.g., 2026): ", "info")))
                start_date: str = f"{year}-01-01"
                end_date: str = f"{year}-12-31"
                return f"{start_date}/{end_date}"

            case 2:
                print(ConsolColor.PreSetUpColoredTextLine("Enter the month and year for which you want the data:", "s_color"))
                month: int = int(input(ConsolColor.PreSetUpColoredTextLine("Month (1-12): ", "info")))
                year: int = int(input(ConsolColor.PreSetUpColoredTextLine("Year (e.g., 2026): ", "info")))
                if 1 <= month <= 12:
                    first_day, last_day = get_first_and_last_day_of_month(month, year)
                    start_date: str = f"{year}-{month:02d}-{first_day:02d}"
                    end_date: str = f"{year}-{month:02d}-{last_day:02d}"
                    return f"{start_date}/{end_date}"
                else:
                    print("Invalid month. Please enter a value between 1 and 12.")

            case 3:
                print(ConsolColor.PreSetUpColoredTextLine("Enter the date for which you want the data:", "s_color"))
                year: int = int(input(ConsolColor.PreSetUpColoredTextLine("Year (e.g., 2026): ", "info")))
                month: int = int(input(ConsolColor.PreSetUpColoredTextLine("Month (1-12): ", "info")))
                day: int = int(input(ConsolColor.PreSetUpColoredTextLine("Day (1-31): ", "info")))
                start_date: str = f"{year}-{month:02d}-{day:02d}"
                return start_date
            
            case 4:
                print(ConsolColor.PreSetUpColoredTextLine("Enter the year range for which you want the data:", "s_color"))
                start_year: int = int(input(ConsolColor.PreSetUpColoredTextLine("Start Year (e.g., 2026): ", "info")))
                end_year: int = int(input(ConsolColor.PreSetUpColoredTextLine("End Year (e.g., 2026): ", "info")))
                start_date: str = f"{start_year}-01-01"
                end_date: str = f"{end_year}-12-31"
                return f"{start_date}/{end_date}"

            case 5:
                print(ConsolColor.PreSetUpColoredTextLine("Enter the month range for which you want the data:", "s_color"))
                start_month: int = int(input(ConsolColor.PreSetUpColoredTextLine("Start Month (1-12): ", "info")))
                start_year: int = int(input(ConsolColor.PreSetUpColoredTextLine("Start Year (e.g., 2026): ", "info")))
                end_month: int = int(input(ConsolColor.PreSetUpColoredTextLine("End Month (1-12): ", "info")))
                end_year: int = int(input(ConsolColor.PreSetUpColoredTextLine("End Year (e.g., 2026): ", "info")))
                start_date: str = f"{start_year}-{start_month:02d}-01"
                end_date: str = f"{end_year}-{end_month:02d}-{get_first_and_last_day_of_month(end_month, end_year)[1]:02d}"
                return f"{start_date}/{end_date}"

            case 6:
                print(ConsolColor.PreSetUpColoredTextLine("Enter the day range for which you want the data:", "s_color"))
                start_year: int = int(input(ConsolColor.PreSetUpColoredTextLine("Start Year (e.g., 2026): ", "info")))
                start_month: int = int(input(ConsolColor.PreSetUpColoredTextLine("Start Month (1-12): ", "info")))
                start_day: int = int(input(ConsolColor.PreSetUpColoredTextLine("Start Day (1-31): ", "info")))
                end_year: int = int(input(ConsolColor.PreSetUpColoredTextLine("End Year (e.g., 2026): ", "info")))
                end_month: int = int(input(ConsolColor.PreSetUpColoredTextLine("End Month (1-12): ", "info")))
                end_day: int = int(input(ConsolColor.PreSetUpColoredTextLine("End Day (1-31): ", "info")))
                start_date: str = f"{start_year}-{start_month:02d}-{start_day:02d}"
                end_date: str = f"{end_year}-{end_month:02d}-{end_day:02d}"
                return f"{start_date}/{end_date}"

            case _:
                print(ConsolColor.PreSetUpColoredTextLine("Invalid option. Please choose a valid option (1-6).", "warning"))

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
    print(ConsolColor.PreSetUpColoredTextLine("What do you need from the list:", "s_color"))
    for optionIndex in range(len(option_list)):
        print(ConsolColor.PreSetUpColoredTextLine(f"\t{optionIndex+1})- {option_list[optionIndex]}", "s_color"))
    print(ConsolColor.PreSetUpColoredTextLine("Type the numbers of the options you need separated by commas (e.g., 1,3,5) or type all if you need all. If you want to leave press enter.:", "s_color"))
    
    user_input: str = input(ConsolColor.PreSetUpColoredTextLine("?.: ", "info"))
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
            print(ConsolColor.PreSetUpColoredTextLine("Invalid input. Please enter valid option numbers separated by commas, 'all', or press enter to leave:", "warning"))

    return [""]

def get_unitGroup() -> str | None:
    """
    Asks the user for their preferred unit group (metric or imperial).

    Returns:
        str: The unit group chosen by the user.
    """
    unit_group: str = input(ConsolColor.PreSetUpColoredTextLine("Enter the unit group (metric/imperial): ", "info")).strip().lower()
    if unit_group in ["metric", "imperial"]:
        return unit_group
    else:
        print(ConsolColor.PreSetUpColoredTextLine("Invalid input. Please enter 'metric' or 'imperial'.", "warning"))

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
        raise Exception(ConsolColor.PreSetUpColoredTextLine(f"API request failed with status code {response.status_code}", "danger"))

def create_file_with_data(data: dict) -> None:
    """
    Creates a file and writes the provided data into it.

    Args:
        data (dict): The data to be written to the file.
    """
    with open("weather_data_response.json", "w") as file:
        file.write(str(data).replace('\'', '"'))

def create_pdf_report(data: dict) -> None:
    """
    Creates a PDF report from the provided data.

    Args:
        data (dict): The data to be included in the PDF report.
    """
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Courier", "B", 16)
    pdf.cell(0, 10, "Weather Report Summary", ln=True, align='C')
    pdf.set_font("Courier", size=10)

    days_data = data.get("days", [])
    pdf.cell(0, 10, f"Total Days: {len(days_data)}", ln=True)
    pdf.cell(0, 10, f"Location: {data.get('address', 'N/A').replace(',', ' | ')}", ln=True)
    pdf.cell(0, 10, f"Timezone: {data.get('timezone', 'N/A').replace('/', ' | ')}", ln=True)
    pdf.ln(10)

    pdf.set_font("Courier", "B", 16)
    pdf.cell(0, 10, "Dataset Summary:", ln=True)
    pdf.set_font("Courier", size=9)

    max_temp = max(day.get('tempmax', float('-inf')) for day in days_data if 'tempmax' in day)
    min_temp = min(day.get('tempmin', float('inf')) for day in days_data if 'tempmin' in day)
    avg_temp = sum(day.get('temp', 0) for day in days_data) / len(days_data) if days_data else 0

    pdf.cell(0, 8, f"Max Temperature: {max_temp}°C", ln=True)
    pdf.cell(0, 8, f"Min Temperature: {min_temp}°C", ln=True)
    pdf.cell(0, 8, f"Average Temperature: {avg_temp:.2f}°C", ln=True)

    fields = ['dew', 'humidity', 'precip', 'windgust', 'windspeed', 'cloudcover', 'visibility', 'solarradiation', 'solarenergy', 'uvindex']
    
    for field in fields:
        values = [day.get(field, 0) for day in days_data if field in day and day.get(field) is not None]
        if values:
            max_val = max(values)
            min_val = min(values)
            avg_val = sum(values) / len(values)
            pdf.cell(0, 8, f"{field.capitalize()} - Max: {max_val}, Min: {min_val}, Avg: {avg_val:.2f}", ln=True)

    pdf.add_page()
    pdf.set_font("Courier", "B", 11)
    pdf.cell(30, 8, "Date", border=1, align='C')
    pdf.cell(30, 8, "Temp", border=1, align='C')
    pdf.cell(30, 8, "Max", border=1, align='C')
    pdf.cell(30, 8, "Min", border=1, ln=True, align='C')
    pdf.set_font("Courier", size=8)

    pdf.ln(2)
    for day in days_data:
        pdf.cell(30, 7, str(day.get('datetime', 'N/A'))[:10], border=1)
        pdf.cell(30, 7, str(day.get('temp', 'N/A')), border=1, align='C')
        pdf.cell(30, 7, str(day.get('tempmax', 'N/A')), border=1, align='C')
        pdf.cell(30, 7, str(day.get('tempmin', 'N/A')), border=1, ln=True, align='C')


    for day in days_data:
        pdf.add_page()
        pdf.set_font("Courier", "B", 14)
        pdf.cell(0, 10, f"Date: {day.get('datetime', 'N/A')}", ln=True, align='C')
        pdf.set_font("Courier", size=10)
        pdf.ln(5)
        
        for key, value in day.items():
            if key != "datetime":
                pdf.cell(0, 8, f"{key.capitalize()}: {value}", ln=True)

    pdf.output("weather_report.pdf")
    print("PDF report created successfully as 'weather_report.pdf'.")

def main() -> None:
    """
    Main function to execute the program.
    """
    print(ConsolColor.PreSetUpColoredTextLine("Data fetching is in progress...", "s_color"))
    data: dict = fetch_api()
    create_file_with_data(data)
    print(ConsolColor.PreSetUpColoredTextLine("Data fetched and saved to 'weather_data_response.json'.", "s_color"))

    print(ConsolColor.PreSetUpColoredTextLine("Do you want a report about the fetched data? (yes/no)", "s_color"))
    report_choice: str = input(ConsolColor.PreSetUpColoredTextLine("?.: ", "info")).strip().lower()
    if report_choice == "no":
        print("Exiting the program.")
        return

    print(ConsolColor.PreSetUpColoredTextLine("Do you want the report in a PDF file? (yes/no)", "s_color"))
    if input(ConsolColor.PreSetUpColoredTextLine("?.: ", "info")).strip().lower() == "yes":
        create_pdf_report(data)

    days_data: list[dict] = data.get("days", [])
    os.system('cls')
    for day in days_data:
        print(ConsolColor.PreSetUpColoredTextLine(f"Date: {day.get('datetime', 'N/A')}", "s_color"))
        for key, value in day.items():
            if key != "datetime":
                print(ConsolColor.PreSetUpColoredTextLine(f"  {key}: {value}", "i_tips"))
        input(ConsolColor.PreSetUpColoredTextLine("\n\nPress Enter to continue to the next day...", "info"))
        os.system('cls')

main()