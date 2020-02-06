def shorting_algorithm(array):
    try:
        if type(array) == list:
            for item_index in range(len(array)):
                minimum = item_index
                for _other in range(item_index + 1, len(array)):
                    if array[_other] < array[minimum]:
                        minimum = _other
                if minimum != item_index:
                    array[minimum], array[item_index] = array[item_index], array[minimum]
        return array
    except Exception as e:
        print(e)
        return array


a = [1, 4, 3, 6, 8, 2]
b = ["a", "c", "b", "e", "d"]

print(shorting_algorithm(a))
