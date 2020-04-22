import matplotlib.pyplot as plt
from math import log2, floor
from numpy import binary_repr

list_bin = []
list_gamma = []
num = []
rapp = []


def insert_n():
    print("Insert a number n >= 1 :")
    n = int(input())

    return n


def create_list(n):
    for i in range(1, n+1):
        n_bin = cod_binary(i)
        n_gamma = cod_gamma(i, n_bin)

        list_bin.append(n_bin)
        list_gamma.append(n_gamma)


def cod_binary(x):
    n_bin = binary_repr(x, width=None)

    return n_bin


def cod_gamma(N, n_bin):
    N = floor(log2(N))
    n_gamma = ('0' * N) + n_bin

    return n_gamma


def cod_gamma_fd(n):
    N = floor(log2(n))
    n_bin = binary_repr(n,width=N+1)
    n_gamma = ('0' * N) + n_bin

    return n_gamma


def print_results(n):
    for i in range(n):
        print("\nx: {0}".format(i+1))
        #print("Binary encoding: {0}".format(list_bin[i]))
        print("Gamma encoding: {0}".format((list_gamma[i])))


def med_lenght_binary(num):
    return (num * (1 + floor(log2(num)))) / num


def med_lenght_gamma(num):
    lmg = 0

    for i in range(1, num+1):
        lmg += ((2 * floor(log2(i)) + 1)) / num

    return lmg


def ratio(n):
    for i in range(1, n+1):
        lmb = med_lenght_binary(i)
        lmg = med_lenght_gamma(i)

        num.append(i)
        rapp.append(lmg / lmb)

    plt.figure(figsize=(14,10))
    plt.xlabel("x")
    plt.ylabel("gamma medium lenght / binary medium lenght")
    plt.plot(num,rapp)
    plt.show()


def exe():
    n = insert_n()
    create_list(n)
    print_results(n)
    ratio(n)
