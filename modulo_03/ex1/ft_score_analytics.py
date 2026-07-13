#!/usr/bin/env python3
import sys


def show_scores(scores: list[int]) -> None:
    if len(scores) == 0:
        raise ValueError('No scores provided. Usage: '
                         './ft_score_analytics.py <score1> <score2> ...')
    print(f'Scores processed: {scores}')
    print(f'Total players: {len(scores)}')
    print(f'Total score: {sum(scores)}')
    print(f'Average score: {round(sum(scores) / len(scores), 2)}')
    print(f'High score: {max(scores)}')
    print(f'Low score: {min(scores)}')
    print(f'Score range: {max(scores) - min(scores)}')


if __name__ == "__main__":
    scores = []
    for i in sys.argv[1:]:
        try:
            scores.append(int(i))
        except ValueError:
            print(f'Invalid parameter: {i}')
            continue

    print('=== Player Score Analytics ===')
    try:
        show_scores(scores)
    except ValueError as ex:
        print(ex)
