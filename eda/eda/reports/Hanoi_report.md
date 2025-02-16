# EDA Report for Hanoi

## Executive Summary
This report provides an Exploratory Data Analysis (EDA) for the weather data of {city_name}. It includes dataset overview, missing value analysis, statistical summaries, correlation analysis, temporal analysis, categorical feature analysis, and data quality evaluation.

## Dataset Overview
This section provides a general overview of the dataset.

* **Number of records:** 9178
* **Time period:** 2000-01-01 00:00:00 to 2025-02-13 00:00:00
* **Number of features:** 37

## Missing Values
This section details the missing values present in the dataset.

* **precip**: 9 missing values
* **preciptype**: 3994 missing values
* **snow**: 5448 missing values
* **snowdepth**: 5448 missing values
* **windgust**: 5378 missing values
* **sealevelpressure**: 9178 missing values
* **solarradiation**: 3653 missing values
* **solarenergy**: 3653 missing values
* **uvindex**: 3653 missing values
* **severerisk**: 8736 missing values

## Key Weather Statistics (Numerical)
This section presents descriptive statistics for the numerical weather metrics.

### tempmax
* **Average:** 27.96
* **Maximum:** 41.70
* **Minimum:** 8.00

### tempmin
* **Average:** 21.38
* **Maximum:** 31.00
* **Minimum:** 3.80

### temp
* **Average:** 24.35
* **Maximum:** 35.50
* **Minimum:** 7.00

### feelslikemax
* **Average:** 31.83
* **Maximum:** 56.70
* **Minimum:** 6.40

### feelslikemin
* **Average:** 21.94
* **Maximum:** 40.40
* **Minimum:** 0.40

### feelslike
* **Average:** 26.55
* **Maximum:** 46.20
* **Minimum:** 4.60

### dew
* **Average:** 20.21
* **Maximum:** 29.00
* **Minimum:** -2.10

### humidity
* **Average:** 79.39
* **Maximum:** 100.00
* **Minimum:** 31.10

### precip
* **Average:** 4.67
* **Maximum:** 331.24
* **Minimum:** 0.00

### precipprob
* **Average:** 56.35
* **Maximum:** 100.00
* **Minimum:** 0.00

### precipcover
* **Average:** 5.89
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
* **Average:** 27.27
* **Maximum:** 118.80
* **Minimum:** 7.20

### windspeed
* **Average:** 17.81
* **Maximum:** 79.20
* **Minimum:** 4.20

### winddir
* **Average:** 126.39
* **Maximum:** 360.00
* **Minimum:** 0.00

### sealevelpressure
* **Average:** nan
* **Maximum:** nan
* **Minimum:** nan

### cloudcover
* **Average:** 67.33
* **Maximum:** 100.00
* **Minimum:** 0.00

### visibility
* **Average:** 8.25
* **Maximum:** 18.00
* **Minimum:** 1.30

### solarradiation
* **Average:** 163.62
* **Maximum:** 333.50
* **Minimum:** 0.00

### solarenergy
* **Average:** 14.12
* **Maximum:** 28.90
* **Minimum:** 0.00

### uvindex
* **Average:** 6.02
* **Maximum:** 10.00
* **Minimum:** 0.00

### severerisk
* **Average:** 29.14
* **Maximum:** 75.00
* **Minimum:** 5.00

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

![Correlation Matrix](../plots/Hanoi_correlation.png)

## Numerical Analysis Plots
Distributions and box plots of key numerical metrics are shown below to understand data spread and potential outliers.

![Distributions](../plots/Hanoi_distributions.png)
![Box Plots](../plots/Hanoi_boxplots.png)

## Temporal Analysis
This section explores the temporal patterns in the weather data, including monthly and daily trends.

![Monthly Temperature](../plots/Hanoi_monthly_temp.png)
![Daily Temperature](../plots/Hanoi_daily_temp.png)
![Temperature vs Humidity](../plots/Hanoi_temp_humidity.png)

