import joblib
import numpy as np
import pandas as pd

def run_inference():
    """
    Loads the pre-trained model and performs real-time traffic analysis
    based on manual user input.
    """
    # 1. Load the trained model
    model_path = 'sentinel_model.joblib'
    print(f"[INFO] Initializing system... Loading model from: {model_path}")
    
    try:
        model = joblib.load(model_path)
    except FileNotFoundError:
        print(f"[ERROR] Model file not found at {model_path}. Please train the model first.")
        return

    print("\n" + "="*40)
    print("      SENTINEL-ML: LIVE PREDICTION      ")
    print("="*40)
    print("Please enter network traffic features for real-time analysis:")
    
    # Simulating a single row of data (Simulated from network sensor input)
    try:
        duration = float(input(" -> Enter duration (0-100): "))
        src_bytes = float(input(" -> Enter source bytes (e.g., 500): "))
        count = float(input(" -> Enter connection count (e.g., 50): "))
        
        # NSL-KDD requires 41 features for the model input.
        # We initialize with zeros and map our manual inputs to specific indices.
        input_data = np.zeros(41) 
        input_data[0] = duration
        input_data[4] = src_bytes
        input_data[22] = count # 'count' feature is located at index 22
        
        # 2. Execute Prediction
        prediction = model.predict([input_data])
        
        # 3. Process and Display Result
        print("\n[ANALYSIS RESULTS]")
        print("-" * 20)
        if prediction[0] == 1:
            print("STATUS: ⚠️ ATTACK DETECTED")
            print("ACTION: Immediate mitigation recommended.")
        else:
            print("STATUS: ✅ NORMAL TRAFFIC")
            print("ACTION: Monitoring continues...")
        print("-" * 20)
        
    except ValueError:
        print("[ERROR] Invalid input. Please enter numeric values only.")
    except Exception as e:
        print(f"[CRITICAL ERROR] An unexpected error occurred: {e}")

if __name__ == "__main__":
    run_inference()