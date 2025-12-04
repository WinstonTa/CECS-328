from cecs328pa4 import aircraft_max_revenue

def run_test(name, cargo, cap, expected):
    actual = aircraft_max_revenue(cargo, cap)
    status = "PASS" if actual == expected else "FAIL"
    print(f"{name}: {status}")
    print(f"  Expected: {expected}")
    print(f"  Actual:   {actual}\n")

# -----------------------------------------
# SMALL TESTS (5)
# -----------------------------------------

run_test("SMALL TEST 1",
         [(1, 3), (2, 4)], 3,
         7)

run_test("SMALL TEST 2",
         [(2,5),(2,6),(3,14)], 4,
         14)

run_test("SMALL TEST 3",
         [(3,10),(4,15),(5,20)], 8,
         30)

run_test("SMALL TEST 4",
         [(4,50),(3,30),(2,20)], 5,
         50)

run_test("SMALL TEST 5",
         [(2,10),(1,4),(2,7)], 3,
         14)

# -----------------------------------------
# MEDIUM TESTS (5)
# -----------------------------------------

run_test("MEDIUM TEST 1",
         [(2,12),(3,20),(4,28),(5,35)], 7,
         48)   # 3+4 = 20+28

run_test("MEDIUM TEST 2",
         [(5,30),(4,28),(6,40),(3,20)], 9,
         60)   # 30 + 20 + 10? (best is 30+28+? actually 30+20+10=60)

run_test("MEDIUM TEST 3",
         [(3,25),(3,24),(4,40),(2,15)], 6,
         55)   # 25 + 30 OR 25 + 24 + 6? actual optimal = 55

run_test("MEDIUM TEST 4",
         [(6,50),(5,45),(4,30),(3,20),(2,15)], 10,
         80)   # 5+3+2 = 45+20+15

run_test("MEDIUM TEST 5",
         [(1,5),(2,9),(5,30),(6,40),(3,14)], 8,
         49)   # 5+3 weight: 30+14 OR 2+6? best = 49

# -----------------------------------------
# LARGE TESTS (5)
# -----------------------------------------

# LARGE TEST 1
cargo1 = [(i, i*3) for i in range(1, 30)]
# Expected computed manually with your output = 150
run_test("LARGE TEST 1",
         cargo1, 50,
         150)

# LARGE TEST 2
cargo2 = [(10,60),(20,100),(30,120),(25,140),(15,75),(5,22),(7,28)]
# Expected confirmed from your output = 275
run_test("LARGE TEST 2",
         cargo2, 50,
         275)

# LARGE TEST 3
cargo3 = [(i, i*10) for i in range(5, 55, 5)]
# Expected output from your DP result = 1000
run_test("LARGE TEST 3",
         cargo3, 100,
         1000)

# LARGE TEST 4
cargo4 = [(i, i*i//2) for i in range(10, 60, 3)]
# Your DP result = 3194
run_test("LARGE TEST 4",
         cargo4, 120,
         3194)

# LARGE TEST 5
cargo5 = [(i, i*4 + 7) for i in range(20, 70)]
# Your DP result = 856
run_test("LARGE TEST 5",
         cargo5, 200,
         856)

# -----------------------------------------
# ASSIGNMENT DOC EXAMPLES (from PA4 PDF)
# -----------------------------------------

doc_cargo = [
    (787,332),(1620,14624),(1204,11673),(147,15671),(423,18752),
    (1824,2418),(1218,6800),(9,685),(1753,5432),(52,17628),
    (1031,9352),(2,11034),(1296,971),(961,1354),(602,11689)
]

run_test("DOC EXAMPLE 1 (capacity=8)",
         [(3,32),(5,22),(4,15)], 8,
         54)

run_test("DOC EXAMPLE 2 (capacity=10000)",
         doc_cargo, 10000,
         125758)

run_test("DOC EXAMPLE 3 (capacity=5000)",
         doc_cargo, 5000,
         103284)

run_test("DOC EXAMPLE 4 (capacity=100)",
         doc_cargo, 100,
         29347)

run_test("DOC EXAMPLE 5 (capacity=10)",
         doc_cargo, 10,
         11034)

run_test("DOC EXAMPLE 6 (capacity=1)",
         doc_cargo, 1,
         0)