## Advanced Temporal Analysis
Advanced time series analysis, including rolling statistics, ACF/PACF plots, and seasonal decomposition, are presented here.

![Temperature Rolling Stats](../plots/Hanoi_temp_rolling.png)
![ACF and PACF](../plots/Hanoi_acf_pacf.png)
![Seasonal Decomposition](../plots/Hanoi_seasonal_decompose.png)

## Categorical Analysis
Analysis of categorical features, including value counts and distribution plots where applicable.

### name Analysis
Column 'name' is constant with only 1 unique value. No further analysis is provided.

### preciptype Analysis
Column 'preciptype' is constant with only 1 unique value. No further analysis is provided.

### conditions Analysis
Value Counts:
* **Rain, Partially cloudy**: 3704
* **Partially cloudy**: 2852
* **Rain, Overcast**: 1439
* **Clear**: 629
* **Overcast**: 525
* **Rain**: 29

![Count Plot for conditions](../plots/Hanoi_conditions_countplot.png)

### description Analysis
Value Counts (Top 20):
* **Partly cloudy throughout the day.**: 2748
* **Partly cloudy throughout the day with rain.**: 856
* **Clear conditions throughout the day.**: 625
* **Partly cloudy throughout the day with late afternoon rain.**: 607
* **Partly cloudy throughout the day with a chance of rain throughout the day.**: 533
* **Cloudy skies throughout the day.**: 525
* **Partly cloudy throughout the day with rain in the morning and afternoon.**: 437
* **Cloudy skies throughout the day with rain.**: 418
* **Partly cloudy throughout the day with early morning rain.**: 405
* **Partly cloudy throughout the day with afternoon rain.**: 399
* **Partly cloudy throughout the day with morning rain.**: 311
* **Cloudy skies throughout the day with rain in the morning and afternoon.**: 204
* **Cloudy skies throughout the day with a chance of rain throughout the day.**: 200
* **Cloudy skies throughout the day with early morning rain.**: 164
* **Cloudy skies throughout the day with late afternoon rain.**: 152
* **Cloudy skies throughout the day with afternoon rain.**: 148
* **Partly cloudy throughout the day with rain clearing later.**: 134
* **Cloudy skies throughout the day with morning rain.**: 112
* **Clearing in the afternoon.**: 69
* **Cloudy skies throughout the day with rain clearing later.**: 41

![Top Value Count Plot for description](../plots/Hanoi_description_top_countplot.png)

### icon Analysis
Value Counts:
* **rain**: 5172
* **partly-cloudy-day**: 2848
* **clear-day**: 629
* **cloudy**: 525
* **wind**: 4

![Count Plot for icon](../plots/Hanoi_icon_countplot.png)

### stations Analysis
Value Counts (Top 20):
* **['48820099999', '48823099999', '48825099999', '48831099999', 'VVNB']**: 3794
* **['48820099999', '48823099999']**: 3388
* **['48820099999', '48823099999', 'VVNB']**: 765
* **['48820099999', '48825099999', '48831099999', 'VVNB']**: 517
* **['48823099999', '48820099999']**: 246
* **['48820099999', '48823099999', '48825099999', '48831099999', 'VVNB', 'remote']**: 142
* **['48820099999', '48823099999', '48831099999', 'VVNB']**: 125
* **['48820099999', '48823099999', 'VVNB', 'remote']**: 72
* **['48820099999', 'VVNB']**: 18
* **['VVNB']**: 16
* **['48820099999', '48823099999', '48825099999', 'VVNB']**: 13
* **['48820099999', '48823099999', '48825099999', '48831099999', 'remote', 'VVNB']**: 12
* **['48820099999', '48825099999', '48831099999', 'VVNB', 'remote']**: 11
* **['48820099999', '48823099999', '48831099999']**: 9
* **['48820099999']**: 9
* **['48820099999', '48823099999', '48831099999', 'VVNB', 'remote']**: 8
* **['48820099999', '48823099999', 'remote', 'VVNB']**: 7
* **['48823099999', '48820099999', '48825099999', '48831099999', 'VVNB']**: 5
* **['VVNB', 'remote']**: 4
* **['48823099999', '48825099999', '48831099999', 'remote']**: 4

