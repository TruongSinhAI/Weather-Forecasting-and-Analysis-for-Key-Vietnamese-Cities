# EDA Report for HoChiMinh

## Executive Summary
This report provides an Exploratory Data Analysis (EDA) for the weather data of {city_name}. It includes dataset overview, missing value analysis, statistical summaries, correlation analysis, temporal analysis, categorical feature analysis, and data quality evaluation.

## Dataset Overview
This section provides a general overview of the dataset.

* **Number of records:** 9178
* **Time period:** 2000-01-01 00:00:00 to 2025-02-13 00:00:00
* **Number of features:** 37

## Missing Values
This section details the missing values present in the dataset.

* **precip**: 3653 missing values
* **preciptype**: 5265 missing values
* **snow**: 5448 missing values
* **snowdepth**: 5448 missing values
* **windgust**: 5335 missing values
* **sealevelpressure**: 9178 missing values
* **solarradiation**: 3653 missing values
* **solarenergy**: 3653 missing values
* **uvindex**: 3653 missing values
* **severerisk**: 8736 missing values

## Key Weather Statistics (Numerical)
This section presents descriptive statistics for the numerical weather metrics.

### tempmax
* **Average:** 32.75
* **Maximum:** 39.00
* **Minimum:** 21.10

### tempmin
* **Average:** 24.38
* **Maximum:** 30.00
* **Minimum:** 7.00

### temp
* **Average:** 27.90
* **Maximum:** 33.00
* **Minimum:** 19.10

### feelslikemax
* **Average:** 38.07
* **Maximum:** 48.70
* **Minimum:** 21.10

### feelslikemin
* **Average:** 24.75
* **Maximum:** 40.00
* **Minimum:** 5.10

### feelslike
* **Average:** 30.64
* **Maximum:** 42.00
* **Minimum:** 19.10

### dew
* **Average:** 23.33
* **Maximum:** 27.90
* **Minimum:** 12.30

### humidity
* **Average:** 78.12
* **Maximum:** 99.80
* **Minimum:** 49.50

### precip
* **Average:** 4.72
* **Maximum:** 227.20
* **Minimum:** 0.00

### precipprob
* **Average:** 42.53
* **Maximum:** 100.00
* **Minimum:** 0.00

### precipcover
* **Average:** 9.84
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
* **Average:** 32.01
* **Maximum:** 216.00
* **Minimum:** 8.30

### windspeed
* **Average:** 19.72
* **Maximum:** 50.40
* **Minimum:** 7.20

### winddir
* **Average:** 182.08
* **Maximum:** 359.90
* **Minimum:** 0.00

### sealevelpressure
* **Average:** nan
* **Maximum:** nan
* **Minimum:** nan

### cloudcover
* **Average:** 57.18
* **Maximum:** 100.00
* **Minimum:** 9.70

### visibility
* **Average:** 9.75
* **Maximum:** 76.60
* **Minimum:** 4.40

### solarradiation
* **Average:** 208.10
* **Maximum:** 320.20
* **Minimum:** 0.00

### solarenergy
* **Average:** 17.97
* **Maximum:** 27.80
* **Minimum:** 0.00

### uvindex
* **Average:** 7.51
* **Maximum:** 10.00
* **Minimum:** 0.00

### severerisk
* **Average:** 32.49
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

![Correlation Matrix](../plots/HoChiMinh_correlation.png)

## Numerical Analysis Plots
Distributions and box plots of key numerical metrics are shown below to understand data spread and potential outliers.

![Distributions](../plots/HoChiMinh_distributions.png)
![Box Plots](../plots/HoChiMinh_boxplots.png)

## Temporal Analysis
This section explores the temporal patterns in the weather data, including monthly and daily trends.

![Monthly Temperature](../plots/HoChiMinh_monthly_temp.png)
![Daily Temperature](../plots/HoChiMinh_daily_temp.png)
![Temperature vs Humidity](../plots/HoChiMinh_temp_humidity.png)

