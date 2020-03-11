"""
This converts an ssp log to a csv.

run in command line: run ssp2csv.py -f input -n output
input and output filenames should include directory if not in current folder

Created by L A Fiorentino, NOAA COP-OPS
Last Updated: 11 March 2020

"""
import argparse
import csv
import itertools

def read_ssp(filename):
    """ This function reads the .hdr file for the number of bins
    and measurements"""
    variables = []
    ssp_dict = {}
    with open(filename) as file:
        for line in file:
            line_split = line.split(',')
            if len(line_split) < 3:
                continue
            new_variable = line_split[2]
            if new_variable in variables:
                ssp_dict[new_variable].append(line_split[3])
                ssp_dict[new_variable + '_time'].append(line_split[0]
                                                        + ' ' + line_split[1])
            else:
                variables.append(new_variable)
                ssp_dict[new_variable + '_time'] = []
                ssp_dict[new_variable] = []
                ssp_dict[new_variable].append(line_split[3])
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

def parse_cmd_arguments():
    '''
    Parse command line arguments
    '''
    parser = argparse.ArgumentParser(description='Get input files')
    parser.add_argument('-f', '--filename', help='input file, no extension',
                        required=True)
    parser.add_argument('-n', '--new_filename', help='input file, no extension',
                        required=True)
    return parser.parse_args()


if __name__ == '__main__':
    filename = parse_cmd_arguments()
    ssp_dict = read_ssp(filename.filename)
    write_csv(ssp_dict, filename.new_filename)
