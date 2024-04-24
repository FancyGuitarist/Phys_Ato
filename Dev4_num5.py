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

Es = []
for index, value in enumerate(As):
    E = E_z(value, Zs[index])
    Es.append(E)
    print(f'E_z{index+1} = {E}')

E1 = Es[0] + Es[1]
E2 = Es[2] + Es[3]

print(f'E1 = {E1}, E2 = {E2}')