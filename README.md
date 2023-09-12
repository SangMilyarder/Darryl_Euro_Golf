Nama        : Darryl Nawawi
NPM         : 2206083104
Kelas       : PBP E
Adaptable   : https://eurogolf.adaptable.app/

## Membuat sebuah proyek Django baru
1. **Buat Direktori Khusus:**
   - Mulailah dengan membuat direktori khusus untuk proyek Django Anda.

2. **Persiapkan Lingkungan Virtual Python:**
   - Di dalam direktori proyek, buka command prompt dan jalankan perintah berikut:
     - Buat lingkungan virtual Python: `python -m venv env`.
     - Aktifkan lingkungan virtual (Mac OS): `source env/bin/activate`.

3. **Kelola Dependencies dengan `requirements.txt`:**
   - Buat file `requirements.txt` di direktori yang sama dan tambahkan daftar dependencies berikut:
     ```
     django
     gunicorn
     whitenoise
     psycopg2-binary
     requests
     urllib3
     ```

4. **Install Dependencies:**
   - Install semua dependencies dengan perintah `pip install -r requirements.txt` dalam lingkungan virtual.

5. **Mulai Proyek Django:**
   - Buat proyek Django dengan perintah `django-admin startproject shopping_list .`.

6. **Konfigurasi Pengaturan Proyek:**
   - Buka file `settings.py` dalam folder proyek yang baru saja dibuat.
   - Tambahkan tanda asterisk ('*') pada bagian `ALLOWED_HOSTS` untuk mengizinkan akses dari semua host.

7. **Jalankan Server Django:**
   - Kembali ke command prompt dan jalankan server dengan perintah `python manage.py runserver` (untuk Windows).
   - Buka http://localhost:8000 di browser untuk memeriksa proyek Django Anda.

8. **Menghentikan Server dan Menonaktifkan Lingkungan Virtual:**
   - Tekan `Ctrl+C` di command prompt untuk menghentikan server.
   - Nonaktifkan lingkungan virtual dengan perintah `deactivate`.

9. **Push ke GitHub:**
    - Terakhir, pastikan untuk melakukan push perubahan proyek Anda ke GitHub.

## Konfigurasi Routing Aplikasi Utama
1. **Membuat Berkas Konfigurasi Routing:**
   - Untuk mengatur rute URL aplikasi utama, buatlah berkas dengan nama `urls.py` di dalam direktori `main`. Isilah berkas tersebut dengan kode berikut:
     ```python
     from django.urls import path
     from main.views import show_main

     app_name = 'main'

     urlpatterns = [
         path('', show_main, name='show_main'),
     ```
     Di sini, `show_main` digunakan sebagai tampilan ketika URL terkait diakses, dan `app_name` berfungsi sebagai nama unik untuk pola URL aplikasi.

2. **Konfigurasi Routing di Berkas Utama:**
   - Buka berkas `urls.py` di direktori proyek Django (bukan di dalam direktori `main`) dan tambahkan rute URL berikut:
     ```python
     urlpatterns = [
         ...
         path('main/', include('main.urls')),
         ...
     ```
     Path `'main/'` akan mengarahkan ke rute yang telah didefinisikan dalam berkas `urls.py` di aplikasi `main`.


# Membuat model pada aplikasi main dengan nama Item dan memiliki atribut wajib sebagai berikut.
1. Buka file `models.py` dan isi file dengan nama dan atribut yang diminta.
2. Berdasarkan ketentuan soal, file minimal harus memiliki isi sebagai berikut:
```python
from django.db import models

class Item(models.Model):
    name = models.CharField(max_length=255)
    amount = models.IntegerField()
    description = models.TextField()
```
3. Jalankan perintah `python manage.py makemigrations` dan `python manage.py migrate` untuk mengaplikasikan perubahan model.

## Membuat Fungsi untuk Tampilan Aplikasi
1. **Membuka Berkas `views.py` dalam Direktori `main`:**
   - Langkah pertama adalah membuka berkas `views.py` yang terletak dalam direktori `main`.

2. **Menambahkan Kode Pembantu:**
   - Tambahkan kode berikut ke dalam berkas tersebut:
     ```python 
     from django.shortcuts import render
     ``` 

