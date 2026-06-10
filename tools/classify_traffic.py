import pandas as pd
import joblib
import os
from sklearn.metrics import accuracy_score

def classify_pipeline():
    processed_csv_path = "datasets/csv/processed_features.csv"
    model_path = "models/random_forest.pkl"
    
    if not os.path.exists(processed_csv_path) or not os.path.exists(model_path):
        print("❌ Thiếu dữ liệu hoặc mô hình. Hãy đảm bảo đã chạy preprocess và train!")
        return

    print("Đang nạp mô hình AI vào bộ nhớ...")
    df = pd.read_csv(processed_csv_path)
    
    X_test = df[['packet_count', 'total_bytes', 'max_packet_size', 'min_packet_size']]
    y_true = df['label_encoded']
    
    # Load model Random Forest
    model = joblib.load(model_path)
    encoder = joblib.load("models/label_encoder.pkl")
    
    print("Đang phân loại lưu lượng...")
    preds = model.predict(X_test)
    
    # Đánh giá độ chính xác (Trong thực tế có thể xuất log các nhãn dự đoán)
    acc = accuracy_score(y_true, preds)
    print(f"✅ Quá trình phân loại hoàn tất! Độ chính xác của AI đạt: {acc * 100:.2f}%")

if __name__ == "__main__":
    classify_pipeline()
