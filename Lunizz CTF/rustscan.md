.----. .-. .-. .----..---.  .----. .---.   .--.  .-. .-.
| {}  }| { } |{ {__ {_   _}{ {__  /  ___} / {} \ |  `| |
| .-. \| {_} |.-._} } | |  .-._} }\     }/  /\  \| |\  |
`-' `-'`-----'`----'  `-'  `----'  `---' `-'  `-'`-' `-'
The Modern Day Port Scanner.
________________________________________
: https://discord.gg/GFrQsGy           :
: https://github.com/RustScan/RustScan :
 --------------------------------------
Real hackers hack time ⌛

[~] The config file is expected to be at "/home/main2004/.rustscan.toml"
[!] File limit is lower than default batch size. Consider upping with --ulimit. May cause harm to sensitive servers
[!] Your file limit is very small, which negatively impacts RustScan's speed. Use the Docker image, or up the Ulimit with '--ulimit 5000'. 
Open 10.10.50.190:22
Open 10.10.50.190:80
Open 10.10.50.190:3306
Open 10.10.50.190:4444
Open 10.10.50.190:5000
[~] Starting Script(s)
[>] Script to be run Some("nmap -vvv -p {{port}} {{ip}}")

[~] Starting Nmap 7.80 ( https://nmap.org ) at 2021-02-25 03:25 PST
NSE: Loaded 151 scripts for scanning.
NSE: Script Pre-scanning.
NSE: Starting runlevel 1 (of 3) scan.
Initiating NSE at 03:25
Completed NSE at 03:25, 0.00s elapsed
NSE: Starting runlevel 2 (of 3) scan.
Initiating NSE at 03:25
Completed NSE at 03:25, 0.00s elapsed
NSE: Starting runlevel 3 (of 3) scan.
Initiating NSE at 03:25
Completed NSE at 03:25, 0.00s elapsed
Initiating Ping Scan at 03:25
Scanning 10.10.50.190 [2 ports]
Completed Ping Scan at 03:25, 0.32s elapsed (1 total hosts)
Initiating Parallel DNS resolution of 1 host. at 03:25
Completed Parallel DNS resolution of 1 host. at 03:25, 0.14s elapsed
DNS resolution of 1 IPs took 0.14s. Mode: Async [#: 1, OK: 0, NX: 1, DR: 0, SF: 0, TR: 1, CN: 0]
Initiating Connect Scan at 03:25
Scanning 10.10.50.190 [5 ports]
Discovered open port 22/tcp on 10.10.50.190
Discovered open port 3306/tcp on 10.10.50.190
Discovered open port 80/tcp on 10.10.50.190
Discovered open port 5000/tcp on 10.10.50.190
Discovered open port 4444/tcp on 10.10.50.190
Completed Connect Scan at 03:25, 0.50s elapsed (5 total ports)
Initiating Service scan at 03:25
Scanning 5 services on 10.10.50.190
Completed Service scan at 03:25, 6.59s elapsed (5 services on 1 host)
NSE: Script scanning 10.10.50.190.
NSE: Starting runlevel 1 (of 3) scan.
Initiating NSE at 03:25
Completed NSE at 03:25, 7.91s elapsed
NSE: Starting runlevel 2 (of 3) scan.
Initiating NSE at 03:25
Completed NSE at 03:25, 1.15s elapsed
NSE: Starting runlevel 3 (of 3) scan.
Initiating NSE at 03:25
Completed NSE at 03:25, 0.00s elapsed
Nmap scan report for 10.10.50.190
Host is up, received syn-ack (0.41s latency).
Scanned at 2021-02-25 03:25:17 PST for 17s

PORT     STATE SERVICE    REASON  VERSION
22/tcp   open  ssh        syn-ack OpenSSH 7.6p1 Ubuntu 4ubuntu0.3 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   2048 f8:08:db:be:ed:80:d1:ef:a4:b0:a9:e8:2d:e2:dc:ee (RSA)
| ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDQ6tpIF+vVAr4XW2jvHXaX311/qtXWgA/XJsPs4e1sAEDV9x9qQb6d6YTUECsJVg7r/HLuK4U3Bn5tco9Aa4cfij07qlbby08K8ByOrCFHeOJreYVqjsCBMdOo29GC83hOH8IzCo99pONcuviuPtRXion4PURNZPkdiMjhJv0ugruICXvqvNuXCtb7o4cF+OGNx7vGzllSrBJoNW6dA3+bhwE+ktZ14Ezbycb4CzbGoKXC+SKqt+82VrwpC4F9B3JPsSs6dkutSW1Zs0mtBYynv4dXzi3/dyY89jNedHOzwlIsOOTPfMhDQ9Qu6LpixmbpTTKnAlW+6gVAo21pwWlZ
|   256 79:01:d6:df:8b:0a:6e:ad:b7:d8:59:9a:94:0a:09:7a (ECDSA)
| ecdsa-sha2-nistp256 AAAAE2VjZHNhLXNoYTItbmlzdHAyNTYAAAAIbmlzdHAyNTYAAABBBBTbAWLeWIuaAVyErImxGlw4qYC6DkIkhWx6m84sgWaNBG5dhXu96NpywKz3Qr/lq2y53WN0RufLUlmQGhJ2QMA=
|   256 b1:a9:ef:bb:7e:5b:01:cd:4c:8e:6b:bf:56:5d:a7:f4 (ED25519)
|_ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAILRqrXXIaHRlVe9pndYgXYOQLkggzjJoC6ZToAWWHeUH
80/tcp   open  http       syn-ack Apache httpd 2.4.29 ((Ubuntu))
| http-methods: 
|_  Supported Methods: GET HEAD POST OPTIONS
|_http-server-header: Apache/2.4.29 (Ubuntu)
|_http-title: Apache2 Ubuntu Default Page: It works
3306/tcp open  mysql      syn-ack MySQL 5.7.32-0ubuntu0.18.04.1
| mysql-info: 
|   Protocol: 10
|   Version: 5.7.32-0ubuntu0.18.04.1
|   Thread ID: 7
|   Capabilities flags: 65535
|   Some Capabilities: Support41Auth, LongPassword, Speaks41ProtocolOld, SupportsLoadDataLocal, ODBCClient, SupportsTransactions, SupportsCompression, FoundRows, LongColumnFlag, DontAllowDatabaseTableColumn, SwitchToSSLAfterHandshake, IgnoreSigpipes, ConnectWithDatabase, IgnoreSpaceBeforeParenthesis, InteractiveClient, Speaks41ProtocolNew, SupportsAuthPlugins, SupportsMultipleResults, SupportsMultipleStatments
|   Status: Autocommit
|   Salt: 0,u\x02
| a{D;\x7FovTIAO*a\x1D+
|_  Auth Plugin Name: mysql_native_password
4444/tcp open  tcpwrapped syn-ack
5000/tcp open  tcpwrapped syn-ack
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

NSE: Script Post-scanning.
NSE: Starting runlevel 1 (of 3) scan.
Initiating NSE at 03:25
Completed NSE at 03:25, 0.00s elapsed
NSE: Starting runlevel 2 (of 3) scan.
Initiating NSE at 03:25
Completed NSE at 03:25, 0.00s elapsed
NSE: Starting runlevel 3 (of 3) scan.
Initiating NSE at 03:25
Completed NSE at 03:25, 0.00s elapsed
Read data files from: /usr/bin/../share/nmap
Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 17.93 seconds
