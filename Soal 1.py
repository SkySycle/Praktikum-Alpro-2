def hitung_berat(tinggi, bmi_diharapkan):
    berat = bmi_diharapkan * (tinggi ** 2)
    return berat

tinggi = float(input("Masukkan tinggi badan (dalam meter): "))
bmi_diharapkan = float(input("Masukkan nilai BMI yang diharapkan: "))

berat = hitung_berat(tinggi, bmi_diharapkan)

print(f"Berat badan yang diperlukan untuk mencapai BMI {bmi_diharapkan} adalah {berat:.2f} kg")
