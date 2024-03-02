def jumlah_bilangan_ganjil(batas_bawah, batas_atas):
    if batas_bawah < 0 or batas_atas < 0:
        return None

    jumlah_ganjil = 0
    bilangan_ganjil = []
    for i in range(batas_bawah, batas_atas):
        if i % 2 != 0:
            bilangan_ganjil.append(i)
            jumlah_ganjil += i

    return jumlah_ganjil, bilangan_ganjil

batas_bawah = int(input("Batas bawah: "))
batas_atas = int(input("Batas atas: "))
hasil_jumlah, bilangan_ganjil = jumlah_bilangan_ganjil(batas_bawah, batas_atas)

if hasil_jumlah is not None:
    print("Bilangan ganjil antara", batas_bawah, "dan", batas_atas, "adalah:")
    for bilangan in bilangan_ganjil:
        print(bilangan)
    print("Jumlahnya adalah:", hasil_jumlah)
else:
    print("Batas bawah dan atas yang dimasukkan tidak boleh di bawah nol.")
