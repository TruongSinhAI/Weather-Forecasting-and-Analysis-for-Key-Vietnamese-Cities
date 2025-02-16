import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from pathlib import Path

# Định nghĩa đường dẫn
DATASET_PATH = "../datasets"
CITIES = ["HoChiMinh", "Hanoi", "DaNang"]
OUTPUT_FOLDER = "eda"
PLOTS_FOLDER = f"{OUTPUT_FOLDER}/plots2"
TEXT_OUTPUT = f"{OUTPUT_FOLDER}/correlation_results.txt"

# Đọc và gộp dữ liệu
dataframes = []
for city in CITIES:
    df = pd.read_csv(f"{DATASET_PATH}/{city}.csv")
    df["city"] = city  # Thêm cột thành phố
    dataframes.append(df)

# Gộp tất cả thành 1 DataFrame
df_merged = pd.concat(dataframes, ignore_index=True)

# Chỉ chọn các cột số để tính tương quan
numeric_cols = df_merged.select_dtypes(include=[np.number]).columns
corr_matrix = df_merged[numeric_cols].corr()

# Xuất kết quả tương quan ra file text
Path(OUTPUT_FOLDER).mkdir(parents=True, exist_ok=True)
with open(TEXT_OUTPUT, "w") as f:
    f.write("### Correlation Matrix ###\n")
    f.write(corr_matrix.to_string())
print(f"✅ Ma trận tương quan đã được lưu vào {TEXT_OUTPUT}")

# Giảm độ rối của heatmap bằng cách chỉ hiển thị giá trị tương quan mạnh
threshold = 0.0  # Ngưỡng hiển thị giá trị tương quan
mask = np.triu(np.ones_like(corr_matrix, dtype=bool))  # Chỉ hiển thị một nửa ma trận
filtered_corr = corr_matrix.where((corr_matrix > threshold) | (corr_matrix < -threshold), np.nan)

# Vẽ heatmap
plt.figure(figsize=(12, 8))
sns.heatmap(filtered_corr, annot=True, cmap='coolwarm', center=0, fmt=".2f",
            linewidths=0.5, linecolor="black", mask=mask, cbar_kws={'shrink': 0.8})

plt.title('Correlation Matrix - Merged Data', fontsize=14)
plt.xticks(rotation=45, ha='right', fontsize=10)
plt.yticks(fontsize=10)
plt.tight_layout()

# Lưu hình ảnh
Path(PLOTS_FOLDER).mkdir(parents=True, exist_ok=True)
heatmap_path = f"{PLOTS_FOLDER}/merged_correlation.png"
plt.savefig(heatmap_path, dpi=300)

print(f"✅ Heatmap đã được lưu vào {heatmap_path}")
