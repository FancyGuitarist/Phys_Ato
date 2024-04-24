import numpy as np
import scipy.constants as sp

cores = ['Th_232', 'Ra_228', 'Ac_228', 'Th_228', 'Ra_224', 'Rn_220', 'Po_216', 'Pb_212']
halves = [(1.405*10**10)*(365*24*60*60), 5.573*(365*24*60*60), 6.132*(60*60), 1.912*(365*24*60*60), 3.623*(24*60*60), 55.6, 145*10**(-3), 10.64*(60*60)]


def R(half):
    return np.log(2)/half


def N_mass(mass, numb):
    return (mass/numb)*sp.N_A


def N(R1, N1, R2):
    return R1*N1/R2


m = 1*10**(-6)
N_Th232 = N_mass(m, 232)
R_Th232 = R(halves[0])

Ns = [N_Th232]
masses = [m]
for index, value in enumerate(halves):
    if index < 1:
        print(f'{cores[index]} : m = {m:.3E}, N = {N_Th232:.3E}, R = {R_Th232:.3E}')
        continue
    else:
        N2 = N(R(halves[index-1]), Ns[index-1], R(halves[index]))
        if N2 < 1:
            M = int(cores[index][3::])
            mass = N2 * M / sp.N_A
            masses.append(mass)
            Ns.append(N2)
            print(f'{cores[index]} : m = {mass:.3E}, N = {0}        , R = {R(halves[index]):.3E}')
        else:
            Ns.append(N2)
            M = int(cores[index][3::])
            mass = N2*M/sp.N_A
            masses.append(mass)
            print(f'{cores[index]} : m = {mass:.3E}, N = {Ns[index]:.3E}, R = {R(halves[index]):.3E}')

