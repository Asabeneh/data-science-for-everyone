import math
from pprint import pprint
ages = [31, 26, 34, 37, 27, 26, 32, 32, 26, 27, 27, 24,
        32, 33, 27, 25, 26, 38, 37, 31, 34, 24, 33, 29, 26]


def calc_sum(lst):
    total = 0
    for i in lst:
        total += i
    return total


def calc_mean(lst):
    total = calc_sum(lst)
    average = total / len(lst)
    return average


def calc_median(lst):
    sorted_list = sorted(lst)
    list_len = len(sorted_list)
    if list_len % 2 == 0:
        middle_index_one = (list_len / 2) - 1
        middle_index_two = (list_len) / 2
        value_one = sorted_list[middle_index_one]
        value_two = sorted_list[middle_index_two]
        median = (value_one + value_two) / 2
        return median
    else:
        middle_index = len(lst) // 2
        median = lst[middle_index]
        return median


def calc_range(lst):
    sorted_list = sorted(lst)
    min_value = min(sorted_list)
    max_value = max(sorted_list)
    return max_value - min_value


def calc_variance(lst):
    variance = 0
    mu = calc_mean(lst)
    for i in lst:
        variance += (i - mu) * (i - mu)
    variance = round(variance / len(lst), 1)
    return variance


def calc_std(lst):
    variance = calc_variance(lst)
    std = math.sqrt(variance)
    return round(std, 1)


def freq_dist(lst):
    freq_table = {}
    for i in lst:
        if i not in freq_table:
            freq_table[i] = 1
        else:
            freq_table[i] += 1
    return freq_table


def calc_mode(lst):
    items = freq_dist(lst).items()
    freq_table = []
    for key, value in items:
        freq_table.append((value, key))
    mode = sorted(freq_dist, reverse=True)[0]


def freq_dist(lst):
    freq_table = {}
    for i in lst:
        if i not in freq_table:
            freq_table[i] = 1
        else:
            freq_table[i] += 1
    return freq_table


def calc_stat(lst):
    detail = {
        'Count: ': len(lst),
        'Sum: ': calc_sum(lst),
        'Min: ': min(lst),
        'Max: ': max(lst),
        'Range: ': calc_range(lst),
        'Mean: ': calc_median(lst),
        'Median': calc_median(lst),
        'Variance: ': calc_variance(lst),
        'Standard Deviation: ': calc_std(lst)
    }
    return detail


print('count:', len(ages))
print('Sum: ', calc_sum(ages))
print('Max:', max(ages))
print('Min: ', min(ages))
print('Range: ', calc_range(ages))
print('Mean: ', calc_mean(ages))
print('Median:', calc_median(ages))
print('Variance: ', calc_variance(ages))
print('Standard Deviation: ', calc_std(ages))
print('Frequency Distribution: ', freq_dist(ages))
