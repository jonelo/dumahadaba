# dumahadaba

Dump Malware Hash DataBase. The script downloads the SQLite database from https://github.com/CYB3RMX/MalwareHashDB/ and it dumps the content (MD5 hash values of malware and their descriptions)
to a GNU/Linux compatible text hash file so that it can be processed further by tools which are able to handle plain text hash value lists. The script also detects records in HashDB that have a hash value but no description (those will be fixed in the dump), and records that do not represent valid MD5 hash values (those will be ignored in the dump).

## Dump the data base

```
$ ./dumahadaba.py
The file called ./HashDB is already there, do you want to download the lastest version from https://github.com/CYB3RMX/MalwareHashDB/raw/main/HashDB? [y]:
Calculating hash of ./HashDB ...
Downloading the latest database from https://github.com/CYB3RMX/MalwareHashDB/raw/main/HashDB and saving it to ./HashDB ...
Calculating hash of ./HashDB ...
This is a new version of the database!
The MalwareHashDB.dump.md5 is not there.
Generating the hash file MalwareHashDB.dump.md5, please wait ...
Warning: There is no description for hash value c26d10bb3f1f2471829499da20f35c64, I set the value to "<malware, but no description>".

0 invalid records have been ignored.
1 records have been fixed.
354976 valid MD5 records have been written to MalwareHashDB.dump.md5.
```

## Use the dump

You can use the text based data base dump to find malware on your devices by using tools like [Jacksum](https://github.com/jonelo/Jacksum) which is able to identify files by hash value lists.

```
$ jacksum -a md5 --wanted-list MalwareHashDB.dump.md5 --style linux .
Jacksum: Info: Option --compat/-style has been set, setting implicitly -a md5 -E hex -F "#ESCAPETAG#CHECKSUM{hex} *#FILENAME", stdin-name=-

Jacksum: total lines in check file: 336587
Jacksum: improperly formatted lines in check file: 0
Jacksum: properly formatted lines in check file: 336587
Jacksum: ignored lines (empty lines and comments): 0
Jacksum: correctness of check file: 100.00 %

Jacksum: total number of wanted hashes: 336587
Jacksum: files matching wanted hashes (MATCH): 0
Jacksum: files not matching wanted hashes (NO MATCH): 5

Jacksum: total files read successfully: 5
Jacksum: total bytes read: 60637434
Jacksum: total bytes read (human readable): 57 MiB, 848 KiB, 250 bytes
Jacksum: total file read errors: 0

Jacksum: elapsed time: 7 s, 153 ms
```
