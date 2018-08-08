#! /usr/bin/env python3

from psutil import process_iter


# Defining process_info function to list all the process, names and usernames with the help of psutil library.
def processes_info():
    for process in process_iter(attrs=['name', 'pid', 'username']):
        print(process.info)
