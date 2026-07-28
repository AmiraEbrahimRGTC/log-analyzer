import sys
from collections import defaultdict

def analyze_log(file_path):
    failed_attempts = defaultdict(int)
    
    try:
        with open(file_path, 'r') as file:
            for line in file:
                # Adjust this condition based on your log file format
                if "Failed login" in line or "failed password" in line.lower():
                    # Example: extract username or IP address from the line
                    parts = line.split()
                    user = None
                    for part in parts:
                        if "user=" in part.lower():
                            user = part.split('=')[1]
                            break
                    if user:
                        failed_attempts[user] += 1

        print("\nSuspicious Failed Login Attempts:")
        for user, count in failed_attempts.items():
            if count > 3:  # Threshold for suspicious activity
                print(f"User/Entity '{user}' had {count} failed login attempts!")

    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python log_analyzer.py /path/to/logfile")
    else:
        analyze_log(sys.argv[1])
