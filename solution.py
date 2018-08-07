from os import listdir
from itertools import combinations
import timeit


def possible_team_formations_based_on_max_proficiency(arr: list):
    n_students, n_proficiencies = arr
    results = dict()

    for i, j in combinations(range(n_students), 2):
        proficiency_count = bin(n_proficiencies[i] |
                                n_proficiencies[j]).count('1')

        if proficiency_count in results:
            results[proficiency_count] += 1
        else:
            results[proficiency_count] = 1

    return results


def max_proficiency_and_number_of_possible_team_formations(table: dict):
    max_proficiency = max(table.keys())

    return f"{max_proficiency}\n{table[max_proficiency]}"


def list_from_file_proficiencies_subjects_and_students(file_name: str):
    with open(file_name) as file:
        items = [line.rstrip() for line in file]

    return int(items[0].split()[0]), [int(n, 2) for n in items[1:]]


if __name__ == '__main__':
    for file in listdir('input'):
        arr = list_from_file_proficiencies_subjects_and_students('input/' +
                                                                 file)
        a = possible_team_formations_based_on_max_proficiency(arr)
        b = max_proficiency_and_number_of_possible_team_formations(a)
        print(file + '\n' + b + '\n\n')
