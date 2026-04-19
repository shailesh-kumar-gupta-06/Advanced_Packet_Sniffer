import os
import hashlib
import shutil

SCAN_DIR = "scan_folder"
QUARANTINE_DIR = "quarantine"
SIGNATURE_FILE = "malware_signatures.txt"

def load_signatures():
    with open(SIGNATURE_FILE, "r") as f:
        return set(line.strip() for line in f)

def file_hash(filepath):
    sha256 = hashlib.sha256()
    with open(filepath, "rb") as f:
        for block in iter(lambda: f.read(4096), b""):
            sha256.update(block)
    return sha256.hexdigest()

def scan_files():
    signatures = load_signatures()
    if not os.path.exists(QUARANTINE_DIR):
        os.mkdir(QUARANTINE_DIR)

    for file in os.listdir(SCAN_DIR):
        path = os.path.join(SCAN_DIR, file)
        if os.path.isfile(path):
            hash_value = file_hash(path)
            print(f"Scanning {file}...")

            if hash_value in signatures:
                print(f"[ALERT] Malware detected: {file}")
                shutil.move(path, os.path.join(QUARANTINE_DIR, file))
            else:
                print(f"[SAFE] {file}")

scan_files()
