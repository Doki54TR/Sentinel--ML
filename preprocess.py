import pandas as pd
from sklearn.preprocessing import LabelEncoder, StandardScaler

def preprocess_data(df):
    """
    Performs data cleaning, encoding, and scaling to prepare the 
    dataset for the Machine Learning model.
    """
    print("\n🛠️ Sentinel-ML: Starting data preprocessing...")
    
    # 1. Binary Label Transformation (Normal vs. Attack)
    # Mapping 'normal' to 0 and any other type of activity to 'attack' (1)
    df['binary_label'] = df['label'].apply(lambda x: 0 if x == 'normal' else 1)
    
    # 2. Categorical Encoding (Label Encoding)
    # Converting string categories into numerical values
    le = LabelEncoder()
    categorical_cols = ['protocol_type', 'service', 'flag']
    
    for col in categorical_cols:
        df[col] = le.fit_transform(df[col])
        print(f"✅ Feature encoded: {col}")

    # 3. Feature (X) and Target (y) Selection
    # Dropping label columns to isolate features from the target variable
    X = df.drop(['label', 'binary_label'], axis=1)
    y = df['binary_label']

    # 4. Feature Scaling
    # Standardizing features is critical for algorithms like SVC or Logistic Regression
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)
    
    print("🚀 Data preprocessing completed successfully!")
    return X_scaled, y

if __name__ == "__main__":
    # Internal test block
    from data_loader import load_nsl_kdd
    
    df = load_nsl_kdd()
    X, y = preprocess_data(df)
    
    print(f"\nProcessed Feature Matrix (X) Shape: {X.shape}")
    print(f"Target Variable (y) Distribution:\n{y.value_counts()}")