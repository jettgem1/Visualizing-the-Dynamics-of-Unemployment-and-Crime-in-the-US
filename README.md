
# Visualizing the Dynamics of Unemployment and Crime in the US

## Project Overview

This project investigates the relationship between unemployment and crime rates in the United States from 1960 to 2019. Utilizing D3.js for data visualization, we've created interactive choropleth maps and 3-axis line charts to explore trends at both the national and state levels. Our visualizations aim to uncover any correlation between unemployment rates and total crime rates over nearly six decades.

## Data Sets Utilized

Our visualizations are based on four key data sets:

- **United States Crime Rates (1960 - 2019):** This data set includes the total number of various crimes across the U.S., normalized per 100,000 people. [Source](https://www.disastercenter.com/crime/uscrime.htm)
- **Labor Force Statistics (Current Population Survey):** Data on the U.S. unemployment rate, adjusted and exported to reflect totals per 100K. [Source](https://data.bls.gov/timeseries/LNS14000000)
- **State Crime Rates:** Focusing on total crime rates per state, extracted from the United Crime Reporting Program. [Source](https://corgis-edu.github.io/corgis/csv/state_crime/)
- **Annual Unemployment Rates by State:** Rates per state, considering individuals 16 or older as employable citizens. [Source](https://www.icip.iastate.edu/tables/employment/unemployment-states)

Data manipulation was performed using a combination of HTML to CSV converters, Python scripting, and manual modifications in Excel.

## Project Setup

To run this project locally, follow these steps:

1. **Clone the Repository:**
   ```sh
   git clone https://your-repository-link.git
   ```
2. **Install Dependencies:**
   Ensure you have D3.js and any other dependencies listed in the `package.json` file installed. If you're using npm, you can run:
   ```sh
   npm install
   ```
3. **Launch the Project:**
   Depending on your setup, you might serve the project using a simple HTTP server. For example, you can use Python's built-in HTTP server:
   ```sh
   python -m http.server 8000
   ```
   Then, access the project at `http://localhost:8000` in your web browser.

4. **Data Files:**
   Make sure the CSV data files are located in the expected directory paths as referenced in the D3 scripts.

## Acknowledgments

This project was a collaborative effort for CS3300: Data-Driven Web Applications at Cornell University. Team members include Jett Gemmer, Andrew Song, Amanda Chen, and Lauren Cali. We extend our gratitude to the providers of the datasets used in this project, which enabled us to conduct this comprehensive analysis.

## License

This project is open-source and licensed under the MIT License. See the LICENSE file for more details.