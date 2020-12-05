#!/usr/bin/env python3

import argparse
import logging

from src.sheluder import Sheluder

def parse_arguments():
    parser = argparse.ArgumentParser()

    parser.add_argument('--verbose', '-v', action = 'store_true', required = False, help = 'Sets logging type to DEBUG')

    parser.add_argument('--strategy', '-s', required = True, choices = ['dummy'], help = 'Choose strategy for planning tasks')
    parser.add_argument('--arbitration', '-a', required = True, choices = ['dummy', 'random', 'cycle', 'chronological'], help = 'Choose arbitration rule to choose between same priority tasks')
    parser.add_argument('--expropriation', '-e', action = 'store_true', required = False, help = 'Don\'t expropriate tasks after each chunk of time')

    parser.add_argument('--timeChunk', '-T', type = int, metavar=('seconds'), required = False, default = '1', help = 'Define time chunk length[seconds]')

    parser.add_argument('--processors', '-p', type = int, required = True, help = 'Processors amount')

    parser.add_argument('--tasks', '-t', type = int, required = True, help = 'Tasks amount')
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

    sheluder = Sheluder(
        strategy = args.strategy,
        arbitration = args.arbitration,
        expropriation = args.expropriation,
        timeChunk = args.timeChunk,
        tasks_amount = args.tasks,
        processors_amount = args.processors,
        durations = duration,
        randomize_durations = randomize_durations)

    sheluder.run()

if __name__ == "__main__":
    main()
