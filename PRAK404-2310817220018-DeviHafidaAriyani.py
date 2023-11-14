def tambahan (angka1,angka2):
    print("Penjumlahan=",angka1+angka2)

def pengurangan (angka1,angka2):
    print("Pengurangan=",angka1-angka2)

def perkalian(angka1,angka2):
    print("Perkalian=",angka1*angka2)

def pembagian (angka1,angka2):
    print("Pembagian=",angka1/angka2)

while True:
    print("1. Penambahan")
    print("2. Pengurangan")
    print("3. Perkalian")
    print("4. Pembagian")    
    print("5. Exit")
    pilihan =int(input("Masukkan Pilihan:"))

    if pilihan==1:
        angka1=int(input("Masukkan Nilai Pertama :"))
        angka2=int(input("Masukkan Nilai Kedua :"))
        hasil= angka1 + angka2
        print(f"Hasil penjumlahan antara {angka1:.2f} dengan {angka2:.2f} adalah {hasil:.2f}")

    elif pilihan ==2:
        angka1=int(input("Masukkan Nilai Pertama :"))
        angka2=int(input("Masukkan Nilai Kedua :"))
        hasil= angka1 - angka2
        print(f"Hasil pengurangan antara {angka1:.2f} dengan {angka2:.2f} adalah {hasil:.2f}")
    
    elif pilihan ==3:
        angka1=int(input("Masukkan Nilai Pertama :"))
        angka2=int(input("Masukkan Nilai Kedua :"))
        hasil= angka1 * angka2
        print(f"Hasil perkalian antara {angka1:.2f} dengan {angka2:.2f} adalah {hasil:.2f}")
    
    elif pilihan ==4:
        angka1=int(input("Masukkan Nilai Pertama :"))
        angka2=int(input("Masukkan Nilai ke-2 :"))
        hasil= angka1 / angka2
        print(f"Hasil pembagian antara {angka1:.2f} dengan {angka2:.2f} adalah {hasil:.2f}")

    elif pilihan ==5:
        print("Terimakasih, telah menggunakan kalkulator Devi")
        break
    else:
       print ( "Input anda salah, silahkan coba lagi.\n" )