def min_max(array):
    array.sort()
    min = array[0]
    max = array[-1]
    print(f"The minimum and maximum numbers of {array} are: {[min, max]}")


# example list
# replace list with desired list
array = [2, 25, 6, 1, -3, 9]
min_max(array)
