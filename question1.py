# Keyword : constructor, getter, setter
# Literasi :
# 1. https://www.geeksforgeeks.org/getter-and-setter-in-python/
# 2. https://www.geeksforgeeks.org/constructors-in-python/
# 3. https://www.tutorialspoint.com/python3/python_classes_objects.htm
#
# 1. Buat class Pelajar yang menyimpan nama dan umur.
# - class dibuat dengan cara -> pelajar = Pelajar()
# - function yang terdapat pada class tersebut:
#     1. set_nama()
#         cara memanggil function -> pelajar.set_nama("Reza")
#         akan menyimpan nama pelajar
#     2. get_nama()
#         cara memanggil function -> pelajar.get_nama()
#         akan menampilkan nama pelajar yang sudah diset sebelumnya "Reza"
#     3. set_umur()
#         cara memanggil function -> pelajar.set_umur(24)
#         akan menyimpan umur tersebut sebagai umur dari pelajar
#     4. get_umur()
#         cara memanggil function -> pelajar.get_umur()
#         akan menampilkan umur yang sudah di set sebelumnya "24"


class Pelajar:

    def __init__(self):
        self.__nama = None
        self.__umur = None

    def set_nama(self, nama_on_parameter):
        self.__nama = nama_on_parameter

    def get_nama(self):
        return self.__nama

    def set_umur(self, umur_on_parameter):
        self.__umur = umur_on_parameter

    def get_umur(self):
        return self.__umur


pelajar_1 = Pelajar()
pelajar_1.set_nama("Reza Andriyunanto")
pelajar_1.set_umur(24)

pelajar_2 = Pelajar()
pelajar_2.set_nama("Chandra Adilaksana")
pelajar_2.set_umur(23)

pelajar_3 = Pelajar()
pelajar_3.set_nama("Jojo Sugandi")
pelajar_3.set_umur(40)


print('Nama Pelajar : %s' % pelajar_1.get_nama())
print('Umur Pelajar : %d' % pelajar_1.get_umur())

print('Nama Pelajar : %s' % pelajar_2.get_nama())
print('Umur Pelajar : %d' % pelajar_2.get_umur())

print('Nama Pelajar : %s' % pelajar_3.get_nama())
print('Umur Pelajar : %d' % pelajar_3.get_umur())
