#! /usr/bin/env python3

import psutil
import variables_data


# Assign variable to store total memory value.
mem = psutil.virtual_memory()
mem_total = float(mem.total/variables_data.gigabyte)

# Assign variable with the value of currently available memory.
mem_free = float(mem.free/variables_data.gigabyte)

# Assign variable with the value of currently used memory.
mem_used = float(mem.used/variables_data.gigabyte)


# Defining function ram_specs that uses modules/functions from psutil library and from variables_data.
def ram_specs():
        print()
        print('Total memory is: ' + str(float(mem_total)) + ' GBs')
        print('Current available memory is: ' + str(float(mem_free)) + ' GBs')
        print('Current used memory is: ' + str(float(mem_used)) + ' GBs')
        print('Percentage of RAM being utilized currently: ' + str(float(mem.percent)) + '%')
