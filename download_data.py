import urllib.request
import os

def download_nsl_kdd():
    url = "https://raw.githubusercontent.com/HoaNP/NSL-KDD-DataSet/master/KDDTrain%2B.txt"
    filename = "KDDTrain+.txt"
    
    if not os.path.exists(filename):
        print(f"📥 {filename} is being downloaded. Please wait...")
        urllib.request.urlretrieve(url, filename)
        print("✅ Download completed!")
    else:
        print("✔️ File already exists.")
if __name__ == "__main__":
    download_nsl_kdd()