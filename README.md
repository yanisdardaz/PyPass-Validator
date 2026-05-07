# PyPass-Validator 🛡️

A Python-based security tool designed to evaluate password strength using **Shannon Entropy** calculations and character set analysis.

## 📋 Features
- **Entropy Calculation**: Measures the information density of the password in bits.
- **Charset Detection**: Identifies lowercase, uppercase, numbers, and special characters.
- **Security Assessment**: Provides a risk level based on standard cryptographic brute-force resistance thresholds.

## 🔬 How it works
The tool uses the formula:  
`Entropy = L * log2(R)`  
Where **L** is the password length and **R** is the size of the pool of characters used.

## 🛠️ Usage
1. Clone the repository:
   ```bash
   git clone https://github.com/yanisdardaz/PyPass-Validator.git
   ```
2. Enter the directory:
   ```bash
   cd PyPass-Validator
   ```
3. Run le scipt:
   ```bash
   python3 password_checker.py
   ```
