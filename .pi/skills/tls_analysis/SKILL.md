# Skill: TLS Flow Analysis

**Mô tả:** Khả năng đọc hiểu và bóc tách các tệp tin lưu lượng mạng (PCAP) thông qua thư viện Scapy để tìm ra các mẫu hành vi đặc trưng của giao thức mã hóa TLS/HTTPS.

**Công cụ liên kết (Tool Binding):**

- Ngôn ngữ: Python
- Đường dẫn file: `tools/extract_tls_flows.py`
- Hàm thực thi: Module cấp cao nhất (chạy trực tiếp CLI)

**Đầu vào (Inputs):**

- Thư mục chứa các tệp mạng: `datasets/pcap/*.pcap`

**Đầu ra (Outputs):**

- Dữ liệu bảng chứa vector đặc trưng: `datasets/csv/extracted_features.csv`
