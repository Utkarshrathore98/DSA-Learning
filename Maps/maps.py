import collections

dict1 = {
    'day_1': 'Monday',
    'day_2': 'Tuesday'
}

dict2 = {
    'day_3': 'Wednesday',
    'day_4': 'Thursday'
}

dict = collections.ChainMap(dict1, dict2)
print(dict.maps, '\n')

# Updating the map
dict2['day_4'] = 'Friday'
print(dict.maps, '\n')

# Accessing all the items in an dictionary
print('Elements in an dictionary :-')
for key, val in dict.items():
    print('{} = {}'.format(key, val))


