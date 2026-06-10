# Skill: Automated Reporting

**Mô tả:** Kỹ năng tổng hợp số liệu phân tích AI và tự động xuất bản báo cáo học thuật dưới định dạng văn bản Markdown.

**Công cụ liên kết (Tool Binding):**

- Ngôn ngữ: Python
- Đường dẫn file: `tools/generate_report.py`
- Tham số dòng lệnh: `--anomalies [số_lượng]`

**Đầu vào (Inputs):**

- File dữ liệu chứa nhãn dự đoán: `datasets/csv/extracted_features.csv`
- Số liệu luồng bất thường quét được từ Agent trước đó.

**Đầu ra (Outputs):**

- Tệp báo cáo hoàn chỉnh: `outputs/reports/kết_quả.md`