![Top Value Count Plot for stations](../plots/Hanoi_stations_top_countplot.png)

## Numerical vs Categorical Analysis
Box plots showing the distribution of numerical features across different categories (for low cardinality categorical features).

### tempmax by name
![Box Plot: tempmax by name](../plots/Hanoi_tempmax_by_name_boxplot.png)

### tempmin by name
![Box Plot: tempmin by name](../plots/Hanoi_tempmin_by_name_boxplot.png)

### temp by name
![Box Plot: temp by name](../plots/Hanoi_temp_by_name_boxplot.png)

### feelslikemax by name
![Box Plot: feelslikemax by name](../plots/Hanoi_feelslikemax_by_name_boxplot.png)

### feelslikemin by name
![Box Plot: feelslikemin by name](../plots/Hanoi_feelslikemin_by_name_boxplot.png)

### feelslike by name
![Box Plot: feelslike by name](../plots/Hanoi_feelslike_by_name_boxplot.png)

### dew by name
![Box Plot: dew by name](../plots/Hanoi_dew_by_name_boxplot.png)

### humidity by name
![Box Plot: humidity by name](../plots/Hanoi_humidity_by_name_boxplot.png)

### precip by name
![Box Plot: precip by name](../plots/Hanoi_precip_by_name_boxplot.png)

### precipprob by name
![Box Plot: precipprob by name](../plots/Hanoi_precipprob_by_name_boxplot.png)

### precipcover by name
![Box Plot: precipcover by name](../plots/Hanoi_precipcover_by_name_boxplot.png)

### snow by name
![Box Plot: snow by name](../plots/Hanoi_snow_by_name_boxplot.png)

### snowdepth by name
![Box Plot: snowdepth by name](../plots/Hanoi_snowdepth_by_name_boxplot.png)

### windgust by name
![Box Plot: windgust by name](../plots/Hanoi_windgust_by_name_boxplot.png)

### windspeed by name
![Box Plot: windspeed by name](../plots/Hanoi_windspeed_by_name_boxplot.png)

### winddir by name
![Box Plot: winddir by name](../plots/Hanoi_winddir_by_name_boxplot.png)

### sealevelpressure by name
![Box Plot: sealevelpressure by name](../plots/Hanoi_sealevelpressure_by_name_boxplot.png)

### cloudcover by name
![Box Plot: cloudcover by name](../plots/Hanoi_cloudcover_by_name_boxplot.png)

### visibility by name
![Box Plot: visibility by name](../plots/Hanoi_visibility_by_name_boxplot.png)

### solarradiation by name
![Box Plot: solarradiation by name](../plots/Hanoi_solarradiation_by_name_boxplot.png)

### solarenergy by name
![Box Plot: solarenergy by name](../plots/Hanoi_solarenergy_by_name_boxplot.png)

### uvindex by name
![Box Plot: uvindex by name](../plots/Hanoi_uvindex_by_name_boxplot.png)

### severerisk by name
![Box Plot: severerisk by name](../plots/Hanoi_severerisk_by_name_boxplot.png)

### moonphase by name
![Box Plot: moonphase by name](../plots/Hanoi_moonphase_by_name_boxplot.png)

### month by name
![Box Plot: month by name](../plots/Hanoi_month_by_name_boxplot.png)

### year by name
![Box Plot: year by name](../plots/Hanoi_year_by_name_boxplot.png)

### day by name
![Box Plot: day by name](../plots/Hanoi_day_by_name_boxplot.png)

### dayofweek by name
![Box Plot: dayofweek by name](../plots/Hanoi_dayofweek_by_name_boxplot.png)

### tempmax by preciptype
![Box Plot: tempmax by preciptype](../plots/Hanoi_tempmax_by_preciptype_boxplot.png)

