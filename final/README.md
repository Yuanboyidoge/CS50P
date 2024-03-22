# Video Demo: [👀](https://youtu.be/iinWwpDyu6Q)
# Description:

## Introduction
This Python script generates a PDF document for a business travel statement. It prompts the user to input relevant information such as name, student ID, dates of travel, location, travel route, hotel details, and road expenses. Then, it calculates the total expenses and generates a PDF document summarizing the business travel statement.

## Requirements
- Python 3.x
- fpdf library (`pip install fpdf`)

## Usage
1. Run the Python script.
2. Follow the prompts to input necessary information:
   - Name
   - Student ID
   - Start date of business travel (in yyyy-mm-dd format)
   - End date of business travel
   - Location of business travel
   - Round trip route
   - Hotel name
   - Hotel unit price
   - Road fares (separated by spaces)
3. After providing the required information, the script will generate a PDF document named `OUTPUT.pdf` in the current directory.


## Output
The generated PDF document contains the following sections:
- Header: "Business Travel Statement"
- Personal Information: Name, Student ID, Duration of Travel
- Travel Details: Location, Travel Route, Accommodation Arrangement
- Total Expenses Breakdown: Road expenses, Accommodation, Allowance, Total
- Signature and Date

## Note
- Ensure all input values are entered correctly to avoid errors in calculation and PDF generation.
- If an invalid date or input format is provided, the script will exit with an error message.

## Author
This script was written by [Your Name].

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---
**Disclaimer:** This script is provided as-is without any warranty. Use it at your own risk.

### Drawbacks

Not as versatile as Word, and the format might not be particularly aesthetic.
