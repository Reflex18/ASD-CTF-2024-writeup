# DFIR nix malchal part 1

## Description

 **From ASD :**  

"ASD has become aware that from at least 27 May 2024, your network has been communicating with a known Sliver C2 orb `192.168.77[.]210`

ASD recommends you review your systems and logs for signs of malicious activity.

ASD advises that you DO NOT probe this IP ADDRESS."

**From the client:** 

"Since being contacted by ASD, we have identified the affected host, and run the Velociraptor offline collector as you requested.

We cannot find the malware though. This server is critical and we cannot take it offline."

 **ACTION:** 

1. As the DFIR analyst, your task is to determine the probable malware location on disk, and its persistence mechanism, to inform remediation of the intrusion.

Finding persistence will find a flag. Submit a flag in the format `ASDCTF{}`

 **Guidance**

1. Extract the data using `7za x <filename>` or download Velociraptor, run Velociraptor in standalone mode by passing it the `gui` parameter, and import the collection using `Server.Utils.ImportCollection`
2. The Velociraptor offline collector is configured to collect the following artifacts:

```yaml
Artifacts:
 Linux.Collection.SysLogs:
 Linux.Detection.AnomalousFiles:
 Linux.Mounts:
 Linux.Network.NetstatEnriched:
 Linux.Proc.Modules:
 Linux.Ssh.AuthorizedKeys:
 Linux.Ssh.KnownHosts:
 Linux.Sys.BashHistory:
 Linux.Sys.Crontab:
 Linux.Sys.Groups:
 Linux.Sys.LastUserLogin:
 Linux.Sys.Pslist:
 Linux.Sys.Services:
 Linux.Sys.Users:
 Linux.Sysinternals.Sysmon:
 Linux.Syslog.SSHLogin:
 Linux.Users.InteractiveUsers:
 Linux.Users.RootUsers:
```

## Files

* [part1_vr_collection.zip](files/part1_vr_collection.zip)

