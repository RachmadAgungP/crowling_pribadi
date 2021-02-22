Program ini digunakan untuk crowling sampe posting
Alur jalannya program Disnaker\appium\publish\:

1. file 1.awal.py digunakan untuk crowling informasi pada website disnakerja.com dari file tersebut terdapat juga beberpa fungsi diantaranya yaitu:
    a. file _parse_content.py digunakan untuk parse data-data seperti nama posisinya , nama perusahaannya, lokasinya, alamat emailnya, dll dan nanti outputnya adalah .csv yang ananti tersimpan di hasil\February 9, 2021\data_namapekerjaan1.csv
    b. file _download_gambar.py digunakan untuk download gambar yg dimana gambar yang didalam website tersebut memakai User-Agent
    c. file _tgl_.py ini berfungsi untuk menulis tanggal sesuai kita di file .txt di Data\tanggal.txt
    
2. file 2.implementasi_data.py digunakan untuk mengeksekusi data yang sudah dicrowling tadi kedalam adobe ilustrator dalam proses ini menggunakan win32com.client dan menghasilkan gambar berformat jpg di dalam folder salah satunya di hasil\February 9, 2021\0. PT Infomedia Nusantara (Telkom Group)\1.jpg

3. file 3.autto_IG.py digunakan untuk meguload foto ke IG dengan menggunakan Appium dan emulator android.

4. file 4.autto_WP.py digunakan untuk meguload content yang dari data hasil\February 9, 2021\data_namapekerjaan1.csv ada bebrapa fungsi didalamnya yaitu:
    a. file _WP_Seleksi_category.py digunakan untuk menyeleksi data yang nantinya sebagai tag di wordpress seperti lowongan kerja itu ada di mana, dan jurusan apa aja yang diperlukan, dan juga pendidikan akhir apa yang diperlukan perusahaan.
    b. file _WP_Posting.py digunakan untuk memposting dengna menggunakan Api Wordpress.
    c. file _buat_content.py digunakan untuk mempuat file html yang nantinya dituliskan ke website posting di wordpress dari proses ini menggunakan selenium. dan proses ini juga membuat format text yang nantinya disebar luaskan ke fb ataupun WA, telegram.

5. file 5.auto_FB.py digunakan untuk upload ke FB beserta gambar yang sudah dihasilkan tadi. akan tetapi ini masih belum sesuai sama apa yang saya harapkan kerana dengan menggunakan selenium tidak bisa. akhirnya menggunakan cara manual.

Program ini masih berjalan dan websitenya juga masih berjalan di Foloker.com dan ig info.lokerja.id
Belum dilanjutkan lagi karena takut dosa mencuri artikel orang lain jadi masih memikirkan metode lain.
