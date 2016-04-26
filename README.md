# Bak
Ultra simple backup utility, v0.2
Copyright 2016, Aswin Babu Karuvally


## Introduction
Bak is an ultra simple backup tool. It is designed to archive your data as quickly as possible,
without hurting your workflow. Bak is devoid of complex features. If you are looking for a full
featured backup tool, look elsewhere.

## Requirements
The program is developed using python. All you need is a standard installation of Python 3,
for this application to run smoothly.

## Installing Bak
- Clone the github repository
- Symlink the 'bak.py' to somewhere convenient eg.'/usr/local/bin/bak'

## Running Bak
- Just type 'bak' in terminal and the present working directory will be backed up
- A message at the end of the backup process will tell you, if the process was successful
- By default, files will be backed up inside 'bak' directory in user's home

## Configuring Bak
- After the initial run, Bak will automatically create the configuration file
- 

## To-Do 
- better bak.conf file
- perform fail check  of the tarball
- allow tar and zip archiving
- better exception handling while reading config file
- check if the path given as runtime argument is valid