## Advanced Temporal Analysis
Advanced time series analysis, including rolling statistics, ACF/PACF plots, and seasonal decomposition, are presented here.

![Temperature Rolling Stats](../plots/HoChiMinh_temp_rolling.png)
![ACF and PACF](../plots/HoChiMinh_acf_pacf.png)
![Seasonal Decomposition](../plots/HoChiMinh_seasonal_decompose.png)

## Categorical Analysis
Analysis of categorical features, including value counts and distribution plots where applicable.

### name Analysis
Column 'name' is constant with only 1 unique value. No further analysis is provided.

### preciptype Analysis
Column 'preciptype' is constant with only 1 unique value. No further analysis is provided.

### conditions Analysis
Value Counts:
* **Partially cloudy**: 5204
* **Rain, Partially cloudy**: 3870
* **Overcast**: 64
* **Rain, Overcast**: 33
* **Clear**: 7

![Count Plot for conditions](../plots/HoChiMinh_conditions_countplot.png)

### description Analysis
Value Counts (Top 20):
* **Partly cloudy throughout the day.**: 5098
* **Partly cloudy throughout the day with rain.**: 994
* **Partly cloudy throughout the day with a chance of rain throughout the day.**: 830
* **Partly cloudy throughout the day with late afternoon rain.**: 744
* **Partly cloudy throughout the day with afternoon rain.**: 406
* **Partly cloudy throughout the day with rain in the morning and afternoon.**: 399
* **Partly cloudy throughout the day with early morning rain.**: 267
* **Partly cloudy throughout the day with morning rain.**: 145
* **Becoming cloudy in the afternoon.**: 77
* **Cloudy skies throughout the day.**: 64
* **Partly cloudy throughout the day with rain clearing later.**: 38
* **Clearing in the afternoon.**: 29
* **Cloudy skies throughout the day with a chance of rain throughout the day.**: 13
* **Becoming cloudy in the afternoon with afternoon rain.**: 12
* **Becoming cloudy in the afternoon with rain.**: 11
* **Becoming cloudy in the afternoon with late afternoon rain.**: 9
* **Cloudy skies throughout the day with rain.**: 8
* **Clear conditions throughout the day.**: 7
* **Becoming cloudy in the afternoon with rain in the morning and afternoon.**: 6
* **Cloudy skies throughout the day with early morning rain.**: 4

![Top Value Count Plot for description](../plots/HoChiMinh_description_top_countplot.png)

### icon Analysis
Value Counts:
* **partly-cloudy-day**: 5204
* **rain**: 3903
* **cloudy**: 63
* **clear-day**: 7
* **wind**: 1

![Count Plot for icon](../plots/HoChiMinh_icon_countplot.png)

### stations Analysis
Value Counts:
* **['48894099999', '48900099999', 'VVTS']**: 4037
* **['48900099999']**: 3653
* **['48900099999', 'VVTS']**: 878
* **['48900099999', 'VVTS', 'remote']**: 418
* **['48894099999', '48900099999', 'VVTS', 'remote']**: 160
* **['VVTS']**: 18
* **['48894099999', 'remote']**: 4
* **['48894099999', '48900099999', 'remote']**: 3
* **['48894099999', '48900099999']**: 2
* **['VVTS', 'remote']**: 2
* **['48900099999', '48904099999', 'VVTS']**: 1
* **['48894099999', 'VVTS']**: 1
* **['48894099999', 'VVTS', 'remote']**: 1

![Count Plot for stations](../plots/HoChiMinh_stations_countplot.png)

## Numerical vs Categorical Analysis
Box plots showing the distribution of numerical features across different categories (for low cardinality categorical features).

### tempmax by name
![Box Plot: tempmax by name](../plots/HoChiMinh_tempmax_by_name_boxplot.png)

### tempmin by name
![Box Plot: tempmin by name](../plots/HoChiMinh_tempmin_by_name_boxplot.png)

