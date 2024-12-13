from Animal import Animal

class Ular(Animal):
    def __init__(self, nama, makanan, hidup, berkembang_biak, berbisa, membelit_mangsa):
        super().__init__(nama, makanan, hidup, berkembang_biak)
        self.berbisa = berbisa
        self.membelit_mangsa = membelit_mangsa
        
    def info_ular(self):
        super().info_animal(),
        print("Berbisa \t\t :", self.berbisa,
              "\nJenis Air \t\t : ", self.membelit_mangsa)
        
ular_python = Ular("Python", "Tikus", "Darat", "Bertelur", "Tidak Berbisa", "Iya")
ular_python.info_ular()
print("=======================================================")
ular_anaconda = Ular("Anaconda", "Tikus", "Darat", "Bertelur", "Tidak Berbisa", "Iya")
ular_anaconda.info_ular()
print("=======================================================")