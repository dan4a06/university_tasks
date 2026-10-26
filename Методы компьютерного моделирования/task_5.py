from sympy import*
n = symbols('n')
x = symbols('x')

# Задание 1
#1 
print("1.1)", limit((4*n**5 + 3 * n**3 - 1)/(3*n**5 + 14*n**2 + 5*n), n, oo))
#2 
print("1.2)", limit((2*n**4 - 6 * n**2 - 1)/(n**4 + 11*n + 3), n, oo))
#3 
print("1.3)", limit((3*n**6 + 5 * n**2 + 9*n)/(4*n**6 + n**2 - 2*n), n, oo))
#4 
print("1.4)", limit((3*n**4 + n**3 - 5*n)/((2*n**2 + 5)**2), n, oo))
#5 
print("1.5)", limit((5*n**4 + 3*n**2 - 2)/((2*n**2 + 3)**2), n, oo))
#6 
print("1.6)", limit((3*n**6 + 2*n**2 - 7*n)/((4*n**2 + n)**3), n, oo))
#7 
print("1.7)", limit((3*n**2 + n - 1)/(5*n**2 + 14*n + 5), n, oo))
#8 
print("1.8)", limit((5*n**3 - 6 * n - 4)/(n**3 + 11*n + 1), n, oo))
#9 
print("1.9)", limit((n**6 + 4 * n**2 - 7*n)/(4*n**6 + n**2 - n), n, oo))
#10 
print("1.10)", limit((3*n**4 + 5*n**3 - 2)/((2*n + 5)**4), n, oo))
#11 
print("1.11)", limit(((2*n**2 + 3)**2)/(3*n**4 - 3), n, oo))
#12 
print("1.12)", limit(((5*n**2 + 2*n)**2)/(4*n**4 + n - 15), n, oo))
#13 
print("1.13)", limit((n**4 + 2*n**3 - 3)/((2*n - 1)**4), n, oo))
#14 
print("1.14)", limit(((2*n**2 + 3)**3)/(3*n**6 - n*2 + 2), n, oo))
#15 
print("1.15)", limit(((5*n**4 + 2*n)**2)/(4*n**8 + n**3 - 10), n, oo))
#16 
print("1.16)", limit((5*n**4 - n**3 + 9)/((2*n - 3)**4), n, oo))
#17 
print("1.17)", limit(((2*n**2 + 3)**2)/(3*n**4 - 3), n, oo))
#18 
print("1.18)", limit(((5*n**3 - 4*n)**2)/(3*n**6 + 2*n - 14), n, oo))
#19 
print("1.19)", limit((3*n**10 + 5*n**3 - 14)/((2*n**5 - 3*n**2 + 1)**2), n, oo))
#20 
print("1.20)", limit(((2*n**4 + 3)**3)/(3*n**12 - n**7 + 2*n**2), n, oo))
#21 
print("1.21)", limit(((2*n**2 + 2*n)**4)/(4*n**8 + 3*n**3 - 1), n, oo))
#22 
print("1.22)", limit((3*n**2 + 5*n - 2)/(11*n**2 + 8*n - 5), n, oo))
#23 
print("1.23)", limit((6*n**3 - 5*n + 4)/(2*n**3 + 11*n - 7), n, oo))
#24 
print("1.24)", limit((n**7 + 9*n**2 - 4*n)/(5*n**7 + n**2 - n), n, oo))
#25 
print("1.25)", limit((3*n**4 - n**3 + 4)/((3*n + 1)**4), n, oo))
#26 
print("1.26)", limit(((2*n**2 + 7)**4)/(3*n**8 - 5), n, oo))
#27 
print("1.27)", limit(((5*n**2 + 2*n)**3)/(4*n**6 + 3*n - 15), n, oo))
#28 
print("1.28)", limit((3*n**5 + n - 1)/(7*n**5 + 14*n + 5), n, oo))
#29 
print("1.29)", limit((5*n**3 - 6*n + 3)/(2*n**3 + 11*n + 1), n, oo))
#30 
print("1.30)", limit((2*n**6 + 3*n**2 - 7*n)/(11*n**6 + 2*n**2 - n), n, oo))

