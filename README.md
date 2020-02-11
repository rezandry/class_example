# class_example

Keyword : constructor, getter, setter
Literasi : 
1. https://www.geeksforgeeks.org/getter-and-setter-in-python/
2. https://www.geeksforgeeks.org/constructors-in-python/
3. https://www.tutorialspoint.com/python3/python_classes_objects.htm

//-----------------------------------------------//
1. Buat class Pelajar yang menyimpan nama dan umur.
- class dibuat dengan cara -> pelajar = Pelajar()
- function yang terdapat pada class tersebut:
    1. set_nama()
        cara memanggil function -> pelajar.set_nama("Reza")
        akan menyimpan nama pelajar
    2. get_nama()
        cara memanggil function -> pelajar.get_nama()
        akan menampilkan nama pelajar yang sudah diset sebelumnya "Reza"
    3. set_umur()
        cara memanggil function -> pelajar.set_umur(24)
        akan menyimpan umur tersebut sebagai umur dari pelajar
    4. get_umur()
        cara memanggil function -> pelajar.get_umur()
        akan menampilkan umur yang sudah di set sebelumnya "24"

2. Buat class TokoKayuJati yang akan menyimpan stok
- class dibuat dengan cara -> toko = TokoKayuJati("Toko Berkah Rahayu")
- asumsi stock pertama adalah 0
- function yang terdapat pada class tersebut:
    1. add_stock()
        cara memanggil function -> toko.add_stock()
        akan menambah stock yang ada dengan +1
    2. reduce_stock()
        cara memanggil function -> toko.reduce_stock()
        akan mengurangi stock yang ada dengan -1
    3. get_stock()
        cara memanggil function -> toko.get_stock()
        akan menampilkan stock yang ada sekarang
    3. get_name()
        cara memanggil function -> toko.get_name()
        akan menampilkan nama toko yang diset pada pembuatan class "Toko Berkah Rahayu"

3. Ada sebuah mobil, mobil tersebut memiliki nama, 
mobil tersebut bisa menambah kecepatan, bisa mengurangi kecepatan,
kita bisa mendapatkan rata rata kecepatan dari mobil tersebut.

Buatlah kelas yang bisa menggambarkan keadaan tersebut.
- Mobil memiliki nama
- Bisa menambah kecepatan 5 km/h
- Bisa mengurangi kecepatan 5 km/h
- Bisa menampilkan rata rata kecepatan mobil
- Bisa menampilkan kecepatan mobil sekarang