# -*- coding: utf-8 -*-
import json

with open('results.json', 'r', encoding='utf-8') as f:
    results = json.load(f)

print('Total file number: {}'.format(len(results)))


def top_sort(top_results, n):
    for i in range(n):
        for j in range(n-1):
            if top_results[j][1] < top_results[j+1][1]:
                top_results[j], top_results[j+1] = top_results[j+1], top_results[j]

    return top_results


def top_n(n):
    top_results = [['', 0] for _ in range(n)]
    for key in results:
        results_key = int(results[key])
        if results[key] > top_results[n-1][1]:
            top_results[n-1] = [key, results_key]
            top_results = top_sort(top_results, n)

    return top_results


if __name__ == '__main__':
    for item in top_n(5):
        print(item)