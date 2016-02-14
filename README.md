# Bak
Ultra simple backup tool

## Introduction
Bak is an ultra simple backup tool. It is designed to archive your data as quickly as possible,
without hurting your workflow. Bak is devoid of complex features. If you are looking for a full
featured backup tool, look elsewhere.

## Requirements
The program is developed using python. You need the following packages for the program to run
smoothly. OS, Shutil and DateTime are part of the standard Python installation.
- Python 3 (a recent version would help)
- OS
- Shutil
- DateTime

## Installing Bak
- Clone the github repository
- Symlink the 'bak.py' to somewhere convinient eg.'/usr/local/bin/bak'

## Running Bak
- edit the 'bak.conf' to configure where backups should be made
- copy it to '~/.config/bak.conf'
- run 'bak' from terminal, a tarball of the present directory will be made

## To-Do 
- better bak.conf file
- specify the source directory through argument (-s)
- specify the exclusive target directory through arugment (-t)
- specify inclusive target directory, ie. also backup to directories in config (-T)
- allow passing custom path for bak.conf (-c)
- check the tarball
- allow tar and zip archiving
- allow specifying archive name (-n)
- better exception handling while reading config file

