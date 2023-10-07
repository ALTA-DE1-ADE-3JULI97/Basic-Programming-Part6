def remove_duplicates(array):
    if len(array) == 0:
        return 0
    left = 0
    right = 1

    while right < len(array):
        if array[left] == array[right]:
            right += 1
        else:
            left += 1
            array[left] = array[right]
            right += 1
    return left + 1

if __name__ == '__main__':
    print(remove_duplicates([2, 3, 3, 3, 6, 9, 9])) # 4
    print(remove_duplicates([2, 3, 4, 5, 6, 9, 9])) # 6
    print(remove_duplicates([2, 2, 2, 11])) # 2
    print(remove_duplicates([2, 2, 2, 11])) # 2
    print(remove_duplicates([1, 2, 3, 11, 11])) # 4