### temp by name
![Box Plot: temp by name](../plots/HoChiMinh_temp_by_name_boxplot.png)

### feelslikemax by name
![Box Plot: feelslikemax by name](../plots/HoChiMinh_feelslikemax_by_name_boxplot.png)

### feelslikemin by name
![Box Plot: feelslikemin by name](../plots/HoChiMinh_feelslikemin_by_name_boxplot.png)

### feelslike by name
![Box Plot: feelslike by name](../plots/HoChiMinh_feelslike_by_name_boxplot.png)

### dew by name
![Box Plot: dew by name](../plots/HoChiMinh_dew_by_name_boxplot.png)

### humidity by name
![Box Plot: humidity by name](../plots/HoChiMinh_humidity_by_name_boxplot.png)

### precip by name
![Box Plot: precip by name](../plots/HoChiMinh_precip_by_name_boxplot.png)

### precipprob by name
![Box Plot: precipprob by name](../plots/HoChiMinh_precipprob_by_name_boxplot.png)

### precipcover by name
![Box Plot: precipcover by name](../plots/HoChiMinh_precipcover_by_name_boxplot.png)

### snow by name
![Box Plot: snow by name](../plots/HoChiMinh_snow_by_name_boxplot.png)

### snowdepth by name
![Box Plot: snowdepth by name](../plots/HoChiMinh_snowdepth_by_name_boxplot.png)

### windgust by name
![Box Plot: windgust by name](../plots/HoChiMinh_windgust_by_name_boxplot.png)

### windspeed by name
![Box Plot: windspeed by name](../plots/HoChiMinh_windspeed_by_name_boxplot.png)

### winddir by name
![Box Plot: winddir by name](../plots/HoChiMinh_winddir_by_name_boxplot.png)

### sealevelpressure by name
![Box Plot: sealevelpressure by name](../plots/HoChiMinh_sealevelpressure_by_name_boxplot.png)

### cloudcover by name
![Box Plot: cloudcover by name](../plots/HoChiMinh_cloudcover_by_name_boxplot.png)

### visibility by name
![Box Plot: visibility by name](../plots/HoChiMinh_visibility_by_name_boxplot.png)

### solarradiation by name
![Box Plot: solarradiation by name](../plots/HoChiMinh_solarradiation_by_name_boxplot.png)

### solarenergy by name
![Box Plot: solarenergy by name](../plots/HoChiMinh_solarenergy_by_name_boxplot.png)

### uvindex by name
![Box Plot: uvindex by name](../plots/HoChiMinh_uvindex_by_name_boxplot.png)

### severerisk by name
![Box Plot: severerisk by name](../plots/HoChiMinh_severerisk_by_name_boxplot.png)

### moonphase by name
![Box Plot: moonphase by name](../plots/HoChiMinh_moonphase_by_name_boxplot.png)

### month by name
![Box Plot: month by name](../plots/HoChiMinh_month_by_name_boxplot.png)

### year by name
![Box Plot: year by name](../plots/HoChiMinh_year_by_name_boxplot.png)

### day by name
![Box Plot: day by name](../plots/HoChiMinh_day_by_name_boxplot.png)

### dayofweek by name
![Box Plot: dayofweek by name](../plots/HoChiMinh_dayofweek_by_name_boxplot.png)

### tempmax by preciptype
![Box Plot: tempmax by preciptype](../plots/HoChiMinh_tempmax_by_preciptype_boxplot.png)

### tempmin by preciptype
![Box Plot: tempmin by preciptype](../plots/HoChiMinh_tempmin_by_preciptype_boxplot.png)

### temp by preciptype
![Box Plot: temp by preciptype](../plots/HoChiMinh_temp_by_preciptype_boxplot.png)

### feelslikemax by preciptype
![Box Plot: feelslikemax by preciptype](../plots/HoChiMinh_feelslikemax_by_preciptype_boxplot.png)

