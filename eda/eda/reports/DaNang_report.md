# EDA Report for DaNang

## Executive Summary
This report provides an Exploratory Data Analysis (EDA) for the weather data of {city_name}. It includes dataset overview, missing value analysis, statistical summaries, correlation analysis, temporal analysis, categorical feature analysis, and data quality evaluation.

## Dataset Overview
This section provides a general overview of the dataset.

* **Number of records:** 9179
* **Time period:** 2000-01-01 00:00:00 to 2025-02-13 00:00:00
* **Number of features:** 37

## Missing Values
This section details the missing values present in the dataset.

* **preciptype**: 4298 missing values
* **snow**: 5448 missing values
* **snowdepth**: 5463 missing values
* **windgust**: 5322 missing values
* **sealevelpressure**: 9179 missing values
* **solarradiation**: 3653 missing values
* **solarenergy**: 3653 missing values
* **uvindex**: 3653 missing values
* **severerisk**: 8736 missing values

## Key Weather Statistics (Numerical)
This section presents descriptive statistics for the numerical weather metrics.

### tempmax
* **Average:** 30.10
* **Maximum:** 42.70
* **Minimum:** 16.10

### tempmin
* **Average:** 23.28
* **Maximum:** 31.00
* **Minimum:** 13.00

### temp
* **Average:** 26.33
* **Maximum:** 34.50
* **Minimum:** 15.80

### feelslikemax
* **Average:** 34.21
* **Maximum:** 56.10
* **Minimum:** 16.10

### feelslikemin
* **Average:** 23.58
* **Maximum:** 35.20
* **Minimum:** 13.00

### feelslike
* **Average:** 28.42
* **Maximum:** 40.90
* **Minimum:** 15.80

### dew
* **Average:** 22.17
* **Maximum:** 26.70
* **Minimum:** 10.20

### humidity
* **Average:** 79.23
* **Maximum:** 98.90
* **Minimum:** 42.70

### precip
* **Average:** 6.64
* **Maximum:** 632.67
* **Minimum:** 0.00

### precipprob
* **Average:** 52.57
* **Maximum:** 100.00
* **Minimum:** 0.00

### precipcover
* **Average:** 5.00
* **Maximum:** 100.00
* **Minimum:** 0.00

### snow
* **Average:** 0.00
* **Maximum:** 0.00
* **Minimum:** 0.00

### snowdepth
* **Average:** 0.00
* **Maximum:** 0.00
* **Minimum:** 0.00

### windgust
* **Average:** 29.32
* **Maximum:** 129.00
* **Minimum:** 12.20

### windspeed
* **Average:** 18.73
* **Maximum:** 156.20
* **Minimum:** 3.60

### winddir
* **Average:** 160.05
* **Maximum:** 360.00
* **Minimum:** 0.00

### sealevelpressure
* **Average:** nan
* **Maximum:** nan
* **Minimum:** nan

### cloudcover
* **Average:** 68.55
* **Maximum:** 100.00
* **Minimum:** 17.60

### visibility
* **Average:** 9.71
* **Maximum:** 76.80
* **Minimum:** 2.70

### solarradiation
* **Average:** 196.59
* **Maximum:** 327.10
* **Minimum:** 0.00

### solarenergy
* **Average:** 16.98
* **Maximum:** 28.30
* **Minimum:** 0.00

### uvindex
* **Average:** 7.03
* **Maximum:** 10.00
* **Minimum:** 0.00

### severerisk
* **Average:** 27.14
* **Maximum:** 75.00
* **Minimum:** 10.00

### moonphase
* **Average:** 0.48
* **Maximum:** 0.98
* **Minimum:** 0.00

### month
* **Average:** 6.50
* **Maximum:** 12.00
* **Minimum:** 1.00

### year
* **Average:** 2012.07
* **Maximum:** 2025.00
* **Minimum:** 2000.00

### day
* **Average:** 15.72
* **Maximum:** 31.00
* **Minimum:** 1.00

### dayofweek
* **Average:** 3.00
* **Maximum:** 6.00
* **Minimum:** 0.00

## Correlation Analysis
Correlation analysis helps to understand the linear relationships between numerical features. The heatmap below visualizes the correlation matrix.

![Correlation Matrix](../plots/DaNang_correlation.png)

## Numerical Analysis Plots
Distributions and box plots of key numerical metrics are shown below to understand data spread and potential outliers.

![Distributions](../plots/DaNang_distributions.png)
![Box Plots](../plots/DaNang_boxplots.png)

