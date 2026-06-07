# Pipeline Execution Chain

```mermaid
graph TD
    A[Bắt đầu Pipeline] --> B(TLS Flow Agent: Trích xuất PCAP)
    B --> C(Feature Engineering Agent: Xử lý số liệu)
    C --> D(Traffic Classifier Agent: Chạy AI dự đoán)
    D --> E(Anomaly Detector Agent: Phát hiện bất thường)
    E --> F(Report Generator Agent: Xuất kết quả.md)