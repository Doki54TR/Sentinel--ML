import pandas as pd
import numpy as np

def load_nsl_kdd():
    """
    Simulates loading the NSL-KDD dataset by generating synthetic data 
    for development purposes.
    """
    print("🛡️ Sentinel-ML: Generating synthetic dataset...")
    
    # NSL-KDD column structure
    columns = [
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
        'dst_host_srv_rerror_rate', 'label'
    ]

    # Generate 1000 rows of sample data
    n_rows = 1000
    data = {col: np.random.randint(0, 100, n_rows) for col in columns}
    
    # Correct categorical data for realism
    data['protocol_type'] = np.random.choice(['tcp', 'udp', 'icmp'], n_rows)
    data['service'] = np.random.choice(['http', 'smtp', 'private', 'ftp_data'], n_rows)
    data['flag'] = np.random.choice(['SF', 'S0', 'REJ', 'RSTR'], n_rows)
    data['label'] = np.random.choice(['normal', 'neptune', 'satan', 'ipsweep'], n_rows)

    df = pd.DataFrame(data)
    print(f"✅ Dataset generated successfully! Shape: {df.shape}")
    return df

if __name__ == "__main__":
    df = load_nsl_kdd()
    
    if df is not None:
        print("\n--- Synthetic Sample: First 5 Rows ---")
        print(df[['protocol_type', 'service', 'flag', 'src_bytes', 'label']].head())
        
        print("\n--- Protocol Distribution ---")
        print(df['protocol_type'].value_counts())