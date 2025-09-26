# Sistem Penilaian Ujian Siswa SMKN 21 Jakarta
Nama = input ("Masukkan nama anda :")
Absen = int (input ("Masukkan no Absen :"))
UTS = float (input("Masukkan Nilai UTS :"))
UAS = float (input("Masukkan Nilai UAS :"))
KKM = 80

# Menentukan Nilai Akhir
Nilai_akhir = (UTS * 0.4 ) + (UAS + 0.6)

# Menentukan Status Kelulusan
if Nilai_akhir >= KKM and UTS > 40 and UAS > 40:
    Status = "Anda Dinyatakan LULUS"
else :
    Status = "Maaf, Anda GAGAL"

# Hasil Penilaian
print ("\n HASIL PENILAIAN")
print ("Nama siswa      :", Nama)
print ("No Absen siswa  :", Absen)
print("Nilai UTS        :", UTS)
print("Nilai UAS        :", UAS)
print("Nilai KKM        : 80")
print("Nilai Akhir      :", Nilai_akhir)
print("")
print("Hasil Penentuan           :", Status)
