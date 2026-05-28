rules = {
    "Hardcoded Password": r"password\s*=\s*[\"'].*[\"']",
    "SQL Injection": r"SELECT .*\\+",
    "Dangerous eval()": r"eval\(",
    "Weak Exception Handling": r"except:\s*pass"
}