### tempmin by preciptype
![Box Plot: tempmin by preciptype](../plots/Hanoi_tempmin_by_preciptype_boxplot.png)

### temp by preciptype
![Box Plot: temp by preciptype](../plots/Hanoi_temp_by_preciptype_boxplot.png)

### feelslikemax by preciptype
![Box Plot: feelslikemax by preciptype](../plots/Hanoi_feelslikemax_by_preciptype_boxplot.png)

### feelslikemin by preciptype
![Box Plot: feelslikemin by preciptype](../plots/Hanoi_feelslikemin_by_preciptype_boxplot.png)

### feelslike by preciptype
![Box Plot: feelslike by preciptype](../plots/Hanoi_feelslike_by_preciptype_boxplot.png)

### dew by preciptype
![Box Plot: dew by preciptype](../plots/Hanoi_dew_by_preciptype_boxplot.png)

### humidity by preciptype
![Box Plot: humidity by preciptype](../plots/Hanoi_humidity_by_preciptype_boxplot.png)

### precip by preciptype
![Box Plot: precip by preciptype](../plots/Hanoi_precip_by_preciptype_boxplot.png)

### precipprob by preciptype
![Box Plot: precipprob by preciptype](../plots/Hanoi_precipprob_by_preciptype_boxplot.png)

### precipcover by preciptype
![Box Plot: precipcover by preciptype](../plots/Hanoi_precipcover_by_preciptype_boxplot.png)

### snow by preciptype
![Box Plot: snow by preciptype](../plots/Hanoi_snow_by_preciptype_boxplot.png)

### snowdepth by preciptype
![Box Plot: snowdepth by preciptype](../plots/Hanoi_snowdepth_by_preciptype_boxplot.png)

### windgust by preciptype
![Box Plot: windgust by preciptype](../plots/Hanoi_windgust_by_preciptype_boxplot.png)

### windspeed by preciptype
![Box Plot: windspeed by preciptype](../plots/Hanoi_windspeed_by_preciptype_boxplot.png)

### winddir by preciptype
![Box Plot: winddir by preciptype](../plots/Hanoi_winddir_by_preciptype_boxplot.png)

### sealevelpressure by preciptype
![Box Plot: sealevelpressure by preciptype](../plots/Hanoi_sealevelpressure_by_preciptype_boxplot.png)

### cloudcover by preciptype
![Box Plot: cloudcover by preciptype](../plots/Hanoi_cloudcover_by_preciptype_boxplot.png)

### visibility by preciptype
![Box Plot: visibility by preciptype](../plots/Hanoi_visibility_by_preciptype_boxplot.png)

### solarradiation by preciptype
![Box Plot: solarradiation by preciptype](../plots/Hanoi_solarradiation_by_preciptype_boxplot.png)

### solarenergy by preciptype
![Box Plot: solarenergy by preciptype](../plots/Hanoi_solarenergy_by_preciptype_boxplot.png)

### uvindex by preciptype
![Box Plot: uvindex by preciptype](../plots/Hanoi_uvindex_by_preciptype_boxplot.png)

### severerisk by preciptype
![Box Plot: severerisk by preciptype](../plots/Hanoi_severerisk_by_preciptype_boxplot.png)

### moonphase by preciptype
![Box Plot: moonphase by preciptype](../plots/Hanoi_moonphase_by_preciptype_boxplot.png)

### month by preciptype
![Box Plot: month by preciptype](../plots/Hanoi_month_by_preciptype_boxplot.png)

### year by preciptype
![Box Plot: year by preciptype](../plots/Hanoi_year_by_preciptype_boxplot.png)

### day by preciptype
![Box Plot: day by preciptype](../plots/Hanoi_day_by_preciptype_boxplot.png)

### dayofweek by preciptype
![Box Plot: dayofweek by preciptype](../plots/Hanoi_dayofweek_by_preciptype_boxplot.png)

