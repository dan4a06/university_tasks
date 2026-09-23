from sympy import symbols, Eq, solve


x1, x2, x3, x4 = symbols('x1 x2 x3 x4')


systems_3var = {
    1: [
        Eq(x1 - 2*x2 + 4*x3, 1),
        Eq(-x1 + 3*x2 - 2*x3, 3),
        Eq(2*x1 - 4*x2 + x3, -5)
    ],
    2: [
        Eq(-2*x1 + 3*x2 - 5*x3, 3),
        Eq(x1 + 2*x2 - 3*x3, 0),
        Eq(3*x1 - x2 + 4*x3, -1)
    ],
    3: [
        Eq(2*x1 - x2 - x3, 4),
        Eq(3*x1 + 4*x2 - 2*x3, 11),
        Eq(3*x1 - 2*x2 + 4*x3, 11)
    ],
    4: [
        Eq(x1 + x2 + 2*x3, -1),
        Eq(2*x1 - x2 + 2*x3, -4),
        Eq(4*x1 + x2 + 4*x3, -2)
    ],
    5: [
        Eq(3*x1 + 2*x2 + x3, 5),
        Eq(2*x1 + 3*x2 + x3, 1),
        Eq(2*x1 + x2 + 3*x3, 11)
    ],
    6: [
        Eq(x1 + 2*x2 + 4*x3, 31),
        Eq(5*x1 + x2 + 2*x3, 29),
        Eq(3*x1 - x2 + x3, 10)
    ],
    7: [
        Eq(2*x1 + 2*x2 + 3*x3, 13),
        Eq(x1 - x2, -1),
        Eq(-x1 + 2*x2 + x3, 5)
    ],
    8: [
        Eq(3*x1 - x2 + x3, 0),
        Eq(-x1 + 3*x2 - 4*x3, -1),
        Eq(2*x1 - 3*x2 + 5*x3, 2)
    ],
    9: [
        Eq(x1 + 2*x2 + x3, 8),
        Eq(4*x1 + 3*x2 - 2*x3, 4),
        Eq(-x1 - 2*x2 + x3, -2)
    ],
    10: [
        Eq(-x1 + 4*x2 - 2*x3, 1),
        Eq(2*x1 - x2 + 3*x3, 4),
        Eq(-x1 - 2*x2 + 4*x3, 1)
    ],
    11: [
        Eq(3*x1 - x2 + x3, -8),
        Eq(5*x1 + x2 + 2*x3, -9),
        Eq(x1 + 2*x2 + 4*x3, -9)
    ],
    12: [
        Eq(2*x1 - x2 + 2*x3, 6),
        Eq(4*x1 + x2 + 4*x3, 18),
        Eq(x1 + x2 - 2*x3, 3)
    ],
    13: [
        Eq(3*x1 - 2*x2 + 4*x3, 11),
        Eq(2*x1 - x2 - x3, 3),
        Eq(3*x1 + x2 - 2*x3, -7)
    ],
    14: [
        Eq(2*x1 + 2*x2 + x3, 4),
        Eq(3*x1 + 2*x2 + x3, 5),
        Eq(2*x1 + x2 + 3*x3, -2)
    ],
    15: [
        Eq(2*x1 + x2 - x3, -1),
        Eq(x1 + 5*x2 + 3*x3, -7),
        Eq(4*x1 + 2*x2 + x3, 0)
    ],
    16: [
        Eq(2*x1 + 3*x2 + 4*x3, 13),
        Eq(3*x1 + x2 + x3, -1),
        Eq(x1 - 5*x2 - 7*x3, -31)
    ],
    17: [
        Eq(4*x1 + 5*x2 + 8*x3, 6),
        Eq(x1 + 3*x2 + x3, 6)
    ],
    18: [
        Eq(x1 - 3*x2 + x3, -6),
        Eq(3*x1 + 3*x2 - x3, 2)
    ],
    19: [
        Eq(3*x1 + 3*x2 + 2*x3, 17),
        Eq(2*x1 - x2 + 3*x3, 7),
        Eq(2*x1 + 5*x2 + x3, 17)
    ],
    20: [
        Eq(2*x1 - x2 + 3*x3, 13),
        Eq(2*x1 + 3*x2 + 2*x3, -1),
        Eq(3*x1 - x2 - x3, 7)
    ],
    21: [
        Eq(2*x1 + 3*x2 + 5*x3, 15),
        Eq(5*x1 + 7*x2 + 6*x3, 24),
        Eq(x1 + x2 - 2*x3, -2)
    ],
    22: [
        Eq(x1 + 2*x2 + 3*x3, 11),
        Eq(2*x1 + x2 + 2*x3, 11),
        Eq(3*x1 + 2*x2 + x3, 11)
    ],
    23: [
        Eq(x1 + 3*x2 + 5*x3, 0),
        Eq(3*x1 + x2 + x3, -6),
        Eq(5*x1 + x2 + 3*x3, -8)
    ],
    24: [
        Eq(3*x1 + 2*x2 + x3, 9),
        Eq(x1 + 3*x2 + 4*x3, 14),
        Eq(4*x1 - 5*x2 - x3, -12)
    ],
    25: [
        Eq(3*x1 + 5*x2 + x3, -6),
        Eq(5*x1 + x2 + 3*x3, 6),
        Eq(x1 + 3*x2 + 5*x3, 0)
    ],
    26: [
        Eq(x1 + 2*x2 + 3*x3, -2),
        Eq(3*x1 + 2*x2 + x3, -2),
        Eq(4*x1 + 3*x2 + 2*x3, -4)
    ],
    27: [
        Eq(2*x1 + 5*x2 - 4*x3, 1),
        Eq(-x1 + 3*x2 - 2*x3, -3),
        Eq(3*x1 - 2*x2 + 4*x3, 12)
    ],
    28: [
        Eq(4*x1 + 3*x2 - x3, 12),
        Eq(2*x1 - 7*x2 + 3*x3, 8),
        Eq(3*x1 - 2*x2 + 4*x3, 19)
    ],
    29: [
        Eq(5*x1 - 2*x2 - 3*x3, -3),
        Eq(2*x1 + 3*x2 - 2*x3, 1),
        Eq(x1 + 4*x2 + 5*x3, 15)
    ],
    30: [
        Eq(2*x1 - 8*x2 + 3*x3, -7),
        Eq(-3*x1 + 4*x2 - x3, 9),
        Eq(2*x1 - x2 + 7*x3, 4)
    ]
}

