#!/usr/bin/env python3

import argparse

from src.sheluder import Sheluder

def parse_arguments():
    parser = argparse.ArgumentParser()

    parser.add_argument('--verbose', '-v', action = 'store_true', required = False, help = 'Sets logging type to DEBUG')

    parser.add_argument('--tasks', required = True, help = 'Tasks amount')
    duration_types = parser.add_mutually_exclusive_group()
    duration_types.required = True
    duration_types.add_argument('--duration_min_max', nargs = 2, help = 'Duration of a task random time frames, usage:\n--duration_min_max min_time max_time')
    duration_types.add_argument('--durations', nargs = '*', help = 'Durations of tasks, usage:\n--durations duration_of_task_1 duration_of_task_2 ...')


def main():
    args = parse_arguments()

    if args.verbose:
        src.sheluder.logger.setLevel(logging.DEBUG)

    if args.duration_min_max:
        sheluder = Sheluder(args.tasks, args.duration_min_max, randomize_durations = True)
    elif args.durations:
    sheluder = Sheluder(args.tasks, args.durations, randomize_durations = False)

    sheluder.run()

if __name__ == "__main__":
    main()
