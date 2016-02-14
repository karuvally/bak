#!/usr/bin/env python3
#bak, an ultra simple backup utility, v0.1
#copyright 2016, Aswin Babu Karuvally
#released under GNU General Public License

##fix
#better bak.conf file
#specify the source directory through argument (-s)
#specify the exclusive target directory through arugment (-t)
#specify inclusive target directory, ie. also backup to directories in config (-T)
#allow passing custom path for bak.conf (-c)
#check the tarball
#allow tar and zip archiving
#allow specifying archive name (-n)
#better exception handling while reading config file

#import some serious stuff
import os
import shutil
from datetime import datetime

#create the backup archive
def create_backup_archive (target_directory_list):
    date_string = '[' + datetime.now().strftime ('%d-%m-%y') + ']'
    time_string = '[' + datetime.now().strftime ('%H:%M:%S') + ']'
    current_directory_path = os.getcwd()
    current_directory_name = '[' + os.path.basename (current_directory_path) + ']'
    archive_name = current_directory_name + date_string + time_string

    try:
        shutil.make_archive (archive_name, 'tar', current_directory_path)
        for target_directory in target_directory_list:
            shutil.copy (archive_name + '.tar', target_directory)
        
        os.remove (archive_name + '.tar')
        print ('files have been archived :)')

    except:
        print ('archive creation failed :(')


#check if target directories exist
def check_target_directories (target_directory_list):
    for target_directory in target_directory_list:
        try:
            if os.path.isdir (target_directory) == False:
                raise Exception()
        except:
            print ('cannot access ' + target_directory)
            exit()

#read config from bak
def read_config (config_file_path):
    target_directory_list = []

    try:
        config_file = open (config_file_path, 'r')
        for line in config_file:
            if (line[0] != '#'):
                target_directory_list.append (line.rstrip())
    except:
        print ('cannot read ' + config_file_path)
        exit()

    return target_directory_list

#the main function
def main():
    user_name = os.getlogin()
    config_file_path = '/home/' + user_name + '/.config/bak.conf'

    target_directory_list = read_config (config_file_path)
    check_target_directories (target_directory_list)
    create_backup_archive (target_directory_list)

main()

