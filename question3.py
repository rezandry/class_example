# Keyword : constructor, getter, setter
# Literasi :
# 1. https://www.geeksforgeeks.org/getter-and-setter-in-python/
# 2. https://www.geeksforgeeks.org/constructors-in-python/
# 3. https://www.tutorialspoint.com/python3/python_classes_objects.htm
#
# 3. Ada sebuah mobil, mobil tersebut memiliki nama,
# mobil tersebut bisa menambah kecepatan, bisa mengurangi kecepatan,
# kita bisa mendapatkan rata rata kecepatan dari mobil tersebut.
#
# Buatlah kelas yang bisa menggambarkan keadaan tersebut.
# - Mobil memiliki nama
# - Bisa menambah kecepatan 5 km/h
# - Bisa mengurangi kecepatan 5 km/h
# - Bisa menampilkan rata rata kecepatan mobil
# - Bisa menampilkan kecepatan mobil sekarang


class Mobil:

    def __init__(self, nama_mobil_dari_parameter):
        self.__nama = nama_mobil_dari_parameter
        self.__speed = 0
        self.__average = 0
        self.__total_speed = 0
        self.__time = 0

    def tambah_kecepatan(self):
        print('Tambah kecepatan')
        self.__speed = self.__speed + 5
        self.__total_speed = self.__total_speed + self.__speed
        self.__time = self.__time + 1
        print('Kecepatan sekarang : %d' % self.__speed)

    def kurangi_kecepatan(self):
        print('Kurangi kecepatan')
        self.__speed = self.__speed - 5
        self.__total_speed = self.__total_speed + self.__speed
        self.__time = self.__time + 1
        print('Kecepatan sekarang : %d' % self.__speed)

    def rata_rata(self):
        return self.__total_speed/self.__time

    def kecepatan_sekarang(self):
        return self.__speed

    def get_nama(self):
        return self.__nama

mobil_1 = Mobil("Avanza")
mobil_1.tambah_kecepatan() # speed = 5
mobil_1.tambah_kecepatan() # speed = 10
mobil_1.tambah_kecepatan() # speed = 15
mobil_1.kurangi_kecepatan() # speed = 10
mobil_1.kurangi_kecepatan() # speed = 5
print(mobil_1.get_nama())
print(mobil_1.kecepatan_sekarang())
print(mobil_1.rata_rata()) # (5+10+15+10+5) / 5 = 9

mobil_2 = Mobil("Terios")
mobil_2.tambah_kecepatan() # speed = 5
mobil_2.tambah_kecepatan() # speed = 10
mobil_2.tambah_kecepatan() # speed = 15
mobil_2.tambah_kecepatan() # speed = 20
mobil_2.kurangi_kecepatan() # speed = 15
mobil_2.kurangi_kecepatan() # speed = 10
print(mobil_2.get_nama())
print(mobil_2.kecepatan_sekarang())
print(mobil_2.rata_rata()) # (5+10+15+20+15+10) / 6 = 12.5
