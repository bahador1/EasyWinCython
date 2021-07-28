
cpdef double tax_cython(double amount ):#
    if amount <= 18200:
        return 0
    elif amount <= 37000:
        return 0.19 * (amount - 18200)
    elif amount <= 80000:
        return 3572 + 0.325 * (amount - 37000)
    elif amount <= 180000:
        return 17547 + 0.37 * (amount - 80000)
    else:
        return 54547 + 0.45 * (amount - 180000)

cpdef double tottax_cython(double[:] incomes):
    cdef int i
    cdef int n = incomes.shape[0]
    cdef double tot = 0
    for i in range(n):
        tot += tax_cython(incomes[i])
    return tot
