# Topic 08 — Encrypted Traffic App Classifier

Hệ thống phân loại ứng dụng và phát hiện hành vi bất thường từ lưu lượng mạng mã hóa (TLS) sử dụng kiến trúc Multi-Agent (.pi framework) kết hợp Machine Learning (Random Forest).

---

## 🎯 1. Giới thiệu bài toán
Trong thời đại an ninh mạng hiện nay, hầu hết các lưu lượng mạng đều được mã hóa bằng giao thức TLS/HTTPS. Điều này bảo vệ quyền riêng tư của người dùng nhưng lại gây khó khăn cho việc quản lý mạng và phát hiện mã độc vì không thể đọc được nội dung bên trong gói tin (Deep Packet Inspection - DPI bị vô hiệu hóa).

Dự án này giải quyết thách thức trên bằng cách sử dụng **Học máy (Machine Learning)** để phân tích các đặc trưng hành vi (kích thước, tần suất, dung lượng gói tin) kết hợp với kiến trúc **Multi-Agent** để tự động hóa toàn bộ quy trình từ thu thập, tiền xử lý dữ liệu cho đến đưa ra cảnh báo bảo mật.

---

## 📂 2. Cấu trúc cây thư mục hệ thống
Cấu trúc dự án tuân thủ nghiêm ngặt framework thiết kế Agent độc lập và Pipeline xử lý dữ liệu chuẩn chỉ:

```text
project/
├── .pi/
│   ├── agents/             # Định nghĩa vai trò, nhiệm vụ của từng AI Agent
│   ├── skills/             # Kỹ thuật chuyên môn và các script liên kết của Agent
│   ├── prompts/            # Cấu hình System Prompt điều khiển hành vi Agent
│   └── chains/             # Sơ đồ phối hợp và điều phối luồng chạy (chain.md)
├── tools/                  # Mã nguồn Python xử lý cốt lõi (Trích xuất, Train AI,...)
├── datasets/               # Dữ liệu mạng đầu vào (PCAP) và dữ liệu trích xuất (CSV)
├── models/                 # Các file mô hình AI sau khi huấn luyện (.pkl)
├── outputs/                # Thành phẩm đầu ra bao gồm Nhật ký (Logs) và Báo cáo (Reports)
├── requirements.txt        # Danh sách các thư viện cần cài đặt
└── run_pipeline.py         # File khởi chạy tổng thể hệ thống
