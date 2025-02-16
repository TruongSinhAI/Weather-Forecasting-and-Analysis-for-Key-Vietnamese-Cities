# EDA Report for Merged_Cities

## Executive Summary
This report provides an Exploratory Data Analysis (EDA) for the weather data of {city_name}. It includes dataset overview, missing value analysis, statistical summaries, correlation analysis, temporal analysis, categorical feature analysis, and data quality evaluation.

## Dataset Overview
This section provides a general overview of the dataset.

* **Number of records:** 27535
* **Time period:** 2000-01-01 00:00:00 to 2025-02-13 00:00:00
* **Number of features:** 38

## Missing Values
This section details the missing values present in the dataset.

* **precip**: 3662 missing values
* **preciptype**: 13557 missing values
* **snow**: 16344 missing values
* **snowdepth**: 16359 missing values
* **windgust**: 16035 missing values
* **sealevelpressure**: 27535 missing values
* **solarradiation**: 10959 missing values
* **solarenergy**: 10959 missing values
* **uvindex**: 10959 missing values
* **severerisk**: 26208 missing values

## Key Weather Statistics (Numerical)
This section presents descriptive statistics for the numerical weather metrics.

### tempmax
* **Average:** 30.27
* **Maximum:** 42.70
* **Minimum:** 8.00

### tempmin
* **Average:** 23.01
* **Maximum:** 31.00
* **Minimum:** 3.80

### temp
* **Average:** 26.19
* **Maximum:** 35.50
* **Minimum:** 7.00

### feelslikemax
* **Average:** 34.70
* **Maximum:** 56.70
* **Minimum:** 6.40

### feelslikemin
* **Average:** 23.42
* **Maximum:** 40.40
* **Minimum:** 0.40

### feelslike
* **Average:** 28.54
* **Maximum:** 46.20
* **Minimum:** 4.60

### dew
* **Average:** 21.90
* **Maximum:** 29.00
* **Minimum:** -2.10

### humidity
* **Average:** 78.92
* **Maximum:** 100.00
* **Minimum:** 31.10

### precip
* **Average:** 5.44
* **Maximum:** 632.67
* **Minimum:** 0.00

### precipprob
* **Average:** 50.48
* **Maximum:** 100.00
* **Minimum:** 0.00

### precipcover
* **Average:** 6.91
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
* **Average:** 29.54
* **Maximum:** 216.00
* **Minimum:** 7.20

### windspeed
* **Average:** 18.76
* **Maximum:** 156.20
* **Minimum:** 3.60

### winddir
* **Average:** 156.17
* **Maximum:** 360.00
* **Minimum:** 0.00

### sealevelpressure
* **Average:** nan
* **Maximum:** nan
* **Minimum:** nan

### cloudcover
* **Average:** 64.35
* **Maximum:** 100.00
* **Minimum:** 0.00

### visibility
* **Average:** 9.24
* **Maximum:** 76.80
* **Minimum:** 1.30

### solarradiation
* **Average:** 189.43
* **Maximum:** 333.50
* **Minimum:** 0.00

### solarenergy
* **Average:** 16.36
* **Maximum:** 28.90
* **Minimum:** 0.00

### uvindex
* **Average:** 6.85
* **Maximum:** 10.00
* **Minimum:** 0.00

### severerisk
* **Average:** 29.59
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

![Correlation Matrix](../plots/Merged_Cities_correlation.png)

## Numerical Analysis Plots
Distributions and box plots of key numerical metrics are shown below to understand data spread and potential outliers.

![Distributions](../plots/Merged_Cities_distributions.png)
![Box Plots](../plots/Merged_Cities_boxplots.png)

## Temporal Analysis
This section explores the temporal patterns in the weather data, including monthly and daily trends.

![Monthly Temperature](../plots/Merged_Cities_monthly_temp.png)
![Daily Temperature](../plots/Merged_Cities_daily_temp.png)
![Temperature vs Humidity](../plots/Merged_Cities_temp_humidity.png)

## Advanced Temporal Analysis
Advanced time series analysis, including rolling statistics, ACF/PACF plots, and seasonal decomposition, are presented here.

![Temperature Rolling Stats](../plots/Merged_Cities_temp_rolling.png)
![ACF and PACF](../plots/Merged_Cities_acf_pacf.png)
![Seasonal Decomposition](../plots/Merged_Cities_seasonal_decompose.png)

## Categorical Analysis
Analysis of categorical features, including value counts and distribution plots where applicable.

