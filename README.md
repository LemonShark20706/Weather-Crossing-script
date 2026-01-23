# This script helps with weather data analysis.
It provides functions to fetch weather data from a API. It uses the Visual Crossing Weather API.

## Description
This script allows users to fetch historical weather data for a specified location and date range using the Visual Crossing Weather API. It supports various weather parameters such as temperature, humidity, wind speed, and precipitation. The script is designed to be user-friendly and customizable, allowing users to specify their desired location, date range, and weather parameters. The fetched data is exported in JSON format for further analysis. For now this works for a hole month at a time. But upgrades are planned to support custom date ranges in the future or more export formats. More analysis features are also planned for future updates. Please refer to the installation instructions below to set up and run the script and note that this API may have usage limits based on your subscription plan.

---
## Installation
1. Clone the repository:
   ```bash
   git clone repository_url
   ```

2. Navigate to the project directory:
    ```bash
    cd project_directory
    ```

3. Install the required dependencies:
    ```bash
    pip install requests python-dotenv colorama fpdf
    ```

4. Set up your Visual Crossing Weather API key:
    - Sign up for an account at [Visual Crossing](https://www.visualcrossing.com)
    - Obtain your API key from the dashboard
    - Create a `.env` file in the project directory and add your API key:
    ```
    API_URL="https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/"
    API_KEY=your_api_key_here
    ```

5. Run the script:
    ```bash
    python your_script_name.py
    ```

6. Output:
    - The fetched weather data will be saved in a JSON file in the project directory. As weather_data_response.json.

---
## Features
- Fetch historical weather data
- Customizable date ranges
- Customizable location input
- Supports multiple weather parameters
- Data export option (JSON)
- Supports different units (metric/imperial)
- Easy-to-use interface
- Color-coded terminal output
- Data validation and error handling
- Logging functionality
- User-friendly prompts
- PDF report generation

------
## Requirements
- Python 3.x
- requests library
- calendar library
- colorama library
- dotenv library
- fpdf library
- os library

---
## Links
- [Visual Crossing](https://www.visualcrossing.com/)
- [Visual Crossing Weather API](https://www.visualcrossing.com/weather-api)