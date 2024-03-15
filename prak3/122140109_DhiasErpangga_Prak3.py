class Dagangan:
    # Inisialisasi atribut kelas
    jumlah_barang = 0
    list_barang = []

    # Metode untuk inisialisasi instance
    def __init__(self, nama, stok, harga):
        # Atribut instance bersifat private dengan awalan "__"
        self.__nama = nama
        self.__stok = stok
        self.__harga = harga
        # Menambahkan jumlah barang dan menambahkan barang ke daftar barang
        Dagangan.jumlah_barang += 1
        Dagangan.list_barang.append((nama, stok, harga))

    # Metode kelas untuk menampilkan barang-barang yang tersedia
    @classmethod
    def lihat_barang(cls):
        print(f"Jumlah barang dagangan pada toko: {cls.jumlah_barang} buah")
        for idx, barang in enumerate(cls.list_barang, start=1):
            nama, stok, harga = barang
            print(f"{idx}. {nama} seharga Rp {harga} (stok: {stok})")

    # Metode untuk menghapus instance dan mengurangi jumlah barang serta menghapus dari daftar barang
    def __del__(self):
        Dagangan.jumlah_barang -= 1
        for i, barang in enumerate(Dagangan.list_barang):
            if barang[0] == self.__nama:
                del Dagangan.list_barang[i]
                print(f"{self.__nama} dihapus dari toko!")
                break


# Contoh penggunaan
Dagangan1 = Dagangan("Galon Aqua 19L", 32, 17000)
Dagangan2 = Dagangan("Gas LPG 5 kg", 22, 88000)
Dagangan3 = Dagangan("Beras Ramos 5 kg", 13, 68000)
Dagangan.lihat_barang()
del Dagangan1
Dagangan.lihat_barang()
