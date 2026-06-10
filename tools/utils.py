import os
import datetime

def write_log(message, log_file="outputs/logs/pipeline_run.log"):
    """Tiện ích ghi log hệ thống dùng chung cho toàn bộ dự án."""
    os.makedirs(os.path.dirname(log_file), exist_ok=True)
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(log_file, "a", encoding="utf-8") as f:
        f.write(f"[{timestamp}] {message}\n")

def check_file_exists(filepath):
    """Tiện ích kiểm tra sự tồn tại của file để tránh lỗi crash chương trình."""
    if not os.path.exists(filepath):
        print(f"❌ CẢNH BÁO: Không tìm thấy tệp {filepath}")
        return False
    return True
