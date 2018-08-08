#! /usr/bin/env python3

import ram_kb
import ram_mb
import ram_gb
import sys_sw_hw_info
import variables_data
import pid_info


# Assigning a variable for the purpose of specifying which data measurement function is to be used.
data_measure = variables_data.megabyte

# Printing system, os, architecture level information using the function system_details in sys_sw_hw_info module.
print('\nSystem & OS level details below:\n')
sys_sw_hw_info.system_details()
print()

# Printing IP address using the ip_addr function within the ip_address module.
# ip_address.ip_addr()
# print()

# Printing RAM details by using if/else statements so that the data measurement is in accordance to value of
# data_measure variable
print('RAM details below: ')

if data_measure == variables_data.kilobyte:
    ram_kb.ram_specs()
elif data_measure == variables_data.megabyte:
    ram_mb.ram_specs()
elif data_measure == variables_data.gigabyte:
    ram_gb.ram_specs()
else:
    print('Data Variable messed up! please check the code.')

# Listing all of the current processes using process_info function in pid_info module.
print('\nCurrent process details below: \n')
pid_info.processes_info()
