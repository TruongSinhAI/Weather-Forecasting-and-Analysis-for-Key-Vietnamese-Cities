import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path
import os
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
from statsmodels.tsa.seasonal import seasonal_decompose
from statsmodels.tsa.stattools import adfuller

####################################
# CONFIGURATION CONSTANTS
####################################
UNIQUE_THRESHOLD = 15
MAIN_METRICS = ['temp', 'humidity', 'precip', 'windspeed']
MISSING_VALUE_STRATEGY = 'ffill'
EDA_OUTPUT_FOLDER = 'eda'
PLOTS_FOLDER_NAME = 'plots'
REPORTS_FOLDER_NAME = 'reports'
CLEANED_DATA_FOLDER_NAME = 'cleaned_data'

####################################
# 1. LOAD DỮ LIỆU
####################################
def load_data(data_folder):
    """
    Load tất cả các file CSV trong folder được chỉ định.
    Mỗi file được coi là dữ liệu của một thành phố.

    Parameters:
        data_folder (str): Đường dẫn đến thư mục chứa các file CSV.

    Returns:
        dict: Dictionary chứa DataFrame cho mỗi thành phố, với tên file làm key.
              Ví dụ: {'city1': DataFrame_city1, 'city2': DataFrame_city2, ...}
    """
    data_dict = {}
    for file in Path(data_folder).glob('*.csv'):
        city_name = file.stem
        try:
            df = pd.read_csv(file)
            df['datetime'] = pd.to_datetime(df['datetime'])
            data_dict[city_name] = df
        except Exception as e:
            print(f"Error loading data for {city_name}: {e}")
    return data_dict


####################################
# 2. PHÂN TÍCH BAN ĐẦU (EDA)
####################################
def basic_info(df, city_name):
    """
    In thông tin cơ bản của dataset, bao gồm shape, missing values, data types, và 5 dòng đầu.

    Parameters:
        df (pd.DataFrame): DataFrame cần phân tích.
        city_name (str): Tên thành phố (để in tiêu đề).
    """
    print(f"\n{'=' * 50}")
    print(f"Basic Information for {city_name}")
    print(f"{'=' * 50}")
    print("Dataset Shape:", df.shape)
    print("Missing Values:\n", df.isnull().sum())
    print("Data Types:\n", df.dtypes)
    print("First 5 Rows:\n", df.head())


