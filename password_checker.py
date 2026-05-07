import math
import re
import sys

def calculate_entropy(password):
    """Calculates the Shannon entropy of a password."""
    character_set = 0
    if re.search(r'[a-z]', password): character_set += 26
    if re.search(r'[A-Z]', password): character_set += 26
    if re.search(r'[0-9]', password): character_set += 10
    if re.search(r'[^a-zA-Z0-9]', password): character_set += 32
    
    if character_set == 0: return 0
    
    entropy = len(password) * math.log2(character_set)
    return round(entropy, 2)

def main():
    print("--- CyberPass Validator v1.0 ---")
    password = input("Enter password to test: ")
    
    if not password:
        print("Error: Password cannot be empty.")
        sys.exit(1)
        
    entropy = calculate_entropy(password)
    
    print(f"\n[+] Analysis for: {password}")
    print(f"[+] Entropy: {entropy} bits")
    
    if entropy < 40:
        print("[-] Result: VERY WEAK - Easy to brute-force.")
    elif entropy < 60:
        print("[!] Result: MEDIUM - Could be cracked with a GPU cluster.")
    elif entropy < 80:
        print("[+] Result: STRONG - Secure against common attacks.")
    else:
        print("[*] Result: EXCELLENT - High resistance.")

if __name__ == "__main__":
    main()