### name Analysis
Value Counts:
* **Đà Nẵng, Việt Nam**: 9179
* **Hà Nội, Việt Nam**: 9178
* **Hồ Chí Minh, Việt Nam**: 9178

![Count Plot for name](../plots/Merged_Cities_name_countplot.png)

### preciptype Analysis
Column 'preciptype' is constant with only 1 unique value. No further analysis is provided.

### conditions Analysis
Value Counts:
* **Partially cloudy**: 12325
* **Rain, Partially cloudy**: 11432
* **Rain, Overcast**: 2439
* **Overcast**: 670
* **Clear**: 640
* **Rain**: 29

![Count Plot for conditions](../plots/Merged_Cities_conditions_countplot.png)

### description Analysis
Value Counts (Top 20):
* **Partly cloudy throughout the day.**: 12051
* **Partly cloudy throughout the day with rain.**: 2882
* **Partly cloudy throughout the day with late afternoon rain.**: 2166
* **Partly cloudy throughout the day with a chance of rain throughout the day.**: 1986
* **Partly cloudy throughout the day with early morning rain.**: 1260
* **Partly cloudy throughout the day with afternoon rain.**: 1053
* **Partly cloudy throughout the day with rain in the morning and afternoon.**: 1030
* **Cloudy skies throughout the day with a chance of rain throughout the day.**: 707
* **Cloudy skies throughout the day with rain.**: 699
* **Cloudy skies throughout the day.**: 670
* **Partly cloudy throughout the day with morning rain.**: 650
* **Clear conditions throughout the day.**: 635
* **Partly cloudy throughout the day with rain clearing later.**: 304
* **Cloudy skies throughout the day with rain in the morning and afternoon.**: 266
* **Cloudy skies throughout the day with early morning rain.**: 202
* **Cloudy skies throughout the day with afternoon rain.**: 193
* **Cloudy skies throughout the day with late afternoon rain.**: 186
* **Becoming cloudy in the afternoon.**: 140
* **Clearing in the afternoon.**: 139
* **Cloudy skies throughout the day with morning rain.**: 130

![Top Value Count Plot for description](../plots/Merged_Cities_description_top_countplot.png)

### icon Analysis
Value Counts:
* **rain**: 13900
* **partly-cloudy-day**: 12316
* **cloudy**: 668
* **clear-day**: 640
* **wind**: 11

![Count Plot for icon](../plots/Merged_Cities_icon_countplot.png)

### stations Analysis
High cardinality column with 52 unique values. Detailed value counts not displayed.

### city Analysis
Value Counts:
* **DaNang**: 9179
* **Hanoi**: 9178
* **HoChiMinh**: 9178

![Count Plot for city](../plots/Merged_Cities_city_countplot.png)

## Numerical vs Categorical Analysis
Box plots showing the distribution of numerical features across different categories (for low cardinality categorical features).

### tempmax by name
![Box Plot: tempmax by name](../plots/Merged_Cities_tempmax_by_name_boxplot.png)

### tempmin by name
![Box Plot: tempmin by name](../plots/Merged_Cities_tempmin_by_name_boxplot.png)

### temp by name
![Box Plot: temp by name](../plots/Merged_Cities_temp_by_name_boxplot.png)

### feelslikemax by name
![Box Plot: feelslikemax by name](../plots/Merged_Cities_feelslikemax_by_name_boxplot.png)

### feelslikemin by name
![Box Plot: feelslikemin by name](../plots/Merged_Cities_feelslikemin_by_name_boxplot.png)

### feelslike by name
![Box Plot: feelslike by name](../plots/Merged_Cities_feelslike_by_name_boxplot.png)

### dew by name
![Box Plot: dew by name](../plots/Merged_Cities_dew_by_name_boxplot.png)

### humidity by name
![Box Plot: humidity by name](../plots/Merged_Cities_humidity_by_name_boxplot.png)

### precip by name
![Box Plot: precip by name](../plots/Merged_Cities_precip_by_name_boxplot.png)

### precipprob by name
![Box Plot: precipprob by name](../plots/Merged_Cities_precipprob_by_name_boxplot.png)

### precipcover by name
![Box Plot: precipcover by name](../plots/Merged_Cities_precipcover_by_name_boxplot.png)

### snow by name
![Box Plot: snow by name](../plots/Merged_Cities_snow_by_name_boxplot.png)

### snowdepth by name
![Box Plot: snowdepth by name](../plots/Merged_Cities_snowdepth_by_name_boxplot.png)

