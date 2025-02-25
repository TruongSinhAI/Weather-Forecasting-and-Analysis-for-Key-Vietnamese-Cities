from pathlib import Path

import pandas as pd
from matplotlib import pyplot as plt
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
from statsmodels.tsa.seasonal import seasonal_decompose

PLOTS_FOLDER_NAME = 'plots2'

def advanced_temporal_analysis(df, city_names, plots_folder=PLOTS_FOLDER_NAME):
    """
    Phân tích chuỗi thời gian nâng cao:
      - Kiểm tra các ngày bị thiếu.
      - Biểu đồ chuỗi thời gian với trung bình trượt và độ lệch chuẩn cho 'temp'.
      - Biểu đồ ACF và PACF cho 'temp'.
      - Phân rã mùa của chuỗi nhiệt độ 'temp'.

    Parameters:
        df (pd.DataFrame): DataFrame cần phân tích. Phải chứa cột 'city' để phân biêt dữ liệu các thành phố.
        city_names (list): Danh sách tên các thành phố.
        plots_folder (str, optional): Tên thư mục con để lưu plots trong thư mục 'eda'. Mặc định là 'plots'.
    """
    plots_dir = Path('eda') / plots_folder
    # for city_name in city_names:
    #     city_df = df[df['city'] == city_name].copy()
    #     city_df.sort_values('datetime', inplace=True)
    #     city_df.set_index('datetime', inplace=True)
    #
    #     # Kiểm tra các ngày bị thiếu (giả sử dữ liệu ghi nhận hàng ngày)
    #     full_date_range = pd.date_range(start=city_df.index.min(), end=city_df.index.max(), freq='D')
    #     missing_dates = full_date_range.difference(city_df.index)
    #
    #     if 'temp' in city_df.columns:
    #         # Trung bình trượt 7 ngày & độ lệch chuẩn
    #         plt.figure(figsize=(14, 7))
    #         plt.plot(city_df.index, city_df['temp'], label='Temperature')
    #         rolling_mean = city_df['temp'].rolling(window=7).mean()
    #         rolling_std = city_df['temp'].rolling(window=7).std()
    #         plt.plot(city_df.index, rolling_mean, color='red', label='7-day Rolling Mean')
    #         plt.fill_between(city_df.index, rolling_mean - rolling_std, rolling_mean + rolling_std,
    #                          color='pink', alpha=0.3, label='Rolling Std')
    #         plt.title(f'Temperature Time Series with Rolling Mean & Std - {city_name}')
    #         plt.xlabel('Date')
    #         plt.ylabel('Temperature')
    #         plt.legend()
    #         plt.tight_layout()
    #         plt.savefig(plots_dir / f'{city_name}_temp_rolling.png')
    #         plt.close()
    #
    #         # Biểu đồ ACF và PACF cho nhiệt độ
    #         fig, axes = plt.subplots(1, 2, figsize=(15, 5))
    #         plot_acf(city_df['temp'].dropna(), lags=30, ax=axes[0])
    #         axes[0].set_title(f'ACF of Temperature - {city_name}')
    #         plot_pacf(city_df['temp'].dropna(), lags=30, ax=axes[1])
    #         axes[1].set_title(f'PACF of Temperature - {city_name}')
    #         plt.tight_layout()
    #         plt.savefig(plots_dir / f'{city_name}_acf_pacf.png')
    #         plt.close()
    #
    #         # Phân rã mùa: period=365 nếu dữ liệu >1 năm, ngược lại dùng period=7
    #         period = 365 if (city_df.index.max() - city_df.index.min()).days > 365 else 7
    #         try:
    #             decomposition = seasonal_decompose(city_df['temp'].dropna(), model='additive', period=period)
    #             fig = decomposition.plot()
    #             fig.set_size_inches(14, 10)
    #             plt.suptitle(f'Seasonal Decomposition of Temperature - {city_name}', fontsize=16)
    #             plt.tight_layout()
    #             plt.savefig(plots_dir / f'{city_name}_seasonal_decompose.png')
    #             plt.close()
    #         except Exception as e:
    #             print(f"Seasonal decomposition failed for {city_name}: {e}")
    #     city_df.reset_index(inplace=True)


    def ana2(city_df):
        city_name = 'all'
        if 'temp' in city_df.columns:
            # Trung bình trượt 7 ngày & độ lệch chuẩn
            plt.figure(figsize=(14, 7))
            plt.plot(city_df.index, city_df['temp'], label='Temperature')
            rolling_mean = city_df['temp'].rolling(window=7).mean()
            rolling_std = city_df['temp'].rolling(window=7).std()
            plt.plot(city_df.index, rolling_mean, color='red', label='7-day Rolling Mean')
            plt.fill_between(city_df.index, rolling_mean - rolling_std, rolling_mean + rolling_std,
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
            plot_acf(city_df['temp'].dropna(), lags=30, ax=axes[0])
            axes[0].set_title(f'ACF of Temperature - {city_name}')
            plot_pacf(city_df['temp'].dropna(), lags=30, ax=axes[1])
            axes[1].set_title(f'PACF of Temperature - {city_name}')
            plt.tight_layout()
            plt.savefig(plots_dir / f'{city_name}_acf_pacf.png')
            plt.close()

            # Phân rã mùa: period=365 nếu dữ liệu >1 năm, ngược lại dùng period=7
            period = 365 if (city_df.index.max() - city_df.index.min()) > 365 else 7
            try:
                decomposition = seasonal_decompose(city_df['temp'].dropna(), model='additive', period=period)
                fig = decomposition.plot()
                fig.set_size_inches(14, 10)
                plt.suptitle(f'Seasonal Decomposition of Temperature - {city_name}', fontsize=16)
                plt.tight_layout()
                plt.savefig(plots_dir / f'{city_name}_seasonal_decompose.png')
                plt.close()
            except Exception as e:
                print(f"Seasonal decomposition failed for {city_name}: {e}")
        city_df.reset_index(inplace=True)

    ana2(df)
# --- 1. Đọc dữ liệu tổng hợp ---
print("\n--- 1. Đọc dữ liệu tổng hợp ---")

file_path = './eda/cleaned_data/Merged_Cities_cleaned.csv'
df = pd.read_csv(file_path)

print("5 dòng dữ liệu đầu tiên:")
print(df.head())

# --- 2. Chuẩn bị dữ liệu ---
print("\n--- 2. Chuẩn bị dữ liệu ---")

# Chuyển đổi 'datetime' thành kiểu datetime
if 'datetime' in df.columns:
    df['datetime'] = pd.to_datetime(df['datetime'])
else:
    print("Lỗi: Không tìm thấy cột 'datetime'.")
    exit()

# Thêm cột 'month', 'year', và 'day' nếu chưa có
if 'month' not in df.columns:
    df['month'] = df['datetime'].dt.month

if 'year' not in df.columns:
    df['year'] = df['datetime'].dt.year

if 'day' not in df.columns:
    df['day'] = df['datetime'].dt.day

# Hỏi người dùng chọn năm hoặc tất cả các năm
year_input = input("Vui lòng nhập năm (hoặc 'all' để chọn tất cả các năm): ").strip().lower()

if year_input != 'all':
    try:
        year_input = int(year_input)
        df = df[df['year'] == year_input]
    except ValueError:
        print("Lỗi: Vui lòng nhập một năm hợp lệ hoặc 'all'.")
        exit()

city_names = df['city'].unique()
advanced_temporal_analysis(df, city_names)