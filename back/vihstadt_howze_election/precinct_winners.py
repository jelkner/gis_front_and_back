#!/usr/bin/env python
"""Determin the winner of each of the 52 voting precincts in the
Vihstadt-Howze Arlington County Council election of November 2014
"""
import csv

CANDIDATE1 = 'John E. Vihstadt'
CANDIDATE2 = 'Alan E. Howze'


def precinct_winner(data, precinct):
    if data[precinct][CANDIDATE1] > data[precinct][CANDIDATE2]:
        return CANDIDATE1
    elif data[precinct][CANDIDATE1] < data[precinct][CANDIDATE2]:
        return CANDIDATE2
    else:
        return 'Tie vote'


def process_data(f):
    results = {}
    winners = [None]

    with open(f) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if row['candidate_name'] in [CANDIDATE1, CANDIDATE2]:
                candidate = row['candidate_name']
                precinct = row['precinct_code']
                votes = row['total_votes']

                if precinct in results:
                    results[precinct][candidate] = votes
                else:
                    results[precinct] = {candidate: votes}

    for i in range(1, 53):
        winners.append(precinct_winner(results, str(i)))

    return winners


def share_results(display=False):
    winners = process_data('data/11042014_complete.csv')
    if display:
        print(winners)
    return winners


if __name__ == '__main__':
    share_results(display=True)