3. **Membuat Fungsi Tampilan:**
   - Selanjutnya, tambahkan fungsi berikut ke dalam berkas `views.py`:
     ```python
     def show_main(request):
         context = {
             'name': 'nama',
             'class': 'kelas'
         }

         return render(request, "main.html", context)
     ```
     Dalam fungsi ini, kita mendefinisikan variabel `context` yang berisi data yang ingin ditampilkan dalam template HTML. Kemudian, fungsi ini mengembalikan tampilan yang dihasilkan oleh template `main.html`.

4. **Membuat Template HTML:**
   - Buat sebuah direktori dengan nama `templates` di dalam direktori `main`, lalu buat berkas dengan nama `main.html`. Isilah berkas ini dengan kode HTML berikut untuk menampilkan data yang ada di fungsi sebelumnya:
     ```html
     <h5>Name: </h5>
     <p>{{ name }}</p>
     <h5>Class: </h5>
     <p>{{ class }}</p>
     ```


## Konfigurasi Routing untuk Aplikasi Utama
1. **Pengaturan Rute URL di Berkas `urls.py`:**
   - Mulailah dengan membuat berkas bernama `urls.py` di dalam direktori `main`. Isilah berkas tersebut dengan kode berikut untuk mengatur rute URL:
     ```python
     from django.urls import path
     from main.views import show_main

     app_name = 'main'

     urlpatterns = [
         path('', show_main, name='show_main'),
     ```
     Di sini, kami telah mendefinisikan rute URL yang akan mengarahkan ke fungsi `show_main` yang telah dibuat di berkas `views.py`.

## Melakukan Deployment Aplikasi ke Adaptable.io
1. **Pendaftaran Akun dan Koneksi ke GitHub:**
   - Pertama, buka situs web Adaptable.io dan buatlah akun dengan menggunakan akun GitHub Anda.

2. **Membuat Aplikasi Baru:**
   - Setelah berhasil login, klik tombol "New APP" dan pilih opsi "Connect an Existing Repository".

3. **Akses Repository GitHub:**
   - Pilih opsi "All Repositories" untuk memberikan akses ke semua repository di akun GitHub Anda.

4. **Pemilihan Repository Aplikasi:**
   - Pilih repository yang berisi aplikasi yang ingin Anda deploy.

5. **Konfigurasi Template Deployment:**
   - Pilih "Python App Template" sebagai template deployment.

6. **Tipe Basis Data:**
   - Pilih "PostgreSQL" sebagai tipe basis data.

7. **Konfigurasi Start Command:**
   - Sesuaikan versi Python dan masukkan perintah `python manage.py migrate && gunicorn (nama direktori utama).wsgi.` di bagian "Start Command".

8. **Penamaan Aplikasi dan Deployment:**
   - Tuliskan nama aplikasi yang Anda inginkan dan centang kotak "HTTP Listener on PORT", lalu klik tombol "Deploy App" untuk memulai proses deployment.

