#sum consecutive numbers
from collections import defaultdict
def sum_consecutive_numbers(arr):
    mp = defaultdict(int)
    for ele in arr:
        mp[ele] += 1

    change = True
    while change:
        change = False
        new_mp = defaultdict(int)
        for key, value in mp.items():
            if value > 1:
                new_mp[key * value] += 1
                change = True
            else:
                new_mp[key] += value

        mp = new_mp.copy()

    result = []
    for key in mp.keys():
        result.append(key)

    return result

print(sum_consecutive_numbers([1,1,2,5,3,3,6,12]))
print(sum_consecutive_numbers([1,1,3,3,5,6,7]))


#reverse vowels
def reverse_vowels(word):
    word_arr = list(word)
    n=len(word)
    vowels = {'a', 'e', 'i', 'o', 'u'}
    i = 0;
    j = len(word) - 1
    while i < j:
        while i < n and word_arr[i] not in vowels:
            i += 1
        while j >= 0 and word_arr[j] not in vowels:
            j -= 1
        temp = word_arr[i]
        word_arr[i] = word_arr[j]
        word_arr[j] = temp
        i += 1
        j -= 1
    return "".join(word_arr)


print(reverse_vowels("icecream")) #acecreim
print(reverse_vowels("elephant")) #alephent


