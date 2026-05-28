import re
import os
from rules import rules

def scan_file(file_path, report_path):
    # Ensure the input file actually exists before trying to open it
    if not os.path.exists(file_path):
        print(f"[Error] Target file '{file_path}' not found.")
        print("Please create 'sample_code/vulnerable.py' with test data.")
        return

    # Ensure output directory exists
    os.makedirs(os.path.dirname(report_path), exist_ok=True)

    try:
        with open(file_path, "r", encoding="utf-8") as file:
            code = file.readlines()
    except Exception as e:
        print(f"[Error] Could not read file: {e}")
        return

    print("\n--- Security Scan Report ---\n")
    
    # Using 'with' context manager automatically closes the file safely
    with open(report_path, "w", encoding="utf-8") as report:
        report.write("--- Security Scan Report ---\n\n")

        for line_no, line in enumerate(code, start=1):
            for issue, pattern in rules.items():
                if re.search(pattern, line):
                    finding = f"[!] {issue} found at line {line_no}\n"
                    code_line = f"    Code: {line.strip()}\n\n"

                    print(finding.strip())
                    print(code_line.strip() + "\n")

                    report.write(finding)
                    report.write(code_line)

    print(f"Report saved to: {report_path}")

if __name__ == "__main__":
    TARGET_FILE = "sample_code/vulnerable.py"
    OUTPUT_REPORT = "reports/security_report.txt"
    
    scan_file(TARGET_FILE, OUTPUT_REPORT)