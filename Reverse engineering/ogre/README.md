# Ogre

## Description

A friend has found a suspicous-looking file on their computer which they think could be malware. They have asked you to analyse it to see what it actually does.

Use your reverse engineering skills to find the flag.

**IMPORTANT NOTES**
* This file is not real malware, but employs code obfuscation techniques and, if executed, will attempt operations that can look malicious. These operations include starting new processes, and running file operations on a file it creates in the working directory from which it was run (it will not touch any system or user files outside this directory). This new file is named "stage3". **Any file in the working directory already named "stage3" could be overwritten**.
* Place this file in an empty folder on its own if you intend execute it. If executing the file, do so from the same folder in which the file was placed to avoid affecting local files anywhere else on the machine. As an extra precaution, use a virtual machine to conduct your analysis - this avoids any files on your real system from being affected.

**Some guidance**
1) What language begins a program with "use warnings;"?
2) How much of the code is actually necessary? Do variables get used normally? What lines look different?
3) Follow a similar decoding process for layer 2.
4) Use a Linux VM if you want to do dynamic analysis (i.e. if you want to execute the file).

## Files

* [ogre](files/ogre)

