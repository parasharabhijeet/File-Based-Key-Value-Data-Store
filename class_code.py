import time
import json
import os
import sys

# Debug variable
debug = 0


class DataStore:
    def __init__(self):
        f = 'my_json.json'
        try:
            os.rename(f,f)
        except OSError:
            print("[-] File already in use")
            sys.exit(0)

        with open('my_json.json') as json_file: 
            self.d = json.load(json_file) 
        if debug:
            print(self.d) 

    def create(self, key, value, timeout=0):
        if key in self.d:
            print("[!] Error: this key already exists\n")  # error message1
        else:
            if key.isalpha():
                if len(self.d) < (1024 * 1020 * 1024) and len(str(value)) <= (
                    16 * 1024 * 1024
                ):  # constraints for file size less than 1GB and Jasonobject value less than 16KB
                    if timeout == 0:
                        l = [value, timeout]
                    else:
                        l = [value, time.time() + timeout]
                    if (
                        len(key) <= 32
                    ):  # constraints for input key_name capped at 32chars
                        self.d[key] = l
                        with open("my_json.json","w") as file:
                            json.dump(self.d, file)
                        print("[+] Key Successfully Added")
                else:
                    print("[!]Error: Memory limit exceeded!!")  # error message2
            else:
                print(
                    "[-] Error: Invalid key_name!! key_name must contain only alphabets and no special characters or numbers"
                )  # error message3

    def read(self, key):
        if key not in self.d:
            print(
                "[-] Error: given key does not exist in database. Please enter a valid key"
            )  # error message4
        else:
            b = self.d[key]
            if b[1] != 0:
                if time.time() < b[1]:  # comparing the present time with expiry time
                    stri = (
                        str(key) + ":" + str(b[0])
                    )  # to return the value in the format of JasonObject i.e.,"key_name:value"
                    return stri
                else:
                    print(
                        "[-] Error: time-to-live of", key, "has expired"
                    )  # error message5
            else:
                stri = str(key) + " : " + str(b[0])
                print(stri)

    def delete(self, key):
        if key not in self.d:
            print(
                "[-] Error: given key does not exist in database. Please enter a valid key"
            )  # error message4
        else:
            b = self.d[key]
            if b[1] != 0:
                if time.time() < b[1]:  # comparing the current time with expiry time
                    del self.d[key]
                    print("[+] Key is successfully deleted")
                else:
                    print(
                        "[-] Error: time-to-live of", key, "has expired"
                    )  # error message5
            else:
                del self.d[key]
                with open("my_json.json","w") as file:
                    json.dump(self.d, file)
                print("[+] Key is successfully deleted")

    
