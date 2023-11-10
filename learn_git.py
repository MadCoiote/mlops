# -*- coding: utf-8 -*-
"""
Created on Fri Nov 10 05:24:56 2023

@author: herna
"""
import numpy as np


"Step 1: Create intendend matrix"
A = np.array([[1,2,3],[3,2,1],[0,5,0]])
print("Matriz de avaliação: \n{}".format(A))
n,m = A.shape
assert n==m, "Only works for square matrices"

"Create the identity matrix"
I = np.identity(A.shape[0])

"Compute the determinant"