## Temporal Analysis
This section explores the temporal patterns in the weather data, including monthly and daily trends.

![Monthly Temperature](../plots/DaNang_monthly_temp.png)
![Daily Temperature](../plots/DaNang_daily_temp.png)
![Temperature vs Humidity](../plots/DaNang_temp_humidity.png)

## Advanced Temporal Analysis
Advanced time series analysis, including rolling statistics, ACF/PACF plots, and seasonal decomposition, are presented here.

![Temperature Rolling Stats](../plots/DaNang_temp_rolling.png)
![ACF and PACF](../plots/DaNang_acf_pacf.png)
![Seasonal Decomposition](../plots/DaNang_seasonal_decompose.png)

## Categorical Analysis
Analysis of categorical features, including value counts and distribution plots where applicable.

### name Analysis
Column 'name' is constant with only 1 unique value. No further analysis is provided.

### preciptype Analysis
Column 'preciptype' is constant with only 1 unique value. No further analysis is provided.

### conditions Analysis
Value Counts:
* **Partially cloudy**: 4269
* **Rain, Partially cloudy**: 3858
* **Rain, Overcast**: 967
* **Overcast**: 81
* **Clear**: 4

![Count Plot for conditions](../plots/DaNang_conditions_countplot.png)

### description Analysis
Value Counts (Top 20):
* **Partly cloudy throughout the day.**: 4205
* **Partly cloudy throughout the day with rain.**: 1032
* **Partly cloudy throughout the day with late afternoon rain.**: 815
* **Partly cloudy throughout the day with a chance of rain throughout the day.**: 623
* **Partly cloudy throughout the day with early morning rain.**: 588
* **Cloudy skies throughout the day with a chance of rain throughout the day.**: 494
* **Cloudy skies throughout the day with rain.**: 273
* **Partly cloudy throughout the day with afternoon rain.**: 248
* **Partly cloudy throughout the day with rain in the morning and afternoon.**: 194
* **Partly cloudy throughout the day with morning rain.**: 194
* **Partly cloudy throughout the day with rain clearing later.**: 132
* **Cloudy skies throughout the day.**: 81
* **Cloudy skies throughout the day with rain in the morning and afternoon.**: 58
* **Cloudy skies throughout the day with afternoon rain.**: 43
* **Clearing in the afternoon.**: 41
* **Cloudy skies throughout the day with early morning rain.**: 34
* **Cloudy skies throughout the day with late afternoon rain.**: 32
* **Becoming cloudy in the afternoon.**: 24
* **Cloudy skies throughout the day with morning rain.**: 18
* **Cloudy skies throughout the day with rain clearing later.**: 15

![Top Value Count Plot for description](../plots/DaNang_description_top_countplot.png)

### icon Analysis
Value Counts:
* **rain**: 4825
* **partly-cloudy-day**: 4264
* **cloudy**: 80
* **wind**: 6
* **clear-day**: 4

![Count Plot for icon](../plots/DaNang_icon_countplot.png)

### stations Analysis
Value Counts:
* **['48855099999', '48852099999']**: 3646
* **['48855099999', 'VVDN', '48852099999']**: 3017
* **['48855099999', 'VVDN', '48852099999', 'VVPB']**: 2222
* **['48855099999', 'VVDN', '48852099999', 'remote']**: 159
* **['48855099999', 'VVDN', '48852099999', 'VVPB', 'remote']**: 98
* **['VVDN', 'VVPB']**: 19
* **['48855099999']**: 9
* **['48855099999', '48852099999', 'remote']**: 6
* **['VVDN', 'VVPB', 'remote']**: 2
* **['48852099999']**: 1

![Count Plot for stations](../plots/DaNang_stations_countplot.png)

## Numerical vs Categorical Analysis
Box plots showing the distribution of numerical features across different categories (for low cardinality categorical features).

### tempmax by name
![Box Plot: tempmax by name](../plots/DaNang_tempmax_by_name_boxplot.png)

### tempmin by name
![Box Plot: tempmin by name](../plots/DaNang_tempmin_by_name_boxplot.png)

### temp by name
![Box Plot: temp by name](../plots/DaNang_temp_by_name_boxplot.png)

### feelslikemax by name
![Box Plot: feelslikemax by name](../plots/DaNang_feelslikemax_by_name_boxplot.png)

### feelslikemin by name
![Box Plot: feelslikemin by name](../plots/DaNang_feelslikemin_by_name_boxplot.png)

