# DFIR nix malchal part 2

## Description

**From the client:** 

"We have remediated. But we think there is still access to the host, because we are seeing activity from this host logging in to systems it shouldnt.

We cannot find how they are still on this server. This server is critical and we cannot take it offline, so we have blocked traffic to the IP from before, and we cannot see the malicious process running any more that you found last time."

**ACTION:** 

1. As the DFIR analyst, your task is to determine how the actor has sustained access.

The flag will be in the new persistence mechanism. Submit a flag in the format `ASDCTF{}`

**Guidance**
1. Extract the data using `7za x <filename>` or download velociraptor, run Velociraptor in standalone mode by passing it the `gui` parameter, and import the collection using `Server.Utils.ImportCollection`
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

* [p2_vr_collection.zip](files/p2_vr_collection.zip)

