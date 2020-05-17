#! /usr/bin/python

# Modules

import sys
import os
from crontab import CronTab

if __name__ == '__main__':
    # Parsing command line arguments

    user = sys.argv[1]
    folder_path = sys.argv[2]

    # Ensures that when the cronjob is set it has the path to filehander.py
    # script

    filehandler_path = os.path.join(os.getcwd(), 'filehandler.py')

    # Creating cron job

    cron = CronTab(user=user)
    job = cron.new(command=f'python {filehandler_path} {folder_path}')
    job.minute.every(1)

    cron.write()
