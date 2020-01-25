my_list = [int(x) for x in input().split()]

i_max = my_list.index(max(my_list))
i_min = my_list.index(min(my_list))

my_list[i_max], my_list[i_min] = my_list[i_min], my_list[i_max]

print(' '.join([str(el) for el in my_list]))