### feelslike by name
![Box Plot: feelslike by name](../plots/DaNang_feelslike_by_name_boxplot.png)

### dew by name
![Box Plot: dew by name](../plots/DaNang_dew_by_name_boxplot.png)

### humidity by name
![Box Plot: humidity by name](../plots/DaNang_humidity_by_name_boxplot.png)

### precip by name
![Box Plot: precip by name](../plots/DaNang_precip_by_name_boxplot.png)

### precipprob by name
![Box Plot: precipprob by name](../plots/DaNang_precipprob_by_name_boxplot.png)

### precipcover by name
![Box Plot: precipcover by name](../plots/DaNang_precipcover_by_name_boxplot.png)

### snow by name
![Box Plot: snow by name](../plots/DaNang_snow_by_name_boxplot.png)

### snowdepth by name
![Box Plot: snowdepth by name](../plots/DaNang_snowdepth_by_name_boxplot.png)

### windgust by name
![Box Plot: windgust by name](../plots/DaNang_windgust_by_name_boxplot.png)

### windspeed by name
![Box Plot: windspeed by name](../plots/DaNang_windspeed_by_name_boxplot.png)

### winddir by name
![Box Plot: winddir by name](../plots/DaNang_winddir_by_name_boxplot.png)

### sealevelpressure by name
![Box Plot: sealevelpressure by name](../plots/DaNang_sealevelpressure_by_name_boxplot.png)

### cloudcover by name
![Box Plot: cloudcover by name](../plots/DaNang_cloudcover_by_name_boxplot.png)

### visibility by name
![Box Plot: visibility by name](../plots/DaNang_visibility_by_name_boxplot.png)

### solarradiation by name
![Box Plot: solarradiation by name](../plots/DaNang_solarradiation_by_name_boxplot.png)

### solarenergy by name
![Box Plot: solarenergy by name](../plots/DaNang_solarenergy_by_name_boxplot.png)

### uvindex by name
![Box Plot: uvindex by name](../plots/DaNang_uvindex_by_name_boxplot.png)

### severerisk by name
![Box Plot: severerisk by name](../plots/DaNang_severerisk_by_name_boxplot.png)

### moonphase by name
![Box Plot: moonphase by name](../plots/DaNang_moonphase_by_name_boxplot.png)

### month by name
![Box Plot: month by name](../plots/DaNang_month_by_name_boxplot.png)

### year by name
![Box Plot: year by name](../plots/DaNang_year_by_name_boxplot.png)

### day by name
![Box Plot: day by name](../plots/DaNang_day_by_name_boxplot.png)

### dayofweek by name
![Box Plot: dayofweek by name](../plots/DaNang_dayofweek_by_name_boxplot.png)

### tempmax by preciptype
![Box Plot: tempmax by preciptype](../plots/DaNang_tempmax_by_preciptype_boxplot.png)

### tempmin by preciptype
![Box Plot: tempmin by preciptype](../plots/DaNang_tempmin_by_preciptype_boxplot.png)

### temp by preciptype
![Box Plot: temp by preciptype](../plots/DaNang_temp_by_preciptype_boxplot.png)

### feelslikemax by preciptype
![Box Plot: feelslikemax by preciptype](../plots/DaNang_feelslikemax_by_preciptype_boxplot.png)

### feelslikemin by preciptype
![Box Plot: feelslikemin by preciptype](../plots/DaNang_feelslikemin_by_preciptype_boxplot.png)

### feelslike by preciptype
![Box Plot: feelslike by preciptype](../plots/DaNang_feelslike_by_preciptype_boxplot.png)

### dew by preciptype
![Box Plot: dew by preciptype](../plots/DaNang_dew_by_preciptype_boxplot.png)

### humidity by preciptype
![Box Plot: humidity by preciptype](../plots/DaNang_humidity_by_preciptype_boxplot.png)

### precip by preciptype
![Box Plot: precip by preciptype](../plots/DaNang_precip_by_preciptype_boxplot.png)

### precipprob by preciptype
![Box Plot: precipprob by preciptype](../plots/DaNang_precipprob_by_preciptype_boxplot.png)

### precipcover by preciptype
![Box Plot: precipcover by preciptype](../plots/DaNang_precipcover_by_preciptype_boxplot.png)

### snow by preciptype
![Box Plot: snow by preciptype](../plots/DaNang_snow_by_preciptype_boxplot.png)

### snowdepth by preciptype
![Box Plot: snowdepth by preciptype](../plots/DaNang_snowdepth_by_preciptype_boxplot.png)

