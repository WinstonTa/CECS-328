from rod_cutting_dp import *
from rod_cutting_recursive import *

# --- Small arrays (quick sanity checks) ---
a1 = [2, 5, 7, 8, 9]           # expect 12
a2 = [3, 5, 8, 9, 10, 17, 17]  # expect 21
a3 = [1, 5]                    # expect 5

print("\n--- Small Tests ---")
print("a1 DP:"); driver_dp(a1)
print("a1 Rec:"); driver_recursive(a1)

print("a2 DP:"); driver_dp(a2)
print("a2 Rec:"); driver_recursive(a2)

print("a3 DP:"); driver_dp(a3)
print("a3 Rec:"); driver_recursive(a3)


# --- Medium slice (safe for recursion) ---
arr20 = [8,31,31,34,50,56,60,61,63,67,77,81,82,83,84,85,88,89,93,96]  # n=20
print("\n--- Medium Slice (n=20) ---")
print("arr20 DP:"); driver_dp(arr20)
print("arr20 Rec:"); driver_recursive(arr20)


# --- Larger slice (moderate runtime) ---
arr30 = [8,31,31,34,50,56,60,61,63,67,77,81,82,83,84,85,88,89,93,96,
         99,105,111,112,122,124,124,143,146,150]  # n=30
print("\n--- Larger Slice (n=30) ---")
print("arr30 DP:"); driver_dp(arr30)
print("arr30 Rec:"); driver_recursive(arr30)


# --- Full assignment array (expected 1186) ---
full = [8,31,31,34,50,56,60,61,63,67,77,81,82,83,84,85,88,89,93,96,99,105,111,112,
        122,124,124,143,146,150,154,158,162,169,172,182,182,185,187,191,201,202,
        205,206,207,223,226,230,234,236,243,245,248,248,254,259,260,262,264,270,
        271,273,281,286,286,287,295,298,299,301,303,308,308,321,346,349,351]

print("\n--- Full Assignment Array (n=77) ---")
print("Full DP:"); driver_dp(full)
print("Full Rec:"); driver_recursive(full)  # may take 15–30 seconds
