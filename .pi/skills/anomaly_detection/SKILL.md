# Skill: Anomaly Detection

**Mô tả:** Cung cấp năng lực săn tìm các mối đe dọa tiềm ẩn và luồng truy cập bất thường (ví dụ: DDoS, kết nối Malware C&C) bằng thuật toán học máy không giám sát (Isolation Forest).

**Công cụ liên kết (Tool Binding):**

- Ngôn ngữ: Python
- Đường dẫn file: `tools/detect_anomaly.py`
- Hàm thực thi: `detect_anomalies()`

**Đầu vào (Inputs):**

- Dữ liệu mạng đã trích xuất: `datasets/csv/extracted_features.csv`

**Đầu ra (Outputs):**

- Số lượng luồng dữ liệu bất thường (Integer).
- Bản ghi log cảnh báo bảo mật hệ thống.
