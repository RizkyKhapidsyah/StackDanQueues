# StackDanQueues

Bahan Ajar Fundamental Pemrograman Python. Mengenal Konsep Stack dan Queue beserta cara menggunakannya.<br><br>
<img src="https://github.com/RizkyKhapidsyah/StackDanQueues/blob/master/result/001.PNG"><br>
<img src="https://github.com/RizkyKhapidsyah/StackDanQueues/blob/master/result/002.PNG"><br><br>
- Lihat <a href="https://github.com/RizkyKhapidsyah/StackDanQueues/blob/master/StackDanQueues.py">Source Code.</a><br><br>

# Stack

Ketika kita belajar mata kuliah struktur data, maka akan muncul bab yang membahas stack dan queue atau sering juga mendapatkan istilah LIFO (Last In First Out) atau FIFO (First In First Out). 
Array adalah struktur data yang bisa diakses secara acak, dimana setiap elemen dapat diakses secara langsung dan dalam waktu yang konstan. Ilustrasi yang bisa digunakan adalah dalam sebuah buku, setiap halaman buku dapat dibuka secara independen. Akses acak sangat penting untuk banyak algoritma, misalnya pencarian biner. 

Sedangkan linked list adalah struktur data yang di akses berurutan, dimana setiap elemen dapat diakses hanya dalam urutan tertentu. Ilustrasi yang bisa digunakan untuk akses sekuensial ini adalah selembar kertas atau rekaman video di mana semua materi sebelumnya harus dibuka untuk mendapatkan data yang Anda inginkan.

Stack adalah struktur data yang dapat ditunjukkan oleh tempat penyisipan dan penghapusan elemen terjadi hanya pada satu tempat yang disebut puncak tumpukan. Cara dasar untuk mengakses data di stack adalah dengan metode Last In First Out (LIFO). Untuk memahami struktur stack, bayangkan setumpuk buku. Seseorang hanya bisa menggunakan ujung atas tumpukan untuk menambahkan atau mengeluarkan buku dari tumpukan. Juga, nomor indeks tidak bisa digunakan ke elemen dalam tumpukan, oleh karena itu, elemen di tengah tumpukan tidak dapat diakses secara langsung. Dalam Python kita bisa menggunakan list sebagai stack, lebih lanjut mengenai List Di Python.  Di bawah ini adalah script sederhananya :

      #!/usr/bin/python

      stack = ['hello','world']; #inisialisasi stack

      print ("stack awal :", stack)
      stack.append("belajar") #tambahkan elemen
      stack.append("stack") #tambahkan elemen
      print("stack setelah ditambahkan : ", stack)

      stack.pop() #hapus elemen terakhir
      print("stack setelah elemen terakhir dihapus : ", stack)
      
# Queue

Queue adalah struktur data yang bisa diwakili oleh antrian (urutan). Dengan kata lain memiliki depan dan belakang. Contohnya : pada antrian loket tiket, orang baru bergabung di belakang dan orang pertama membeli tiket terlebih dahulu akan pergi lebih dulu. Demikian pula, antrian struktur data ini mengikuti prinsip First In First Out (FIFO). Penambahan elemen disebut “Enqueue” dan Penghapusan elemen disebut “Dequeue”. Enqueue berlangsung di bagian belakang, sementara Dequeue terjadi di depan. Untuk menggunakan list sebagai queue dalam Python, kita menggunakan collections.deque. Seperti contoh di bawah :

      #!/usr/bin/python

      from collections import deque #import module

      queue = deque(['hello','world']); #inisialisasi queue

      print ("queue awal :", queue)
      queue.append("belajar") #tambahkan elemen
      queue.append("stack") #tambahkan elemen
      print("queue setelah ditambahkan : ", queue)

      queue.popleft() #hapus elemen pertama
      print("queue setelah elemen pertama dihapus : ", queue)

# Python List Stack dan Queues.

Sekarang kita akan Belajar Python List Stack dan Queues. Karena dari kedua tersebut adalah salah satu bagian dari List. Kita Sudah Belajar List yang kemaren itu dan sekarang kita akan melanjutkan salah satu bagian dari List. Perbedaan dari Python List Stack dan Queues :

