#!/usr/bin/env python3
#
# Downloads the SQLite database from https://github.com/CYB3RMX/MalwareHashDB/
# and dumps the content (MD5 hash values of malware and their descriptions)
# to a GNU/Linux compatible text hash file which has the following format:
#
# Values are separated by two blanks, first value contains the hash value,
# encoded in hex, lowercase; the second value contains a description,
# description may contain spaces. Example:
#
# f4c3fa43b5bdfaa0205990d25ce51c5a  Trojan.Win32.Emotet.471040.A
#
# You could use Jacksum to find malware on your disk(s):
#
# > jacksum -a md5 --wanted-list MalwareHashDB.dump.md5 --style linux .
#
# see also: <https://jacksum.net>
# author: Johann N. Löfflmann <https://johann.loefflmann.net>
#


import requests
import sqlite3
import re
import os.path
import hashlib


# init constants
DATABASE_REMOTE = 'https://github.com/CYB3RMX/MalwareHashDB/raw/main/HashDB'
DATABASE_LOCAL = "./HashDB"
MALWARE_HASHES_FILENAME = "MalwareHashDB.dump.md5"
NO_DESCRIPTION = "<malware, but no description>"


# functions
def yesno(prompt):
    answer = None
    while answer not in ("y", "n"): 
        answer = input(prompt) 
        if answer == "y" or answer == "":
            answer = "y"
            return True            
            # Do this.
        elif answer == "n": 
            return False
            # Do that.
        else:
            print("Please enter y or n.") 


# returns a sha256 hash value from a file
def hashfile(filename):
    with open(DATABASE_LOCAL,"rb") as f:
        bytes = f.read() # read entire file as bytes
        readable_hash = hashlib.sha256(bytes).hexdigest();
        return readable_hash


# returns singular or plural text fragment, depentend on the number
def singular_or_plural(number):
    if (number == 1):
        return " has"
    else:
        return "s have"


# download or not to download?
database_local_exists = os.path.exists(DATABASE_LOCAL)
if database_local_exists:
    download_wanted = yesno(f"The file called {DATABASE_LOCAL} is already there, do you want to download the lastest version from {DATABASE_REMOTE}? [y]: ")
    if download_wanted:
        print(f"Calculating hash of {DATABASE_LOCAL} ...")
        hash1 = hashfile(DATABASE_LOCAL)
else:
    download_wanted = yesno(f"The file called {DATABASE_LOCAL} is not there, do you want to download the lastest version from {DATABASE_REMOTE}? [y]: ")

if download_wanted: 
    # Download the MalwareHashDB
    print (f"Downloading the latest database from {DATABASE_REMOTE} and saving it to {DATABASE_LOCAL} ...")
    response = requests.get(DATABASE_REMOTE, allow_redirects=True)
    with open(DATABASE_LOCAL, 'wb') as f:
        f.write(response.content)

    if database_local_exists:
        print(f"Calculating hash of {DATABASE_LOCAL} ...")
        hash2 = hashfile(DATABASE_LOCAL)

        # give the user a hint whether it is required to generate the .md5 file
        if (hash1 == hash2):
            print ("This is the same database that we have had previously.")
        else:
            print ("This is a new version of the database!")
else:
    print ("Ok.")

if os.path.exists(MALWARE_HASHES_FILENAME):
    print (f"The {MALWARE_HASHES_FILENAME} is already there.")
    if not yesno (f"Do you want to regenerate the hash file? [y]: "):    
        print ("Ok.")
        exit()
else:
    print (f"The {MALWARE_HASHES_FILENAME} is not there.")

print (f"Generating the hash file {MALWARE_HASHES_FILENAME}, please wait ...")

# init variables
hash_values = {}
successful_records = 0
fixed_records = 0
invalid_records = 0

# read the entire SQlite database
connection = sqlite3.connect(DATABASE_LOCAL)
cursor = connection.cursor()
cursor.execute("SELECT * FROM HashDB")
records = cursor.fetchall()

for record in records:
    # header related
    if record[0] == "hash": # it is the header of the table
        continue

    # hash value related
    hash_value = record[0].strip()
    if hash_value == "": # there is no hash value
        print (f"Warning: The hash value string is empty.")
        invalid_records +=1
        continue
    if not re.search(r'[a-z0-9]{32}', hash_value): # not a MD5 hash value            
        print (f"Warning: The string {hash_value} does not represent a valid lowercase hex encoded MD5 hash value.")
        invalid_records +=1
        continue

    # description related
    description = record[1].strip()
    if description == "": # there is no description
        description = NO_DESCRIPTION
        fixed_records += 1
        print (f"Warning: There is no description for hash value {hash_value}, I set the value to \"{NO_DESCRIPTION}\".")
    # removal of the line feeds, new lines, and resolve of any tabs in the description
    description = description.replace('\n','').replace('\r','').replace('\t',' ')

    # add or update record
    hash_values[hash_value] = description


# write the hash_value dict to a file
with open(MALWARE_HASHES_FILENAME, "w", newline='\n') as malware_hashes:
    for hash_value, description in hash_values.items():
        successful_records += 1;
        print(f"{hash_value}  {description}", file=malware_hashes)

# print some statistics
print()
print(f"{invalid_records} invalid record{singular_or_plural(invalid_records)} been ignored.")
print(f"{fixed_records} record{singular_or_plural(fixed_records)} been fixed.")
print(f"{successful_records} valid MD5 record{singular_or_plural(successful_records)} been written to {MALWARE_HASHES_FILENAME}.")

