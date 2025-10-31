# Winston Ta  Mindy Yun

from sympy import Symbol, log, limit, simplify, oo
import sympy as sp

# symbolic input size
n = sp.symbols('n')

def same_asymptotic(left_function, right_function):
    # asymptotic runtime check
    same_runtime = False

    # simplify f1 and f2 so that only highest ordered term is preserved
    f1_compare = sp.simplify(left_function)
    f2_compare = sp.simplify(right_function)

    # compare function runtimes with a limit
    ratio = sp.limit(f1_compare / f2_compare, n, oo)

    same_runtime = True if ratio.is_finite and ratio != 0 else False
    
    return same_runtime