### feelslikemin by preciptype
![Box Plot: feelslikemin by preciptype](../plots/HoChiMinh_feelslikemin_by_preciptype_boxplot.png)

### feelslike by preciptype
![Box Plot: feelslike by preciptype](../plots/HoChiMinh_feelslike_by_preciptype_boxplot.png)

### dew by preciptype
![Box Plot: dew by preciptype](../plots/HoChiMinh_dew_by_preciptype_boxplot.png)

### humidity by preciptype
![Box Plot: humidity by preciptype](../plots/HoChiMinh_humidity_by_preciptype_boxplot.png)

### precip by preciptype
![Box Plot: precip by preciptype](../plots/HoChiMinh_precip_by_preciptype_boxplot.png)

### precipprob by preciptype
![Box Plot: precipprob by preciptype](../plots/HoChiMinh_precipprob_by_preciptype_boxplot.png)

### precipcover by preciptype
![Box Plot: precipcover by preciptype](../plots/HoChiMinh_precipcover_by_preciptype_boxplot.png)

### snow by preciptype
![Box Plot: snow by preciptype](../plots/HoChiMinh_snow_by_preciptype_boxplot.png)

### snowdepth by preciptype
![Box Plot: snowdepth by preciptype](../plots/HoChiMinh_snowdepth_by_preciptype_boxplot.png)

### windgust by preciptype
![Box Plot: windgust by preciptype](../plots/HoChiMinh_windgust_by_preciptype_boxplot.png)

### windspeed by preciptype
![Box Plot: windspeed by preciptype](../plots/HoChiMinh_windspeed_by_preciptype_boxplot.png)

### winddir by preciptype
![Box Plot: winddir by preciptype](../plots/HoChiMinh_winddir_by_preciptype_boxplot.png)

### sealevelpressure by preciptype
![Box Plot: sealevelpressure by preciptype](../plots/HoChiMinh_sealevelpressure_by_preciptype_boxplot.png)

### cloudcover by preciptype
![Box Plot: cloudcover by preciptype](../plots/HoChiMinh_cloudcover_by_preciptype_boxplot.png)

### visibility by preciptype
![Box Plot: visibility by preciptype](../plots/HoChiMinh_visibility_by_preciptype_boxplot.png)

### solarradiation by preciptype
![Box Plot: solarradiation by preciptype](../plots/HoChiMinh_solarradiation_by_preciptype_boxplot.png)

### solarenergy by preciptype
![Box Plot: solarenergy by preciptype](../plots/HoChiMinh_solarenergy_by_preciptype_boxplot.png)

### uvindex by preciptype
![Box Plot: uvindex by preciptype](../plots/HoChiMinh_uvindex_by_preciptype_boxplot.png)

### severerisk by preciptype
![Box Plot: severerisk by preciptype](../plots/HoChiMinh_severerisk_by_preciptype_boxplot.png)

### moonphase by preciptype
![Box Plot: moonphase by preciptype](../plots/HoChiMinh_moonphase_by_preciptype_boxplot.png)

### month by preciptype
![Box Plot: month by preciptype](../plots/HoChiMinh_month_by_preciptype_boxplot.png)

### year by preciptype
![Box Plot: year by preciptype](../plots/HoChiMinh_year_by_preciptype_boxplot.png)

### day by preciptype
![Box Plot: day by preciptype](../plots/HoChiMinh_day_by_preciptype_boxplot.png)

### dayofweek by preciptype
![Box Plot: dayofweek by preciptype](../plots/HoChiMinh_dayofweek_by_preciptype_boxplot.png)

### tempmax by conditions
![Box Plot: tempmax by conditions](../plots/HoChiMinh_tempmax_by_conditions_boxplot.png)

### tempmin by conditions
![Box Plot: tempmin by conditions](../plots/HoChiMinh_tempmin_by_conditions_boxplot.png)

