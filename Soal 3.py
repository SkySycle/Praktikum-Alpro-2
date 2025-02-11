gaji_per_jam = float(input("Masukkan gaji per jam yang diinginkan (dalam Rp): "))
jam_per_minggu = int(input("Masukkan jumlah jam kerja per minggu: "))

pendapatan_per_minggu = gaji_per_jam * jam_per_minggu
pendapatan_selama_liburan = pendapatan_per_minggu * 5  
pajak = 0.14

pendapatan_setelah_pajak = pendapatan_selama_liburan * 0.86

baju_dan_aksesoris = pendapatan_setelah_pajak * 0.10
alat_tulis = pendapatan_setelah_pajak * 0.01

sisa_uang_setelah_belanja = pendapatan_setelah_pajak - baju_dan_aksesoris - alat_tulis
uang_disedekahkan = sisa_uang_setelah_belanja * 0.25

uang_untuk_anak_yatim = uang_disedekahkan * 0.30
uang_untuk_kaum_dhuafa = uang_disedekahkan * 0.70

print("\nLaporan Pendapatan dan Pengeluaran:")
print(f"1. Pendapatan Budi selama libur musim panas sebelum pajak: Rp {pendapatan_selama_liburan:,.0f}")
print(f"2. Pendapatan Budi selama libur musim panas setelah pajak: Rp {pendapatan_setelah_pajak:,.0f}")
print(f"3. Jumlah uang yang akan Budi habiskan untuk membeli pakaian dan aksesoris: Rp {baju_dan_aksesoris:,.0f}")
print(f"4. Jumlah uang yang akan Budi habiskan untuk membeli alat tulis: Rp {alat_tulis:,.0f}")
print(f"5. Jumlah uang yang akan Budi sedekahkan: Rp {uang_disedekahkan:,.0f}")
print(f"6. Jumlah uang yang akan diterima anak yatim: Rp {uang_untuk_anak_yatim:,.0f}")
print(f"7. Jumlah uang yang akan diterima kaum dhuafa: Rp {uang_untuk_kaum_dhuafa:,.0f}")
