array = [5,2,4,1,6,3]

for i in range(len(array)):
    num = array[i]
    print(f'i: {i}\nnum: {num}')
    print(f'array append num: {array}')
    j = i - 1
    while j >= 0 and array[j] < num:
        array[j + 1] = array[j]
        j = j - 1
    array[j + 1] = num

print(array)