def hitung_fungsi(x):
    if x == 0:
        return "gagal0, bilangan gaboleh 0"
    return 2 * (x ** 3) + 2 * x + (15 / x)

x = int(input("Masukkan bilangan bulat x: "))

hasil = hitung_fungsi(x)
print(f"Hasil dari f(x) = 2x^3 + 2x + 15/x untuk x = {x} adalah {hasil}")
