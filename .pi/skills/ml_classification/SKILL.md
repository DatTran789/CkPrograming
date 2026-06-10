# Skill: Machine Learning Classification

**Mô tả:** Cung cấp khả năng chạy thuật toán học máy Random Forest để phân loại đặc trưng của các luồng TLS/HTTPS đã mã hóa.

**Công cụ liên kết (Tool Binding):**

- Ngôn ngữ: Python
- Đường dẫn: `tools/classify_traffic.py` và `tools/train_model.py`
- Hàm chính: `classify_pipeline()`

**Đầu vào (Inputs):**

- Tập dữ liệu: `datasets/csv/processed_features.csv`
- Mô hình: `models/random_forest.pkl`

**Đầu ra (Outputs):**

- Mảng các nhãn dự đoán (Predicted Labels).
- Số liệu đánh giá độ chính xác (Accuracy metric).
