write_log(log_file, "Kích hoạt Traffic Classifier Agent -> Dự đoán nhãn ứng dụng.")
    try:
        if os.path.exists("tools/train_model.py"):
            subprocess.run(["python", "tools/train_model.py"], check=True)
            write_log(log_file, "Traffic Classifier Agent phân loại dữ liệu thành công dựa trên Random Forest.")
    except Exception as e:
        write_log(log_file, f"LỖI tại Traffic Classifier Agent: {e}")