### windgust by preciptype
![Box Plot: windgust by preciptype](../plots/DaNang_windgust_by_preciptype_boxplot.png)

### windspeed by preciptype
![Box Plot: windspeed by preciptype](../plots/DaNang_windspeed_by_preciptype_boxplot.png)

### winddir by preciptype
![Box Plot: winddir by preciptype](../plots/DaNang_winddir_by_preciptype_boxplot.png)

### sealevelpressure by preciptype
![Box Plot: sealevelpressure by preciptype](../plots/DaNang_sealevelpressure_by_preciptype_boxplot.png)

### cloudcover by preciptype
![Box Plot: cloudcover by preciptype](../plots/DaNang_cloudcover_by_preciptype_boxplot.png)

### visibility by preciptype
![Box Plot: visibility by preciptype](../plots/DaNang_visibility_by_preciptype_boxplot.png)

### solarradiation by preciptype
![Box Plot: solarradiation by preciptype](../plots/DaNang_solarradiation_by_preciptype_boxplot.png)

### solarenergy by preciptype
![Box Plot: solarenergy by preciptype](../plots/DaNang_solarenergy_by_preciptype_boxplot.png)

### uvindex by preciptype
![Box Plot: uvindex by preciptype](../plots/DaNang_uvindex_by_preciptype_boxplot.png)

### severerisk by preciptype
![Box Plot: severerisk by preciptype](../plots/DaNang_severerisk_by_preciptype_boxplot.png)

### moonphase by preciptype
![Box Plot: moonphase by preciptype](../plots/DaNang_moonphase_by_preciptype_boxplot.png)

### month by preciptype
![Box Plot: month by preciptype](../plots/DaNang_month_by_preciptype_boxplot.png)

### year by preciptype
![Box Plot: year by preciptype](../plots/DaNang_year_by_preciptype_boxplot.png)

### day by preciptype
![Box Plot: day by preciptype](../plots/DaNang_day_by_preciptype_boxplot.png)

### dayofweek by preciptype
![Box Plot: dayofweek by preciptype](../plots/DaNang_dayofweek_by_preciptype_boxplot.png)

### tempmax by conditions
![Box Plot: tempmax by conditions](../plots/DaNang_tempmax_by_conditions_boxplot.png)

### tempmin by conditions
![Box Plot: tempmin by conditions](../plots/DaNang_tempmin_by_conditions_boxplot.png)

### temp by conditions
![Box Plot: temp by conditions](../plots/DaNang_temp_by_conditions_boxplot.png)

### feelslikemax by conditions
![Box Plot: feelslikemax by conditions](../plots/DaNang_feelslikemax_by_conditions_boxplot.png)

### feelslikemin by conditions
![Box Plot: feelslikemin by conditions](../plots/DaNang_feelslikemin_by_conditions_boxplot.png)

### feelslike by conditions
![Box Plot: feelslike by conditions](../plots/DaNang_feelslike_by_conditions_boxplot.png)

### dew by conditions
![Box Plot: dew by conditions](../plots/DaNang_dew_by_conditions_boxplot.png)

### humidity by conditions
![Box Plot: humidity by conditions](../plots/DaNang_humidity_by_conditions_boxplot.png)

### precip by conditions
![Box Plot: precip by conditions](../plots/DaNang_precip_by_conditions_boxplot.png)

### precipprob by conditions
![Box Plot: precipprob by conditions](../plots/DaNang_precipprob_by_conditions_boxplot.png)

### precipcover by conditions
![Box Plot: precipcover by conditions](../plots/DaNang_precipcover_by_conditions_boxplot.png)

### snow by conditions
![Box Plot: snow by conditions](../plots/DaNang_snow_by_conditions_boxplot.png)

### snowdepth by conditions
![Box Plot: snowdepth by conditions](../plots/DaNang_snowdepth_by_conditions_boxplot.png)

### windgust by conditions
![Box Plot: windgust by conditions](../plots/DaNang_windgust_by_conditions_boxplot.png)

### windspeed by conditions
![Box Plot: windspeed by conditions](../plots/DaNang_windspeed_by_conditions_boxplot.png)

### winddir by conditions
![Box Plot: winddir by conditions](../plots/DaNang_winddir_by_conditions_boxplot.png)

### sealevelpressure by conditions
![Box Plot: sealevelpressure by conditions](../plots/DaNang_sealevelpressure_by_conditions_boxplot.png)

