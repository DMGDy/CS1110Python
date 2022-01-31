: = 50
import math
e = math.e
pi = math.pi
import math
e = math.e
pi = math.pi
rho = 0.002377
b = 53.3
S = 318
W = 19815
#in lbs#
FC = 1119
PP = 3650
SFC = .6
CDp = .02
oswald = 0.81
AR = (b**2)/S
v1 = []
v2 = []
v3 = []
v4 = []
v5 = []
v6 = []
v7 = []
v8 = []
v9 = []
for x in range(19):
    v += 50
    v1.append(v)
    Cl = W / (((rho * v**2) / 2) * S)
    v2.append(Cl)
    Cd = (Cl**2)/(pi*oswald*(b**2/S)) + CDp
    v3.append(Cd)
    LDr = Cl/Cd
    v4.append(LDr)
    Tr = 0.5*rho*(v**2)*S*(CDp+(Cl**2)/(pi*oswald*AR))
    v5.append(Tr)
    Pr = (Tr * v)*550**-1
    v6.append(Pr)
    Pa = (3650 * v)/550
    v7.append(Pa)
    RoC = ((Pa - Pr)*550)/W
    v8.append(RoC)
    Excess = Pa - Pr
    v9.append(Excess)
    if v == 1000:
        break
print(v1)
print(v2)
print(v3)
print(v4)
print(v5)
print(v6)
print(v7)
print(v8)
print(v9)
