import joblib
import os

def load_ai_models(model_dir="models"):
    """Tiện ích nạp tất cả các mô hình AI đã huấn luyện."""
    rf_path = os.path.join(model_dir, "random_forest.pkl")
    scaler_path = os.path.join(model_dir, "scaler.pkl")
    encoder_path = os.path.join(model_dir, "label_encoder.pkl")
    
    models = {}
    
    if os.path.exists(rf_path):
        models['classifier'] = joblib.load(rf_path)
        print("✅ Nạp thành công mô hình Random Forest Classifier.")
    
    if os.path.exists(scaler_path):
        models['scaler'] = joblib.load(scaler_path)
        print("✅ Nạp thành công mô hình chuẩn hóa StandardScaler.")
        
    if os.path.exists(encoder_path):
        models['encoder'] = joblib.load(encoder_path)
        print("✅ Nạp thành công mô hình mã hóa LabelEncoder.")
        
    return models

if __name__ == "__main__":
    print("Đang kiểm tra tiến trình tải mô hình từ ổ cứng...")
    loaded_models = load_ai_models()
    if not loaded_models:
        print("⚠️ Chưa có mô hình nào được huấn luyện và lưu trữ.")
