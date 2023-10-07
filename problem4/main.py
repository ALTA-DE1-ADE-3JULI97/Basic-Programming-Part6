def find_max_sum_sub_array(k, arr):
    max_sum = float('-inf')
    window_sum = 0

    for i in range(len(arr)):
        window_sum += arr[i]

        if i >= k -1:
            max_sum = max(max_sum, window_sum)
            window_sum -= arr[i - k +1]
    return max_sum

if __name__ == '__main__':
    print(find_max_sum_sub_array(3, [2, 1, 5, 1, 3, 2])) # 9
    print(find_max_sum_sub_array(2, [2, 3, 4, 1, 5])) # 7
    print(find_max_sum_sub_array(2, [2, 1, 4, 1, 1])) # 5
    print(find_max_sum_sub_array(3, [2, 1, 4, 1, 1])) # 7
    print(find_max_sum_sub_array(4, [2, 1, 4, 1, 1])) # 8