print('Задание 2')
#1 
print("2.1)", limit((3*n**5 + 5*n**3 - 2)/((2*n + 5)**4), n, oo))
#2 
print("2.2)", limit(((2*n**2 + 3)**3)/(3*n**4 - 3), n, oo))
#3 
print("2.3)", limit(((5*n**3 + 2*n)**2)/(4*n**4 + n - 15), n, oo))
#4 
print("2.4)", limit((n**6 + 2*n**3 - 3)/((2*n - 1)**4), n, oo))
#5 
print("2.5)", limit(((2*n**3 + 3)**3)/(3*n**6 - n**2 + 2), n, oo))
#6 
print("2.6)", limit(((5*n**4 + 2*n)**2)/(4*n**7 + n**3 - 10), n, oo))
#7 
print("2.7)", limit((4*n**5 + 3*n**3 - 1)/(3*n**4 + 10*n**2 + 5*n), n, oo))
#8 
print("2.8)", limit((2*n**4 - 6*n**2 - 1)/(n**3 + 11*n + 3), n, oo))
#9 
print("2.9)", limit((3*n**6 + 5*n**2 + 9*n)/(4*n**3 + n**2 - 2*n), n, oo))
#10 
print("2.10)", limit((5*n**6 - n**3 + 9)/((2*n - 3)**4), n, oo))
#11 
print("2.11)", limit(((2*n**2 + 3)**2)/(3*n**3 - 3), n, oo))
#12 
print("2.12)", limit(((5*n**3 - 4*n)**2)/(3*n**5 + 2*n - 14), n, oo))

print('Задание 4')
#1 
print("4.1)", limit(6/(x**2 - 9) - 1/(x - 3), x, 3))
#2 
print("4.2)", limit(8/(x**2 - 16) - 1/(x - 4), x, 4))
#3 
print("4.3)", limit(12/(x**2 - 36) - 1/(x - 6), x, 6))
#4 
print("4.4)", limit(16/(x**2 - 64) - 1/(x - 8), x, 8))
#5 
print("4.5)", limit(10/(x**2 - 25) - 1/(x - 5), x, 5))
#6 
print("4.6)", limit(18/(x**2 - 81) - 1/(x - 9), x, 9))
#7 
print("4.7)", limit(6/(4*x**2 - 9) - 1/(2*x - 3), x, Rational(3, 2)))
#8 
print("4.8)", limit(2/(4*x**2 - 1) - 1/(2*x - 1), x, Rational(1, 2)))
#9 
print("4.9)", limit(8/(9*x**2 - 16) - 1/(3*x - 4), x, Rational(4, 3)))
#10 
print("4.10)", limit(4/(9*x**2 - 4) - 1/(3*x - 2), x, Rational(2, 3)))
#11 
print("4.11)", limit(10/(4*x**2 - 25) - 1/(2*x - 5), x, Rational(5, 2)))
#12 
print("4.12)", limit(10/(9*x**2 - 25) - 1/(3*x - 5), x, Rational(5, 3)))
#13 
print("4.13)", limit(16/(9*x**2 - 64) - 1/(3*x - 8), x, Rational(8, 3)))
#14 
print("4.14)", limit(10/(64*x**2 - 25) - 1/(8*x - 5), x, Rational(5, 8)))
#15 
print("4.15)", limit(6/(64*x**2 - 9) - 1/(8*x - 3), x, Rational(3, 8)))
#16 
print("4.16)", limit(2/(64*x**2 - 1) - 1/(8*x - 1), x, Rational(1, 8)))
#17 
print("4.17)", limit(2/(9*x**2 - 1) - 1/(3*x - 1), x, Rational(1, 3)))
#18 
print("4.18)", limit(2/(25*x**2 - 1) - 1/(5*x - 1), x, Rational(1, 5)))
#19 
print("4.19)", limit(4/(25*x**2 - 4) - 1/(5*x - 2), x, Rational(2, 5)))
#20 
print("4.20)", limit(6/(25*x**2 - 9) - 1/(5*x - 3), x, Rational(3, 5)))
#21 
print("4.21)", limit(8/(25*x**2 - 16) - 1/(5*x - 4), x, Rational(4, 5)))
#22 
print("4.22)", limit(14/(25*x**2 - 49) - 1/(5*x - 7), x, Rational(7, 5)))
#23 
print("4.23)", limit(16/(25*x**2 - 64) - 1/(5*x - 8), x, Rational(8, 5)))
#24 
print("4.24)", limit(18/(25*x**2 - 81) - 1/(5*x - 9), x, Rational(9, 5)))
#25 
print("4.25)", limit(14/(9*x**2 - 49) - 1/(3*x - 7), x, Rational(7, 3)))
#26 
print("4.26)", limit(6/(16*x**2 - 9) - 1/(4*x - 3), x, Rational(3, 4)))
#27 
print("4.27)", limit(10/(16*x**2 - 25) - 1/(4*x - 5), x, Rational(5, 4)))
#28 
print("4.28)", limit(10/(81*x**2 - 25) - 1/(9*x - 5), x, Rational(5, 9)))
#29 
print("4.29)", limit(8/(81*x**2 - 16) - 1/(9*x - 4), x, Rational(4, 9)))
#30 
print("4.30)", limit(14/(81*x**2 - 49) - 1/(9*x - 7), x, Rational(7, 9)))

