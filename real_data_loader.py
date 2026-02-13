import pandas as pd
import numpy as np

# NSL-KDD Standard Column Names
COLUMNS = [
    'duration', 'protocol_type', 'service', 'flag', 'src_bytes', 'dst_bytes',
    'land', 'wrong_fragment', 'urgent', 'hot', 'num_failed_logins',
    'logged_in', 'num_compromised', 'root_shell', 'su_attempted',
    'num_root', 'num_file_creations', 'num_shells', 'num_access_files',
    'num_outbound_cmds', 'is_host_login', 'is_guest_login', 'count',
    'srv_count', 'serror_rate', 'srv_serror_rate', 'rerror_rate',
    'srv_rerror_rate', 'same_srv_rate', 'diff_srv_rate', 'srv_diff_host_rate',
    'dst_host_count', 'dst_host_srv_count', 'dst_host_same_srv_rate',
    'dst_host_diff_srv_rate', 'dst_host_same_src_port_rate',
    'dst_host_srv_diff_host_rate', 'dst_host_serror_rate',
    'dst_host_srv_serror_rate', 'dst_host_rerror_rate',
    'dst_host_srv_rerror_rate', 'label', 'difficulty_level'
]

def load_data(mode='real'):
    """
    Loads either a synthetic dataset for testing or the actual 
    NSL-KDD dataset from the local file system.
    """
    if mode == 'fake':
        print("[DEBUG] Mode: Loading Synthetic (Random) Data...")
        n_rows = 1000
        data = {col: np.random.randint(0, 100, n_rows) for col in COLUMNS}
        data['protocol_type'] = np.random.choice(['tcp', 'udp', 'icmp'], n_rows)
        data['label'] = np.random.choice(['normal', 'attack'], n_rows)
        return pd.DataFrame(data)
    
    else:
        print("[INFO] Mode: Loading Authentic NSL-KDD Dataset...")
        try:
            # Loading the dataset from CSV (TXT) file with predefined headers
            df = pd.read_csv("KDDTrain+.txt", names=COLUMNS, header=None)
            
            # Dropping 'difficulty_level' as it's not used for training the model
            df = df.drop('difficulty_level', axis=1)
            return df
            
        except FileNotFoundError:
            print("[CRITICAL ERROR] KDDTrain+.txt not found! Ensure download_data.py has been executed.")
            return None

if __name__ == "__main__":
    # Internal validation
    df = load_data('real')
    if df is not None:
        print(f"✅ Authentic Dataset Loaded. Shape: {df.shape}")