### windgust by name
![Box Plot: windgust by name](../plots/Merged_Cities_windgust_by_name_boxplot.png)

### windspeed by name
![Box Plot: windspeed by name](../plots/Merged_Cities_windspeed_by_name_boxplot.png)

### winddir by name
![Box Plot: winddir by name](../plots/Merged_Cities_winddir_by_name_boxplot.png)

### sealevelpressure by name
![Box Plot: sealevelpressure by name](../plots/Merged_Cities_sealevelpressure_by_name_boxplot.png)

### cloudcover by name
![Box Plot: cloudcover by name](../plots/Merged_Cities_cloudcover_by_name_boxplot.png)

### visibility by name
![Box Plot: visibility by name](../plots/Merged_Cities_visibility_by_name_boxplot.png)

### solarradiation by name
![Box Plot: solarradiation by name](../plots/Merged_Cities_solarradiation_by_name_boxplot.png)

### solarenergy by name
![Box Plot: solarenergy by name](../plots/Merged_Cities_solarenergy_by_name_boxplot.png)

### uvindex by name
![Box Plot: uvindex by name](../plots/Merged_Cities_uvindex_by_name_boxplot.png)

### severerisk by name
![Box Plot: severerisk by name](../plots/Merged_Cities_severerisk_by_name_boxplot.png)

### moonphase by name
![Box Plot: moonphase by name](../plots/Merged_Cities_moonphase_by_name_boxplot.png)

### month by name
![Box Plot: month by name](../plots/Merged_Cities_month_by_name_boxplot.png)

### year by name
![Box Plot: year by name](../plots/Merged_Cities_year_by_name_boxplot.png)

### day by name
![Box Plot: day by name](../plots/Merged_Cities_day_by_name_boxplot.png)

### dayofweek by name
![Box Plot: dayofweek by name](../plots/Merged_Cities_dayofweek_by_name_boxplot.png)

### tempmax by preciptype
![Box Plot: tempmax by preciptype](../plots/Merged_Cities_tempmax_by_preciptype_boxplot.png)

### tempmin by preciptype
![Box Plot: tempmin by preciptype](../plots/Merged_Cities_tempmin_by_preciptype_boxplot.png)

### temp by preciptype
![Box Plot: temp by preciptype](../plots/Merged_Cities_temp_by_preciptype_boxplot.png)

### feelslikemax by preciptype
![Box Plot: feelslikemax by preciptype](../plots/Merged_Cities_feelslikemax_by_preciptype_boxplot.png)

### feelslikemin by preciptype
![Box Plot: feelslikemin by preciptype](../plots/Merged_Cities_feelslikemin_by_preciptype_boxplot.png)

### feelslike by preciptype
![Box Plot: feelslike by preciptype](../plots/Merged_Cities_feelslike_by_preciptype_boxplot.png)

### dew by preciptype
![Box Plot: dew by preciptype](../plots/Merged_Cities_dew_by_preciptype_boxplot.png)

### humidity by preciptype
![Box Plot: humidity by preciptype](../plots/Merged_Cities_humidity_by_preciptype_boxplot.png)

### precip by preciptype
![Box Plot: precip by preciptype](../plots/Merged_Cities_precip_by_preciptype_boxplot.png)

### precipprob by preciptype
![Box Plot: precipprob by preciptype](../plots/Merged_Cities_precipprob_by_preciptype_boxplot.png)

### precipcover by preciptype
![Box Plot: precipcover by preciptype](../plots/Merged_Cities_precipcover_by_preciptype_boxplot.png)

### snow by preciptype
![Box Plot: snow by preciptype](../plots/Merged_Cities_snow_by_preciptype_boxplot.png)

### snowdepth by preciptype
![Box Plot: snowdepth by preciptype](../plots/Merged_Cities_snowdepth_by_preciptype_boxplot.png)

### windgust by preciptype
![Box Plot: windgust by preciptype](../plots/Merged_Cities_windgust_by_preciptype_boxplot.png)

### windspeed by preciptype
![Box Plot: windspeed by preciptype](../plots/Merged_Cities_windspeed_by_preciptype_boxplot.png)

### winddir by preciptype
![Box Plot: winddir by preciptype](../plots/Merged_Cities_winddir_by_preciptype_boxplot.png)

### sealevelpressure by preciptype
![Box Plot: sealevelpressure by preciptype](../plots/Merged_Cities_sealevelpressure_by_preciptype_boxplot.png)

