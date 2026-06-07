write_log(log_file, "Kích hoạt TLS Flow Agent -> Trích xuất file PCAP.")
    try:
        # Chạy script trích xuất dữ liệu
        if os.path.exists("tools/extract_tls_flows.py"):
            subprocess.run(["python", "tools/extract_tls_flows.py"], check=True)
            write_log(log_file, "TLS Flow Agent hoàn thành trích xuất dữ liệu mạng thành công.")
    except Exception as e:
        write_log(log_file, f"LỖI tại TLS Flow Agent: {e}")