import pandas as pd
import joblib
import os
from sklearn.preprocessing import LabelEncoder, StandardScaler

def preprocess_pipeline():
    csv_path = "datasets/csv/extracted_features.csv"
    processed_csv_path = "datasets/csv/processed_features.csv"
    
    if not os.path.exists(csv_path):
        print("❌ Không tìm thấy file dữ liệu gốc!")
        return

    print("Đang đọc dữ liệu thô...")
    df = pd.read_csv(csv_path)
    
    # Chia tách Features và Labels
    X = df[['packet_count', 'total_bytes', 'max_packet_size', 'min_packet_size']]
    y = df['label']
    
    # Mã hóa nhãn chữ thành số
    encoder = LabelEncoder()
    y_encoded = encoder.fit_transform(y)
    
    # Chuẩn hóa dữ liệu số (Scaling)
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)
    
    # Lưu các file model tiền xử lý (.pkl)
    os.makedirs("models", exist_ok=True)
    joblib.dump(scaler, "models/scaler.pkl")
    joblib.dump(encoder, "models/label_encoder.pkl")
    
    # Lưu dữ liệu đã xử lý ra một file CSV mới để Train/Classify dùng chung
    df_processed = pd.DataFrame(X_scaled, columns=X.columns)
    df_processed['label_encoded'] = y_encoded
    df_processed['label_original'] = y
    df_processed.to_csv(processed_csv_path, index=False)
    
    print(f"✅ Đã tiền xử lý xong! Dữ liệu mới lưu tại: {processed_csv_path}")

if __name__ == "__main__":
    preprocess_pipeline()
