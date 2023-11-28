# -*- coding: utf-8 -*-
"""
Created on Tue Sep 22 14:18:03 2020

@author: Laura.Fiorentino
"""
import csv
import itertools

def read_ssp(filename):
    variables = []
    ssp_dict = {}
    with open(filename) as file:
        for line in file:
            line_split = line.split(',')
            if len(line_split) < 3:
                continue
            new_variable = line_split[2]
            if new_variable in variables:
                if line_split[-1] == 'G\n':
                    ssp_dict[new_variable].append(line_split[3])
                else:
                    ssp_dict[new_variable].append('NaN')
                ssp_dict[new_variable + '_time'].append(line_split[0]
                                                        + ' ' + line_split[1])
            else:
                variables.append(new_variable)
                ssp_dict[new_variable + '_time'] = []
                ssp_dict[new_variable] = []
                if line_split[-1] == 'G\n':
                    ssp_dict[new_variable].append(line_split[3])
                else:
                    ssp_dict[new_variable].append('NaN')
                ssp_dict[new_variable + '_time'].append(line_split[0]
                                                        + ' ' + line_split[1])
    return ssp_dict


def write_csv(ssp_dict, new_filename):
    """ This function writes thew new csv file. Each column is a time then the
    corresponding variable"""
    with open(new_filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(ssp_dict.keys())
        writer.writerows(itertools.zip_longest(*ssp_dict.values()))
        
def ssp2csv(logfile, csvfile):
    ssp_dict = read_ssp(logfile)
    write_csv(ssp_dict, csvfile)