### cloudcover by conditions
![Box Plot: cloudcover by conditions](../plots/DaNang_cloudcover_by_conditions_boxplot.png)

### visibility by conditions
![Box Plot: visibility by conditions](../plots/DaNang_visibility_by_conditions_boxplot.png)

### solarradiation by conditions
![Box Plot: solarradiation by conditions](../plots/DaNang_solarradiation_by_conditions_boxplot.png)

### solarenergy by conditions
![Box Plot: solarenergy by conditions](../plots/DaNang_solarenergy_by_conditions_boxplot.png)

### uvindex by conditions
![Box Plot: uvindex by conditions](../plots/DaNang_uvindex_by_conditions_boxplot.png)

### severerisk by conditions
![Box Plot: severerisk by conditions](../plots/DaNang_severerisk_by_conditions_boxplot.png)

### moonphase by conditions
![Box Plot: moonphase by conditions](../plots/DaNang_moonphase_by_conditions_boxplot.png)

### month by conditions
![Box Plot: month by conditions](../plots/DaNang_month_by_conditions_boxplot.png)

### year by conditions
![Box Plot: year by conditions](../plots/DaNang_year_by_conditions_boxplot.png)

### day by conditions
![Box Plot: day by conditions](../plots/DaNang_day_by_conditions_boxplot.png)

### dayofweek by conditions
![Box Plot: dayofweek by conditions](../plots/DaNang_dayofweek_by_conditions_boxplot.png)

### tempmax by icon
![Box Plot: tempmax by icon](../plots/DaNang_tempmax_by_icon_boxplot.png)

### tempmin by icon
![Box Plot: tempmin by icon](../plots/DaNang_tempmin_by_icon_boxplot.png)

### temp by icon
![Box Plot: temp by icon](../plots/DaNang_temp_by_icon_boxplot.png)

### feelslikemax by icon
![Box Plot: feelslikemax by icon](../plots/DaNang_feelslikemax_by_icon_boxplot.png)

### feelslikemin by icon
![Box Plot: feelslikemin by icon](../plots/DaNang_feelslikemin_by_icon_boxplot.png)

### feelslike by icon
![Box Plot: feelslike by icon](../plots/DaNang_feelslike_by_icon_boxplot.png)

### dew by icon
![Box Plot: dew by icon](../plots/DaNang_dew_by_icon_boxplot.png)

### humidity by icon
![Box Plot: humidity by icon](../plots/DaNang_humidity_by_icon_boxplot.png)

### precip by icon
![Box Plot: precip by icon](../plots/DaNang_precip_by_icon_boxplot.png)

### precipprob by icon
![Box Plot: precipprob by icon](../plots/DaNang_precipprob_by_icon_boxplot.png)

### precipcover by icon
![Box Plot: precipcover by icon](../plots/DaNang_precipcover_by_icon_boxplot.png)

### snow by icon
![Box Plot: snow by icon](../plots/DaNang_snow_by_icon_boxplot.png)

### snowdepth by icon
![Box Plot: snowdepth by icon](../plots/DaNang_snowdepth_by_icon_boxplot.png)

### windgust by icon
![Box Plot: windgust by icon](../plots/DaNang_windgust_by_icon_boxplot.png)

### windspeed by icon
![Box Plot: windspeed by icon](../plots/DaNang_windspeed_by_icon_boxplot.png)

### winddir by icon
![Box Plot: winddir by icon](../plots/DaNang_winddir_by_icon_boxplot.png)

### sealevelpressure by icon
![Box Plot: sealevelpressure by icon](../plots/DaNang_sealevelpressure_by_icon_boxplot.png)

### cloudcover by icon
![Box Plot: cloudcover by icon](../plots/DaNang_cloudcover_by_icon_boxplot.png)

### visibility by icon
![Box Plot: visibility by icon](../plots/DaNang_visibility_by_icon_boxplot.png)

### solarradiation by icon
![Box Plot: solarradiation by icon](../plots/DaNang_solarradiation_by_icon_boxplot.png)

### solarenergy by icon
![Box Plot: solarenergy by icon](../plots/DaNang_solarenergy_by_icon_boxplot.png)

### uvindex by icon
![Box Plot: uvindex by icon](../plots/DaNang_uvindex_by_icon_boxplot.png)

### severerisk by icon
![Box Plot: severerisk by icon](../plots/DaNang_severerisk_by_icon_boxplot.png)

### moonphase by icon
![Box Plot: moonphase by icon](../plots/DaNang_moonphase_by_icon_boxplot.png)

