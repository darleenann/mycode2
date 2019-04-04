#!/usr/bin/env pyghon3
## moving files with sftp

## import paramkiko so we can talk ssh
import paramiko
import os

## where to connect to
t = paramiko.Transport("10.10.2.3", 22) ## ip and port

## how to connect (see other labs on using id_rsa private / public keypairs) 
t.connect(username="bender", password="alta3")

## Make an sftp connection object
sftp = paramiko.SFTPClient.from_transport (t)

## iterate across the files within directory

for x in os.listdir("/home/student/filestocopy"):  # iterate on directory contents
    if not os.path.isdir("/home/student/filestocopy/"+x):  # filter everything that is NOT a dictionary 
        sftp.put("/home/student/filestocopy/"+x, "/tmp/"+x)  # move file to tartet loction

## close the connection
sftp.close() # close the connection 
