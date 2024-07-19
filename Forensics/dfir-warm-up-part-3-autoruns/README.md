# DFIR warm-up part 3 (autoruns)

## Description

**From ASD :**  

> "ASD has become aware of malicious activity on your network occurring between: `2024-04-01` and `2024-04-20`
>
> ASD expects tradecraft that includes:
> 1. File-based malware with an invalid digital signature.
> 1. Persistence via an autostart mechanism. 

**From the client:** 

> As requested we have collected autoruns, please find the output attached. 

**ACTION:** As the DFIR analyst, your task is to determine:

1. The first argument to the command that launches the malware process. Flag example:  `ASDCTF{C:\Users\Bob\malware.dat}`

## Files

* [autoruns.txt](files/autoruns.txt)

Method:

I need to find the first argument to the command that launches the malware process however the file is very large. What method do i need to use to parse it?

I asked google to figure out the methods to parse the large file.

I figured out that this can be easily imported into an excel file and i made sure to split it via delimiter for the | symbol.

This made it much easier to read.

I then added in header details.

One that that interesting was the date-time. Since i need to filter only for a specific time frame. This should reduce the amount of entries to look at.

It greatly reduced it to a few entries and one sticks out alot

I have found a file that looks interesting as the amount of files to check seem rather low after filtering for only the right date

C:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe -NonI -W hidden -enc //5TAHQAYQByAHQALQBQAHIAbwBjAGUAcwBzACAALQBXAG8AcgBrAGkAbgBnAEQAaQByAGUAYwB0AG8AcgB5ACAAIgBDADoAXABXAGkAbgBkAG8AdwBzAFwAVABlAG0AcAAiACAAIgBDADoAXABVAHMAZQByAHMAXABQAHUAYgBsAGkAYwBcAHMAdgBjAGgAbwBzAHQALgBlAHgAZQAiAA== 

it has the following arugement in it which seems to decode to: Start-Process -WorkingDirectory "C:\Windows\Temp" "C:\Users\Public\svchost.exe"

The first argument to the command that launches the malware process. Flag example: ASDCTF{C:\Users\Bob\malware.dat}

Thats what the flag needs to look like... trying to figure that out now


I got it!! ASDCTF{C:\Windows\Temp} was the flag