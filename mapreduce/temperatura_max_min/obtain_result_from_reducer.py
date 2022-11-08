#!/usr/bin/env python
import os


path = os.getcwd() + "/salida_2017_temp/"
files = os.listdir(path)
max_temperature = 0
max_temperature_code = None
min_temperature = 0
min_temperature_code = None


for file in files:
    if os.path.isfile(os.path.join(path, file)) and os.path.basename(os.path.join(path, file)).split("/")[-1] not in ['_SUCCESS', '_FAILED']:
        with open(os.path.join(path, file), "r") as f:
            lines = f.readlines()
            for line in lines:
                process_line = line.strip().split("\t")

                if process_line[0] == 'Min':
                    try:
                        min_tmp = float(process_line[2])
                    except ValueError:
                        continue
                    if min_temperature > min_tmp:
                        min_temperature = min_tmp
                        min_temperature_code = process_line[1]
                elif process_line[0] == 'Max':
                    try:
                        max_tmp = float(process_line[2])
                    except ValueError:
                        continue
                    if max_temperature < max_tmp:
                        max_temperature = max_tmp
                        max_temperature_code = process_line[1]


data_path = os.getcwd() + "/files/2017/"
for file in os.listdir(data_path):
    if os.path.isfile(os.path.join(data_path, file)):
        with open(os.path.join(data_path, file), "r") as f:
            first_line = f.readline(5)
            if first_line == min_temperature_code:
                print("%s\t%s" % (file.strip().split("_")[1], min_temperature))
            elif first_line == max_temperature_code:
                print("%s\t%s" % (file.strip().split("_")[1], max_temperature))
            else:
                continue
