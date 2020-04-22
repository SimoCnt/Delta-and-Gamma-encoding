import matplotlib.pyplot as plt
from math import log2, floor
from numpy import binary_repr
import cod_gamma

list_bin = []
list_delta = []
num = []
rapp = []


def insert_n():
    print("Insert a number n >= 1 :")
    n = int(input())

    return n


def create_list(n):
    for i in range(1, n+1):
        n_bin = cod_binary(i)
        n_delta = cod_delta(i, n_bin)

        list_bin.append(n_bin)
        list_delta.append(n_delta)


def cod_binary(x):
    n_bin = binary_repr(x, width=None)

    return n_bin


def cod_delta(N, n_bin):
    N = floor(log2(N))
    #n_bin_gamma = binary_repr(N, width=N+1)
    n_gamma = cod_gamma.cod_gamma_fd(N+1)
    n_delta = ((n_gamma) + n_bin[1:])

    return n_delta


def print_results(n):
    for i in range(n):
        print("\nx: {0}".format(i+1))
        #print("Binary encoding: {0}".format(list_bin[i]))
        print("Delta encoding: {0}".format((list_delta[i])))


def med_lenght_binary(num):
    return (num * (1 + floor(log2(num)))) / num


def med_lenght_delta(num):
    lmd = 0

    for i in range(1, num+1):
        #lmd += ((2 * floor(log2(i)) + 1)) / num
        lmd += ((1 + 2 * floor(log2(floor(log2(i)) + 1))) + floor(log2(i))) / num

    return lmd


def ratio(n):
    for i in range(1, n+1):
        lmb = med_lenght_binary(i)
        lmd = med_lenght_delta(i)

        num.append(i)
        rapp.append(lmd / lmb)

    plt.figure(figsize=(14,10))
    plt.xlabel("x")
    plt.ylabel("delta medium lenght / binary medium lenght")
    plt.plot(num,rapp)
    plt.show()


def exe():
    n = insert_n()
    create_list(n)
    print_results(n)
    ratio(n)