### month by icon
![Box Plot: month by icon](../plots/DaNang_month_by_icon_boxplot.png)

### year by icon
![Box Plot: year by icon](../plots/DaNang_year_by_icon_boxplot.png)

### day by icon
![Box Plot: day by icon](../plots/DaNang_day_by_icon_boxplot.png)

### dayofweek by icon
![Box Plot: dayofweek by icon](../plots/DaNang_dayofweek_by_icon_boxplot.png)

### tempmax by stations
![Box Plot: tempmax by stations](../plots/DaNang_tempmax_by_stations_boxplot.png)

### tempmin by stations
![Box Plot: tempmin by stations](../plots/DaNang_tempmin_by_stations_boxplot.png)

### temp by stations
![Box Plot: temp by stations](../plots/DaNang_temp_by_stations_boxplot.png)

### feelslikemax by stations
![Box Plot: feelslikemax by stations](../plots/DaNang_feelslikemax_by_stations_boxplot.png)

### feelslikemin by stations
![Box Plot: feelslikemin by stations](../plots/DaNang_feelslikemin_by_stations_boxplot.png)

### feelslike by stations
![Box Plot: feelslike by stations](../plots/DaNang_feelslike_by_stations_boxplot.png)

### dew by stations
![Box Plot: dew by stations](../plots/DaNang_dew_by_stations_boxplot.png)

### humidity by stations
![Box Plot: humidity by stations](../plots/DaNang_humidity_by_stations_boxplot.png)

### precip by stations
![Box Plot: precip by stations](../plots/DaNang_precip_by_stations_boxplot.png)

### precipprob by stations
![Box Plot: precipprob by stations](../plots/DaNang_precipprob_by_stations_boxplot.png)

### precipcover by stations
![Box Plot: precipcover by stations](../plots/DaNang_precipcover_by_stations_boxplot.png)

### snow by stations
![Box Plot: snow by stations](../plots/DaNang_snow_by_stations_boxplot.png)

### snowdepth by stations
![Box Plot: snowdepth by stations](../plots/DaNang_snowdepth_by_stations_boxplot.png)

### windgust by stations
![Box Plot: windgust by stations](../plots/DaNang_windgust_by_stations_boxplot.png)

### windspeed by stations
![Box Plot: windspeed by stations](../plots/DaNang_windspeed_by_stations_boxplot.png)

### winddir by stations
![Box Plot: winddir by stations](../plots/DaNang_winddir_by_stations_boxplot.png)

### sealevelpressure by stations
![Box Plot: sealevelpressure by stations](../plots/DaNang_sealevelpressure_by_stations_boxplot.png)

### cloudcover by stations
![Box Plot: cloudcover by stations](../plots/DaNang_cloudcover_by_stations_boxplot.png)

### visibility by stations
![Box Plot: visibility by stations](../plots/DaNang_visibility_by_stations_boxplot.png)

### solarradiation by stations
![Box Plot: solarradiation by stations](../plots/DaNang_solarradiation_by_stations_boxplot.png)

### solarenergy by stations
![Box Plot: solarenergy by stations](../plots/DaNang_solarenergy_by_stations_boxplot.png)

### uvindex by stations
![Box Plot: uvindex by stations](../plots/DaNang_uvindex_by_stations_boxplot.png)

### severerisk by stations
![Box Plot: severerisk by stations](../plots/DaNang_severerisk_by_stations_boxplot.png)

### moonphase by stations
![Box Plot: moonphase by stations](../plots/DaNang_moonphase_by_stations_boxplot.png)

### month by stations
![Box Plot: month by stations](../plots/DaNang_month_by_stations_boxplot.png)

### year by stations
![Box Plot: year by stations](../plots/DaNang_year_by_stations_boxplot.png)

### day by stations
![Box Plot: day by stations](../plots/DaNang_day_by_stations_boxplot.png)

### dayofweek by stations
![Box Plot: dayofweek by stations](../plots/DaNang_dayofweek_by_stations_boxplot.png)

## Evaluation Summary
This section summarizes the data quality evaluation. Please refer to the detailed evaluation report for in-depth analysis of outliers, skewness/kurtosis, and stationarity.

Please refer to the detailed evaluation report: `DaNang_evaluation.txt`.
This file includes information about outliers, skewness/kurtosis, and stationarity test results.

## Conclusion
Based on the EDA, key findings for {city_name} include: ... (Summary of key findings, e.g., important correlations, trends, data quality issues).