import csv
import os

# Sistem Pemesanan Tiket Bioskop

class Bioskop:
    def __init__(self):
        self.films = [
            {"judul": "Pengabdi Setan", "jam": "18:00", "harga": 50000, "tiket_tersedia": 30},
            {"judul": "Terrifier 3   ",    "jam": "16:30", "harga": 55000, "tiket_tersedia": 25},
            {"judul": "Terrifier 2   ",    "jam": "19:00", "harga": 60000, "tiket_tersedia": 20}
        ]
        self.riwayat_pemesanan = []

    def tampilkan_film(self):
        print("Daftar Film yang Tersedia:")
        print("="*60)
        print("No |Judul Film|Jam Tayang|Harga|Tiket Tersedia")
        print("="*60)
        for i, film in enumerate(self.films):
            print(f"{i+1} | {film['judul']} | {film['jam']} | Rp{film['harga']} | {film['tiket_tersedia']}")
        print("="*60)

    def pesan_tiket(self):
        self.tampilkan_film()
        pilihan_film = int(input("Pilih nomor film yang ingin ditonton: ")) - 1
        film_terpilih = self.films[pilihan_film]
        
        jumlah_tiket = int(input(f"Berapa tiket yang ingin dipesan untuk {film_terpilih['judul']}? "))
        
        if jumlah_tiket > film_terpilih['tiket_tersedia']:
            print(f"Maaf, tiket tersedia hanya {film_terpilih['tiket_tersedia']}")
            return

        total_harga = jumlah_tiket * film_terpilih['harga']
        print(f"Total Harga untuk {jumlah_tiket} tiket: Rp{total_harga}")
        konfirmasi = input(f"Apakah Anda yakin ingin memesan {jumlah_tiket} tiket untuk {film_terpilih['judul']}? (y/n): ")

        if konfirmasi.lower() == 'y':
            film_terpilih['tiket_tersedia'] -= jumlah_tiket
            pemesanan = {
                "judul": film_terpilih['judul'],
                "jam": film_terpilih['jam'],
                "jumlah_tiket": jumlah_tiket,
                "total_harga": total_harga
            }
            self.riwayat_pemesanan.append(pemesanan)
            self.simpan_ke_csv(pemesanan)  # Simpan ke file CSV
            print("Pemesanan berhasil disimpan ke riwayat pemesanan dan CSV!")
        else:
            print("Pemesanan dibatalkan.")

    def simpan_ke_csv(self, pemesanan):
        # Nama file CSV
        nama_file = r'C:\Users\Toshiba\OneDrive\Desktop\belajar python\bioskop_history.csv'
        # Menuliskan header jika file belum ada
        file_baru = not os.path.exists(nama_file)
        with open(nama_file, mode='a', newline='', encoding='utf-8') as file:
            penulis = csv.writer(file)
            if file_baru:
                penulis.writerow(['Judul Film', 'Jam Tayang', 'Jumlah Tiket', 'Total Harga'])
            penulis.writerow([pemesanan['judul'], pemesanan['jam'], pemesanan['jumlah_tiket'], pemesanan['total_harga']])

    def lihat_riwayat_pemesanan(self):
        if not self.riwayat_pemesanan:
            print("Tidak ada riwayat pemesanan.")
        else:
            print("Riwayat Pemesanan:")
            print("="*60)
            print("Judul Film | Jam Tayang | Jumlah Tiket | Total Harga")
            print("="*60)
            for pemesanan in self.riwayat_pemesanan:
                print(f"{pemesanan['judul']} | {pemesanan['jam']} | {pemesanan['jumlah_tiket']} | Rp{pemesanan['total_harga']}")
            print("="*60)            

def menu():
    bioskop = Bioskop()
    while True:
        print("\n=== Sistem Pemesanan Tiket Bioskop ===")
        print("1. Pesan Tiket")
        print("2. Lihat Riwayat Pemesanan")
        print("3. Keluar")
        
        pilihan = input("Pilih menu (1/2/3): ")

        if pilihan == '1':
            bioskop.pesan_tiket()
        elif pilihan == '2':
            bioskop.lihat_riwayat_pemesanan()
        elif pilihan == '3':
            print("Terima kasih telah menggunakan sistem pemesanan tiket!")
            break
        else:
            print("Pilihan tidak valid, silakan coba lagi.")

if __name__ == "__main__":
    menu()