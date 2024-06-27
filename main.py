data_siswa = [] #untuk menampung semua yang diinput user
ulang = "Y"
while ulang == "Y":
   print("="*50)
   print(" DATA SISWA")
   print("="*50)
   print(" MENU")
   print("1. Input data siswa")
   print("2. Jumlah data siswa")
   print("3. Pencarian data siswa")
   print("4. Pengurutan data siswa")
   print("5. Cetak data siswa")

   print("="*50)
   pilihan = input("Pilih menu [1-5] : ")
   print("="*50)

   if pilihan == "1":
      nama = input("Masukkan Nama Siswa : ")
      semester = input("Masukkan Semester :")
      npm = input("Masukkan npm : ")
      jurusan = input("Masukkan Jurusan : ")
      kelas = input("Masukkan Kelas : ")
      data_siswa.append({"nama": nama, "semester": semester, "npm": npm, "jurusan": jurusan, "kelas": kelas})
      