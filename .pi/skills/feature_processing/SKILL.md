# Skill: Feature Processing

**Mô tả:** Cung cấp khả năng tiền xử lý, làm sạch và chuẩn hóa dữ liệu thô (Scaling & Encoding) để hệ thống sẵn sàng đưa vào các mô hình học máy.

**Công cụ liên kết (Tool Binding):**

- Ngôn ngữ: Python
- Đường dẫn file: `tools/preprocess_features.py`
- Hàm thực thi: `preprocess_pipeline()`

**Đầu vào (Inputs):**

- Dữ liệu thô: `datasets/csv/extracted_features.csv`

**Đầu ra (Outputs):**

- Dữ liệu đã chuẩn hóa: `datasets/csv/processed_features.csv`
- Các tệp cấu hình toán học: `models/scaler.pkl`, `models/label_encoder.pkl`
