import pandas as pd
import joblib
import os
from sklearn.ensemble import RandomForestClassifier

def train_pipeline():
    processed_csv_path = "datasets/csv/processed_features.csv"
    
    if not os.path.exists(processed_csv_path):
        print("❌ Chưa có dữ liệu tiền xử lý. Hãy chạy preprocess_features.py trước!")
        return

    print("Đang tải dữ liệu để huấn luyện...")
    df = pd.read_csv(processed_csv_path)
    
    X_train = df[['packet_count', 'total_bytes', 'max_packet_size', 'min_packet_size']]
    y_train = df['label_encoded']
    
    print("Đang huấn luyện mô hình Random Forest...")
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)
    
    # Lưu mô hình đã học xong
    os.makedirs("models", exist_ok=True)
    joblib.dump(model, "models/random_forest.pkl")
    
    print("✅ Đã huấn luyện và lưu mô hình thành công vào models/random_forest.pkl")

if __name__ == "__main__":
    train_pipeline()