### temp by conditions
![Box Plot: temp by conditions](../plots/HoChiMinh_temp_by_conditions_boxplot.png)

### feelslikemax by conditions
![Box Plot: feelslikemax by conditions](../plots/HoChiMinh_feelslikemax_by_conditions_boxplot.png)

### feelslikemin by conditions
![Box Plot: feelslikemin by conditions](../plots/HoChiMinh_feelslikemin_by_conditions_boxplot.png)

### feelslike by conditions
![Box Plot: feelslike by conditions](../plots/HoChiMinh_feelslike_by_conditions_boxplot.png)

### dew by conditions
![Box Plot: dew by conditions](../plots/HoChiMinh_dew_by_conditions_boxplot.png)

### humidity by conditions
![Box Plot: humidity by conditions](../plots/HoChiMinh_humidity_by_conditions_boxplot.png)

### precip by conditions
![Box Plot: precip by conditions](../plots/HoChiMinh_precip_by_conditions_boxplot.png)

### precipprob by conditions
![Box Plot: precipprob by conditions](../plots/HoChiMinh_precipprob_by_conditions_boxplot.png)

### precipcover by conditions
![Box Plot: precipcover by conditions](../plots/HoChiMinh_precipcover_by_conditions_boxplot.png)

### snow by conditions
![Box Plot: snow by conditions](../plots/HoChiMinh_snow_by_conditions_boxplot.png)

### snowdepth by conditions
![Box Plot: snowdepth by conditions](../plots/HoChiMinh_snowdepth_by_conditions_boxplot.png)

### windgust by conditions
![Box Plot: windgust by conditions](../plots/HoChiMinh_windgust_by_conditions_boxplot.png)

### windspeed by conditions
![Box Plot: windspeed by conditions](../plots/HoChiMinh_windspeed_by_conditions_boxplot.png)

### winddir by conditions
![Box Plot: winddir by conditions](../plots/HoChiMinh_winddir_by_conditions_boxplot.png)

### sealevelpressure by conditions
![Box Plot: sealevelpressure by conditions](../plots/HoChiMinh_sealevelpressure_by_conditions_boxplot.png)

### cloudcover by conditions
![Box Plot: cloudcover by conditions](../plots/HoChiMinh_cloudcover_by_conditions_boxplot.png)

### visibility by conditions
![Box Plot: visibility by conditions](../plots/HoChiMinh_visibility_by_conditions_boxplot.png)

### solarradiation by conditions
![Box Plot: solarradiation by conditions](../plots/HoChiMinh_solarradiation_by_conditions_boxplot.png)

### solarenergy by conditions
![Box Plot: solarenergy by conditions](../plots/HoChiMinh_solarenergy_by_conditions_boxplot.png)

### uvindex by conditions
![Box Plot: uvindex by conditions](../plots/HoChiMinh_uvindex_by_conditions_boxplot.png)

### severerisk by conditions
![Box Plot: severerisk by conditions](../plots/HoChiMinh_severerisk_by_conditions_boxplot.png)

### moonphase by conditions
![Box Plot: moonphase by conditions](../plots/HoChiMinh_moonphase_by_conditions_boxplot.png)

### month by conditions
![Box Plot: month by conditions](../plots/HoChiMinh_month_by_conditions_boxplot.png)

### year by conditions
![Box Plot: year by conditions](../plots/HoChiMinh_year_by_conditions_boxplot.png)

### day by conditions
![Box Plot: day by conditions](../plots/HoChiMinh_day_by_conditions_boxplot.png)

### dayofweek by conditions
![Box Plot: dayofweek by conditions](../plots/HoChiMinh_dayofweek_by_conditions_boxplot.png)

### tempmax by icon
![Box Plot: tempmax by icon](../plots/HoChiMinh_tempmax_by_icon_boxplot.png)

### tempmin by icon
![Box Plot: tempmin by icon](../plots/HoChiMinh_tempmin_by_icon_boxplot.png)

