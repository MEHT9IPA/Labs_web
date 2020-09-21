from math import sqrt
import sys

def Input(line):
    is_error = True
    while is_error:
        is_error = False
        try:
            coeff = int(line)
        except ValueError:
            try:
                coeff = float(line)
            except ValueError:
                is_error = True
                line = input("Некорректный ввод, повторите попытку: ")
    return coeff

def A_Input(arg):
    try:
        coeff = int(arg)
    except ValueError:
        try:
            coeff = float(arg)
        except ValueError:
            coeff = "e"
    return coeff

print("|Аникин Филипп Автандилович, ИУ5-53Б|\n")
A_incorrect = True
if len(sys.argv)>1:
    print("<Режим принятия аргументов из КС>")
    if len(sys.argv) == 4:
        A = A_Input(sys.argv[1])
        B = A_Input(sys.argv[2])
        C = A_Input(sys.argv[3])
        A_incorrect = False
        if A == "e" or B == "e" or C == "e":
            print("*Некорректные аргументы, переход на ручной ввод*")
            A_incorrect = True
    else:
        print("*Некорректное количество аргументов, переход на ручной ввод*")
        A_incorrect = True

if A_incorrect == True:
    print("<Введите коэффициенты биквадратного уравнения>")
    line = input("A = ")
    A = Input(line)
    line = input("B = ")
    B = Input(line)
    line = input("C = ")
    C = Input(line)

print("======================================================")
print("A = ", A, "; B = ", B, "; C = ", C, sep='')

D = B*B - 4*A*C
if D-int(D) == 0:
    D = int(D)
print("Дискриминант =",D)

print("------------------------------------------------------")
if A != 0:
    if D >= 0:
        B = -B
        A = A + A
        D = sqrt(D)
        Q1 = (B+D)/A
        Q2 = (B-D)/A
        if D == 0:
            Q2 = -1
        D = -1

        if Q1 > 0:
            D = 1
            Q1 = sqrt(Q1)
            if Q1-int(Q1) == 0:
                Q1 = int(Q1)
            print("X", D, " = ", Q1, ", X", D+1, " = ", -Q1, sep='')
            D = D + 2
        elif Q1 == 0:
            D = 1
            Q1 = int(Q1)
            print("X", D, " = ", Q1, sep='')
            D = D + 1

        if Q2 >= 0:
            Q2 = sqrt(Q2)
            if Q2-int(Q2) == 0:
                Q2 = int(Q2)
            if D == -1:
                D = 1
            print("X", D, " = ", Q2, ", X", D+1, " = ", -Q2, sep='')
        elif Q2 == 0:
            if D == -1:
                D = 1
            Q2 = int(Q2)
            print("X", D, " = ", Q2, sep='')

        if D == -1:
            print("Действительных корней нет")
    else:
        print("Действительных корней нет")
else:
    if B!= 0:
        Q = -C/B
        if Q >= 0:
            Q = sqrt(Q)
            if Q-int(Q) == 0:
                Q = int(Q)
            print("X1 = ", -Q, ", X2 = ", Q, sep='')
        else:
            print("Действительных корней нет")
    else:
        if C != 0:
            print("Действительных корней нет")
        else:
            print("Решение - любое число")
print("======================================================")