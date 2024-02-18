
def linear_search(x, array):
    for i in range(len(array)):
        if array[i] == x:
            return i
    return None

x = 3
array = [7,3,5,4,8]

print(linear_search(x, array))