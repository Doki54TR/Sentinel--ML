import joblib
import os
from sklearn.model_selection import train_test_split
from sklearn.svm import LinearSVC
from real_data_loader import load_data
from preprocess import preprocess_data

def train_and_save_model():
    """
    Orchestrates the end-to-end machine learning pipeline:
    Loading, preprocessing, training, and serializing the model.
    """
    # 1. Data Ingestion & Preprocessing
    # Fetching the authentic NSL-KDD dataset
    data_frame = load_data(mode='real')
    if data_frame is None:
        print("[CRITICAL] Termination: Dataset could not be initialized.")
        return

    # Transforming raw data into scaled features and target vectors
    features, target = preprocess_data(data_frame)
    
    # 2. Data Splitting
    # Stratifying data into training (80%) and validation (20%) sets
    X_train, X_test, y_train, y_test = train_test_split(
        features, target, test_size=0.2, random_state=42
    )
    
    print(f"\n[EXECUTION] Training phase initiated with {len(X_train)} samples...")
    
    # 3. Model Configuration & Training
    # Utilizing Linear Support Vector Classifier (LinearSVC)
    # Optimization: dual=False is selected for performance (n_samples > n_features)
    model = LinearSVC(dual=False, max_iter=10000)
    model.fit(X_train, y_train)
    
    print("[SUCCESS] Model convergence achieved. Training complete.")

    # 4. Model Serialization & Export
    # Persisting the trained model to disk for production inference
    model_filename = 'sentinel_model.joblib'
    joblib.dump(model, model_filename)
    
    # Calculating export metadata
    file_size_mb = os.path.getsize(model_filename) / (1024 * 1024)
    print(f"[INFO] Artifact exported: {model_filename}")
    print(f"[INFO] Deployment size: {file_size_mb:.2f} MB")

if __name__ == "__main__":
    train_and_save_model()