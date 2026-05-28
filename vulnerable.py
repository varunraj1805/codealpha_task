# sample_code/vulnerable.py

# 1. Hardcoded Password Test
db_password = "super_secret_password123"

# 2. SQL Injection Test
query = "SELECT * FROM users WHERE username = " + user_input

# 3. Dangerous eval Test
user_calculation = eval(input("Enter math expression: "))

# 4. Weak Exception Handling Test
try:
    result = 10 / 0
except:
    pass