<table class="wp-block-table is-style-regular">
<tbody>
<tr>
<td> </td>
<td><strong>Stack</strong></td><td>
<strong>Queues</strong></td>
</tr><tr>
<td></td>
<td>Cara Kerjanya Terakhir Masuk Pertama Yang Keluar</td>
<td>Cara Kerjanya Pertama masuk Pertama keluar</td>
</tr><tr>
<td></td>
<td>strukturenya Ujung yang sama digunakan untuk menyisipkan dan menghapus elemen.</td>
<td>strukturenya Satu ujung digunakan untuk penyisipan, yaitu, ujung belakang dan ujung lainnya digunakan untuk penghapusan elemen, yaitu ujung depan.</td>
</tr><tr><td></td>
<td>Jumlah pointer yang digunakan 1 </td>
<td>Jumlah pointer yang digunakan 2</td>
</tr><tr>
<td></td>
<td>Pemriksaan kondisi kosong  Atas == -1</td>
<td>Belakang == Maks &#8211; 1</td>
</tr><tr><td></td>
<td>Tidak memiliki variasi </td>
<td>memiliki varian seperti antrian melingkar, antrian prioritas, antrian berakhir ganda.</td>
</tr>
<tr><td></td>
<td>Implementasi lebih sederhana</td>
<td>Implementasinya relatif komplek</td></tr><tr>
</tr></tbody></table>

Diatas adalah contoh perbedaan antara list stack dan queues.

Stack adalah jenis struktur data yang menumpuk dan dimana item baru akan ditambahkan dan yang sudah ada akan dihapuskan. Semua penghapusan dan penyisipan dalam tumpukan dilakukan dari atas tumpukan, elemen terakhir yang ditambahkan akan menjadi yang pertama dihapus dari tumpukan. Queues adalah jenis struktur data yang mengantri (antrian ) dan dimana item yang masuk di antrian akan keluar di depan bukan dibelakang.

Note : append menambahkan data list tepat dibelakangnya data tersebut

Stack Contoh :

      stacks = [1,2,3,4,5,6,7,8,9,10]

      print(“data yang belum ditambahkan adalah :”,stacks)

      stacks.append(11)
      print(“data yang masuk : “,11)
      print(“data sekarang adalah :”,stacks)

      stacks.append(12)
      print(“data yang masuk : “,12)
      print(“data sekarang adalah :”,stacks)

      #stack
      keluar = stacks.pop()
      print(“data keluar :”, keluar)
      print(“data sekarang :”,stacks)

## Belajar Python List Stack dan Queues

Contoh Queues :

      from collections import deque

      queues = deque([1,2,3,4,5,6,7,8])
      print(“data listnya :”,queues)

      queues.append(9) #menambahkan data

      print(“data yang ditambah :”,9)
      print(“data sekarang :”,queues)

      hapusdepan = queues.popleft()
      print(“data nyang dihapus :”,hapusdepan)
      print(“data sekarang :”,queues)

Note : Karena list ngak bisa dipakai untuk menghapus antrian maka menggunakan library from collections import deque.
Nah itu contoh perbedaan antara python list struktur teknik stack dan queues.

# Cara Terbaik Untuk Implementasi queue (antrian) Sederhana

List sederhana dapat digunakan dengan mudah untuk digunakan dan diimplementasikan sebagai struktur data queue. Queue seperti ini akan memiliki prinsip first-in, first-out (FIFO). Akan tetapi, pendekatan ini merupakan langkah yang tidak efisien karena memasukkan dan mengambil data dari index pertama list python cenderung “lambat” karena semua elemen perlu bergeser satu index. Direkomendasikan untuk mengimplementasikan queue menggunakan modul collections.deque, karena modul ini telah didisain agar menambahkan dan mengambil data dengan cepat baik dari index pertama maupun terakhir.

      from collections import deque
      queue = deque(["a", "b", "c"])
      queue.append("d")
      queue.append("e")
      queue.popleft()
      queue.popleft()
      print(queue)
      # keluarannya adalah: deque(['c', 'd', 'e'])

Queue balikannya dapat dimplementasikan dengan menggunakan metode <code class="highlighter-rouge">appendleft</code> daripada <code class="highlighter-rouge">append</code> dan metode <code class="highlighter-rouge">pop</code> daripada <code class="highlighter-rouge">popleft</code>.

-----
Referensi Artikel: <a href="https://www.codezeroo.com">CodeZeroo</a>, <a href="https://sinaudev.github.io">SinauDev</a>, <a href="https://www.yudana.id">Yudana</a>. Thanks to: <a href="https://www.codezeroo.com">CodeZeroo</a>, <a href="https://sinaudev.github.io">SinauDev</a>, <a href="https://www.yudana.id">Yudana.</a><br><br> 
Referensi Source Code Pada Repository: <a href="https://www.youtube.com/user/faqihzamukhlish"> Kelas Terbuka </a> dan <a href="https://github.com/kelasterbuka"> Kelas Terbuka (Repository)</a>. Created by <a href="https://github.com/faqihza">Faqihza Mukhlish.</a> Thanks To: <a href="https://www.youtube.com/channel/UCRGHjysoCemh4y7tCJQs30w/about">Faqihza Mukhlish.</a><br>

-----
All Source Code is Modified.


