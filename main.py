#!/usr/bin/env python3

import argparse

from src.sheluder import Sheluder

def parse_arguments():
    parser = argparse.ArgumentParser()

    parser.add_argument('--verbose', '-v', action = 'store_true', required = False, help = 'Sets logging type to DEBUG')

def main():
    args = parse_arguments()

    sheluder = Sheluder()

    if args.verbose:
        src.sheluder.logger.setLevel(logging.DEBUG)

    sheluder.run()

if __name__ == "__main__":
    main()