### tempmax by conditions
![Box Plot: tempmax by conditions](../plots/Hanoi_tempmax_by_conditions_boxplot.png)

### tempmin by conditions
![Box Plot: tempmin by conditions](../plots/Hanoi_tempmin_by_conditions_boxplot.png)

### temp by conditions
![Box Plot: temp by conditions](../plots/Hanoi_temp_by_conditions_boxplot.png)

### feelslikemax by conditions
![Box Plot: feelslikemax by conditions](../plots/Hanoi_feelslikemax_by_conditions_boxplot.png)

### feelslikemin by conditions
![Box Plot: feelslikemin by conditions](../plots/Hanoi_feelslikemin_by_conditions_boxplot.png)

### feelslike by conditions
![Box Plot: feelslike by conditions](../plots/Hanoi_feelslike_by_conditions_boxplot.png)

### dew by conditions
![Box Plot: dew by conditions](../plots/Hanoi_dew_by_conditions_boxplot.png)

### humidity by conditions
![Box Plot: humidity by conditions](../plots/Hanoi_humidity_by_conditions_boxplot.png)

### precip by conditions
![Box Plot: precip by conditions](../plots/Hanoi_precip_by_conditions_boxplot.png)

### precipprob by conditions
![Box Plot: precipprob by conditions](../plots/Hanoi_precipprob_by_conditions_boxplot.png)

### precipcover by conditions
![Box Plot: precipcover by conditions](../plots/Hanoi_precipcover_by_conditions_boxplot.png)

### snow by conditions
![Box Plot: snow by conditions](../plots/Hanoi_snow_by_conditions_boxplot.png)

### snowdepth by conditions
![Box Plot: snowdepth by conditions](../plots/Hanoi_snowdepth_by_conditions_boxplot.png)

### windgust by conditions
![Box Plot: windgust by conditions](../plots/Hanoi_windgust_by_conditions_boxplot.png)

### windspeed by conditions
![Box Plot: windspeed by conditions](../plots/Hanoi_windspeed_by_conditions_boxplot.png)

### winddir by conditions
![Box Plot: winddir by conditions](../plots/Hanoi_winddir_by_conditions_boxplot.png)

### sealevelpressure by conditions
![Box Plot: sealevelpressure by conditions](../plots/Hanoi_sealevelpressure_by_conditions_boxplot.png)

### cloudcover by conditions
![Box Plot: cloudcover by conditions](../plots/Hanoi_cloudcover_by_conditions_boxplot.png)

### visibility by conditions
![Box Plot: visibility by conditions](../plots/Hanoi_visibility_by_conditions_boxplot.png)

### solarradiation by conditions
![Box Plot: solarradiation by conditions](../plots/Hanoi_solarradiation_by_conditions_boxplot.png)

### solarenergy by conditions
![Box Plot: solarenergy by conditions](../plots/Hanoi_solarenergy_by_conditions_boxplot.png)

### uvindex by conditions
![Box Plot: uvindex by conditions](../plots/Hanoi_uvindex_by_conditions_boxplot.png)

### severerisk by conditions
![Box Plot: severerisk by conditions](../plots/Hanoi_severerisk_by_conditions_boxplot.png)

### moonphase by conditions
![Box Plot: moonphase by conditions](../plots/Hanoi_moonphase_by_conditions_boxplot.png)

### month by conditions
![Box Plot: month by conditions](../plots/Hanoi_month_by_conditions_boxplot.png)

### year by conditions
![Box Plot: year by conditions](../plots/Hanoi_year_by_conditions_boxplot.png)

### day by conditions
![Box Plot: day by conditions](../plots/Hanoi_day_by_conditions_boxplot.png)

### dayofweek by conditions
![Box Plot: dayofweek by conditions](../plots/Hanoi_dayofweek_by_conditions_boxplot.png)

### tempmax by icon
![Box Plot: tempmax by icon](../plots/Hanoi_tempmax_by_icon_boxplot.png)

