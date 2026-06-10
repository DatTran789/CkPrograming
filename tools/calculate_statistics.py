import pandas as pd
import os

def calculate_flow_stats():
    csv_path = "datasets/csv/extracted_features.csv"
    if not os.path.exists(csv_path):
        print("❌ Không tìm thấy file dữ liệu mạng. Hãy chạy bộ trích xuất trước.")
        return

    df = pd.read_csv(csv_path)
    print("=== 📊 BẢNG THỐNG KÊ LƯU LƯỢNG MẠNG (FLOW STATISTICS) ===")
    print(f"- Tổng số luồng (flows) đã phân tích: {len(df)}")
    
    if 'label' in df.columns:
        print("\n[Phân bố theo nhãn ứng dụng]")
        print(df['label'].value_counts().to_string())
    
    print("\n[Thống kê mô tả chi tiết các đặc trưng]")
    # Tính toán mean, std, min, max cho các cột số liệu mạng
    stats = df[['packet_count', 'total_bytes', 'max_packet_size', 'min_packet_size']].describe()
    print(stats.to_string())

if __name__ == "__main__":
    calculate_flow_stats()
