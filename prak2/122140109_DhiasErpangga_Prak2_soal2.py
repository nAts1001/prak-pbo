class BurungDewasa:
    def __init__(self, nama):
        self.nama = nama
        print(f"{self.nama} si burung telah menetas!")

    def __del__(self):
        print(f"{self.nama} si burung telah meninggal. Semoga terbang bebas di alam sana, {self.nama}.")

def destructor_decorator(cls):
    class Wrapper:
        def __init__(self, *args, **kwargs):
            self.wrapped = cls(*args, **kwargs)
            print(f"Sebuah {cls.__name__} baru telah menetas!")

        def __getattr__(self, name):
            return getattr(self.wrapped, name)

        def __del__(self):
            print(f"{self.wrapped.nama} si {cls.__name__} telah meninggal. Semoga terbang bebas di alam sana, {self.wrapped.nama}.")
            self.wrapped.__del__()

    return Wrapper

@destructor_decorator
class AnakBurung:
    def __init__(self, nama):
        self.nama = nama
        print(f"{self.nama} si anak burung telah menetas!")

if __name__ == "__main__":
    burung_dewasa = BurungDewasa("Merpati")
    anak_burung = AnakBurung("Cucu Cendet")

