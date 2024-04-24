a_v = 15.75
a_s = 17.80
a_c = 0.711
a_A = 94.78
a_p = 11.18

As = [219, 4, 209, 14]
Zs = [86, 2, 82, 6]

def E_z(A, Z):
    e_z = a_v*A - a_s*A**(2/3) - a_c*(Z**2)/A**(1/3) - a_A*((Z - A/2)**2)/A + a_p*(((-1)**Z + (-1)**(A-Z))/(2*A**(0.5)))
    return e_z
print(f'E_Ra = {E_z(223, 88)} MeV')
Es = []
for index, value in enumerate(As):
    E = E_z(value, Zs[index])
    Es.append(E)
    print(f'E_z{index+1} = {E}')

E1 = Es[0] + Es[1]
E2 = Es[2] + Es[3]

print(f'E1 = {E1}, E2 = {E2}')

As_alph = [286, 4]
Zs_alph = [104, 2]
A_beta = 290
Zs_beta = [107, 105]

E_tot_alph = 0
E_tot_beta_min = E_z(A_beta, Zs_beta[0])
E_tot_beta_max = E_z(A_beta, Zs_beta[1])
for index, value in enumerate(As_alph):
    E_tot_alph += E_z(value, Zs_alph[index])/value

E_tot_alph = E_z(As_alph[0], Zs_alph[0])/As_alph[0]

print(f'E_tot alpha = {E_tot_alph}MeV/A, E_tot beta- = {E_tot_beta_min/A_beta}MeV/A, E_tot beta+ = {E_tot_beta_max/A_beta}MeV/A')

