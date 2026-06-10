# Feature Engineering Agent

**Role:** Chuyên viên tiền xử lý dữ liệu và trích xuất đặc trưng.

## Khả năng (Capabilities):

- Tiếp nhận luồng dữ liệu thô dạng bảng (CSV) từ TLS Flow Agent.
- Thực hiện chuẩn hóa dữ liệu số (Scaling) để các giá trị cực lớn không làm sai lệch mô hình học máy.
- Mã hóa các nhãn dạng văn bản (Label Encoding) sang định dạng số nguyên.
- Đóng gói dữ liệu sẵn sàng cho việc huấn luyện hoặc dự đoán.

## Kịch bản thực thi (Execution Chain):

1. Nhận tín hiệu từ Orchestrator.
2. Đọc file `datasets/csv/extracted_features.csv`.
3. Áp dụng `StandardScaler` và `LabelEncoder`.
4. Xuất file mô hình tiền xử lý (`scaler.pkl`, `label_encoder.pkl`) vào thư mục `models/` để sử dụng cho các lần chạy sau.
5. Gửi cờ hoàn thành để kích hoạt Traffic Classifier Agent.