print('Задание 5')
#1 
print("5.1)", limit((x + 2)/(sqrt(6 + x) - 2), x, -2))
#2 
print("5.2)", limit((x + 3)/(sqrt(12 + x) - 3), x, -3))
#3 
print("5.3)", limit((x + 1)/(sqrt(10 + x) - 3), x, -1))
#4 
print("5.4)", limit((sqrt(4 + x + x**2) - 2)/(x + 1), x, -1))
#5 
print("5.5)", limit((sqrt(1 + 2*x) - 3)/(sqrt(x) - 2), x, 4))
#6 
print("5.6)", limit((sqrt(1 + x + x**2) - sqrt(7 + 2*x - x**2))/(x**2 - 2*x), x, 2))
#7 
print("5.7)", limit((sqrt(2 - x) - 1)/(x - 1), x, 1))
#8 
print("5.8)", limit((sqrt(1 - x) - 3)/(x + 8), x, -8))
#9 
print("5.9)", limit((sqrt(1 + x + x**2) - sqrt(1 - x + x**2))/(x**2 - x), x, 0))
#10 
print("5.10)", limit((x - 1)/(sqrt(10 - x) - 3), x, 1))
#11 
print("5.11)", limit((sqrt(3 + 2*x) - 3)/(x - 3), x, 3))
#12 
print("5.12)", limit((cbrt(2*x - 1) - cbrt(3*x - 2))/(x - 1), x, 1))
#13 
print("5.13)", limit((sqrt(2 + x) - 2)/(x - 2), x, 2))
#14 
print("5.14)", limit((x + 4)/(sqrt(5 - x) - 3), x, -4))
#15 
print("5.15)", limit((sqrt(x + 6) - sqrt(10*x - 21))/(5*x - 15), x, 3))
#16 
print("5.16)", limit((x - 2)/(sqrt(11 - x) - 3), x, 2))
#17 
print("5.17)", limit((x**2 + x - 2)/(sqrt(2 - x) - 1), x, 1))
#18 
print("5.18)", limit((x + 3)/(sqrt(6 - x) - 3), x, -3))
#19 
print("5.19)", limit((sqrt(x**2 + 5) - 3)/(x - 2), x, 2))
#20 
print("5.20)", limit((x - 6)/(2 - sqrt(x - 2)), x, 6))
#21 
print("5.21)", limit((x**2 - 2*x - 3)/(sqrt(x + 1) - 2), x, 3))
#22 
print("5.22)", limit((cbrt(5*x + 2) - 3)/(x - 5), x, 5))
#23 
print("5.23)", limit((x**2 + x - 2)/(sqrt(x + 6) - 2), x, -2))
#24 
print("5.24)", limit((sqrt(x + 1) - sqrt(3*x - 5))/(x - 3), x, 3))
#25 
print("5.25)", limit((x - 5)/(1 - sqrt(x - 4)), x, 5))
#26 
print("5.26)", limit((sqrt(x + 5) - 4)/(x - 11), x, 11))
#27 
print("5.27)", limit((x**2 - 2*x - 3)/(sqrt(3 - x) - 2), x, -1))
#28 
print("5.28)", limit((sqrt(x + 1) - 3)/(x - 8), x, 8))
#29 
print("5.29)", limit((sqrt(3 + x) - 3)/(x - 6), x, 6))
#30 
print("5.30)", limit((x**2 + x - 2)/(sqrt(x + 6) - 2), x, -2))

