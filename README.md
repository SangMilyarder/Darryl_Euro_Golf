Nama        : Darryl Nawawi
NPM         : 2206083104
Kelas       : PBP E
Adaptable   : https://euro-golf.adaptable.app/main/

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
   - Buka http://localhost:8000 di browser untuk memeriksa proyek Django yang sudah dibuat.

8. **Menghentikan Server dan Menonaktifkan Lingkungan Virtual:**
   - Tekan `Ctrl+C` di command prompt untuk menghentikan server.
   - Nonaktifkan lingkungan virtual dengan perintah `deactivate`.

9. **Push ke GitHub:**
    - Terakhir, pastikan untuk melakukan push perubahan proyek ke GitHub.

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
![DJango Framework](https://github.com/SangMilyarder/Darryl_Euro_Golf/blob/main/PBP-Tugas2.png)

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

## Tugas 3

## Perbedaan antara Form POST dan Form GET dalam Django

1. **Form POST:**

- Digunakan untuk mengirim data ke server sebagai permintaan yang akan diproses.
- Data dikirim dalam tubuh permintaan HTTP dan tidak terlihat dalam URL.
- Cocok untuk operasi yang mempengaruhi data di server, seperti membuat, mengedit, atau menghapus data.
- Data biasanya dienkripsi sehingga lebih aman.

2. **Form GET:**

- Digunakan untuk mengirim data sebagai bagian dari URL.
- Data terlihat dalam URL dan dapat dibaca oleh siapa saja yang melihatnya (tidak begitu aman)
- Cocok untuk permintaan yang hanya mengambil atau mengambil data dari server tanpa mempengaruhi data di server.
- Data dikirim sebagai parameter query string di URL.

**Sumber**: [DjangoForms](https://docs.djangoproject.com/en/3.2/topics/forms/)

## Perbedaan Utama antara XML, JSON, dan HTML dalam Konteks Pengiriman Data

1. **XML (eXtensible Markup Language):**

XML digunakan untuk menyusun dan mengirim data dalam bentuk hierarki dengan tag. XML memiliki struktur ketat dan aturan yang ketat untuk markup. XML lebih berat dan lebih banyak overhead dibandingkan dengan JSON. XML biasanya digunakan dalam lingkungan yang memerlukan pertukaran data terstruktur.

**Sumber**: [W3Schools](https://www.w3schools.com/xml/xml_whatis.asp)

2. **JSON (JavaScript Object Notation):**

JSON digunakan untuk pertukaran data ringan dan mudah dibaca antara aplikasi. JSON memiliki representasi data dalam format key-value pairs, sehingga lebih sederhana dan mudah dibaca oleh manusia. JSON lebih efisien dalam hal ukuran dan parsing dibanding XML. JSON digunakan dalam pertukaran data antara aplikasi web modern (terutama dalam konteks RESTful API)

**Sumber**: [JSON](https://www.json.org/json-en.html)

3. **HTML (HyperText Markup Language):**

HTML digunakan untuk membuat halaman web dan menampilkan konten kepada pengguna. HTML memiliki struktur hierarkis yang digunakan untuk merancang tampilan halaman web. HTML lebih ringan dibanding XML, namun tidak dirancang untuk pertukaran data antar aplikasi. HTML tidak digunakan langsung untuk pertukaran data antara aplikasi melainkan untuk merender konten web.

**Sumber**: [MDN Web Docs](https://developer.mozilla.org/en-US/docs/Web/HTML)

## Penyebab JSON sering digunakan dalam pertukaran data antara aplikasi web modern

JSON memiliki format yang ringan dan mudah dibaca oleh manusia. Ini memudahkan pengembang untuk memahami dan memeriksa data saat mereka mengembangkan dan menguji aplikasi serta mempermudah dalam mengelola. JSON juga didukung oleh hampir semua bahasa pemrograman dan dapat dengan mudah diuraikan menjadi objek atau struktur data dalam bahasa yang berbeda. Hal ini membuatnya cocok untuk komunikasi antara berbagai komponen aplikasi, termasuk server, peramban web, dan bahasa pemrograman backend. JSON juga merupakan format data yang diakui secara luas dan menjadi standar de facto dalam pertukaran data dalam aplikasi web modern. JSON juga memiliki overhead yang lebih rendah dibandingkan dengan format data yang lebih kompleks seperti XML, sehingga memungkinkan pertukaran data yang lebih efisien. JSON mendukung nested data, yang memungkinkan Anda untuk menggabungkan berbagai jenis data dalam satu dokumen JSON. Ini berguna ketika aplikasi membutuhkan data yang kompleks dan terstruktur.
JSON menjadi pilihan yang populer dalam pengembangan aplikasi web modern karena sifatnya yang sederhana, fleksibel, dan mudah digunakan dalam berbagai konteks pengiriman data.

Sumber:**Sumber**: [JSON](https://www.json.org/json-en.html)[MDN](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Objects/JSON)

## Langkah mengimplementasikan checklist secara step-by-step

## Mengatur Routing dari main/ ke /

1. **Jalankan virtual environment terlebih dahulu**
   - Aktifkan lingkungan virtual (Mac OS): `source env/bin/activate`.

2. **Mengubah path pada urls.py di folder Euro_Golf**
   - Mengubah path main/ menjadi '' pada urlpatterns
   ```python
   urlpatterns = [
   path('', include('main.urls')),
   path('admin/', admin.site.urls),
   ]
   ```

## Implementasi Skeleton sebagai kerangka views

1. **Membuat kerangka umun untuk halaman web lain di dalam proyek**
   - Membuat folder templates di rootfolder beserta file HTML di dalamnya bernama base.html. Kemudian isi file berikut dengan kode :
   ```html
   {% load static %}
   <!DOCTYPE html>
   <html lang="en">
      <head>
         <meta charset="UTF-8" />
         <meta
               name="viewport"
               content="width=device-width, initial-scale=1.0"
         />
         {% block meta %}
         {% endblock meta %}
      </head>

      <body>
         {% block content %}
         {% endblock content %}
      </body>
   </html>
   ```

2. **Menyesuaikan kode agar berkas base.html terdeteksi sebagai berkas template**
   - Buka settings.py yang berada di subdirektori Euro_Golf dan perbaik baris TEMPLATES
   ```python
   ...
   TEMPLATES = [
      {
         'BACKEND': 'django.template.backends.django.DjangoTemplates',
         'DIRS': [BASE_DIR / 'templates'], # Tambahkan kode ini
         'APP_DIRS': True,
         ...
      }
   ]
   ...
   ```

3. **Mengubah kode pada main.html**
   - main.html diubah untuk menggunakan base.html sebagai template utama
   ```python
   {% extends 'base.html' %}

   {% block content %}
      <h1>Shopping List Page</h1>

      <h5>Name:</h5>
      <p>{{name}}</p>

      <h5>Class:</h5>
      <p>{{class}}</p>
   {% endblock content %}
   ```

## Membuat Form Input Data dan Menampilkan Data Produk Pada HTML

1. **Membuat struktur form yang dapat menerima data produk baru**
   - Membuat berkas baru pada direktori main dengan nama forms.py
   ```python
   from django.forms import ModelForm
   from main.models import Product

   class ProductForm(ModelForm):
      class Meta:
         model = Product
         fields = ["name", "price", "description"]
   ```

2. **Menambah beberapa import di views.py pada folder main**
   - Berikut tambahannya :
   ```python
   from django.http import HttpResponseRedirect
   from main.forms import ProductForm
   from django.urls import reverse
   ```

3. **Membuat fungsi baru untuk menghasilkan  formulir yang dapat menambahkan data produk secara otomatis ketika data di-submit dari form**
   - Membuat fungsi baru dengan nama create_product yang menerima parameter request dan tambahkan kode berikut ini :
   ```python
   def create_product(request):
      form = ProductForm(request.POST or None)

      if form.is_valid() and request.method == "POST":
         form.save()
         return HttpResponseRedirect(reverse('main:show_main'))

      context = {'form': form}
      return render(request, "create_product.html", context)
   ```

4. **Mengubah fungsi show_main di berkas views.py**
   - Ubah menjadi seperti berikut :
   ```python
   def show_main(request):
      products = Product.objects.all()

      context = {
         'name': 'Pak Bepe', # Nama kamu
         'class': 'PBP A', # Kelas PBP kamu
         'products': products
      }

      return render(request, "main.html", context)
   ```

5. **Menambah import fungsi create_product yang sudah dibuat**
   - Buka urls.py yang ada di folder main kemudian tambahkan import fungsi
   ```python
   from main.views import show_main, create_product
   ```

6. **Mengakses fungsi yang sudah diimport sebelumnya**
   - Tambahkan path url ke dalam urlpatterns pada urls.py di main
   ```python
   path('create-product', create_product, name='create_product'),
   ```

7. **Membuat berkas HTML baru**
   - Buat berkas HTML baru dengan nama create_product.html pada direktori main/templates dan isi dengan kode berikut :
   ```html
   {% extends 'base.html' %} 

   {% block content %}
   <h1>Add New Product</h1>

   <form method="POST">
      {% csrf_token %}
      <table>
         {{ form.as_table }}
         <tr>
               <td></td>
               <td>
                  <input type="submit" value="Add Product"/>
               </td>
         </tr>
      </table>
   </form>

   {% endblock %}
   ```

8. **Menampilkan data produk dalam bentuk table serta tombol "Add New Product" yang akan redirect ke halaman form**
   - Buka main.html dan tambahkan kode berikut di dalam {% block content %}
   ```html
   ...
   <table>
      <tr>
         <th>Name</th>
         <th>Price</th>
         <th>Description</th>
         <th>Date Added</th>
      </tr>

      {% comment %} Berikut cara memperlihatkan data produk di bawah baris ini {% endcomment %}

      {% for product in products %}
         <tr>
               <td>{{product.name}}</td>
               <td>{{product.price}}</td>
               <td>{{product.description}}</td>
               <td>{{product.date_added}}</td>
         </tr>
      {% endfor %}
   </table>

   <br />

   <a href="{% url 'main:create_product' %}">
      <button>
         Add New Product
      </button>
   </a>

   {% endblock content %}
   ```

9. **Jalankan proyek Django dengan perintah python manage.py runserver dan bukalah http://localhost:8000 di browser**

## Mengembalikan data dalam bentuk XML dan JSON

1. **Menambahkan import HttpResponse dan Serializer**
   - Buka views.py yang ada pada folder main kemudian tambahkan import berikut :
   ```python
   from django.http import HttpResponse
   from django.core import serializers
   ```

2. **Membuat fungsi untuk XML dan JSON**
   - Buat fungsi baru yang menerima parameter request
   ```python
   def show_xml(request):
      data = Product.objects.all()
      return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")
   
   def show_json(request):
      data = Product.objects.all()
      return HttpResponse(serializers.serialize("json", data), content_type="application/json")
   ```

3. **Mengimport fungsi yang sudah dibuat**
   - Buka urls.py di folder main dan tambahkan import fungsi seperti berikut :
   ```python
   from main.views import show_main, create_product, show_xml, show_json
   ```

4. **Menambahkan path url ke urlpatterns untuk mengakses fungsi yang sudah diimport**
   - Berikut hal yang perlu ditambahkan :
   ```python
   ...
   path('xml/', show_xml, name='show_xml'), 
   path('json/', show_json, name='show_json'), 
   ...
   ```

5. **Jalankan proyek Django dengan perintah python manage.py runserver dan bukalah http://localhost:8000/json atau http://localhost:8000/xml  di browser untuk melihat hasilnya**

## Mengembalikan Data Berdasarkan ID dalam Bentuk XML dan JSON

1. **Membuat fungsi baru XML dan JSON**
   - Buat sebuah fungsi baru yang menerima parameter request dan id
   ```python
   def show_xml_by_id(request, id):
      data = Product.objects.filter(pk=id)
      return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

   def show_json_by_id(request, id):
    data = Product.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")
   ```

2. **Mengimport fungsi yang sudah dibuat**
   - Buka urls.py di folder main dan tambahkan import fungsi seperti berikut :
   ```python
   from main.views import show_main, create_product, show_xml, show_json, show_xml_by_id, show_json_by_id 
   ```

3. **Menambahkan path url ke urlpatterns untuk mengakses fungsi yang sudah diimport**
   - Berikut hal yang perlu ditambahkan :
   ```python
   ...
   path('xml/<int:id>/', show_xml_by_id, name='show_xml_by_id'),
   path('json/<int:id>/', show_json_by_id, name='show_json_by_id'), 
   ...
   ```

4. **Jalankan proyek Django dengan perintah python manage.py runserver dan bukalah http://localhost:8000/xml/[id] atau http://localhost:8000/json/[id] di browser untuk melihat hasilnya**

## Penggunaan Postman sebagai data viewer

1. **Jalankan server dengan perintah python manage.py runserver**

2. **Buka Postman dan buatlah sebuah request baru dengan method GET dan url http://localhost:8000/xml atau http://localhost:8000/json untuk mengetes apakah data terkirimkan dengan baik**

3. **Klik tombol Send untuk mengirimkan request tersebut**

4. **Hasil response dari request tersebut akan terlihat pada bagian bawah Postman.**

5. **untuk mengetes fungsi pengambilan data produk berdasarkan ID url dapat diubah menjadi http://localhost:8000/xml/[id] atau http://localhost:8000/json/[id]**

## Postman dengan Bentuk Data HTML
