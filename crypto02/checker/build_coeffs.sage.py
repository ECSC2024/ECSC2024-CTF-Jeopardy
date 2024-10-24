

# This file was *autogenerated* from the file build_coeffs.sage
from sage.all_cmdline import *   # import sage library

_sage_const_1 = Integer(1); _sage_const_0 = Integer(0); _sage_const_2 = Integer(2); _sage_const_101 = Integer(101); _sage_const_100 = Integer(100); _sage_const_102 = Integer(102)
import json

def get_coeff(n_shares):
    M = matrix(ZZ, [[x**i for i in range(n_shares)] for x in range(_sage_const_1 , n_shares+_sage_const_1 )])
    coeffs = M.solve_left(vector(ZZ, [_sage_const_1 ] + [_sage_const_0 ]*(n_shares - _sage_const_1 )))
    return coeffs[n_shares-_sage_const_2 ]

def build_M():
    m = []
    for n_shares in range(_sage_const_2 , _sage_const_101 ):
        c = get_coeff(n_shares)
        row = c*vector(ZZ, [(n_shares - _sage_const_1 )**i for i in range(n_shares)] + [_sage_const_0 ]*(_sage_const_100  - n_shares))
        m.append(row)
    c = get_coeff(_sage_const_101 )
    m.append(c*vector(ZZ, [(_sage_const_100 )**i for i in range(_sage_const_100 )]))
    c = get_coeff(_sage_const_102 )
    m.append(c*vector(ZZ, [(_sage_const_101 )**i for i in range(_sage_const_100 )]))

    return matrix(ZZ, m)

M = build_M()
coeffs = M.left_kernel().basis()[_sage_const_0 ]
assert all(x in ZZ for x in coeffs)

with open("coeffs.json", "w") as wf:
    wf.write(json.dumps([int(x) for x in list(coeffs)]))
