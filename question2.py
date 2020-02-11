# Keyword : constructor, getter, setter
# Literasi :
# 1. https://www.geeksforgeeks.org/getter-and-setter-in-python/
# 2. https://www.geeksforgeeks.org/constructors-in-python/
# 3. https://www.tutorialspoint.com/python3/python_classes_objects.htm
#
# 2. Buat class TokoKayuJati yang akan menyimpan stok
# - class dibuat dengan cara -> toko = TokoKayuJati("Toko Berkah Rahayu")
# - asumsi stock pertama adalah 0
# - function yang terdapat pada class tersebut:
#     1. add_stock()
#         cara memanggil function -> toko.add_stock()
#         akan menambah stock yang ada dengan +1
#     2. reduce_stock()
#         cara memanggil function -> toko.reduce_stock()
#         akan mengurangi stock yang ada dengan -1
#     3. get_stock()
#         cara memanggil function -> toko.get_stock()
#         akan menampilkan stock yang ada sekarang
#     3. get_name()
#         cara memanggil function -> toko.get_name()
#         akan menampilkan nama toko yang diset pada pembuatan class "Toko Berkah Rahayu"


class TokoKayuJati:

    def __init__(self, nama_toko):
        self.__nama = nama_toko
        self.__stock = 0

    def add_stock(self):
        self.__stock = self.__stock + 1
        print("Melakukan penambahan stock +1")
        print("Stock sekarang %d" % self.__stock)

    def reduce_stock(self):
        self.__stock = self.__stock - 1
        print("Melakukan pengurangan stock -1")
        print("Stock sekarang %d" % self.__stock)

    def get_stock(self):
        return self.__stock

    def get_name(self):
        return self.__nama


print("==========================================================================")
toko_1 = TokoKayuJati("Toko Berkah Rahayu") # Stock = 0
print(toko_1.get_name())
toko_1.add_stock() # Stock = 1
toko_1.add_stock() # Stock = 2
toko_1.add_stock() # Stock = 3
toko_1.add_stock() # Stock = 4
print("Stock terakhir toko : %d" % toko_1.get_stock())

toko_1.reduce_stock() # Stock = 3
toko_1.reduce_stock() # Stock = 2
print("Stock terakhir toko : %d" % toko_1.get_stock())

print("==========================================================================")
toko_2 = TokoKayuJati("Toko Jati Husada") # Stock = 0
print(toko_2.get_name())
toko_2.add_stock() # Stock = 1
toko_2.add_stock() # Stock = 2
toko_2.add_stock() # Stock = 3
toko_2.add_stock() # Stock = 4
toko_2.add_stock() # Stock = 5
toko_2.add_stock() # Stock = 6
print("Stock terakhir toko : %d" % toko_2.get_stock())

toko_2.reduce_stock() # Stock = 5
toko_2.reduce_stock() # Stock = 4
print("Stock terakhir toko : %d" % toko_2.get_stock())
