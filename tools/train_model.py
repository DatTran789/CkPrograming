import pandas as pd
import joblib
import os
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.metrics import accuracy_score

def train_pipeline():
    csv_path = "datasets/csv/extracted_features.csv"
    if not os.path.exists(csv_path):
        print("Không tìm thấy file CSV dữ liệu. Hãy chạy extract_tls_flows.py trước!")
        return

    # 1. Đọc dữ liệu
    df = pd.read_csv(csv_path)
    
    # 2. Chia tách Features (X) và Labels (y)
    X = df[['packet_count', 'total_bytes', 'max_packet_size', 'min_packet_size']]
    y = df['label']
    
    # 3. Mã hóa nhãn chữ thành số
    encoder = LabelEncoder()
    y_encoded = encoder.fit_transform(y)
    
    # 4. Chuẩn hóa dữ liệu số (Scaling)
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)
    
    # 5. Chia tập Train/Test
    X_train, X_test, y_train, y_test = train_test_split(X_scaled, y_encoded, test_size=0.2, random_state=42)
    
    # 6. Huấn luyện mô hình Random Forest
    print("Đang huấn luyện mô hình Random Forest...")
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)
    
    # 7. Đánh giá nhanh
    preds = model.predict(X_test)
    acc = accuracy_score(y_test, preds)
    print(f"Độ chính xác của mô hình đạt: {acc * 100:.2f}%")
    
    # 8. Lưu các file model (.pkl)
    os.makedirs("models", exist_ok=True)
    joblib.dump(model, "models/random_forest.pkl")
    joblib.dump(scaler, "models/scaler.pkl")
    joblib.dump(encoder, "models/label_encoder.pkl")
    print("Đã lưu các mô hình thành công vào thư mục models/!")

if __name__ == "__main__":
    train_pipeline()