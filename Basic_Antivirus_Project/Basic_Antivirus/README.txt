Basic Antivirus Simulation (Signature-Based Scanner)

Project Description:
This project is a Python-based Basic Antivirus Simulation that detects malicious files 
using signature-based detection. It scans files in a specified directory, generates 
their SHA-256 hashes, and compares them against a known malware signature database.

If a match is found, the file is flagged as malicious and moved to a quarantine folder.

--------------------------------------------------

Objective:
To understand how signature-based antivirus systems work and to implement
a basic malware detection mechanism using hashing techniques.

--------------------------------------------------

Features:
- Scans files in a selected folder
- Generates SHA-256 hash for each file
- Compares file hash with known malware signatures
- Moves detected malicious files to a quarantine folder
- Simple and educational implementation

--------------------------------------------------

Tools & Technologies Used:
- Python 3
- hashlib library
- os module
- shutil module
- Linux (Ubuntu environment)

--------------------------------------------------

Project Structure:

Basic_Antivirus/
│
├── scanner.py
├── malware_signatures.txt
├── scan_folder/
├── quarantine/
└── README.txt

--------------------------------------------------

How to Run:

1. Place files to be scanned inside the "scan_folder".
2. Ensure malware signatures are listed in "malware_signatures.txt".
3. Run the following command:

   python3 scanner.py

4. Detected malicious files will be moved to the "quarantine" folder.

--------------------------------------------------

Disclaimer:
This project is developed strictly for educational and ethical purposes.
It does not detect real-world malware unless valid signatures are added.
No real systems were harmed during testing.

--------------------------------------------------

Learning Outcome:
- Understanding of signature-based detection
- Practical implementation of file hashing
- Basic security automation concept
- Safe malware simulation using controlled environment
