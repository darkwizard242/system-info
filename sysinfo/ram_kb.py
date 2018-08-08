#! /usr/bin/env python3

import psutil
import variables_data


# Assign variable to store total memory value.
mem = psutil.virtual_memory()
mem_total = float(mem.total/variables_data.kilobyte)

# Assign variable with the value of currently available memory.
mem_free = float(mem.free/variables_data.kilobyte)

# Assign variable with the value of currently used memory.
mem_used = float(mem.used/variables_data.kilobyte)

# Set Threshold
threshold = variables_data.kilobyte * 700  # 7000MB


# Defining function ram_specs that uses modules/functions from psutil library and from variables_data.
def ram_specs():
    # Set flow based on Threshold value.
        print()
        print('Total memory is: ' + str(float(mem_total)) + ' KBs')
        print('Current available memory is: ' + str(float(mem_free)) + ' KBs')
        print('Current used memory is: ' + str(float(mem_used)) + ' KBs')
        print('Percentage of RAM being utilized currently: ' + str(float(mem.percent)) + '%')