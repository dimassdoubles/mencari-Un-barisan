from rumus_barisan import *


def main():
    numbers = input("barisan: ").split(" ")
    barisan = [int(num) for num in numbers]

    linier = cek(barisan)
    if linier:
        Un, properti = barisan_linier(barisan)
        print(Un)
        while True:
            n = int(input("Cari suku ke berapa?: "))
            cari_suku_ke(n, properti, linier)
    elif not linier:
        Un, properti = barisan_kuadrat(barisan)
        print(Un)
        while True:
            n = int(input("Cari suku ke berapa?: "))
            cari_suku_ke(n, properti, linier)
    print(Un)


if __name__ == "__main__":
    main()
