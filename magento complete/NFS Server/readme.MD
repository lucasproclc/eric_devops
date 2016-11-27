# What is NFS Server?
Network File System (NFS) is a distributed file system protocol originally developed by Sun Microsystems in 1984, 
allowing a user on a client computer to access files over a network much like local storage is accessed. 
NFS, like many other protocols, builds on the Open Network Computing Remote Procedure Call (ONC RPC) system. 
The Network File System is an open standard defined in RFCs, allowing anyone to implement the protocol.

# Description
This box installs, configures and starts NFS Server to serve the files of an specified data folder to an specified export.

***

# Deployment Variables
|  Variable                  | Description                                                      | Value                 |
|----------------------------|------------------------------------------------------------------|-----------------------|
|   **EXPORT_HOST** | Export Host variable that defines with what remote hosts can be shared the file system ||
|   **EXPORT_DIRECTORY** | Data Folder which files are served using NFS protocol |/data/export||

***

# Deployment behavior
An instance executing this box will use bash scripting to install and configure NFS Server.

# Supported Distributions
The box supports deploying to these linux distributions:

* Amazon Linux AMI 2015.03
* Centos 6.5, 7
* RedHat 7

***
