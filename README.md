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
```

---

## 🧠 3. Triết lý Thiết kế Hệ thống (Agent-Native Philosophy)
Dự án được thiết kế và vận hành nghiêm ngặt dựa trên tư duy Agent-Native hiện đại nhằm tối ưu hóa hiệu suất theo chỉ thị chuyên môn của Giảng viên hướng dẫn:

Hạn chế cài đặt Package thủ công: Không lạm dụng việc cài đặt môi trường rườm rà hay các thư viện nặng nề. Hệ thống tận dụng khả năng của Pi Agent để tự động nhận diện và thiết lập công cụ linh hoạt khi vận hành.

Tự động xây dựng mã nguồn (Auto-Build): Lập trình viên không cần viết code cứng (Hardcoded) cho các file trong thư mục tools/. Pi Agent sẽ đọc hiểu các bản thiết kế tư duy (SKILL.md và PROMPT.md) bằng ngôn ngữ tự nhiên, từ đó tự động sinh ra mã nguồn Python tương ứng và thực thi ngầm.

Tối ưu hóa Token & Tốc độ phản hồi: Hệ thống được chia nhỏ thành 5 Agent độc lập phối hợp tuần tự thông qua chain.md. Khi chạy đến bước nào, Pi chỉ nạp đúng file cấu hình của Agent đó thay vì ôm đồm toàn bộ dự án vào Context Window, giúp tiết kiệm tối đa token API OpenAI và tăng tốc độ xử lý lên gấp nhiều lần.

## 🚀 4. Hướng dẫn Khởi chạy hệ thống qua Pi Agent
Để kích hoạt thực thi Pipeline tự động thông qua tài khoản OpenAI của nhóm, hãy thực hiện tuần tự các bước sau trong môi trường Terminal (VS Code):

Bước 1: Mở khóa quyền chạy Script trên Windows (Nếu dùng PowerShell)
Mở tab Terminal tại thư mục dự án và chạy lệnh sau để nới lỏng chính sách bảo mật của Windows:
```text
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
```

Bước 2: Nạp API Key OpenAI vào két sắt bảo mật của Pi
Tiến hành đăng nhập và lưu vĩnh viễn khóa API trả phí của nhóm vào framework bằng cú pháp:
```text
npx pi /login openai sk-proj-MÃ_API_KEY_OPENAI_CỦA_NHÓM
```

Bước 3: Gửi "Lệnh" kích hoạt Orchestrator
Sao chép toàn bộ mệnh lệnh dưới đây, dán vào Terminal để ép Pi Agent sử dụng mô hình gpt-4o đọc hiểu kiến trúc và tự động triển khai toàn bộ đồ án:
```text
npx pi --provider openai --model gpt-4o "Hãy đóng vai trò là Orchestrator hệ thống. Hãy đọc file .pi/chains/chain.md để nắm bắt kiến trúc. Dựa vào sơ đồ đó, hãy tuần tự đóng vai các Agent, đọc các file cấu hình trong .pi/prompts/ và .pi/skills/ tương ứng, sau đó tự động triển khai hoặc thực thi code trong thư mục tools/ để hoàn thành đường ống phân loại lưu lượng mạng. Nếu có lỗi phát sinh, hãy tự động debug và đi tiếp cho đến khi tạo ra file báo cáo kết_quả.md"
```

## 📊 5. Nghiệm thu sản phẩm đầu ra
Sau khi Pipeline hoàn thành chu kỳ thực thi, nhóm có thể kiểm tra các thành phẩm thu được tại:

tools/: Chứa toàn bộ các file code Python cốt lõi do AI tự tạo lập và tối ưu.

outputs/reports/kết_quả.md: File báo cáo động bằng tiếng Việt (chuẩn mã hóa UTF-8) tổng hợp trực quan biểu đồ lưu lượng mạng, nhãn ứng dụng phân loại và danh sách các dòng chảy mạng nghi vấn độc hại do thuật toán phát hiện.

## 👥 6. Thành viên thực hiện
Đồ án được nghiên cứu và phát triển bởi nhóm sinh viên lớp Lập trình mạng - HCMUTE:

Nguyễn Thái Hưng

Trần Ngọc Đạt