print('Задание 6')

#1
print("6.1)", limit(sqrt(x**2 - 7) - sqrt(x**2 + 5), x, oo))
#2
print("6.2)", limit(sqrt(x**2 + 16) - x, x, oo))
#3
print("6.3)", limit(sqrt(x**2 + x + 3) - sqrt(x**2 - 3*x + 1), x, oo))
#4
print("6.4)", limit(sqrt(1 + x**2) - x, x, oo))
#5
print("6.5)", limit(sqrt(x**2 + 9) + x, x, oo))
#6
print("6.6)", limit(sqrt(x**2 + 4) - sqrt(x**2 + 1), x, oo))
#7
print("6.7)", limit(sqrt(x**2 + 4*x) - x, x, oo))
#8
print("6.8)", limit(sqrt(x**2 - 5*x + 6) - x, x, oo))
#9
print("6.9)", limit(sqrt(x**2 + 8*x - 3) - sqrt(x**2 + 4*x + 3), x, oo))
#10
print("6.10)", limit(sqrt(x + 2) - sqrt(x), x, oo))
#11
print("6.11)", limit(sqrt(4*x**2 - 3*x + 11) - 6*x, x, oo))
#12
print("6.12)", limit(sqrt(9*x**2 + 2*x) - sqrt(x**2 + 3*x + 1), x, oo))
#13
print("6.13)", limit(sqrt(9*x**2 + x) - 3*x, x, oo))
#14
print("6.14)", limit(sqrt(8*x**2 - 5*x + 1) - 3*x, x, oo))
#15
print("6.15)", limit(cbrt(x + 1) - cbrt(x), x, oo))
#16
print("6.16)", limit(sqrt(5*x**2 - 7*x) - 2*x, x, oo))
#17
print("6.17)", limit(sqrt(x**2 - 8*x) - sqrt(x**2 - 2), x, oo))
#18
print("6.18)", limit(sqrt(16*x**2 - 3*x) - sqrt(x**2 + 5), x, oo))
#19
print("6.19)", limit(sqrt(5*x + 6) - sqrt(x - 1), x, oo))
#20
print("6.20)", limit(cbrt(4*x + 1) - cbrt(3*x), x, oo))
#21
print("6.21)", limit(sqrt(3*x**2 + 7*x) - sqrt(x**2 + 13), x, oo))
#22
print("6.22)", limit(cbrt(6*x + 1) - cbrt(2*x), x, oo))
#23
print("6.23)", limit(sqrt(10*x**2 - x + 6) - 3*x, x, oo))
#24
print("6.24)", limit(sqrt(5*x**2 + 8*x - 1) - sqrt(2*x**2 + 3*x), x, oo))
#25
print("6.25)", limit(sqrt(3*x**2 - x + 2) - 2*x, x, oo))
#26
print("6.26)", limit(sqrt(7*x + 5) - sqrt(2*x - 3), x, oo))
#27
print("6.27)", limit(sqrt(12*x**2 - 3) - sqrt(2*x**2 + 5*x + 4), x, oo))
#28
print("6.28)", limit(sqrt(6*x**2 - 2*x + 5) - 2*x, x, oo))
#29
print("6.29)", limit(sqrt(11*x**2 + 2*x - 1) - 3*x, x, oo))
#30
print("6.30)", limit(sqrt(8*x**2 + 3*x) - sqrt(3*x**2 - 9*x), x, oo))