# DFIR corrupt file system

## Description

**From ASD :**  

"ASD has received reporting from an unnamed department that a trusted insider is suspected of removing sensitive departmental information via a USB.

The Department has provided an image of the device, however it appears to be corrupted."

**From the client:** 

"We attempted to investigate the USB to determine whether it contained any sensitive information, however when we attempt to mount the drive on a Linux system we received the error:"

```sh
mount: /media/usb: wrong fs type, bad option, bad superblock on 
/dev/loop15, missing codepage or helper program, or other error.
```

**ACTION:** 

As the DFIR analyst, your task is to determine if there was any senstive information on the device, and recover that information.

Submit your discovery in the form `ASDCTF{FLAG}`

**Guidance:**

MD5 of `challenge.img.zip`: e899ba02de334c9ce6276f0c34dd3b41

The flag is a composite case-sensitive flag derived from:

1. part 1 read from the flag file content
2. part 2 is the filepath with directory separators removed. e.g.  `/<mount_point>/A/B/C/D/flag.file` becomes `ABCD`

- [FAT32 filesystem](https://en.wikipedia.org/wiki/Design_of_the_FAT_file_system)

## Files

* [challenge.img.zip](files/challenge.img.zip)

