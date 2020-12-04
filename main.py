#!/usr/bin/env python3

import argparse
import logging

from src.sheluder import Sheluder

def parse_arguments():
    parser = argparse.ArgumentParser()

    parser.add_argument('--verbose', '-v', action = 'store_true', required = False, help = 'Sets logging type to DEBUG')

    parser.add_argument('--tasks', '-t', type=int, required = True, help = 'Tasks amount')
    parser.add_argument('--processors', '-p', type=int, required = True, help = 'Processors amount')
    duration_types = parser.add_mutually_exclusive_group()
    duration_types.required = True
    duration_types.add_argument('--duration_min_max', nargs = 2, type=int, metavar=('MIN','MAX'), help = 'Duration of a task random time frames')
    duration_types.add_argument('--durations', nargs = '+', type=int, metavar=('DURATION'), help = 'Durations of tasks')

    return parser.parse_args()


def main():
    args = parse_arguments()

    if args.verbose:
        logging.getLogger().setLevel(logging.DEBUG)

    if args.duration_min_max:
        duration = args.duration_min_max
        randomize_durations = True
    elif args.durations:
        duration = args.durations
        randomize_durations = False

    sheluder = Sheluder(tasks_amount = args.tasks,
        processors_amount = args.processors,
        durations = duration,
        randomize_durations = randomize_durations)

    sheluder.run()

if __name__ == "__main__":
    main()