## Proses Request dan Respon pada Aplikasi Django
![DJango Framework](https://github.com/SangMilyarder/Darryl_Euro_Golf)

Pada awalnya, pengguna atau klien akan mengirim permintaan (request) untuk mengakses sumber daya. Django kemudian akan memproses URL dari klien dan mencocokkannya dengan file `urls.py` (URL Mapping).

Selanjutnya, Django akan membuka file `views.py` dan meminta tampilan (view). File `models.py` akan mengelola data yang berkaitan dengan permintaan pengguna, sementara folder `template` akan berisi file dengan ekstensi HTML. File-file HTML ini berisi kode-kode HTML yang mengatur teks, tabel, tata letak, dan elemen-elemen visual lainnya. Setelah proses ini selesai, tampilan akan disajikan kepada klien atau pengguna.

(Sumber: [intellipaat.com](https://intellipaat.com/blog/tutorial/python-django-tutorial/))

## Mengapa Kita Menggunakan Virtual Environment?
Virtual environment adalah alat yang sangat berguna dalam pengembangan perangkat lunak. Berikut adalah beberapa alasan mengapa kita menggunakannya:

1. **Isolasi Dependencies**: Virtual environment memungkinkan untuk mengisolasi dependensi atau paket yang digunakan dalam proyek. Hal ini membantu menghindari konflik antara versi paket yang berbeda di berbagai proyek.

2. **Menghindari Konflik**: Dengan virtual environment, konflik antara versi paket yang berbeda dalam proyek-proyek yang berbeda dapat terhindari.

3. **Kemudahan Pengelolaan Proyek**: Virtual environment mempermudah pengelolaan proyek-proyek sehingga memungkinkan untuk beralih antara proyek-proyek dengan dependensi yang berbeda dengan mudah.

4. **Versi Python yang Berbeda**: Menggunakan virtual environment untuk mengganti versi Python yang digunakan dalam proyek tertentu.

5. **Keamanan**: Virtual environment membantu menjaga keamanan proyek-proyek dengan membatasi akses paket-paket tertentu.

6. **Portabilitas**: Dengan virtual environment, proyek dapat dengan mudah dipindahkan atau dibagikan kepada orang lain.

(Sumber: [docs.python.org](https://docs.python.org/3/tutorial/venv.html))

## Apakah kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment?
Meskipun memungkinkan untuk membuat aplikasi web Django tanpa menggunakan virtual environment, sangat disarankan untuk selalu menggunakan virtual environment. Ini adalah praktik terbaik dalam pengembangan aplikasi web Django dan membantu kita menghindari masalah terkait dependensi dan konflik yang mungkin muncul.

(Sumber: [docs.python.org](https://www.w3schools.com/django/django_create_virtual_environment.php))

## Penjelasan MVC, MVT, MVVM dan perbedaan dari ketiganya.
MVC, MVT, dan MVVM adalah tiga pendekatan arsitektur perangkat lunak yang digunakan dalam pengembangan aplikasi berbasis pemisahan tanggung jawab. Meskipun memiliki prinsip-prinsip umum, mereka digunakan dalam kerangka kerja yang berbeda dan digunakan untuk mengatasi berbagai tantangan pengembangan perangkat lunak.

## Model-View-Controller (MVC)
Pola arsitektur MVC menyarankan pemisahan kode menjadi tiga komponen utama:

- **Model**: Bertanggung jawab untuk menyimpan data aplikasi, menangani logika domain, dan berkomunikasi dengan lapisan basis data serta jaringan. Model tidak memiliki pengetahuan tentang antarmuka pengguna.
- **View**: Merupakan lapisan antarmuka pengguna (UI) yang mengatur komponen-komponen yang terlihat di layar. Selain itu, View menampilkan data yang disimpan dalam Model dan memungkinkan interaksi dengan pengguna.
- **Controller**: Membentuk hubungan antara View dan Model, mengandung logika aplikasi inti, dan merespons input pengguna serta memperbarui Model sesuai kebutuhan.

## Model-View-Presenter (MVP)
Pola arsitektur MVP mengatasi beberapa tantangan dari MVC dan memberikan cara yang lebih mudah untuk struktur kode proyek. Ini terdiri dari komponen berikut:

- **Model**: Berperan sebagai lapisan penyimpanan data, menangani logika domain, dan berkomunikasi dengan lapisan basis data serta jaringan.
- **View**: Merupakan lapisan antarmuka pengguna (UI), memberi tahu Presenter tentang tindakan pengguna, dan bertanggung jawab atas visualisasi data.
- **Presenter**: Mengambil data dari Model, menerapkan logika UI, mengelola status View, dan mengambil tindakan sesuai dengan notifikasi input pengguna dari View.

## Model-View-ViewModel (MVVM)
Pola arsitektur MVVM memiliki beberapa kesamaan dengan MVP, tetapi mengatasi kekurangan yang ada. Pola ini memisahkan logika presentasi data (UI) dari logika bisnis inti aplikasi, dengan komponen berikut:

- **Model**: Bertanggung jawab atas abstraksi sumber data, bekerja sama dengan ViewModel untuk mengambil dan menyimpan data.
- **View**: Bertujuan untuk memberi tahu ViewModel tentang tindakan pengguna, hanya mengamati ViewModel, dan tidak berisi logika aplikasi.
- **ViewModel**: Mengekspos aliran data yang relevan untuk View, berfungsi sebagai penghubung antara Model dan View, serta mengubah data ke format yang sesuai untuk ditampilkan oleh View.

**Sumber**: [geeksforgeeks](https://www.geeksforgeeks.org/difference-between-mvc-mvp-and-mvvm-architecture-pattern-in-android/)