def numeric_analysis(df, city_name, metrics=MAIN_METRICS, plots_folder=PLOTS_FOLDER_NAME):
    """
    Phân tích biến số: thống kê mô tả, biểu đồ phân phối và boxplot cho các metrics chỉ định.

    Parameters:
        df (pd.DataFrame): DataFrame cần phân tích.
        city_name (str): Tên thành phố (để đặt tên file và tiêu đề).
        metrics (list, optional): Danh sách các metrics số cần phân tích. Mặc định là MAIN_METRICS.
        plots_folder (str, optional): Tên thư mục con để lưu plots trong thư mục 'eda'. Mặc định là 'plots'.
    """
    numeric_cols = df.select_dtypes(include=[np.number]).columns
    print(f"\n{'=' * 50}")
    print(f"Numeric Analysis for {city_name}")
    print(f"{'=' * 50}")
    print("Statistical Summary:\n", df[numeric_cols].describe())

    plots_dir = Path(EDA_OUTPUT_FOLDER) / plots_folder
    plots_dir.mkdir(parents=True, exist_ok=True)

    # Biểu đồ phân phối
    fig, axes = plt.subplots(2, 2, figsize=(15, 10))
    fig.suptitle(f'Distribution of Main Weather Metrics - {city_name}', fontsize=16)
    for idx, metric in enumerate(metrics):
        if metric in df.columns:
            sns.histplot(df[metric].dropna(), kde=True, bins=30, ax=axes[idx // 2, idx % 2])
            axes[idx // 2, idx % 2].set_title(f'{metric.capitalize()} Distribution')
    plt.tight_layout(rect=[0, 0, 1, 0.96])
    plt.savefig(plots_dir / f'{city_name}_distributions.png')
    plt.close()

    # Box Plots
    fig, axes = plt.subplots(2, 2, figsize=(15, 10))
    fig.suptitle(f'Box Plots of Main Weather Metrics - {city_name}', fontsize=16)
    for idx, metric in enumerate(metrics):
        if metric in df.columns:
            sns.boxplot(y=df[metric].dropna(), ax=axes[idx // 2, idx % 2])
            axes[idx // 2, idx % 2].set_title(f'{metric.capitalize()} Box Plot')
    plt.tight_layout(rect=[0, 0, 1, 0.96])
    plt.savefig(plots_dir / f'{city_name}_boxplots.png')
    plt.close()


def smart_categorical_analysis(df, city_name, unique_threshold=UNIQUE_THRESHOLD, plots_folder=PLOTS_FOLDER_NAME):
    """
    Phân tích các biến phân loại một cách thông minh:
      - Loại bỏ các cột không cần thiết (ví dụ: datetime, sunrise, sunset).
      - Nếu cột chỉ có 1 giá trị duy nhất, thông báo rằng cột đó là hằng số và không vẽ plot.
      - Nếu số giá trị duy nhất của biến <= unique_threshold thì hiển thị value counts và vẽ count plot.
      - Nếu không thì chỉ in ra thông tin tóm tắt.

    Parameters:
        df (pd.DataFrame): DataFrame cần phân tích.
        city_name (str): Tên thành phố.
        unique_threshold (int, optional): Ngưỡng số lượng giá trị duy nhất để vẽ countplot. Mặc định là UNIQUE_THRESHOLD.
        plots_folder (str, optional): Tên thư mục con để lưu plots trong thư mục 'eda'. Mặc định là 'plots'.
    """
    cat_cols = df.select_dtypes(include=['object']).columns.tolist()
    skip_cols = ['datetime', 'sunrise', 'sunset']
    cat_cols = [col for col in cat_cols if col not in skip_cols]

    print(f"\n{'=' * 50}")
    print(f"Smart Categorical Analysis for {city_name}")
    print(f"{'=' * 50}")

    plots_dir = Path(EDA_OUTPUT_FOLDER) / plots_folder
    plots_dir.mkdir(parents=True, exist_ok=True)

    for col in cat_cols:
        nunique = df[col].nunique()
        print(f"\nColumn '{col}' has {nunique} unique value(s).")
        if nunique == 1:
            print(f"Column '{col}' is constant; skipping plot.")
            continue
        if nunique <= unique_threshold:
            print(df[col].value_counts())
            # Vẽ count plot
            plt.figure(figsize=(8, 4))
            order = df[col].value_counts().index
            sns.countplot(data=df, x=col, order=order)
            plt.title(f'Count Plot for {col} - {city_name}')
            plt.xticks(rotation=45, ha='right') # Cải thiện hiển thị nhãn x-axis khi bị dài
            plt.tight_layout()
            plt.savefig(plots_dir / f'{city_name}_{col}_countplot.png')
            plt.close()
        elif nunique <= 50: # Ví dụ, ngưỡng 50 cho top N bar chart
            print(f"Medium cardinality ({nunique} unique values). Showing top 20 value counts and bar chart.")
            top_n = 20
            top_value_counts = df[col].value_counts().nlargest(top_n)
            print(top_value_counts)
            plt.figure(figsize=(10, 5))
            top_value_counts.plot(kind='bar')
            plt.title(f'Top {top_n} Value Counts for {col} - {city_name}')
            plt.xticks(rotation=45, ha='right')
            plt.tight_layout()
            plt.savefig(plots_dir / f'{city_name}_{col}_top_countplot.png')
            plt.close()

        else:
            print(f"High cardinality: Skipping detailed value counts and plot for '{col}'.")


def temporal_analysis(df, city_name, metrics=MAIN_METRICS, plots_folder=PLOTS_FOLDER_NAME):
    """
    Phân tích thời gian cơ bản: xu hướng theo tháng, ngày, và mối quan hệ giữa các metrics và độ ẩm.

    Parameters:
        df (pd.DataFrame): DataFrame cần phân tích.
        city_name (str): Tên thành phố.
        metrics (list, optional): Danh sách các metrics số cần phân tích theo thời gian. Mặc định là MAIN_METRICS.
        plots_folder (str, optional): Tên thư mục con để lưu plots trong thư mục 'eda'. Mặc định là 'plots'.
    """
    df['month'] = df['datetime'].dt.month
    df['year'] = df['datetime'].dt.year
    df['day'] = df['datetime'].dt.day
    df['dayofweek'] = df['datetime'].dt.dayofweek

    plots_dir = Path(EDA_OUTPUT_FOLDER) / plots_folder

    for metric in metrics:
        if metric not in df.columns:
            print(f"Warning: Metric '{metric}' not found in DataFrame, skipping temporal analysis for this metric.")
            continue

        # Xu hướng theo tháng
        plt.figure(figsize=(12, 6))
        monthly_metric = df.groupby('month')[metric].mean()
        monthly_metric.plot(marker='o')
        plt.title(f'Average Monthly {metric.capitalize()} - {city_name}')
        plt.xlabel('Month')
        plt.ylabel(metric.capitalize())
        plt.grid(True)
        plt.savefig(plots_dir / f'{city_name}_monthly_{metric}.png')
        plt.close()

        # Xu hướng theo ngày
        plt.figure(figsize=(12, 6))
        daily_metric = df.groupby('day')[metric].mean()
        daily_metric.plot(marker='o')
        plt.title(f'Average Daily {metric.capitalize()} - {city_name}')
        plt.xlabel('Day')
        plt.ylabel(metric.capitalize())
        plt.grid(True)
        plt.savefig(plots_dir / f'{city_name}_daily_{metric}.png')
        plt.close()

    # Biểu đồ nhiệt độ vs độ ẩm (luôn vẽ nếu có cả 2 cột)
    if 'temp' in df.columns and 'humidity' in df.columns:
        plt.figure(figsize=(10, 6))
        plt.scatter(df['temp'], df['humidity'], alpha=0.5)
        plt.title(f'Temperature vs Humidity - {city_name}')
        plt.xlabel('Temperature')
        plt.ylabel('Humidity')
        plt.grid(True)
        plt.savefig(plots_dir / f'{city_name}_temp_humidity.png')
        plt.close()


def advanced_temporal_analysis(df, city_name, plots_folder=PLOTS_FOLDER_NAME):
    """
    Phân tích chuỗi thời gian nâng cao:
      - Kiểm tra các ngày bị thiếu.
      - Biểu đồ chuỗi thời gian với trung bình trượt và độ lệch chuẩn cho 'temp'.
      - Biểu đồ ACF và PACF cho 'temp'.
      - Phân rã mùa của chuỗi nhiệt độ 'temp'.

    Parameters:
        df (pd.DataFrame): DataFrame cần phân tích.
        city_name (str): Tên thành phố.
        plots_folder (str, optional): Tên thư mục con để lưu plots trong thư mục 'eda'. Mặc định là 'plots'.
    """
    plots_dir = Path(EDA_OUTPUT_FOLDER) / plots_folder
    df_ts = df.sort_values('datetime').copy()
    df_ts.set_index('datetime', inplace=True)

    # Kiểm tra các ngày bị thiếu (giả sử dữ liệu ghi nhận hàng ngày)
    full_date_range = pd.date_range(start=df_ts.index.min(), end=df_ts.index.max(), freq='D')
    missing_dates = full_date_range.difference(df_ts.index)
    report_dir = Path(EDA_OUTPUT_FOLDER) / REPORTS_FOLDER_NAME
    report_dir.mkdir(parents=True, exist_ok=True)
    missing_info_file = report_dir / f'{city_name}_missing_dates.txt'
    with open(missing_info_file, 'w', encoding='utf-8') as f:
        f.write(f"Missing Dates for {city_name}:\n")
        if len(missing_dates) == 0:
            f.write("No missing dates detected.\n")
        else:
            for date in missing_dates:
                f.write(f"{date.strftime('%Y-%m-%d')}\n")

    if 'temp' in df_ts.columns:
        # Trung bình trượt 7 ngày & độ lệch chuẩn
        plt.figure(figsize=(14, 7))
        plt.plot(df_ts.index, df_ts['temp'], label='Temperature')
        rolling_mean = df_ts['temp'].rolling(window=7).mean()
        rolling_std = df_ts['temp'].rolling(window=7).std()
        plt.plot(df_ts.index, rolling_mean, color='red', label='7-day Rolling Mean')
        plt.fill_between(df_ts.index, rolling_mean - rolling_std, rolling_mean + rolling_std,
                         color='pink', alpha=0.3, label='Rolling Std')
        plt.title(f'Temperature Time Series with Rolling Mean & Std - {city_name}')
        plt.xlabel('Date')
        plt.ylabel('Temperature')
        plt.legend()
        plt.tight_layout()
        plt.savefig(plots_dir / f'{city_name}_temp_rolling.png')
        plt.close()

        # Biểu đồ ACF và PACF cho nhiệt độ
        fig, axes = plt.subplots(1, 2, figsize=(15, 5))
        plot_acf(df_ts['temp'].dropna(), lags=30, ax=axes[0])
        axes[0].set_title(f'ACF of Temperature - {city_name}')
        plot_pacf(df_ts['temp'].dropna(), lags=30, ax=axes[1])
        axes[1].set_title(f'PACF of Temperature - {city_name}')
        plt.tight_layout()
        plt.savefig(plots_dir / f'{city_name}_acf_pacf.png')
        plt.close()

        # Phân rã mùa: period=365 nếu dữ liệu >1 năm, ngược lại dùng period=7
        period = 365 if (df_ts.index.max() - df_ts.index.min()).days > 365 else 7
        try:
            decomposition = seasonal_decompose(df_ts['temp'].dropna(), model='additive', period=period)
            fig = decomposition.plot()
            fig.set_size_inches(14, 10)
            plt.suptitle(f'Seasonal Decomposition of Temperature - {city_name}', fontsize=16)
            plt.tight_layout()
            plt.savefig(plots_dir / f'{city_name}_seasonal_decompose.png')
            plt.close()
        except Exception as e:
            print(f"Seasonal decomposition failed for {city_name}: {e}")
    df_ts.reset_index(inplace=True)


import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from pathlib import Path

def merge_city_data(data_dict):
    """
    Gộp tất cả các DataFrame từ dictionary vào một DataFrame duy nhất.
    Thêm cột 'city' để xác định nguồn gốc dữ liệu.

    Parameters:
        data_dict (dict): Dictionary chứa DataFrame cho mỗi thành phố.

    Returns:
        pd.DataFrame: DataFrame đã được gộp.
    """
    dfs = []
    for city_name, df in data_dict.items():
        df_copy = df.copy()  # Tạo bản sao để không sửa đổi DataFrame gốc trong data_dict
        df_copy['city'] = city_name
        dfs.append(df_copy)
    merged_df = pd.concat(dfs, ignore_index=True)
    return merged_df



def correlation_analysis(df, city_name, plots_folder=PLOTS_FOLDER_NAME, threshold=0.3):
    """
    Tạo ma trận tương quan cho các biến số và lưu hình ảnh dưới dạng heatmap.

    Parameters:
        df (pd.DataFrame): DataFrame cần phân tích.
        city_name (str): Tên thành phố.
        plots_folder (str, optional): Tên thư mục con để lưu plots trong thư mục 'eda'. Mặc định là 'plots'.
        threshold (float, optional): Ngưỡng để hiển thị giá trị tương quan. Mặc định là 0.3.
    """
    numeric_cols = df.select_dtypes(include=[np.number]).columns
    corr_matrix = df[numeric_cols].corr()

    plt.figure(figsize=(min(2 + 0.5 * len(numeric_cols), 15), min(2 + 0.5 * len(numeric_cols), 15)))

    mask = np.triu(np.ones_like(corr_matrix, dtype=bool))  # Chỉ hiển thị một nửa ma trận
    sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', center=0, mask=mask,
                fmt=".2f", annot_kws={"size": 8}, vmin=-1, vmax=1,
                cbar_kws={'shrink': 0.8}, linewidths=0.5, linecolor='black')

    plt.title(f'Correlation Matrix - {city_name}', fontsize=14)
    plt.xticks(rotation=45, ha='right', fontsize=10)
    plt.yticks(fontsize=10)
    plt.tight_layout()

    plots_dir = Path(EDA_OUTPUT_FOLDER) / plots_folder
    plots_dir.mkdir(parents=True, exist_ok=True)
    plt.savefig(plots_dir / f'{city_name}_correlation.png', dpi=300)
    plt.close()


####################################
# 3. ĐÁNH GIÁ & TIỀN XỬ LÝ DỮ LIỆU
####################################
def evaluate_data(df, city_name, metrics=MAIN_METRICS):
    """
    Đánh giá dữ liệu phục vụ cho mô hình dự báo:
      - Đếm số outlier và tỷ lệ outlier dựa trên IQR.
      - Tính skewness và kurtosis cho các biến số.
      - Kiểm định ADF cho chuỗi thời gian của các metrics chỉ định.

    Parameters:
        df (pd.DataFrame): DataFrame cần đánh giá.
        city_name (str): Tên thành phố.
        metrics (list, optional): Danh sách các metrics số cần đánh giá. Mặc định là MAIN_METRICS.

    Returns:
        dict: Dictionary chứa kết quả đánh giá (outlier counts, skewness/kurtosis, stationarity).
    """
    evaluation = {}

    # Đếm outlier theo IQR và tính tỷ lệ
    outlier_counts = {}
    for metric in metrics:
        if metric in df.columns:
            Q1 = df[metric].quantile(0.25)
            Q3 = df[metric].quantile(0.75)
            IQR = Q3 - Q1
            lower_bound = Q1 - 1.5 * IQR
            upper_bound = Q3 + 1.5 * IQR
            outliers = df[(df[metric] < lower_bound) | (df[metric] > upper_bound)]
            outlier_count = outliers.shape[0]
            outlier_percentage = (outlier_count / len(df)) * 100 if len(df) > 0 else 0
            outlier_counts[metric] = {'count': outlier_count, 'percentage': outlier_percentage}
    evaluation['outlier_counts'] = outlier_counts

    # Tính skewness và kurtosis
    skew_kurt = {}
    for metric in metrics:
        if metric in df.columns:
            skew_kurt[metric] = {
                'skewness': df[metric].skew(),
                'kurtosis': df[metric].kurtosis()
            }
    evaluation['skewness_kurtosis'] = skew_kurt

    # Kiểm định ADF cho chuỗi thời gian của các metrics
    stationarity = {}
    for metric in metrics:
        if metric in df.columns:
            temp_series = df[metric].dropna() # Tên biến 'temp_series' không còn đúng, cần đổi tên nếu dùng cho nhiều metrics
            try:
                result = adfuller(temp_series)
                stationarity[metric] = { # Lưu kết quả ADF cho từng metric
                    'ADF Statistic': result[0],
                    'p-value': result[1],
                    'Used Lag': result[2],
                    'Number of Observations': result[3],
                    'Critical Values': result[4],
                    'Stationary': result[1] < 0.05
                }
            except Exception as e:
                stationarity[metric] = {'error': str(e)} # Lưu lỗi cho từng metric
    evaluation['stationarity'] = stationarity

    return evaluation


def generate_evaluation_report(city_name, evaluation, report_folder=REPORTS_FOLDER_NAME):
    """
    Xuất báo cáo đánh giá chi tiết dưới dạng file text.

    Parameters:
        city_name (str): Tên thành phố.
        evaluation (dict): Dictionary chứa kết quả đánh giá từ `evaluate_data`.
        report_folder (str, optional): Tên thư mục con để lưu reports trong thư mục 'eda'. Mặc định là REPORTS_FOLDER_NAME.
    """
    report_dir = Path(EDA_OUTPUT_FOLDER) / report_folder
    report_dir.mkdir(parents=True, exist_ok=True)
    eval_file = report_dir / f'{city_name}_evaluation.txt'

    with open(eval_file, 'w', encoding='utf-8') as f:
        f.write(f"Evaluation Summary for {city_name}\n")
        f.write("=" * 40 + "\n\n")

        f.write("Outlier Counts (IQR method):\n")
        for metric, counts in evaluation.get('outlier_counts', {}).items(): # Lặp qua các metrics và counts
            f.write(f"  - {metric}: Count = {counts['count']}, Percentage = {counts['percentage']:.2f}%\n")
        f.write("\n")

        f.write("Skewness and Kurtosis:\n")
        for metric, stats in evaluation.get('skewness_kurtosis', {}).items():
            f.write(f"  - {metric}: skewness = {stats['skewness']:.4f}, kurtosis = {stats['kurtosis']:.4f}")
            if abs(stats['skewness']) > 1:
                f.write(f" (Skewness > 1 indicates a moderately skewed distribution)") # Thêm diễn giải
            f.write("\n")
        f.write("\n")

        f.write("Stationarity Test (ADF) on Time Series:\n")
        for metric, stationarity_result in evaluation.get('stationarity', {}).items(): # Lặp qua các metrics và kết quả ADF
            f.write(f"  - {metric}:\n")
            if 'error' in stationarity_result:
                f.write(f"    Error: {stationarity_result['error']}\n")
            else:
                f.write(f"    - ADF Statistic: {stationarity_result.get('ADF Statistic'):.4f}\n")
                f.write(f"    - p-value: {stationarity_result.get('p-value'):.4f}")
                if stationarity_result.get('p-value') < 0.05:
                    f.write(" (p-value < 0.05 suggests the series is stationary)") # Thêm diễn giải
                else:
                    f.write(" (p-value >= 0.05 suggests the series is non-stationary)")
                f.write(f"\n    - Used Lag: {stationarity_result.get('Used Lag')}\n")
                f.write(f"    - Number of Observations: {stationarity_result.get('Number of Observations')}\n")
                f.write("    - Critical Values:\n")
                for key, value in stationarity_result.get('Critical Values', {}).items():
                    f.write(f"        {key}: {value:.4f}\n")
                f.write(f"    - Stationary: {'Yes' if stationarity_result.get('Stationary') else 'No'}\n")
        f.write("\n")

        # Gợi ý tiền xử lý (ví dụ đơn giản)
        f.write("--- \n")
        f.write("Suggested Preprocessing Steps based on Evaluation:\n")
        for metric, stationarity_result in evaluation.get('stationarity', {}).items():
            if 'Stationary' in stationarity_result and not stationarity_result['Stationary']:
                f.write(f"  - Metric '{metric}' appears to be non-stationary. Consider applying differencing or other stationarization techniques for time series modeling.\n")
        for metric, stats in evaluation.get('skewness_kurtosis', {}).items():
            if abs(stats['skewness']) > 1:
                f.write(f"  - Metric '{metric}' is skewed. Consider applying transformations like log or box-cox to reduce skewness.\n")


    print(f"Evaluation report generated: {eval_file}")


####################################
# 4. TIỀN XỬ LÝ DỮ LIỆU CHO DỰ BÁO
####################################
def handle_missing_values(df, strategy=MISSING_VALUE_STRATEGY):
    """
    Xử lý giá trị thiếu:
      - 'ffill': forward-fill (với back-fill dự phòng).
      - 'interpolate': nội suy theo thời gian.

    Parameters:
        df (pd.DataFrame): DataFrame cần xử lý missing values.
        strategy (str, optional): Chiến lược xử lý missing values ('ffill' hoặc 'interpolate'). Mặc định là MISSING_VALUE_STRATEGY.

    Returns:
        pd.DataFrame: DataFrame đã được xử lý missing values.
    """
    if strategy == 'ffill':
        df_cleaned = df.fillna(method='ffill').fillna(method='bfill')
    elif strategy == 'interpolate':
        df_cleaned = df.interpolate(method='time')
    else:
        df_cleaned = df.fillna(method='ffill').fillna(method='bfill')
    return df_cleaned


def handle_outliers(df, columns):
    """
    Xử lý outlier bằng cách cắt (clip) giá trị dựa trên phương pháp IQR cho các cột chỉ định.

    Parameters:
        df (pd.DataFrame): DataFrame cần xử lý outliers.
        columns (list): Danh sách tên cột cần xử lý outliers.

    Returns:
        pd.DataFrame: DataFrame đã được xử lý outliers.
    """
    df_cleaned = df.copy()
    for col in columns:
        if col in df_cleaned.columns:
            Q1 = df_cleaned[col].quantile(0.25)
            Q3 = df_cleaned[col].quantile(0.75)
            IQR = Q3 - Q1
            lower_bound = Q1 - 1.5 * IQR
            upper_bound = Q3 + 1.5 * IQR
            df_cleaned[col] = df_cleaned[col].clip(lower=lower_bound, upper=upper_bound)
    return df_cleaned


def preprocess_data(df, city_name, metrics=MAIN_METRICS, cleaned_data_folder=CLEANED_DATA_FOLDER_NAME):
    """
    Quy trình tiền xử lý:
      1. Xử lý giá trị thiếu.
      2. Xử lý outlier cho các biến số chính.
      3. Lưu dữ liệu đã xử lý ra file CSV.

    Parameters:
        df (pd.DataFrame): DataFrame cần tiền xử lý.
        city_name (str): Tên thành phố.
        metrics (list, optional): Danh sách các metrics số cần xử lý outliers. Mặc định là MAIN_METRICS.
        cleaned_data_folder (str, optional): Tên thư mục con để lưu cleaned data trong thư mục 'eda'. Mặc định là CLEANED_DATA_FOLDER_NAME.

    Returns:
        pd.DataFrame: DataFrame đã được tiền xử lý.
    """
    print(f"Preprocessing data for {city_name}...")
    df_clean = handle_missing_values(df, strategy=MISSING_VALUE_STRATEGY)
    df_clean = handle_outliers(df_clean, metrics)

    cleaned_dir = Path(EDA_OUTPUT_FOLDER) / cleaned_data_folder
    cleaned_dir.mkdir(parents=True, exist_ok=True)
    cleaned_file = cleaned_dir / f'{city_name}_cleaned.csv'
    df_clean.to_csv(cleaned_file, index=False)
    print(f"Cleaned data saved to: {cleaned_file}")
    return df_clean


####################################
# 5. PHÂN TÍCH GIỮA NUMERICAL & CATEGORICAL
####################################
def cross_analysis(df, city_name, plots_folder=PLOTS_FOLDER_NAME):
    """
    Phân tích mối quan hệ giữa các biến số và biến phân loại.
    Chỉ thực hiện với các biến phân loại có số lượng giá trị duy nhất nhỏ (<= 10).

    Parameters:
        df (pd.DataFrame): DataFrame cần phân tích.
        city_name (str): Tên thành phố.
        plots_folder (str, optional): Tên thư mục con để lưu plots trong thư mục 'eda'. Mặc định là 'plots'.
    """
    cat_cols = df.select_dtypes(include=['object']).columns.tolist()
    if 'datetime' in cat_cols:
        cat_cols.remove('datetime')
    num_cols = df.select_dtypes(include=[np.number]).columns.tolist()

    plots_dir = Path(EDA_OUTPUT_FOLDER) / plots_folder
    for cat in cat_cols:
        if df[cat].nunique() <= 10:
            for num in num_cols:
                try:
                    data = df[[cat, num]].dropna()
                    if data.empty:
                        continue
                    plt.figure(figsize=(10, 6))
                    sns.boxplot(x=data[cat], y=data[num])
                    plt.title(f'{num} Distribution by {cat} - {city_name}')
                    plt.xticks(rotation=45, ha='right')
                    plt.tight_layout()
                    plt.savefig(plots_dir / f'{city_name}_{num}_by_{cat}_boxplot.png')
                    plt.close()
                except Exception as e:
                    print(f"Error plotting {num} by {cat} for {city_name}: {e}")


####################################
# 6. TẠO BÁO CÁO EDA (MARKDOWN)
####################################
def generate_eda_report(city_name, df, report_folder=REPORTS_FOLDER_NAME, plots_folder=PLOTS_FOLDER_NAME):
    """
    Tạo báo cáo EDA dạng Markdown, bao gồm:
      - Thông tin dataset, thống kê của biến số.
      - Phân tích tương quan.
      - Các biểu đồ của phân tích thời gian.
      - Phân tích các biến phân loại thông minh và mối quan hệ numerical vs categorical.
      - Tham chiếu đến báo cáo đánh giá.

    Parameters:
        city_name (str): Tên thành phố.
        df (pd.DataFrame): DataFrame đã được phân tích.
        report_folder (str, optional): Tên thư mục con để lưu reports trong thư mục 'eda'. Mặc định là REPORTS_FOLDER_NAME.
        plots_folder (str, optional): Tên thư mục con chứa plots trong thư mục 'eda'. Mặc định là 'plots'.
    """
    report_dir = Path(EDA_OUTPUT_FOLDER) / report_folder
    report_dir.mkdir(parents=True, exist_ok=True)

    with open(report_dir / f'{city_name}_report.md', 'w', encoding='utf-8') as f:
        f.write(f"# EDA Report for {city_name}\n\n")

        # Tóm tắt chung (thêm vào đầu báo cáo)
        f.write("## Executive Summary\n")
        f.write("This report provides an Exploratory Data Analysis (EDA) for the weather data of {city_name}. ")
        f.write("It includes dataset overview, missing value analysis, statistical summaries, ")
        f.write("correlation analysis, temporal analysis, categorical feature analysis, and data quality evaluation.\n\n")

        # Dataset Overview
        f.write("## Dataset Overview\n")
        f.write("This section provides a general overview of the dataset.\n\n") # Thêm mô tả section
        f.write(f"* **Number of records:** {len(df)}\n")
        f.write(f"* **Time period:** {df['datetime'].min()} to {df['datetime'].max()}\n")
        f.write(f"* **Number of features:** {len(df.columns)}\n\n")

        # Missing Values
        f.write("## Missing Values\n")
        f.write("This section details the missing values present in the dataset.\n\n") # Thêm mô tả section
        missing_values = df.isnull().sum()
        for col, missing in missing_values[missing_values > 0].items():
            f.write(f"* **{col}**: {missing} missing values\n")
        f.write("\n")

        # Key Weather Statistics (Numerical)
        f.write("## Key Weather Statistics (Numerical)\n")
        f.write("This section presents descriptive statistics for the numerical weather metrics.\n\n") # Thêm mô tả section
        num_cols = df.select_dtypes(include=[np.number]).columns.tolist()
        for col in num_cols:
            f.write(f"### {col}\n")
            f.write(f"* **Average:** {df[col].mean():.2f}\n")
            f.write(f"* **Maximum:** {df[col].max():.2f}\n")
            f.write(f"* **Minimum:** {df[col].min():.2f}\n\n")

        # Correlation Analysis
        f.write("## Correlation Analysis\n")
        f.write("Correlation analysis helps to understand the linear relationships between numerical features. ") # Thêm mô tả section
        f.write("The heatmap below visualizes the correlation matrix.\n\n")
        f.write(f"![Correlation Matrix](../{plots_folder}/{city_name}_correlation.png)\n\n")

        # Numerical Analysis Plots
        f.write("## Numerical Analysis Plots\n")
        f.write("Distributions and box plots of key numerical metrics are shown below to understand data spread and potential outliers.\n\n") # Thêm mô tả section
        f.write(f"![Distributions](../{plots_folder}/{city_name}_distributions.png)\n")
        f.write(f"![Box Plots](../{plots_folder}/{city_name}_boxplots.png)\n\n")

        # Temporal Analysis
        f.write("## Temporal Analysis\n")
        f.write("This section explores the temporal patterns in the weather data, including monthly and daily trends.\n\n") # Thêm mô tả section
        f.write(f"![Monthly Temperature](../{plots_folder}/{city_name}_monthly_temp.png)\n")
        f.write(f"![Daily Temperature](../{plots_folder}/{city_name}_daily_temp.png)\n")
        f.write(f"![Temperature vs Humidity](../{plots_folder}/{city_name}_temp_humidity.png)\n\n")

        # Advanced Temporal Analysis
        f.write("## Advanced Temporal Analysis\n")
        f.write("Advanced time series analysis, including rolling statistics, ACF/PACF plots, and seasonal decomposition, are presented here.\n\n") # Thêm mô tả section
        f.write(f"![Temperature Rolling Stats](../{plots_folder}/{city_name}_temp_rolling.png)\n")
        f.write(f"![ACF and PACF](../{plots_folder}/{city_name}_acf_pacf.png)\n")
        f.write(f"![Seasonal Decomposition](../{plots_folder}/{city_name}_seasonal_decompose.png)\n\n")

        # Categorical Analysis (Smart)
        f.write("## Categorical Analysis\n")
        f.write("Analysis of categorical features, including value counts and distribution plots where applicable.\n\n") # Thêm mô tả section
        cat_cols = df.select_dtypes(include=['object']).columns.tolist()
        skip_cols = ['datetime', 'sunrise', 'sunset']
        cat_cols = [col for col in cat_cols if col not in skip_cols]
        for col in cat_cols:
            nunique = df[col].nunique()
            f.write(f"### {col} Analysis\n")
            if nunique == 1:
                f.write(f"Column '{col}' is constant with only 1 unique value. No further analysis is provided.\n\n")
            elif nunique <= 15:
                f.write("Value Counts:\n")
                value_counts = df[col].value_counts().to_dict()
                for k, v in value_counts.items():
                    f.write(f"* **{k}**: {v}\n")
                f.write(f"\n![Count Plot for {col}](../{plots_folder}/{city_name}_{col}_countplot.png)\n\n")
            elif nunique <= 50:
                f.write(f"Value Counts (Top 20):\n")
                value_counts = df[col].value_counts().nlargest(20).to_dict()
                for k, v in value_counts.items():
                    f.write(f"* **{k}**: {v}\n")
                f.write(f"\n![Top Value Count Plot for {col}](../{plots_folder}/{city_name}_{col}_top_countplot.png)\n\n")
            else:
                f.write(
                    f"High cardinality column with {nunique} unique values. Detailed value counts not displayed.\n\n")

        # Numerical vs Categorical Analysis
        f.write("## Numerical vs Categorical Analysis\n")
        f.write("Box plots showing the distribution of numerical features across different categories (for low cardinality categorical features).\n\n") # Thêm mô tả section
        for col in cat_cols:
            if df[col].nunique() <= 10:
                for num in num_cols:
                    f.write(f"### {num} by {col}\n")
                    f.write(f"![Box Plot: {num} by {col}](../{plots_folder}/{city_name}_{num}_by_{col}_boxplot.png)\n\n")

        # Evaluation Summary
        f.write("## Evaluation Summary\n")
        f.write("This section summarizes the data quality evaluation. ") # Thêm mô tả section
        f.write("Please refer to the detailed evaluation report for in-depth analysis of outliers, skewness/kurtosis, and stationarity.\n\n")
        f.write(f"Please refer to the detailed evaluation report: `{city_name}_evaluation.txt`.\n")
        f.write("This file includes information about outliers, skewness/kurtosis, and stationarity test results.\n")

        # Conclusion (thêm vào cuối báo cáo)
        f.write("\n## Conclusion\n")
        f.write("Based on the EDA, key findings for {city_name} include: ... (Summary of key findings, e.g., important correlations, trends, data quality issues).") # Thêm tóm tắt kết luận

    print(f"EDA report generated: {report_dir / f'{city_name}_report.md'}")


####################################
# 7. CHẠY TOÀN BỘ QUY TRÌNH
####################################
def run_eda_for_city(city_name, df):
    """Thực hiện quy trình EDA cho một thành phố cụ thể."""
    print(f"\nProcessing {city_name}...")

    # Phân tích ban đầu
    basic_info(df, city_name)
    numeric_analysis(df, city_name)
    smart_categorical_analysis(df, city_name)
    temporal_analysis(df, city_name)
    correlation_analysis(df, city_name)
    advanced_temporal_analysis(df, city_name)
    cross_analysis(df, city_name)

    # Đánh giá dữ liệu gốc
    evaluation = evaluate_data(df, city_name)
    generate_evaluation_report(city_name, evaluation)

    # Tiền xử lý dữ liệu cho mô hình dự báo
    df_clean = preprocess_data(df, city_name)
    # (Có thể đánh giá lại dữ liệu sau tiền xử lý nếu cần)
    evaluation_clean = evaluate_data(df_clean, f"{city_name}_clean")
    generate_evaluation_report(f"{city_name}_clean", evaluation_clean)

    # Tạo báo cáo EDA dạng Markdown (tham chiếu đến báo cáo đánh giá)
    generate_eda_report(city_name, df)

    print(f"Completed analysis for {city_name}")
    print("Evaluation Summary:")
    print(evaluation)


def main():
    """
    Chạy quy trình EDA cho tất cả các file CSV trong thư mục 'datasets'.
    Tạo thư mục 'eda' và các thư mục con nếu chưa tồn tại.
    """
    # Tạo cấu trúc thư mục cho EDA
    Path(EDA_OUTPUT_FOLDER).mkdir(exist_ok=True)
    (Path(EDA_OUTPUT_FOLDER) / PLOTS_FOLDER_NAME).mkdir(exist_ok=True) # Tạo thư mục plots
    (Path(EDA_OUTPUT_FOLDER) / REPORTS_FOLDER_NAME).mkdir(exist_ok=True) # Tạo thư mục reports
    (Path(EDA_OUTPUT_FOLDER) / CLEANED_DATA_FOLDER_NAME).mkdir(exist_ok=True) # Tạo thư mục cleaned_data

    # Load dữ liệu (giả sử các file CSV nằm trong thư mục '../datasets')
    data_dict = load_data('../datasets')

    # Gộp dữ liệu của tất cả các thành phố vào một DataFrame duy nhất
    merged_df = merge_city_data(data_dict)

    # Với mỗi tập dữ liệu (mỗi file CSV tương ứng với 1 thành phố)
    for city_name, df in data_dict.items():
        run_eda_for_city(city_name, df)

    print("\n====================== PHÂN TÍCH DATAFRAME GỘP (merged_df) =======================")
    run_eda_for_city("Merged_Cities", merged_df)  # Gọi EDA cho DataFrame đã gộp, đặt tên là "Merged_Cities"


if __name__ == "__main__":
    # main()
    Path(EDA_OUTPUT_FOLDER).mkdir(exist_ok=True)
    (Path(EDA_OUTPUT_FOLDER) / PLOTS_FOLDER_NAME).mkdir(exist_ok=True)  # Tạo thư mục plots
    (Path(EDA_OUTPUT_FOLDER) / REPORTS_FOLDER_NAME).mkdir(exist_ok=True)  # Tạo thư mục reports
    (Path(EDA_OUTPUT_FOLDER) / CLEANED_DATA_FOLDER_NAME).mkdir(exist_ok=True)  # Tạo thư mục cleaned_data

    # Load dữ liệu (giả sử các file CSV nằm trong thư mục '../datasets')
    data_dict = load_data('../datasets')

    # Gộp dữ liệu của tất cả các thành phố vào một DataFrame duy nhất
    merged_df = merge_city_data(data_dict)

    print("\n====================== PHÂN TÍCH DATAFRAME GỘP (merged_df) =======================")
    run_eda_for_city("Merged_Cities", merged_df)  # Gọi EDA cho DataFrame đã gộp, đặt tên là "Merged_Cities"
