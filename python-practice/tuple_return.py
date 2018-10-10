# Use tuples to return multiple values
from collections import Counter

STATS_FORMAT_1 = """Statistics:
Mean: {mean}
Median: {median}
Mode: {mode}"""

STATS_FORMAT_2= """Statistics:
Mode: {mode}"""

def calculate_staistics(value_list):
	mean = float(sum(value_list) / len(value_list))
	median = value_list[int(len(value_list) / 2)]
	mode = Counter(value_list).most_common(1)[0][0]
	return (mean, median, mode)

(mean, median, mode) = calculate_staistics([10, 20, 40, 30])

print(STATS_FORMAT_2.format(mode=mode))