### cloudcover by preciptype
![Box Plot: cloudcover by preciptype](../plots/Merged_Cities_cloudcover_by_preciptype_boxplot.png)

### visibility by preciptype
![Box Plot: visibility by preciptype](../plots/Merged_Cities_visibility_by_preciptype_boxplot.png)

### solarradiation by preciptype
![Box Plot: solarradiation by preciptype](../plots/Merged_Cities_solarradiation_by_preciptype_boxplot.png)

### solarenergy by preciptype
![Box Plot: solarenergy by preciptype](../plots/Merged_Cities_solarenergy_by_preciptype_boxplot.png)

### uvindex by preciptype
![Box Plot: uvindex by preciptype](../plots/Merged_Cities_uvindex_by_preciptype_boxplot.png)

### severerisk by preciptype
![Box Plot: severerisk by preciptype](../plots/Merged_Cities_severerisk_by_preciptype_boxplot.png)

### moonphase by preciptype
![Box Plot: moonphase by preciptype](../plots/Merged_Cities_moonphase_by_preciptype_boxplot.png)

### month by preciptype
![Box Plot: month by preciptype](../plots/Merged_Cities_month_by_preciptype_boxplot.png)

### year by preciptype
![Box Plot: year by preciptype](../plots/Merged_Cities_year_by_preciptype_boxplot.png)

### day by preciptype
![Box Plot: day by preciptype](../plots/Merged_Cities_day_by_preciptype_boxplot.png)

### dayofweek by preciptype
![Box Plot: dayofweek by preciptype](../plots/Merged_Cities_dayofweek_by_preciptype_boxplot.png)

### tempmax by conditions
![Box Plot: tempmax by conditions](../plots/Merged_Cities_tempmax_by_conditions_boxplot.png)

### tempmin by conditions
![Box Plot: tempmin by conditions](../plots/Merged_Cities_tempmin_by_conditions_boxplot.png)

### temp by conditions
![Box Plot: temp by conditions](../plots/Merged_Cities_temp_by_conditions_boxplot.png)

### feelslikemax by conditions
![Box Plot: feelslikemax by conditions](../plots/Merged_Cities_feelslikemax_by_conditions_boxplot.png)

### feelslikemin by conditions
![Box Plot: feelslikemin by conditions](../plots/Merged_Cities_feelslikemin_by_conditions_boxplot.png)

### feelslike by conditions
![Box Plot: feelslike by conditions](../plots/Merged_Cities_feelslike_by_conditions_boxplot.png)

### dew by conditions
![Box Plot: dew by conditions](../plots/Merged_Cities_dew_by_conditions_boxplot.png)

### humidity by conditions
![Box Plot: humidity by conditions](../plots/Merged_Cities_humidity_by_conditions_boxplot.png)

### precip by conditions
![Box Plot: precip by conditions](../plots/Merged_Cities_precip_by_conditions_boxplot.png)

### precipprob by conditions
![Box Plot: precipprob by conditions](../plots/Merged_Cities_precipprob_by_conditions_boxplot.png)

### precipcover by conditions
![Box Plot: precipcover by conditions](../plots/Merged_Cities_precipcover_by_conditions_boxplot.png)

### snow by conditions
![Box Plot: snow by conditions](../plots/Merged_Cities_snow_by_conditions_boxplot.png)

### snowdepth by conditions
![Box Plot: snowdepth by conditions](../plots/Merged_Cities_snowdepth_by_conditions_boxplot.png)

### windgust by conditions
![Box Plot: windgust by conditions](../plots/Merged_Cities_windgust_by_conditions_boxplot.png)

### windspeed by conditions
![Box Plot: windspeed by conditions](../plots/Merged_Cities_windspeed_by_conditions_boxplot.png)

### winddir by conditions
![Box Plot: winddir by conditions](../plots/Merged_Cities_winddir_by_conditions_boxplot.png)

### sealevelpressure by conditions
![Box Plot: sealevelpressure by conditions](../plots/Merged_Cities_sealevelpressure_by_conditions_boxplot.png)

### cloudcover by conditions
![Box Plot: cloudcover by conditions](../plots/Merged_Cities_cloudcover_by_conditions_boxplot.png)

### visibility by conditions
![Box Plot: visibility by conditions](../plots/Merged_Cities_visibility_by_conditions_boxplot.png)

### solarradiation by conditions
![Box Plot: solarradiation by conditions](../plots/Merged_Cities_solarradiation_by_conditions_boxplot.png)

