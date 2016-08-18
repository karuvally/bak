#!/usr/bin/env python3
# bak, an ultra simple backup utility, v0.3
# Released under GNU General Public License
# Copyright 2016, Aswin Babu Karuvally

# import some serious stuff
import os
from os.path import getsize, join
import argparse
import shutil
from datetime import datetime


# find directory size
def find_directory_size(source_directory_path):
    total_size = 0
    for root, sub_directories, files in os.walk(source_directory_path):
        for file in files:
            total_size += getsize(join(root, file))
    
    if total_size < 1024:
        return_string = str(total_size) + ' bytes'

    elif total_size > 1024 and total_size < 1024 * 1024:
        total_size = int(total_size / 1024)
        return_string = str(total_size) + ' kilos'

    elif total_size > 1024*1024 and total_size < 1024 * 1024 * 1024:
        total_size = int(total_size / (1024 * 1024))
        return_string = str(total_size) + ' megs'

    else:
        total_size = int(total_size / (1024 * 1024 * 1024))
        return_string = str(total_size) + ' gigs'

    return return_string


# create the backup archive
def create_backup_archive(target_directory_list, source_directory_path):
    date_string = '[' + datetime.now().strftime('%d-%m-%y') + ']'
    time_string = '[' + datetime.now().strftime('%H:%M:%S') + ']'
    source_directory_name = '[' + os.path.basename(source_directory_path) + ']'
    archive_name = source_directory_name + date_string + time_string

    try:
        shutil.make_archive(archive_name, 'tar', source_directory_path)
        for target_directory in target_directory_list:
            shutil.copy(archive_name + '.tar', target_directory)
        os.remove(archive_name + '.tar')

        source_directory_size = find_directory_size(source_directory_path)
        print(source_directory_size, 'of files have been archived :)')

    except:
        print('archive creation failed :(')


# check target directories, create if non existent
def check_target_directories(target_directory_list):
    for target_directory in target_directory_list:
        if not os.path.isdir(target_directory):
            try:
                os.mkdir(target_directory)
                print('created', target_directory)
            except:
                print('creation of', target_directory, 'failed :(')
                exit()


# read configuration from bak
def read_configuration_file(configuration_file_path):
    target_directory_list = []

    try:
        configuration_file = open(configuration_file_path, 'r')
        for line in configuration_file:
            if line[0] != '#':
                target_directory_list.append(line.rstrip())
    except:
        print('cannot read ' + configuration_file_path)
        exit()

    return target_directory_list


# check configuration file, create if non existent
def check_configuration_file(configuration_file_path, user_name):
    if not os.path.isfile(configuration_file_path):
        configuration_file = open(configuration_file_path, 'w')
        configuration_file.write('/home/' + user_name + '/bak')
        configuration_file.close()


# the main function
def main():
    target_directory_list = []
    parser = argparse.ArgumentParser(description=
        'bak, an ultra simple backup utility, v0.3')
    parser.add_argument('-s', '--source', help='Choose the source directory')
    arguments = parser.parse_args()

    user_name = os.getlogin()
    configuration_file_path = '/home/' + user_name + '/.config/bak.conf'
    check_configuration_file(configuration_file_path, user_name)
    target_directory_list = read_configuration_file(configuration_file_path)
    check_target_directories(target_directory_list)

    if arguments.source:
        source_directory_path = arguments.source
    else:
        source_directory_path = os.getcwd()
    create_backup_archive(target_directory_list, source_directory_path)

main()
