from collections import deque

print("=" * 5, "CONTOH 1: STACK", "=" * 5)
X = [1, 2, 3, 4, 5, 6]
print("Data Sekarang : ", X)

# Memasukkan Data Baru
X.append(7)
print("Data Masuk    : ", 7)
print("Data Sekarang : ", X)

X.append(8)
print("Data Masuk    : ", 8)
print("Data Sekarang : ", X)

# Mengeluarkan Data Yang Terakhir
X.pop() 
print("Data Sekarang : ", X)

# Stacking
Y = X.pop()
print("Data Keluar   : ", Y)
print("Data Sekarang : ", X)

print('\n\n')

#=========================================
print("=" * 5, "CONTOH 2: QUEUE", "=" * 5)

Antrian = deque([1,2,3,4,5])
print("Data Sekarang : ", Antrian)

# Menambahkan Data
Antrian.append(6)
print("Data Masuk    : ", 6)
print("Data Sekarang : ", Antrian)

Antrian.append(7)
print("Data Masuk    : ", 7)
print("Data Sekarang : ", Antrian)

# Mengurangi Antrian
Z = Antrian.popleft()
print("Data Keluar   : ", Z)
print("Data Sekarang : ", Antrian)

Z = Antrian.popleft()
print("Data Keluar   : ", Z)
print("Data Sekarang : ", Antrian)

Z = Antrian.popleft()
print("Data Keluar   : ", Z)
print("Data Sekarang : ", Antrian)

Antrian.append(8)
print("Data Masuk    : ", 8)
print("Data Sekarang : ", Antrian)