import matplotlib
matplotlib.use('TkAgg')  # Use 'TkAgg' for interactive plots, or 'agg' for non-interactive plots
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import os

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

var = 'humidity'  # Biến cần vẽ

# Tính giá trị trung bình hàng tháng
monthly_avg = df.groupby(['city', 'year', 'month'])[var].mean().reset_index()

# Tính giá trị trung bình hàng ngày
daily_avg = df.groupby(['city', 'year', 'month', 'day'])[var].mean().reset_index()

# --- 3. Vẽ Biểu Đồ Giá Trị Trung Bình Hàng Tháng và Hàng Ngày ---
print("\n--- 3. Vẽ Biểu Đồ Giá Trị Trung Bình Hàng Tháng và Hàng Ngày ---")

# Thiết lập theme đẹp hơn
sns.set_theme(style="darkgrid")

# Tạo subplot với 2 biểu đồ (1 hàng, 2 cột)
fig, axes = plt.subplots(1, 1, figsize=(18, 8))

var2 = 'month'
# Biểu đồ 1: Giá trị trung bình hàng tháng
sns.lineplot(data=monthly_avg, x=var2, y=var, hue='city', marker='o', ax=axes)
axes.set_title(f'Average {var.capitalize()} by {var2}')
axes.set_xlabel(var2.capitalize())
axes.set_ylabel(f'Average {var.capitalize()}')
axes.legend(title='City')
axes.grid(True)

# Điều chỉnh layout để không bị chồng nhãn
plt.tight_layout()

# Lưu biểu đồ vào folder eda/plots2
output_dir = './eda/plots2'
os.makedirs(output_dir, exist_ok=True)
output_file = os.path.join(output_dir, f'average_{var}_{var2}ly_plots_{year_input}.png')
plt.savefig(output_file)

plt.show()

print("\n--- Hoàn thành vẽ Biểu Đồ Giá Trị Trung Bình Hàng Tháng và Hàng Ngày ---")
print(f"Biểu đồ đã được lưu vào {output_file}")