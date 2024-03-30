class Persegi :
    def __init__(self, sisi):
        self.sisi = sisi 
    
    def hitung_luas(self):
        print(f"Luas Persegi : {self.sisi * self.sisi}")

class Lingkaran :
    def __init__(self, jari2):
        self.jari2 = jari2
    
    def hitung_luas(self):
        print(f"Luas Persegi : {3.14 * self.jari2 * self.jari2}")

persegi = Persegi(5)
lingkaran = Lingkaran(3)

persegi.hitung_luas()
lingkaran.hitung_luas()
