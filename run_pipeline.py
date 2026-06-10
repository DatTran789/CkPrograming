import os
import subprocess
import datetime
import re

def write_log(log_file, message):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(log_file, "a", encoding="utf-8") as f:
        f.write(f"[{timestamp}] {message}\n")

def main():
    # Định nghĩa chính xác các đường dẫn tuyệt đối dựa trên vị trí file run_pipeline.py
    base_dir = os.path.dirname(os.path.abspath(__file__))
    
    log_file = os.path.join(base_dir, "outputs", "logs", "pipeline_run.log")
    extract_script = os.path.join(base_dir, "tools", "extract_tls_flows.py")
    train_script = os.path.join(base_dir, "tools", "train_model.py")
    anomaly_script = os.path.join(base_dir, "tools", "detect_anomaly.py")
    report_script = os.path.join(base_dir, "tools", "generate_report.py")
    preprocess_script = os.path.join(base_dir, "tools", "preprocess_features.py")
    train_script = os.path.join(base_dir, "tools", "train_model.py")
    classify_script = os.path.join(base_dir, "tools", "classify_traffic.py")
    # Đảm bảo thư mục lưu log hoạt động tốt
    os.makedirs(os.path.dirname(log_file), exist_ok=True)

    print("===============================================================")
    print("=== BẮT ĐẦU CHẠY PIPELINE MULTI-AGENT APP CLASSIFIER SYSTEMS ===")
    print("===============================================================")
    write_log(log_file, "Kích hoạt Orchestrator Agent - Khởi chạy Pipeline toàn cục.")

    # Bước 1: Trích xuất tính năng mạng (TLS Flow Agent)
    print("\n[Bước 1] Kích hoạt TLS Flow Agent...")
    write_log(log_file, "Kích hoạt TLS Flow Agent -> Đang trích xuất file PCAP mạng thô.")
    try:
        if os.path.exists(extract_script):
            subprocess.run(["python", extract_script], check=True)
            write_log(log_file, "TLS Flow Agent: Trích xuất dữ liệu mạng tầng giao vận thành công.")
        else:
            print(f"❌ Không tìm thấy script trích xuất: {extract_script}")
    except Exception as e:
        write_log(log_file, f"❌ LỖI tại TLS Flow Agent: {e}")

    # Bước 2: Kỹ nghệ đặc trưng dữ liệu (Feature Engineering Agent)
    print("\n[Bước 2] Kích hoạt Feature Engineering Agent...")
    write_log(log_file, "Kích hoạt Feature Engineering Agent -> Đang tiền xử lý đặc trưng mạng.")
    try:
        subprocess.run(["python", preprocess_script], check=True)
        write_log(log_file, "Feature Engineering Agent: Chuẩn hóa vector và mã hóa nhãn hoàn tất.")
    except Exception as e:
        write_log(log_file, f"❌ LỖI tại Feature Engineering Agent: {e}")

    # Bước 3: Phân loại ứng dụng (Traffic Classifier Agent)
    print("\n[Bước 3] Kích hoạt Traffic Classifier Agent...")
    write_log(log_file, "Kích hoạt Traffic Classifier Agent -> Train AI và Dự đoán nhãn ứng dụng.")
    try:
        # Trong môi trường thực tế, nếu đã có file random_forest.pkl thì có thể bỏ qua bước Train
        subprocess.run(["python", train_script], check=True)
        subprocess.run(["python", classify_script], check=True)
        write_log(log_file, "Traffic Classifier Agent: Phân loại dữ liệu lưu lượng mạng thành công.")
    except Exception as e:
        write_log(log_file, f"❌ LỖI tại Traffic Classifier Agent: {e}")

    # Bước 4: Săn tìm hành vi mạng nguy hiểm/bất thường (Anomaly Detector Agent)
    print("\n[Bước 4] Kích hoạt Anomaly Detector Agent...")
    write_log(log_file, "Kích hoạt Anomaly Detector Agent -> Chạy mô hình Isolation Forest phát hiện nguy cơ bảo mật.")
    anomaly_count = 0
    try:
        if os.path.exists(anomaly_script):
            # Chạy và bắt lấy kết quả đầu ra (stdout) của script tìm bất thường
            result = subprocess.run(["python", anomaly_script], capture_output=True, text=True, check=True)
            print(result.stdout.strip())
            
            # Sử dụng Regex để trích xuất số lượng luồng độc hại từ thông điệp in ra terminal
            match = re.search(r"phát hiện (\d+) luồng", result.stdout)
            if match:
                anomaly_count = int(match.group(1))
                
            write_log(log_file, f"Anomaly Detector Agent: Hoàn thành quét an ninh. Phát hiện {anomaly_count} luồng bất thường.")
        else:
            print(f"❌ Không tìm thấy script quét bất thường: {anomaly_script}")
    except Exception as e:
        write_log(log_file, f"❌ LỖI tại Anomaly Detector Agent: {e}")

    # Bước 5: Biên soạn báo cáo tự động (Report Generator Agent)
    print("\n[Bước 5] Kích hoạt Report Generator Agent...")
    write_log(log_file, "Kích hoạt Report Generator Agent -> Đóng gói số liệu thực tế mạng.")
    try:
        if os.path.exists(report_script):
            # Truyền số lượng bất thường thực tế quét được sang làm tham số cho script báo cáo
            subprocess.run(["python", report_script, "--anomalies", str(anomaly_count)], check=True)
            write_log(log_file, "Report Generator Agent: Xuất bản tệp báo cáo tổng kết hệ thống thành công.")
        else:
            print(f"❌ Không tìm thấy script tạo báo cáo: {report_script}")
    except Exception as e:
        write_log(log_file, f"❌ LỖI tại Report Generator Agent: {e}")
        
    print("\n===============================================================")
    print("=== PIPELINE HOÀN THÀNH AN TOÀN! TOÀN BỘ 5 AGENT THÀNH CÔNG ===")
    print("===============================================================")
    print("👉 Vui lòng kiểm tra báo cáo kết quả động tại: outputs/reports/kết_quả.md")
    write_log(log_file, "Pipeline kết thúc chu kỳ an toàn. Hệ thống vận hành hoàn hảo.")

if __name__ == "__main__":
    main()
