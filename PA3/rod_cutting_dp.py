# Mindy Yun, Winston Ta

import time

def cut_rod_dp(price_arr, n):
    # price_arr: list of prices for each rod length 1..n
    # n: total length of rod
    new_arr = [0] * (n + 1)  # new array of size n+1

    for j in range(1, n + 1):  
        q = float('-inf')
        for i in range(1, j + 1):
            q = max(q, price_arr[i - 1] + new_arr[j - i])
        new_arr[j] = q

    return new_arr[n]
    

# define driver function
def driver_dp(price_arr):

    len_arr = len(price_arr)

    start = time.time()
    max = cut_rod_dp(price_arr, len_arr)
    end = time.time()

    print(f"Size of array: {len_arr}\nMax profit: {max}\nCode execution time: {(end-start):.4f}")




    
