
#              1st


# nested_list = [[1, 2], [3, 4], [5, 6]]
# result = list(map(lambda sublist: list(map(lambda x: x + 5, sublist)), nested_list))
# print(result)


#               2nd


# d = {"apple": 100, "banana": 40, "cherry": 150}
# filtered_keys = list(filter(lambda key: d[key] > 50, d))
# print(filtered_keys)


#               3rd


# from functools import reduce
# l = [21,32,4,345,34,6,543,3]
# k = reduce(lambda x,y:x if x>y else y,l)
# print(k)


#                4th



#                 5th


# text = "Python"
#
# ascii_values = list(map(ord, text))
# print(ascii_values)


#                 6th


# text = "Beautiful Day"
# vowels = "aeiouAEIOU"
#
# consonants_only = filter(lambda char: char not in vowels, text)
#
# final_string = "".join(consonants_only)
# print(final_string)


#                7th


from functools import reduce
chars = ['P', 'y', 't', 'h', 'o', 'n']
result = reduce(lambda x, y: x + y, chars)
print(result)







