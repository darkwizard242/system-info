#! /usr/bin/env python3

import platform
import sys


# Defining system_details function.
# Use of platform and sys libraries to obtain and print system, os and architecture info.
def system_details():
    os_type = platform.system()
    print('OS Type: ' + os_type)
    os_name = platform.release()
    print('OS Release version: ' + os_name)
    processor_name = platform.processor()
    print('Processor Name: ' + processor_name)
    network_name = platform.node()
    print('Machine Name on Network is: ' + network_name)
    machine_type = platform.machine()
    print('Machine Type is: ' + machine_type)
    system_platform = sys.platform
    print('System platform type is: ' + system_platform)
