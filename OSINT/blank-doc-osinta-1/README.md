# Blank Doc - OSINT(a) 1

## Description

Pssssst…. You there. I need you to help me locate an image and find out where it is online. We’ll need the full URL of where the image is located. My boss said something about needing to scan that url later. But here’s the thing – all they gave me was this empty word document! I’m stuck. You can help me right?
Flag is of the format ASDCTF{url}, where url is a string that doesn't include https:// at the start.
Note: This flag is case-sensitive.

## Files

* [A_CTF_document.docx](files/A_CTF_document.docx)

So far i have used exfiltools to find a hash for the picture.

b62e294585d6ae804b10083fd70f13f0cd358b61452ffac6eefd1be74fa6bbcc

Since it is 64 characters long it is a sha256 hash.

I believe if i can search for the image with the hash i can find the url.

Im not sure if it is a hash...

https://www.whatsmyip.org/hash-lookup/

I tried the following site to find it but was not able to.


Tineye might help. It did not...

Google images did not sadly