### tempmin by icon
![Box Plot: tempmin by icon](../plots/Hanoi_tempmin_by_icon_boxplot.png)

### temp by icon
![Box Plot: temp by icon](../plots/Hanoi_temp_by_icon_boxplot.png)

### feelslikemax by icon
![Box Plot: feelslikemax by icon](../plots/Hanoi_feelslikemax_by_icon_boxplot.png)

### feelslikemin by icon
![Box Plot: feelslikemin by icon](../plots/Hanoi_feelslikemin_by_icon_boxplot.png)

### feelslike by icon
![Box Plot: feelslike by icon](../plots/Hanoi_feelslike_by_icon_boxplot.png)

### dew by icon
![Box Plot: dew by icon](../plots/Hanoi_dew_by_icon_boxplot.png)

### humidity by icon
![Box Plot: humidity by icon](../plots/Hanoi_humidity_by_icon_boxplot.png)

### precip by icon
![Box Plot: precip by icon](../plots/Hanoi_precip_by_icon_boxplot.png)

### precipprob by icon
![Box Plot: precipprob by icon](../plots/Hanoi_precipprob_by_icon_boxplot.png)

### precipcover by icon
![Box Plot: precipcover by icon](../plots/Hanoi_precipcover_by_icon_boxplot.png)

### snow by icon
![Box Plot: snow by icon](../plots/Hanoi_snow_by_icon_boxplot.png)

### snowdepth by icon
![Box Plot: snowdepth by icon](../plots/Hanoi_snowdepth_by_icon_boxplot.png)

### windgust by icon
![Box Plot: windgust by icon](../plots/Hanoi_windgust_by_icon_boxplot.png)

### windspeed by icon
![Box Plot: windspeed by icon](../plots/Hanoi_windspeed_by_icon_boxplot.png)

### winddir by icon
![Box Plot: winddir by icon](../plots/Hanoi_winddir_by_icon_boxplot.png)

### sealevelpressure by icon
![Box Plot: sealevelpressure by icon](../plots/Hanoi_sealevelpressure_by_icon_boxplot.png)

### cloudcover by icon
![Box Plot: cloudcover by icon](../plots/Hanoi_cloudcover_by_icon_boxplot.png)

### visibility by icon
![Box Plot: visibility by icon](../plots/Hanoi_visibility_by_icon_boxplot.png)

### solarradiation by icon
![Box Plot: solarradiation by icon](../plots/Hanoi_solarradiation_by_icon_boxplot.png)

### solarenergy by icon
![Box Plot: solarenergy by icon](../plots/Hanoi_solarenergy_by_icon_boxplot.png)

### uvindex by icon
![Box Plot: uvindex by icon](../plots/Hanoi_uvindex_by_icon_boxplot.png)

### severerisk by icon
![Box Plot: severerisk by icon](../plots/Hanoi_severerisk_by_icon_boxplot.png)

### moonphase by icon
![Box Plot: moonphase by icon](../plots/Hanoi_moonphase_by_icon_boxplot.png)

### month by icon
![Box Plot: month by icon](../plots/Hanoi_month_by_icon_boxplot.png)

### year by icon
![Box Plot: year by icon](../plots/Hanoi_year_by_icon_boxplot.png)

### day by icon
![Box Plot: day by icon](../plots/Hanoi_day_by_icon_boxplot.png)

### dayofweek by icon
![Box Plot: dayofweek by icon](../plots/Hanoi_dayofweek_by_icon_boxplot.png)

## Evaluation Summary
This section summarizes the data quality evaluation. Please refer to the detailed evaluation report for in-depth analysis of outliers, skewness/kurtosis, and stationarity.

Please refer to the detailed evaluation report: `Hanoi_evaluation.txt`.
This file includes information about outliers, skewness/kurtosis, and stationarity test results.

## Conclusion
Based on the EDA, key findings for {city_name} include: ... (Summary of key findings, e.g., important correlations, trends, data quality issues).