### temp by icon
![Box Plot: temp by icon](../plots/HoChiMinh_temp_by_icon_boxplot.png)

### feelslikemax by icon
![Box Plot: feelslikemax by icon](../plots/HoChiMinh_feelslikemax_by_icon_boxplot.png)

### feelslikemin by icon
![Box Plot: feelslikemin by icon](../plots/HoChiMinh_feelslikemin_by_icon_boxplot.png)

### feelslike by icon
![Box Plot: feelslike by icon](../plots/HoChiMinh_feelslike_by_icon_boxplot.png)

### dew by icon
![Box Plot: dew by icon](../plots/HoChiMinh_dew_by_icon_boxplot.png)

### humidity by icon
![Box Plot: humidity by icon](../plots/HoChiMinh_humidity_by_icon_boxplot.png)

### precip by icon
![Box Plot: precip by icon](../plots/HoChiMinh_precip_by_icon_boxplot.png)

### precipprob by icon
![Box Plot: precipprob by icon](../plots/HoChiMinh_precipprob_by_icon_boxplot.png)

### precipcover by icon
![Box Plot: precipcover by icon](../plots/HoChiMinh_precipcover_by_icon_boxplot.png)

### snow by icon
![Box Plot: snow by icon](../plots/HoChiMinh_snow_by_icon_boxplot.png)

### snowdepth by icon
![Box Plot: snowdepth by icon](../plots/HoChiMinh_snowdepth_by_icon_boxplot.png)

### windgust by icon
![Box Plot: windgust by icon](../plots/HoChiMinh_windgust_by_icon_boxplot.png)

### windspeed by icon
![Box Plot: windspeed by icon](../plots/HoChiMinh_windspeed_by_icon_boxplot.png)

### winddir by icon
![Box Plot: winddir by icon](../plots/HoChiMinh_winddir_by_icon_boxplot.png)

### sealevelpressure by icon
![Box Plot: sealevelpressure by icon](../plots/HoChiMinh_sealevelpressure_by_icon_boxplot.png)

### cloudcover by icon
![Box Plot: cloudcover by icon](../plots/HoChiMinh_cloudcover_by_icon_boxplot.png)

### visibility by icon
![Box Plot: visibility by icon](../plots/HoChiMinh_visibility_by_icon_boxplot.png)

### solarradiation by icon
![Box Plot: solarradiation by icon](../plots/HoChiMinh_solarradiation_by_icon_boxplot.png)

### solarenergy by icon
![Box Plot: solarenergy by icon](../plots/HoChiMinh_solarenergy_by_icon_boxplot.png)

### uvindex by icon
![Box Plot: uvindex by icon](../plots/HoChiMinh_uvindex_by_icon_boxplot.png)

### severerisk by icon
![Box Plot: severerisk by icon](../plots/HoChiMinh_severerisk_by_icon_boxplot.png)

### moonphase by icon
![Box Plot: moonphase by icon](../plots/HoChiMinh_moonphase_by_icon_boxplot.png)

### month by icon
![Box Plot: month by icon](../plots/HoChiMinh_month_by_icon_boxplot.png)

### year by icon
![Box Plot: year by icon](../plots/HoChiMinh_year_by_icon_boxplot.png)

### day by icon
![Box Plot: day by icon](../plots/HoChiMinh_day_by_icon_boxplot.png)

### dayofweek by icon
![Box Plot: dayofweek by icon](../plots/HoChiMinh_dayofweek_by_icon_boxplot.png)

## Evaluation Summary
This section summarizes the data quality evaluation. Please refer to the detailed evaluation report for in-depth analysis of outliers, skewness/kurtosis, and stationarity.

Please refer to the detailed evaluation report: `HoChiMinh_evaluation.txt`.
This file includes information about outliers, skewness/kurtosis, and stationarity test results.

## Conclusion
Based on the EDA, key findings for {city_name} include: ... (Summary of key findings, e.g., important correlations, trends, data quality issues).