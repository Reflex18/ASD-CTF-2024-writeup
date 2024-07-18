# DFIR warm-up part 2 (pslist)

## Description

**From ASD :**  

> "ASD has become aware of malicious activity on your network occurring between: `2024-04-01` and `2024-04-20`
>
> ASD expects tradecraft that includes:
> 1. File-based malware with an invalid digital signature.
> 1. Persistence via an autostart mechanism. 

**From the client:** 

> As requested we have taken a process listing, please find the pslist attached. 

**ACTION:** As the DFIR analyst, your task is to determine:

1. The pid of the malicious process from the pslist, wrapped in the usual ASDCTF{} wrapper.

## Files

* [pslist.txt](files/pslist.txt)

7676 is incorrect

Assumed this because of the weridness in the file output.

4 more attempts remain.

Some info i found about it from the following blog:
https://www.varonis.com/blog/how-to-use-volatility

Below are the keys headers from ‘pslist’ that you will need to understand when you begin using the tool:

- **PID** -  Process ID number
- **PPID** - Parent process ID number
- **ImageFileName** -  Name of the running process
- **Offset** -  Hexadecimal value representing the location in memory the process is running
- **CreateTime** - Time process started
- **ExitTime** - Time process ended

Using this function I like to just take a look at the process names and see if there is anything that jumps out at me. If there is anything that catches your attention then simply google the name, you should be able to quickly understand if it is something that looks legitimate or requires further attention.

