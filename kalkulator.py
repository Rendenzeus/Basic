def kalkulator():
    try:
        ekspresi = input("Masukkan ekspresi matematika: ")
        hasil = eval(ekspresi)
        print("Hasil:", hasil)
    except Exception as e:
        print("Terjadi kesalahan:", e)

# Panggil fungsi kalkulator
kalkulator()