### solarenergy by conditions
![Box Plot: solarenergy by conditions](../plots/Merged_Cities_solarenergy_by_conditions_boxplot.png)

### uvindex by conditions
![Box Plot: uvindex by conditions](../plots/Merged_Cities_uvindex_by_conditions_boxplot.png)

### severerisk by conditions
![Box Plot: severerisk by conditions](../plots/Merged_Cities_severerisk_by_conditions_boxplot.png)

### moonphase by conditions
![Box Plot: moonphase by conditions](../plots/Merged_Cities_moonphase_by_conditions_boxplot.png)

### month by conditions
![Box Plot: month by conditions](../plots/Merged_Cities_month_by_conditions_boxplot.png)

### year by conditions
![Box Plot: year by conditions](../plots/Merged_Cities_year_by_conditions_boxplot.png)

### day by conditions
![Box Plot: day by conditions](../plots/Merged_Cities_day_by_conditions_boxplot.png)

### dayofweek by conditions
![Box Plot: dayofweek by conditions](../plots/Merged_Cities_dayofweek_by_conditions_boxplot.png)

### tempmax by icon
![Box Plot: tempmax by icon](../plots/Merged_Cities_tempmax_by_icon_boxplot.png)

### tempmin by icon
![Box Plot: tempmin by icon](../plots/Merged_Cities_tempmin_by_icon_boxplot.png)

### temp by icon
![Box Plot: temp by icon](../plots/Merged_Cities_temp_by_icon_boxplot.png)

### feelslikemax by icon
![Box Plot: feelslikemax by icon](../plots/Merged_Cities_feelslikemax_by_icon_boxplot.png)

### feelslikemin by icon
![Box Plot: feelslikemin by icon](../plots/Merged_Cities_feelslikemin_by_icon_boxplot.png)

### feelslike by icon
![Box Plot: feelslike by icon](../plots/Merged_Cities_feelslike_by_icon_boxplot.png)

### dew by icon
![Box Plot: dew by icon](../plots/Merged_Cities_dew_by_icon_boxplot.png)

### humidity by icon
![Box Plot: humidity by icon](../plots/Merged_Cities_humidity_by_icon_boxplot.png)

### precip by icon
![Box Plot: precip by icon](../plots/Merged_Cities_precip_by_icon_boxplot.png)

### precipprob by icon
![Box Plot: precipprob by icon](../plots/Merged_Cities_precipprob_by_icon_boxplot.png)

### precipcover by icon
![Box Plot: precipcover by icon](../plots/Merged_Cities_precipcover_by_icon_boxplot.png)

### snow by icon
![Box Plot: snow by icon](../plots/Merged_Cities_snow_by_icon_boxplot.png)

### snowdepth by icon
![Box Plot: snowdepth by icon](../plots/Merged_Cities_snowdepth_by_icon_boxplot.png)

### windgust by icon
![Box Plot: windgust by icon](../plots/Merged_Cities_windgust_by_icon_boxplot.png)

### windspeed by icon
![Box Plot: windspeed by icon](../plots/Merged_Cities_windspeed_by_icon_boxplot.png)

### winddir by icon
![Box Plot: winddir by icon](../plots/Merged_Cities_winddir_by_icon_boxplot.png)

### sealevelpressure by icon
![Box Plot: sealevelpressure by icon](../plots/Merged_Cities_sealevelpressure_by_icon_boxplot.png)

### cloudcover by icon
![Box Plot: cloudcover by icon](../plots/Merged_Cities_cloudcover_by_icon_boxplot.png)

### visibility by icon
![Box Plot: visibility by icon](../plots/Merged_Cities_visibility_by_icon_boxplot.png)

### solarradiation by icon
![Box Plot: solarradiation by icon](../plots/Merged_Cities_solarradiation_by_icon_boxplot.png)

### solarenergy by icon
![Box Plot: solarenergy by icon](../plots/Merged_Cities_solarenergy_by_icon_boxplot.png)

### uvindex by icon
![Box Plot: uvindex by icon](../plots/Merged_Cities_uvindex_by_icon_boxplot.png)

### severerisk by icon
![Box Plot: severerisk by icon](../plots/Merged_Cities_severerisk_by_icon_boxplot.png)

### moonphase by icon
![Box Plot: moonphase by icon](../plots/Merged_Cities_moonphase_by_icon_boxplot.png)

