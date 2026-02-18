import hashlib
import os
import platform
import time

def clear():
    #had to make it work on windows and big Linux
    if platform.system() == "Windows":
        os.system('cls')
    else:
        os.system('clear')

def crack_hash(the_hash):
    print("Cracking...")
    the_hash = the_hash.lower()
    start = time.time()
    current_hash = ""
    with open("rockyou.txt", errors="ignore") as passlist:
        for line in passlist:
            line = line.strip()
            #md5 hashes are 32 chars long, sha256 hashes are 64 chars long
            if len(the_hash) == 32:
                current_hash = hashlib.md5(line.encode('utf-8')).hexdigest()
            elif len(the_hash) == 64:
                current_hash = hashlib.sha256(line.encode('utf-8')).hexdigest()
            if current_hash == the_hash:
                clear()
                end = time.time()
                print(f"Done! Took {round(end - start)} seconds")
                return line
    return "Not found!"
    
def get_hashes():
    inputs = True
    hash1 = input("Input a hash (enter blank to exit): ")
    while inputs:
        if hash1 == "":
            inputs = False
            break
        print(crack_hash(hash1))
        hash1 = input("Input a hash (enter blank to exit): ")

def main():
    clear()
    print("This program uses the rockyou wordlist to decrypt MD5 and SHA-256 hashes.")
    get_hashes()
    print("Goodbye.")

if __name__ == "__main__":
    main()
