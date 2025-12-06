# Mindy Yun, Winston Ta

# cecs328pa4.py

def aircraft_max_revenue(cargo_pool: list[tuple[int, int]], weight_capacity: int) -> int:
    # ---------- Input validation ----------
    if not isinstance(cargo_pool, (list, tuple)):
        raise TypeError("cargo_pool must be a list or tuple of (weight:int, price:int) tuples.")

    if not isinstance(weight_capacity, int):
        raise TypeError("weight_capacity must be an integer.")

    if weight_capacity < 1 or weight_capacity > 20000:
        raise ValueError("weight_capacity must be between 1 and 20,000 (inclusive).")

    # Validate each cargo item inline (no helper functions allowed)
    for idx, item in enumerate(cargo_pool):
        if not isinstance(item, (list, tuple)):
            raise TypeError(f"cargo_pool[{idx}] must be a tuple/list of (weight:int, price:int).")
        if len(item) != 2:
            raise TypeError(f"cargo_pool[{idx}] must contain exactly two elements (weight, price).")

        weight, price = item

        # Disallow non-integer types for weight/price
        if not isinstance(weight, int):
            raise TypeError(f"cargo_pool[{idx}][0] (weight) must be an integer.")
        if not isinstance(price, int):
            raise TypeError(f"cargo_pool[{idx}][1] (price) must be an integer.")

        # Disallow non-positive values (negative or zero)
        if weight <= 0:
            raise ValueError(f"cargo_pool[{idx}][0] (weight) must be > 0.")
        if price <= 0:
            raise ValueError(f"cargo_pool[{idx}][1] (price) must be > 0.")

    # ---------- Early exit: empty cargo pool ----------
    if len(cargo_pool) == 0:
        return 0

    # ---------- Core DP (1D knapsack) ----------
    # dp[c] will be the maximum revenue achievable with capacity exactly c (or up to c).
    cap = weight_capacity
    dp: list[int] = [0] * (cap + 1)

    # Loop through each cargo item (weight, price)
    # For each item, update dp array from high->low to ensure each item is only used once.
    for (w, v) in cargo_pool:
        # Skip items that individually exceed the full capacity (they can never be taken)
        if w > cap:
            continue

        # iterate descending to preserve 0/1 knapsack property
        # local variables for speed
        local_dp = dp
        start = w
        # iterate capacity from cap down to w (inclusive)
        for c in range(cap, start - 1, -1):
            # compute candidate value if we include this item
            candidate = local_dp[c - w] + v
            if candidate > local_dp[c]:
                local_dp[c] = candidate
        # dp reference updated in-place

    # The maximum revenue for capacity 'cap' is dp[cap]. If all items were heavier than capacity,
    # dp[cap] will remain 0 as required.
    result = dp[cap]
    # Ensure an integer is returned
    return int(result)
