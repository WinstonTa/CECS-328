# Mindy Yun, Winston Ta

import time

# define cut rod function
def cut_rod_recursive(price, index, n):
    # price: list of prices for each rod length (1..len(price))
    # index: current index (starting from len(price) - 1)
    # n: remaining rod length

    if index == 0:
        return n * price[0] 

    if n == 0:
        return 0

    # option 1: don't cut
    no_cut = cut_rod_recursive(price, index - 1, n)

    # option 2: cut if you can
    # cut is q in pseudocode from class btw
    cut = float('-inf')
    rod_length = index + 1
    if rod_length <= n:
        cut = price[index] + cut_rod_recursive(price, index, n - rod_length)

    # return whatever is better between cut or no cut
    return max(cut, no_cut)




# define driver function
def driver_recursive(price_arr):
    len_arr = len(price_arr)

    start = time.time()
    max = cut_rod_recursive(price_arr, len_arr - 1, len_arr)
    end = time.time()

    print(f"Size of array: {len_arr}\nMax profit: {max}\nCode execution time: {(end-start):.4f}")


