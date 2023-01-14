import os
import argparse
from subprocess import Popen

def get_grbs(input_file: str) -> list:
    with open (input_file, 'r') as f:
        grbs = f.read().splitlines()
    return [elm.strip() for elm in grbs]

def write_exe_file(grb: str, GWFish_folder: str) -> str:
    file_name = f'{grb}.sh'
    with open (file_name, 'w') as f:
        f.write('#!/usr/bin/env bash\n')
        f.write('source activate gw_analysis\n')
        f.write(f'cd {GWFish_folder}\n')
        f.write(f'python CBC_Simulation.py --pop_file {grb}_population_100000.hdf5 --pop_id BNS --detectors ET\n')
    os.chmod(file_name, 0o755)
    return os.path.join(os.getcwd(), file_name)

def pipeline(grbs: list, GWFish_folder: str):
    for grb in grbs:
        file = write_exe_file(grb, GWFish_folder)
        cmd = f"screen -dmS GRB_session_{grb} sh -c '{file}; exec bash'"
        Popen(cmd, shell=True)

def main():
    parser = argparse.ArgumentParser(description='Job Submission Pipeline')
    parser.add_argument("-i", "--input", type=str, dest='input', help='Input file')
    parser.add_argument("-fish", "--GWFish_folder", type=str, dest='gw_fish', default='/home/alessandra/GWFish', help='GWFish analysis folder')
    opts = parser.parse_args()

    try:
        assert opts.input, "[ERROR] Please provide a valid input file"
    except AssertionError as e:
        print(e)
        raise

    grbs = get_grbs(opts.input)
    pipeline(grbs, opts.gw_fish)
    

if __name__ == '__main__':
    main()