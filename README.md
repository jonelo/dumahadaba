# dumahadaba

Dump Malware Hash DataBase. The script downloads the SQLite database from https://github.com/CYB3RMX/MalwareHashDB/ and it dumps the content (MD5 hash values of malware and their descriptions)
to a GNU/Linux compatible text hash file so that it can be processed further by tools which are able to handle plain text hash value lists.

## Dump the data base

```
$ ./dumahadaba.py
The file called ./HashDB is already there, do you want to download the lastest version from https://github.com/CYB3RMX/MalwareHashDB/raw/main/HashDB? [y]:
Calculating hash of ./HashDB ...
Downloading the latest database from https://github.com/CYB3RMX/MalwareHashDB/raw/main/HashDB and saving it to ./HashDB ...
Calculating hash of ./HashDB ...
This is the same database that we have had previously.
The MalwareHashDB.dump.md5 is not there.
Generating the hash file MalwareHashDB.dump.md5, please wait ...
Warning: There is no description for hash value 6a55fe937cfe460e781c4c72f3ca0f61, I set the value to "<malware, but no description>".
Warning: There is no description for hash value 03e93302c256f81a631a4130707179ae, I set the value to "<malware, but no description>".
Warning: There is no description for hash value 17485ab26ea18e09a01242e521531727, I set the value to "<malware, but no description>".
Warning: There is no description for hash value 7b6917f8657669a2417dadf08412bcf9, I set the value to "<malware, but no description>".
Warning: There is no description for hash value f7248f64728236bf4dc2e106e3156ef8, I set the value to "<malware, but no description>".
Warning: There is no description for hash value 87da9e311d939223496558261559d877, I set the value to "<malware, but no description>".
Warning: There is no description for hash value 4223c8aae820d83ee656f82e1315f3a5, I set the value to "<malware, but no description>".
Warning: There is no description for hash value 5171ba9e93a9d70de4f49651d2d5914e, I set the value to "<malware, but no description>".
Warning: The string 0E84AFF18D42FC691CB1104018F44403C325AD21 does not represent a valid lowercase hex encoded MD5 hash value.
Warning: The string 379FF9236F0F72963920232F4A0782911A6BD7F7 does not represent a valid lowercase hex encoded MD5 hash value.
Warning: The string 87BD9404A68035F8D70804A5159A37D1EB0A3568 does not represent a valid lowercase hex encoded MD5 hash value.
Warning: The string B33DD3EE12F9E6C150C964EA21147BF6B7F7AFA9 does not represent a valid lowercase hex encoded MD5 hash value.
Warning: The string 912342F1C840A42F6B74132F8A7C4FFE7D40FB77 does not represent a valid lowercase hex encoded MD5 hash value.
Warning: The string 61B25D11392172E587D8DA3045812A66C3385451 does not represent a valid lowercase hex encoded MD5 hash value.
Warning: The string F32D791EC9E6385A91B45942C230F52AFF1626DF does not represent a valid lowercase hex encoded MD5 hash value.
Warning: There is no description for hash value ede5a8ecfb91343f9efc355b9a265829, I set the value to "<malware, but no description>".
Warning: There is no description for hash value 29b90e8a29f0e63922fab7c0234da1ce, I set the value to "<malware, but no description>".
Warning: There is no description for hash value 100113e1a6f4423bda1b65fe770e2f51, I set the value to "<malware, but no description>".
Warning: There is no description for hash value d4a8f3712d5f1c4d9e333ca519ff8419, I set the value to "<malware, but no description>".
Warning: There is no description for hash value 9d72f27e9778490ec43835dae69e9ee4, I set the value to "<malware, but no description>".
Warning: There is no description for hash value a2bbc72ffc43ccfe0a135ef6a811410b, I set the value to "<malware, but no description>".
Warning: There is no description for hash value 02e89ba67a5315f222be9090f4be3372, I set the value to "<malware, but no description>".
Warning: There is no description for hash value 817a3cf8eb47b860b8945906308f81a6, I set the value to "<malware, but no description>".
Warning: There is no description for hash value 8c3444f0ec99c9eca14c4c48937136e1, I set the value to "<malware, but no description>".

7 invalid records have been ignored.
17 records have been fixed.
336587 valid MD5 records have been written to MalwareHashDB.dump.md5.
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
