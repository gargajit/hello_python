def concat_list_data(lst):
    s = ""
    for item in lst:
        s = s + str(item)

    return s

print(concat_list_data(['aj', 'it', 0, 8]))

print(concat_list_data(['++', '>>', '||', '<<', '++']))
