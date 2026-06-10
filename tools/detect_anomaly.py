import pandas as pd
import os
from sklearn.ensemble import IsolationForest
import datetime

def write_log(log_file, message):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(log_file, "a", encoding="utf-8") as f:
        f.write(f"[{timestamp}] {message}\n")

def detect_anomalies():
    csv_path = "datasets/csv/extracted_features.csv"
    log_path = "outputs/logs/pipeline_run.log"
    
    if not os.path.exists(csv_path):
        print("LỖI: Không tìm thấy file dữ liệu. Hãy chạy extract_tls_flows.py trước!")
        return 0
        
    # 1. Đọc dữ liệu
    df = pd.read_csv(csv_path)
    features = df[['packet_count', 'total_bytes', 'max_packet_size', 'min_packet_size']]
    
    print("Đang quét các luồng mạng để săn tìm hành vi bất thường (DDoS, Malware, Scanning)...")
    
    # 2. Sử dụng thuật toán Isolation Forest
    # Thiết lập contamination=0.05 nghĩa là giả định có khoảng 5% luồng mạng là độc hại/bất thường
    iso_forest = IsolationForest(contamination=0.05, random_state=42)
    
    # AI trả về 1 (Bình thường) và -1 (Bất thường)
    df['anomaly'] = iso_forest.fit_predict(features)
    
    # 3. Lọc và đếm các luồng bị đánh dấu là bất thường
    anomalies = df[df['anomaly'] == -1]
    anomaly_count = len(anomalies)
    
    if anomaly_count > 0:
        print(f"CẢNH BÁO BẢO MẬT: Đã phát hiện {anomaly_count} luồng mạng nghi vấn!")
        write_log(log_path, f"Anomaly Detector Agent -> Phát hiện {anomaly_count} luồng dữ liệu mạng bất thường.")
    else:
        print("Hệ thống an toàn. Không phát hiện luồng mạng bất thường nào.")
        write_log(log_path, "Anomaly Detector Agent -> Không phát hiện luồng dữ liệu mạng bất thường.")
        
    return anomaly_count

if __name__ == "__main__":
    detect_anomalies()
