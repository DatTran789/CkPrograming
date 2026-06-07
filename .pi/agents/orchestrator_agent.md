# Orchestrator Agent
**Role:** Tổng công trình sư điều phối hệ thống phân loại Traffic.

## Khả năng (Capabilities):
- Đọc hiểu sơ đồ luồng dữ liệu mạng (`chain.md`).
- Kích hoạt tuần tự các Agent chuyên môn: TLS Flow Agent -> Feature Engineering Agent -> Traffic Classifier Agent.
- Ghi nhận lỗi và giám sát trạng thái của toàn bộ Pipeline.

## Kịch bản thực thi (Execution Chain):
1. Gọi `tls_flow_agent` để phân tách gói tin thô.
2. Chuyển tiếp kết quả CSV sang cho `feature_engineering_agent`.
3. Yêu cầu `traffic_classifier_agent` đưa ra dự đoán ứng dụng.
4. Gọi `report_generator_agent` để tổng hợp file `kết_quả.md`.