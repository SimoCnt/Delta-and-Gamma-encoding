import cod_gamma
import cod_delta


def menu():
    print("\n\n__Menu__")
    print("1. Gamma encoding")
    print("2. Delta encoding")
    print("0. Exit\n")
    temp = int(input())
    print()
    return temp


c = -1
while c != 0:
    c = menu()
    if c == 0:
        break
    elif c == 1:
        cod_gamma.exe()
    elif c == 2:
        cod_delta.exe()
    else:
        print("Unknown command")
