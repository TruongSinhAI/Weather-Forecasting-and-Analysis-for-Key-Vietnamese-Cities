# DSP391m Project: Weather Forecasting and Analysis for Key Vietnamese Cities

## Description
This repository contains the code and resources for the DSP391m Project, which focuses on developing a weather forecasting model and analyzing historical weather data for three major Vietnamese cities: Ho Chi Minh City, Da Nang, and Hanoi. The project aims to provide accurate weather predictions and insights for better planning and decision-making, particularly in areas such as agriculture, disaster management, and energy planning.

## Team Members
- Huynh Phuoc Truong Sinh
- Ho Quang Hien
- Nguyen Anh Hao

## Introduction
Vietnam's diverse climatic conditions and vulnerability to extreme weather events make accurate weather forecasting crucial. This project leverages historical weather data from 2000 to the present to predict key weather parameters such as temperature, precipitation, and wind conditions. By analyzing and forecasting weather patterns, we aim to provide actionable insights for various sectors.

## Objectives
- Develop a weather forecasting model for Ho Chi Minh City, Da Nang, and Hanoi
- Analyze historical weather data to identify trends and patterns
- Compare the performance of various machine learning and deep learning models for weather prediction
- Provide visualizations and dashboards for easy interpretation of results

## Data Description

### Geographic Focus
- Cities: Ho Chi Minh City, Da Nang, Hanoi
- Time Period: From 2000-01-01 to the present
- Data Size: Approximately ~9,000 rows of data for each city
- Format: CSV

### Features
The dataset includes the following features:
- Name: City name
- Datetime: Date and time
- tempmax: Maximum temperature (Celsius)
- tempmin: Minimum temperature (Celsius)
- temp: Average temperature (Celsius)
- feelslikemax: Maximum "feels like" temperature
- feelslikemin: Minimum "feels like" temperature
- feelslike: Average "feels like" temperature
- dew: Dew point (Celsius)
- humidity: Relative humidity (%)
- precip: Precipitation (mm)
- precipprob: Probability of precipitation (%)
- precipcover: Precipitation coverage (%)
- preciptype: Type of precipitation (rain, snow, etc.)
- snow: Snowfall amount (mm)
- snowdepth: Snow depth (mm)
- windgust: Wind gust speed (km/h)
- windspeed: Average wind speed (km/h)
- winddir: Wind direction (degrees)
- sealevelpressure: Sea level pressure (hPa)
- cloudcover: Cloud cover (%)
- visibility: Visibility (km)
- solarradiation: Solar radiation (W/m²)
- solarenergy: Solar energy (MJ/m²)
- uvindex: UV index
- severerisk: Severe weather risk (%)
- sunrise: Sunrise time
- sunset: Sunset time
- moonphase: Moon phase
- conditions: Weather conditions (e.g., Clear, Rain)
- description: Detailed weather description
- icon: Weather icon
- stations: Reporting stations

### Data Source
- API: Weather data is obtained from the Visual Crossing Weather API
- Format: CSV files for historical data

## Methodology

### Benchmark Models
- Baseline: Seasonal ARIMA for time series forecasting
- Advanced Models:
  - Long Short-Term Memory (LSTM) Neural Networks
  - Gradient Boosting Models (e.g., XGBoost, LightGBM)
  - Graph Neural Networks (GNNs)
  - TabPFN for tabular data with high-dimensional features
  - DUET for multivariate time series analysis

### Evaluation Metrics
- Mean Absolute Error (MAE)
- Root Mean Squared Error (RMSE)
- R-Squared (R²)
- Mean Squared Error (MSE)
- Mean Absolute Percentage Error (MAPE)

## Timeline
The project is divided into an 8-week timeline:
1. Week 1-2: Data Collection and Cleaning
2. Week 3: Exploratory Data Analysis (EDA)
3. Week 4: Model Selection and Baseline
4. Week 5-6: Advanced Modeling
5. Week 7: Visualization and Reporting
6. Week 8: Final Presentation and Documentation

## Installation
To set up the project locally, follow these steps:

1. Clone the repository:
```bash
git clone https://github.com/TruongSinhAI/Weather-Forecasting-and-Analysis-for-Key-Vietnamese-Cities.git
```

2. Navigate to the project directory:
```bash
cd Weather-Forecasting-and-Analysis-for-Key-Vietnamese-Cities
```

3. Install the required dependencies:
```bash
pip install -r requirements.txt
```

## Usage
Updating later

## Contributing
Contributions are welcome! If you'd like to contribute, please follow these steps:
1. Fork the repository
2. Create a new branch for your feature or bugfix
3. Commit your changes
4. Submit a pull request

## License
This project is licensed under the MIT License. See the LICENSE file for more details.

## Contact
For any questions or suggestions, please contact:
- Huynh Phuoc Truong Sinh: [sinhhptse173032@fpt.edu.vn]
- Ho Quang Hien
- Nguyen Anh Hao

*Note: This README will be updated as the project progresses. Stay tuned for more details!*
