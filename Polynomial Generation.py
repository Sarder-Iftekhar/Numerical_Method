import numpy as np
# create as many polynomials as size of coeff_vector
final_pol = np.polynomial.Polynomial([0.]) # our target polynomial
n = coeff_vector.shape[0] # get number of coeffs
for i in range(n):
    p = np.polynomial.Polynomial([1.]) # create a dummy polynomial
    for j in range(i):
        # each vector has degree of i
        # their terms are dependant on 'x' values
        p_temp = np.polynomial.Polynomial([-x[j], 1.]) # (x - x_j)
        p = np.polymul(p, p_temp) # multiply dummy with expression
    p *= coeff_vector[i] # apply coefficient
    final_pol = np.polyadd(final_pol, p) # add to target polynomial

p = np.flip(final_pol[0].coef, axis=0)
print(p)