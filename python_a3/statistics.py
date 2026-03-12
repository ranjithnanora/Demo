"""
Write three functions: to calculate mean, median and mode of a list of
numbers. Write a fourth function that takes two arguments. First argument
is a list of numbers, second argument is optional and is a string. String can
be any of the three: “mean”, “median”, “mode”. Function must return the
correct statistical value depending on the string input. By default, it must
return mean of the list.
"""
def get_mean(data):
    if not data: return 0
    return sum(data) / len(data)

def get_median(data):
    if not data: return 0
    n = len(data)
    sorted_data = sorted(data)
    mid = n // 2
    if n % 2 == 0:
        return (sorted_data[mid - 1] + sorted_data[mid]) / 2
    else:
        return sorted_data[mid]
def get_mode(data):
    if not data: return None
    counts = {}
    for num in data:
        counts[num] = counts.get(num, 0) + 1
    max_count = max(counts.values())
    modes = [key for key, val in counts.items() if val == max_count]
    return modes[0]

def calculate_stats(numbers, stat_type="mean"):
    stat_type = stat_type.lower()
    
    if stat_type == "mean":
        return get_mean(numbers)
    elif stat_type == "median":
        return get_median(numbers)
    elif stat_type == "mode":
        return get_mode(numbers)
    else:
        return f"Error: '{stat_type}' is not a valid statistic type."

sample_data = [10, 20, 20, 30, 40]

print(f"Default (Mean): {calculate_stats(sample_data)}")          
print(f"Explicit Mean:  {calculate_stats(sample_data, 'mean')}")   
print(f"Median:         {calculate_stats(sample_data, 'median')}") 
print(f"Mode:           {calculate_stats(sample_data, 'mode')}")  