### month by icon
![Box Plot: month by icon](../plots/Merged_Cities_month_by_icon_boxplot.png)

### year by icon
![Box Plot: year by icon](../plots/Merged_Cities_year_by_icon_boxplot.png)

### day by icon
![Box Plot: day by icon](../plots/Merged_Cities_day_by_icon_boxplot.png)

### dayofweek by icon
![Box Plot: dayofweek by icon](../plots/Merged_Cities_dayofweek_by_icon_boxplot.png)

### tempmax by city
![Box Plot: tempmax by city](../plots/Merged_Cities_tempmax_by_city_boxplot.png)

### tempmin by city
![Box Plot: tempmin by city](../plots/Merged_Cities_tempmin_by_city_boxplot.png)

### temp by city
![Box Plot: temp by city](../plots/Merged_Cities_temp_by_city_boxplot.png)

### feelslikemax by city
![Box Plot: feelslikemax by city](../plots/Merged_Cities_feelslikemax_by_city_boxplot.png)

### feelslikemin by city
![Box Plot: feelslikemin by city](../plots/Merged_Cities_feelslikemin_by_city_boxplot.png)

### feelslike by city
![Box Plot: feelslike by city](../plots/Merged_Cities_feelslike_by_city_boxplot.png)

### dew by city
![Box Plot: dew by city](../plots/Merged_Cities_dew_by_city_boxplot.png)

### humidity by city
![Box Plot: humidity by city](../plots/Merged_Cities_humidity_by_city_boxplot.png)

### precip by city
![Box Plot: precip by city](../plots/Merged_Cities_precip_by_city_boxplot.png)

### precipprob by city
![Box Plot: precipprob by city](../plots/Merged_Cities_precipprob_by_city_boxplot.png)

### precipcover by city
![Box Plot: precipcover by city](../plots/Merged_Cities_precipcover_by_city_boxplot.png)

### snow by city
![Box Plot: snow by city](../plots/Merged_Cities_snow_by_city_boxplot.png)

### snowdepth by city
![Box Plot: snowdepth by city](../plots/Merged_Cities_snowdepth_by_city_boxplot.png)

### windgust by city
![Box Plot: windgust by city](../plots/Merged_Cities_windgust_by_city_boxplot.png)

### windspeed by city
![Box Plot: windspeed by city](../plots/Merged_Cities_windspeed_by_city_boxplot.png)

### winddir by city
![Box Plot: winddir by city](../plots/Merged_Cities_winddir_by_city_boxplot.png)

### sealevelpressure by city
![Box Plot: sealevelpressure by city](../plots/Merged_Cities_sealevelpressure_by_city_boxplot.png)

### cloudcover by city
![Box Plot: cloudcover by city](../plots/Merged_Cities_cloudcover_by_city_boxplot.png)

### visibility by city
![Box Plot: visibility by city](../plots/Merged_Cities_visibility_by_city_boxplot.png)

### solarradiation by city
![Box Plot: solarradiation by city](../plots/Merged_Cities_solarradiation_by_city_boxplot.png)

### solarenergy by city
![Box Plot: solarenergy by city](../plots/Merged_Cities_solarenergy_by_city_boxplot.png)

### uvindex by city
![Box Plot: uvindex by city](../plots/Merged_Cities_uvindex_by_city_boxplot.png)

### severerisk by city
![Box Plot: severerisk by city](../plots/Merged_Cities_severerisk_by_city_boxplot.png)

### moonphase by city
![Box Plot: moonphase by city](../plots/Merged_Cities_moonphase_by_city_boxplot.png)

### month by city
![Box Plot: month by city](../plots/Merged_Cities_month_by_city_boxplot.png)

### year by city
![Box Plot: year by city](../plots/Merged_Cities_year_by_city_boxplot.png)

### day by city
![Box Plot: day by city](../plots/Merged_Cities_day_by_city_boxplot.png)

### dayofweek by city
![Box Plot: dayofweek by city](../plots/Merged_Cities_dayofweek_by_city_boxplot.png)

## Evaluation Summary
This section summarizes the data quality evaluation. Please refer to the detailed evaluation report for in-depth analysis of outliers, skewness/kurtosis, and stationarity.

Please refer to the detailed evaluation report: `Merged_Cities_evaluation.txt`.
This file includes information about outliers, skewness/kurtosis, and stationarity test results.

## Conclusion
Based on the EDA, key findings for {city_name} include: ... (Summary of key findings, e.g., important correlations, trends, data quality issues).