systems_4var = {
    1: [
        Eq(x1 + x2 + 2*x3 + x4, 0),
        Eq(4*x1 + 5*x2 + 8*x3 + 5*x4, 1),
        Eq(x1 + 3*x2 + x3 + 3*x4, 3),
        Eq(2*x1 + 5*x2 + 5*x3 + x4, -2)
    ],
    2: [
        Eq(2*x1 + 3*x2 + 3*x3 + 3*x4, 0),
        Eq(x1 - 3*x2 + x3 + x4, -4),
        Eq(3*x1 + 3*x2 - x3 + 3*x4, -2),
        Eq(2*x1 + 2*x2 + 2*x3 - x4, 0)
    ],
    3: [
        Eq(3*x1 + 3*x2 + 3*x3 + 2*x4, 2),
        Eq(2*x1 - x2 + 3*x3 + 2*x4, -2),
        Eq(2*x1 + 5*x2 + x3 + x4, 5),
        Eq(x1 + x2 + x3 + x4, 1)
    ],
    4: [
        Eq(2*x1 - x2 + 3*x3 + 2*x4, -2),
        Eq(2*x1 + 3*x2 + 3*x3 + 2*x4, 2),
        Eq(3*x1 - x2 - x3 + 2*x4, 2),
        Eq(3*x1 - x2 + 3*x3 - x4, -5)
    ],
    5: [
        Eq(2*x1 + 3*x2 + 5*x3 + 4*x4, -3),
        Eq(5*x1 + 7*x2 + 9*x3 + 6*x4, -4),
        Eq(x1 + x2 + 2*x3 + x4, -1),
        Eq(2*x1 + 3*x2 + 2*x3 + x4, 0)
    ],
    6: [
        Eq(x1 + 2*x2 + 3*x3 + 4*x4, -3),
        Eq(2*x1 + x2 + 2*x3 + 3*x4, -1),
        Eq(3*x1 + 2*x2 + x3 + 2*x4, 1),
        Eq(4*x1 + 3*x2 + 2*x3 + x4, 3)
    ],
    7: [
        Eq(x1 + 3*x2 + 5*x3 + x4, -1),
        Eq(3*x1 + 5*x2 + x3 + x4, 7),
        Eq(5*x1 + x2 + x3 + 3*x4, 5),
        Eq(7*x1 + 7*x2 + 11*x3 + 5*x4, 3)
    ],
    8: [
        Eq(4*x1 + 3*x2 + 2*x3 + x4, 5),
        Eq(x1 + 2*x2 + 3*x3 + 4*x4, 0),
        Eq(3*x1 + 2*x2 + x3 + 2*x4, 2),
        Eq(6*x1 + 7*x2 + 8*x3 + 9*x4, 5)
    ],
    9: [
        Eq(2*x1 + x2 + x3 + x4, 4),
        Eq(x1 + 2*x2 - x3 + 2*x4, 2),
        Eq(x1 + x2 + 4*x3 + x4, 6),
        Eq(x1 + x2 + x3 + x4, 1)
    ],
    10: [
        Eq(2*x1 + 2*x2 - x3 + x4, -1),
        Eq(4*x1 + 3*x2 - x3 + 2*x4, -3),
        Eq(8*x1 + 5*x2 - 3*x3 + 4*x4, -7),
        Eq(3*x1 + 3*x2 - 2*x3 + 2*x4, -2)
    ],
    11: [
        Eq(2*x1 + 3*x2 + 11*x3 + 5*x4, -1),
        Eq(x1 + x2 + 5*x3 + 2*x4, -1),
        Eq(2*x1 + x2 + 3*x3 + 2*x4, 2),
        Eq(x1 + x2 + 3*x3 + 4*x4, 3)
    ],
    12: [
        Eq(2*x1 + 5*x2 + 4*x3 + x4, 6),
        Eq(x1 + 2*x2 + 2*x3 + x4, 3),
        Eq(2*x1 + 10*x2 + 9*x3 + 7*x4, 5),
        Eq(3*x1 + 8*x2 + 9*x3 + 2*x4, 9)
    ]
}


def solve_system(equations, variables):
    solution = solve(equations, variables)
    return solution


print("="*80)
print("СИСТЕМЫ С ТРЕМЯ ПЕРЕМЕННЫМИ (x1, x2, x3)")
print("="*80)

for num, system in sorted(systems_3var.items()):
    print(f"\nСистема {num}:")
    for eq in system:
        print(f"  {eq}")
    solution = solve_system(system, (x1, x2, x3))
    print(f"Решение: {solution}")
    print("-"*80)


print("\n" + "="*80)
print("СИСТЕМЫ С ЧЕТЫРЬМЯ ПЕРЕМЕННЫМИ (x1, x2, x3, x4)")
print("="*80)

for num, system in sorted(systems_4var.items()):
    print(f"\nСистема {num}:")
    for eq in system:
        print(f"  {eq}")
    solution = solve_system(system, (x1, x2, x3, x4))
    print(f"Решение: {solution}")
    print("-"*80)