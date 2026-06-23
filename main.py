import math

def function(x):
    return math.log10(x + 5) - math.cos(x)

def bisection(a, b, tochnost=0.01):
    if function(a) * function(b) >= 0:
        return None
    while (b - a) / 2 > tochnost:
        mid = (a + b) / 2
        if function(mid) == 0:
            return mid
        elif function(a) * function(mid) < 0:
            b = mid
        else:
            a = mid
    return (a + b) / 2
def secushaya(x0, x1, tochnost=0.01):
    while abs(x1 - x0) > tochnost:
        if function(x1) - function(x0) == 0:
            break
        x_next = x1 - function(x1) * (x1 - x0) / (function(x1) - function(x0))
        x0, x1 = x1, x_next
    return x1

a, b = 0, 1
root_bisect = bisection(a, b)
root_secant = secushaya(a, b)
print(f"Root by bisection method: {root_bisect:.3f}")
print(f"Root by secant method: {root_secant:.3f}")



import numpy as np

A = np.array([
    [-0.2, 1.6, -0.1],
    [-0.3, 0.1, -1.5],
    [1.2, -0.2, 0.3]
], dtype=float)

B = np.array([0.3, 0.4, -0.6], dtype=float)
def gauss_method(A, B):
    n = len(B)
    M = np.hstack([A, B.reshape(-1, 1)])
    
    for i in range(n):
        pivot = i + np.argmax(abs(M[i:, i]))
        M[[i, pivot]] = M[[pivot, i]]
        M[i] = M[i] / M[i, i]
        for j in range(i + 1, n):
            M[j] -= M[j, i] * M[i]
    x = np.zeros(n)
    for i in range(n - 1, -1, -1):
        x[i] = M[i, -1] - np.sum(M[i, i+1:n] * x[i+1:n])
    return x
solution = gauss_method(A, B)

print("Solution of the system (Gauss method):")
print(f"x1 = {solution[0]:.3f}, x2 = {solution[1]:.3f}, x3 = {solution[2]:.3f}")