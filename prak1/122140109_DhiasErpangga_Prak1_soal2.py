pi = 3.14

def luas_lingkaran(jari_jari):
    return pi * jari_jari ** 2

def keliling_lingkaran(jari_jari):
    return 2 * pi * jari_jari

def hitung_lingkaran():
    jari_jari = int(input("Masukkan jari-jari lingkaran: "))
    if jari_jari < 0:
        print("Jari-jari lingkaran tidak boleh negatif")
        return None
    else:
        lingkaran = {
            "jari_jari": jari_jari,
            "luas": luas_lingkaran(jari_jari),
            "keliling": keliling_lingkaran(jari_jari)
        }
        return lingkaran

lingkaran_info = hitung_lingkaran()

if lingkaran_info:
    print(f"Luas lingkaran: {lingkaran_info['luas']}")
    print(f"Keliling lingkaran: {lingkaran_info['keliling']}")
