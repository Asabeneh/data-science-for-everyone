import math
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


class Stats:
    def __init__(self, lst):
        self.lst = lst
        self.lst_len = len(self.lst)

    def count(self):
        return self.lst_len

    def sum(self):
        total = 0
        lst = self.lst
        for i in lst:
            total += i
        return total

    def min(self):
        return min(self.lst)

    def max(self):
        return max(self.lst)

    def range(self):
        diff = self.max() - self.min()
        return diff

    def mean(self):
        total = self.sum()
        average = total / self.lst_len
        return average

    def median(self):
        lst = self.lst
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
            middle_index = self.lst_len // 2
            median = lst[middle_index]
            return median

    def mode(self):
        items = self.list_of_tuples()
        sorted_lst = []
        for key, value in items:
            if key and value:
                sorted_lst.append((value, key))
            else:
                pass
        x, y = sorted(sorted_lst, reverse=True)[0]
        return {'mode': y, 'count': x}

        mode_and_count = self.freq_dist()[0]
        return mode_and_count

    def var(self):
        variance = 0
        mu = self.mean()
        lst = self.lst
        for i in lst:
            variance += (i - mu) * (i - mu)
        variance = round(variance / len(lst), 1)
        return variance

    def std(self):
        variance = self.var()
        sd = math.sqrt(variance)
        return round(sd, 1)

    def list_of_tuples(self):
        dct = {}
        lst = self.lst
        for i in lst:
            if i not in dct:
                dct[i] = 1
            else:
                dct[i] += 1
        return dct.items()

    def freq_dist(self):
        freq_table = []
        items = self.list_of_tuples()
        for key, value in items:
            value = int(value) * (100) / self.count()
            freq_table.append((value, key))
        return sorted(freq_table, reverse=True)

    def describe(self):
        count = self.count()
        sum = self.sum()
        min = self.min()
        max = self.max()
        range = self.range()
        mean = self.mean()
        median = self.median()
        variance = self.var()
        std = self.std()
        freq_dist = self.freq_dist()
        detail = {
            'Count: ': count,
            'Sum: ': sum,
            'Min: ': min,
            'Max: ': max,
            'Range: ': range,
            'Mean: ': mean,
            'Median': median,
            'Variance: ': variance,
            'Standard Deviation: ': std
        }
        return detail


data = Stats(ages)
print('Count: ', data.count())
print('Sum: ', data.sum())
print('Min: ', data.min())
print('Max: ', data.max())
print('Range: ', data.range())
print('Mean: ', data.mean())
print('Median: ', data.median())
print('Mode: ', data.mode())
print('Variance: ', data.var())
print('Standard Deviation: ', data.std())
print('Frequency Distribution: ', data.freq_dist())
print('==== Details ====')
print(data.describe())
