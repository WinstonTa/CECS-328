# pa4_test2.py
# Unit testing file for aircraft_max_revenue() from cecs328pa4.py

from cecs328pa4 import aircraft_max_revenue


def unit_test(name, cargo, cap, expected):
    """
    Runs a single unit test for aircraft_max_revenue and reports:
    - test name
    - expected value
    - actual value
    - PASS/FAIL
    """
    try:
        actual = aircraft_max_revenue(cargo, cap)
        status = "PASS" if actual == expected else "FAIL"
        print(f"{name}: EXPECTED={expected}, ACTUAL={actual} -- {status}")
    except Exception as e:
        # If an error was expected, expected should be the exception type
        if isinstance(expected, type) and isinstance(e, expected):
            print(f"{name}: EXPECTED EXCEPTION={expected.__name__}, ACTUAL={e.__class__.__name__} -- PASS")
        else:
            print(f"{name}: EXPECTED={expected}, ACTUAL EXCEPTION={e.__class__.__name__} -- FAIL")


# ===================================================
# =============== Invalid / Valid Inputs =============
# ===================================================

# 1. Negative value test (invalid cargo weight): Should raise ValueError
unit_test(
    name="Invalid Negative Weight",
    cargo=[(-5, 100)],
    cap=50,
    expected=ValueError
)

# 2. Zero value test (weight or price = 0): Should raise ValueError
unit_test(
    name="Invalid Zero Value",
    cargo=[(0, 100)],
    cap=50,
    expected=ValueError
)

# 3. Positive values (valid)
# simple: pick best of two items under cap
# cargo: (weight, price)
# Best is taking item (5,100)
unit_test(
    name="Valid Positive Input",
    cargo=[(5, 100), (10, 120)],
    cap=7,
    expected=100
)


# ===================================================
# ==================== Small Tests ==================
# ===================================================

# Small Test 1
# Best: (3,40)+(4,50)=90 (weight limit is 7)
unit_test(
    name="Small Test 1",
    cargo=[(3, 40), (4, 50), (5, 60)],
    cap=7,
    expected=90
)

# Small Test 2
# Best: (2,20)+(2,25)+(3,40)=85 (cap=7)
unit_test(
    name="Small Test 2",
    cargo=[(2, 20), (2, 25), (3, 40)],
    cap=7,
    expected=85
)

# Small Test 3
# Best: (1,10)+(4,50)=60 (cap=5)
unit_test(
    name="Small Test 3",
    cargo=[(1, 10), (3, 25), (4, 50)],
    cap=5,
    expected=60
)


# ===================================================
# ==================== Medium Tests =================
# ===================================================

# Medium Test 1
# Items: (5,80),(7,110),(3,40),(9,150)
# cap=14
# Best: (5,80)+(9,150)=230
unit_test(
    name="Medium Test 1",
    cargo=[(5, 80), (7, 110), (3, 40), (9, 150)],
    cap=14,
    expected=230
)

# Medium Test 2
# Items: (6,90),(4,60),(5,75),(3,40)
# cap=10
# Best: (6,90)+(4,60)=150
unit_test(
    name="Medium Test 2",
    cargo=[(6, 90), (4, 60), (5, 75), (3, 40)],
    cap=10,
    expected=150
)

# Medium Test 3
# Items: (8,120),(6,95),(5,80),(4,60)
# cap=12
# Best combination: (8,120)+(4,60)=180
unit_test(
    name="Medium Test 3",
    cargo=[(8, 120), (6, 95), (5, 80), (4, 60)],
    cap=12,
    expected=180
)


# ===================================================
# ===================== Large Tests =================
# ===================================================

# Large Test 1
# items chosen for predictable knapsack result
# Best: 1000 + 2000 + 3500 = 6500
unit_test(
    name="Large Test 1",
    cargo=[(10, 1000), (20, 2000), (30, 3500), (40, 4200)],
    cap=60,
    expected=6500
)

# Large Test 2
# Best: (25,3000)+(15,1800)+(10,1500)=6300
unit_test(
    name="Large Test 2",
    cargo=[(25, 3000), (15, 1800), (10, 1500), (40, 3900)],
    cap=50,
    expected=6300
)

# Large Test 3
# Best: (50,6000)+(30,3500)+(20,2200)=11700
unit_test(
    name="Large Test 3",
    cargo=[(50, 6000), (30, 3500), (20, 2200), (70, 8000)],
    cap=100,
    expected=11700
)
