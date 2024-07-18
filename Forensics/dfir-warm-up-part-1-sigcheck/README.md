# DFIR warm-up part 1 (sigcheck)

## Description

**From ASD :**  

>  "ASD has become aware of malicious activity on your network occurring between: `2024-04-01` and `2024-04-20`
>
>  ASD expects tradecraft that includes:
>  1. File based malware with a valid digital signature.
>  1. Persistence via an autostart mechanism. 

**From the client:** 

>  As requested we have run a sigcheck and attached the output, we have taken a look and don't recognise many of the files in the listing. 

**ACTION:** As the DFIR analyst, your task is to determine:

1. The 'productversion' or 'fileversion' of the malicious binary from sigcheck. Flag example: `ASDCTF{1.3.3.7}`

## Files

* [sigcheck.txt](files/sigcheck.txt)

I looked at the files that were signed at the 2024 since that was when the issue occured.

I thought i would need to narrow it to down days but only one file was signed in 2024 therefore svhost.exe was the malicious file.

flag = ASDCTF{1.4.19.6}

