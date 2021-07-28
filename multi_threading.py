from concurrent.futures import ThreadPoolExecutor
from tax_c import  tottax_cython
import numpy as np

def threads(incomes):
    with ThreadPoolExecutor(max_workers = 4) as exe:
        sections = np.array_split(incomes, 4)
        jobs = [exe.submit(tottax_cython , s) for s in sections]
    sum(job.result() for job in jobs)




