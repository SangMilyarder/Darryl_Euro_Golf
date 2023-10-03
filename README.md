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
   - Buka settings.py yang berada di subdirektori Euro_Golf dan modifikasi baris TEMPLATES
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
   - Kode pada main.html diubah untuk menggunakan base.html sebagai template utama
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
![DJango Framework](https://github.com/SangMilyarder/Darryl_Euro_Golf/blob/staging/HTML.png)

## Postman dengan Bentuk Data XML
![DJango Framework](https://github.com/SangMilyarder/Darryl_Euro_Golf/blob/staging/XML.png)

## Postman dengan Bentuk Data JSON
![DJango Framework](https://github.com/SangMilyarder/Darryl_Euro_Golf/blob/staging/JSON.png)

## Postman dengan Bentuk Data XML by ID
![DJango Framework](https://github.com/SangMilyarder/Darryl_Euro_Golf/blob/staging/XML%20by%20ID.png)

## Postman dengan Bentuk Data JSON by ID
![DJango Framework](https://github.com/SangMilyarder/Darryl_Euro_Golf/blob/staging/JSON%20by%20ID.png)

## Tugas 4

## Pengertian Django UserCreationForm serta Kekurangan dan Kelebihannya

Django UserCreationForm adalah salah satu fitur yang disediakan oleh Django. Form ini bertujuan untuk memungkinkan pengguna untuk mendaftar ke situs web atau aplikasi yang dibuat dengan mudah. Form ini dapat digunakan untuk pembuatan dan validasi data pengguna, termasuk username, password, dan informasi lain yang dibutuhkan saat mendaftar.

**Kelebihan :**
- Mudah Digunakan:
Penggunaan Django UserCreationForm mudah digunakan, pengguna dapat mengintegrasikannya ke dalam aplikasi Djangonya dengan cepat tanpa perlu menulis banyak kode.
- Validasi Otomatis: Django UserCreationForm ini menyediakan validasi otomatis untuk berbagai hal seperti username dan password untuk membantu memastikan bahwa data yang dimasukkan oleh pengguna sesuai dengan aturan yang sudah ditentukan.
- Integrasi yang Mudah: UserCreationForm dapat dengan mudah diintegrasikan sehingga mudah untuk mengelola data pengguna, seperti penyimpanan password yang aman dan otentikasi pengguna.
- Kustomisasi: UserCreationForm dapat dikustomisasi sesuai dengan keperluan yang kita inginkan
- Keamanan: Password user disimpan di database, sehingga memastikan keamanan data pengguna.

**Kekurangan :**
- Tampilan Default: Tampilan default UserCreationForm sangat sederhana sehingga memerlukan kustomisasi jika ingin terlihat menarik di mata user.
- Fitur Terbatas: UserCreationForm memiliki fitur yang terbatas sehingga jika ingin lebih detail, penulisan kode diperlukan.
- Bahasa Bawaan: Default dari Django UserCreationForm adalah bahasa inggris sehingga jika ingin menggunakan bahasa lain, penyesuaian program diperlukan.
- Validasi Email: UserCreationForm tidak memvalidasi apakah alamat email yang dimasukkan oleh user valid atau tidak sehingga diperlukan validasi tambahan jika diperlukan.

**Sumber**: [DjangoForms](https://docs.djangoproject.com/en/3.2/topics/auth/default/#user-creation)

## Perbedaan antara autentikasi dan otorisasi dalam konteks Django

## Autentikasi:
- Autentikasi adalah proses verifikasi identitas pengguna yang mencoba mengakses sistem atau aplikasi. Autentikasi mencakup pengenalan pengguna melalui kombinasi username/email dan password atau metode otentikasi lainnya seperti SSO (Single Sign-On), OAuth, atau autentikasi berbasis token. Autentikasi bertujuan untuk memastikan bahwa pengguna yang mencoba mengakses sistem atau aplikasi adalah pengguna yang sah dan memiliki izin untuk masuk. Contoh pengaplikasiannya di Django adalah Django menyediakan sistem autentikasi yang kuat yang memungkinkan pengguna untuk mendaftar, masuk, dan keluar dari aplikasi. Ini juga mencakup pengelolaan sesi pengguna, penyimpanan password yang aman, serta berbagai metode otentikasi tambahan yang dapat diintegrasikan.

## Otorisasi:
- Otorisasi adalah proses mengontrol akses dan izin yang diberikan kepada pengguna setelah mereka berhasil diautentikasi. Otoriasasi menentukan apa yang dapat dilakukan oleh pengguna yang terautentikasi dalam sistem atau aplikasi. Otorisasi bertujuan untuk membatasi tindakan dan sumber daya yang dapat diakses oleh pengguna berdasarkan peran, izin, atau aturan yang sudah ditentukan. Contoh pengaplikasiannya di Django adalah Django memiliki sistem otorisasi yang memungkinkan kita untuk mendefinisikan peran dan izin pengguna. Kita dapat menentukan siapa yang dapat mengakses bagian-bagian tertentu dari aplikasi dan apa yang dapat dilakukan di dalamnya.

## Mengapa Autentikasi dan Otorisasi Penting? 
- **Keamanan**: Autentikasi memastikan bahwa hanya pengguna yang sah yang dapat mengakses sistem dan otorisasi berguna untuk membatasi akses pengguna berdasarkan izin yang diberikan.
- **Kontrol Akses**: Autentikasi dan otorisasi memberikan pengembang kontrol atas siapa yang dapat mengakses data dan fungsi tertentu dalam aplikasi. Hal ini memungkinkan untuk mengatur penggunaan aplikasi dengan lebih baik.
- **Pribadiasi Pengguna**: Autentikasi membantu melindungi identitas pengguna, sementara otorisasi memastikan bahwa data pribadi pengguna hanya dapat diakses oleh pihak yang berwenang.
- **Manajemen Pengguna**: Autentikasi dan otorisasi memungkinkan manajemen pengguna yang efisien, termasuk pendaftaran, penentuan peran, dan pengaturan izin.

**Sumber**: [DjangoForms](https://docs.djangoproject.com/en/4.2/topics/auth/)

## Cookies dalam konteks aplikasi web
Cookies adalah mekanisme penyimpanan data sederhana yang digunakan dalam aplikasi web.  Cookies biasanya berupa sepotong kecil data yang disimpan di sisi user (biasanya di browser pengguna) dan dikirimkan ke server dalam setiap permintaan HTTP. Cookies biasanya digunakan untuk:

- **Autentikasi**: Untuk mengidentifikasi pengguna yang telah login ke situs web.
- **Penyimpanan Preferensi Pengguna**: Untuk mengingat preferensi pengguna seperti bahasa atau tema.
- **Pelacakan Aktivitas Pengguna**: Untuk menganalisis perilaku pengguna dan memberikan pengalaman yang dipersonalisasi.
- **Penyimpanan Data Sesi**: Untuk mengelola data sesi pengguna.

## Django dan Pengelolaan Cookies

Django menggunakan cookies untuk mengelola data sesi pengguna. Di bawah ini adalah cara Django mengimplementasikan pengelolaan cookies:

- **Session Middleware**: Django memiliki middleware khusus yang disebut SessionMiddleware. Middleware ini mengelola cookies sesi pengguna secara otomatis. Ketika pengguna pertama kali mengakses situs web, Django akan membuat cookie sesi baru dengan ID sesi unik.
- **Penyimpanan Data Sesi**: Django menyediakan tempat penyimpanan sesi yang fleksibel. Anda dapat mengonfigurasi Django untuk menyimpan data sesi di berbagai tempat, termasuk dalam database, dalam cache, atau dalam file.
- **Fungsi Bawaan**: Django menyediakan fungsi bawaan seperti request.session yang memungkinkan Anda untuk menyimpan dan mengambil data sesi dengan mudah. Anda dapat menyimpan data seperti ID pengguna setelah autentikasi, preferensi pengguna, atau data sesi lainnya.
- **Keamanan**: Django secara otomatis mengatur cookie untuk melindungi privasi pengguna. Misalnya, Anda dapat mengonfigurasi cookie agar hanya dikirim melalui HTTPS untuk melindungi data sesi dari serangan yang mungkin terjadi saat mengirim data melalui koneksi yang tidak aman.

**Sumber**: [DjangoForms](https://docs.djangoproject.com/en/4.2/topics/http/sessions/)

## Keamanan Penggunaan Cookies dalam Pengembangan Web

Penggunaan cookies dalam pengembangan web aman jika diimplementasikan secara benar, tetapi tetap ada risiko potensial yang harus diwaspadai. Berikut adalah beberapa pertimbangan keamanan terkait penggunaan cookies:

- **Data Sensitif**: Cookies dapat digunakan untuk menyimpan data sensitif seperti token otentikasi, ID sesi, atau informasi pengguna. Data sensitif harus dipastikan sudah dienkripsi sebelum disimpan dalam cookies.
- **Enkripsi**: Menggunakan HTTPS (SSL/TLS) adalah penting untuk mengamankan pengiriman cookies antara klien dan server. Pengiriman cookies melalui koneksi HTTP tanpa enkripsi dapat menyebabkan pencurian data.
- **HttpOnly Flag**: Cookies yang disetel dengan atribut HttpOnly hanya dapat diakses oleh server dan tidak oleh skrip JavaScript di browser pengguna. Ini dapat membantu melindungi cookies dari serangan XSS (Cross-Site Scripting).
- **Secure Flag**: Atribut Secure pada cookies memastikan bahwa cookies hanya dikirimkan melalui koneksi HTTPS yang aman.
- **Path dan Domain**: Menggunakan atribut path dan domain dengan benar pada cookies dapat membantu mengendalikan area tempat cookies dapat digunakan.
- **Timeout Sesuai**: Cookies sesi harus memiliki waktu timeout yang sesuai untuk menghindari akses yang tidak diinginkan setelah pengguna keluar atau tidak aktif.

## Risiko Potensial:
- **Pencurian Cookies**: Cookies dapat menjadi target pencurian jika tidak dienkripsi atau jika ada celah keamanan dalam aplikasi yang memungkinkan pengambilan cookies oleh pihak yang tidak sah.
- **Pencurian Data**: Jika cookies mengandung data sensitif seperti token otentikasi, pencurian cookies dapat mengakibatkan akses tidak sah ke akun pengguna.
- **Tracking Pengguna**: Penggunaan cookies untuk pelacakan perilaku pengguna juga memiliki implikasi privasi. Pengguna mungkin merasa tidak nyaman jika data mereka terlalu intens dipantau dan dilacak.
- **Serangan CSRF**: Cookies dapat digunakan dalam serangan CSRF (Cross-Site Request Forgery) jika tidak dilindungi dengan benar.
- **Larangan Cookies**: Beberapa pengguna dapat melarang cookies di browser mereka, yang dapat memengaruhi fungsionalitas aplikasi web.

**Sumber**: [AppMaster](https://appmaster.io/id/blog/peran-cookie-dalam-pengembangan-web)

## Langkah mengimplementasikan checklist secara step-by-step

## Membuat Fungsi dan Form Registrasi

1. **Jalankan virtual environment terlebih dahulu**
   - Aktifkan lingkungan virtual (Mac OS): `source env/bin/activate`.

2. **Menambah import pada file views.py yang ada di subdirektori main**
   - Tambahkan import redirect, UserCreationForm, dan messages
   ```python
   from django.shortcuts import redirect
   from django.contrib.auth.forms import UserCreationForm
   from django.contrib import messages  
   ```

3. **Menambah fungsi baru pada file**
   - Tambahkan fungsi baru dengan nama register yang berguna untuk menghasilkan formulir registrasi secara otomatis dan menghasilkan akun pengguna ketika data di-submit dari form.
   ```python
   def register(request):
      form = UserCreationForm()

      if request.method == "POST":
         form = UserCreationForm(request.POST)
         if form.is_valid():
               form.save()
               messages.success(request, 'Your account has been successfully created!')
               return redirect('main:login')
      context = {'form':form}
      return render(request, 'register.html', context)
   ```

4. **Membuat berkas HTML baru**
   - Buat berkas HTML baru dengan nama register.html pada direktori main/templates dan isi dengan kode berikut :
   ```html
   {% extends 'base.html' %}

   {% block meta %}
      <title>Register</title>
   {% endblock meta %}

   {% block content %}  

   <div class = "login">
      
      <h1>Register</h1>  

         <form method="POST" >  
               {% csrf_token %}  
               <table>  
                  {{ form.as_table }}  
                  <tr>  
                     <td></td>
                     <td><input type="submit" name="submit" value="Daftar"/></td>  
                  </tr>  
               </table>  
         </form>

      {% if messages %}  
         <ul>   
               {% for message in messages %}  
                  <li>{{ message }}</li>  
                  {% endfor %}  
         </ul>   
      {% endif %}

   </div>  

   {% endblock content %}
   ```

5. **Mengimport fungsi yang sudah dibuat**
   - Buka urls.py di folder main dan tambahkan import fungsi seperti berikut :
   ```python
   from main.views import register
   ```

6. **Menambahkan path url ke urlpatterns untuk mengakses fungsi yang sudah diimport**
   - Berikut hal yang perlu ditambahkan :
   ```python
   path('register/', register, name='register'),
   ```

## Membuat Fungsi Login

1. **Menambah import pada file views.py yang ada di subdirektori main**
   - Tambahkan import authenticate dan login
   ```python
   from django.contrib.auth import authenticate, login
   ```

2. **Menambah fungsi baru pada file**
   - Tambahkan fungsi baru dengan nama login_user yang berguna untuk mengautentikasi pengguna yang ingin login.
   ```python
   def login_user(request):
      if request.method == 'POST':
         username = request.POST.get('username')
         password = request.POST.get('password')
         user = authenticate(request, username=username, password=password)
         if user is not None:
               login(request, user)
               return redirect('main:show_main')
         else:
               messages.info(request, 'Sorry, incorrect username or password. Please try again.')
      context = {}
      return render(request, 'login.html', context)
   ```

3. **Membuat berkas HTML baru**
   - Buat berkas HTML baru dengan nama login.html pada direktori main/templates dan isi dengan kode berikut :
   ```html
   {% extends 'base.html' %}

   {% block meta %}
      <title>Login</title>
   {% endblock meta %}

   {% block content %}

   <div class = "login">

      <h1>Login</h1>

      <form method="POST" action="">
         {% csrf_token %}
         <table>
               <tr>
                  <td>Username: </td>
                  <td><input type="text" name="username" placeholder="Username" class="form-control"></td>
               </tr>
                     
               <tr>
                  <td>Password: </td>
                  <td><input type="password" name="password" placeholder="Password" class="form-control"></td>
               </tr>

               <tr>
                  <td></td>
                  <td><input class="btn login_btn" type="submit" value="Login"></td>
               </tr>
         </table>
      </form>

      {% if messages %}
         <ul>
               {% for message in messages %}
                  <li>{{ message }}</li>
               {% endfor %}
         </ul>
      {% endif %}     
         
      Don't have an account yet? <a href="{% url 'main:register' %}">Register Now</a>

   </div>

   {% endblock content %}
   ```

4. **Mengimport fungsi yang sudah dibuat**
   - Buka urls.py di folder main dan tambahkan import fungsi seperti berikut :
   ```python
   from main.views import login_user
   ```

5. **Menambahkan path url ke urlpatterns untuk mengakses fungsi yang sudah diimport**
   - Berikut hal yang perlu ditambahkan :
   ```python
   path('login/', login_user, name='login'),
   ```

## Membuat Fungsi Logout

1. **Menambah import pada file views.py yang ada di subdirektori main**
   - Tambahkan import logout
   ```python
   from django.contrib.auth import logout
   ```

2. **Menambah fungsi baru pada file**
   - Tambahkan fungsi baru dengan nama logout_user yang berguna untuk melakukan mekanisme logout
   ```python
   def logout_user(request):
      logout(request)
      return redirect('main:login')
   ```

3. **Menambah kode di file main.html**
   - Tambahkan potongan kode di bawah ini setelah hyperlink tag untuk Add New Product
   ```html
   <a href="{% url 'main:logout' %}">
      <button>
         Logout
      </button>
   </a>
   ```

4. **Mengimport fungsi yang sudah dibuat**
   - Buka urls.py di folder main dan tambahkan import fungsi seperti berikut :
   ```python
   from main.views import logout_user
   ```

5. **Menambahkan path url ke urlpatterns untuk mengakses fungsi yang sudah diimport**
   - Berikut hal yang perlu ditambahkan :
   ```python
   path('logout/', logout_user, name='logout'),
   ```

## Merestriksi Akses Halaman Main

1. **Menambah import pada file views.py yang ada di subdirektori main**
   - Tambahkan import login_required
   ```python
   from django.contrib.auth.decorators import login_required
   ```

2. **Menambah kode di atas fungsi show_main**
   - Tambahkan kode @login_required(login_url='/login') di atas fungsi show_main agar halaman main hanya dapat diakses oleh pengguna yang sudah login (terautentikasi).
   ```python
   @login_required(login_url='/login')
   def show_main(request):
   ```

## Menggunakan Data dari Cookies

1. **Menambah import pada file views.py yang ada di subdirektori main**
   - Tambahkan import datetime
   ```python
   import datetime
   ```

2. **Menambah fungsi pada fungsi login_user**
   - Tambahkan fungsi untuk menambahkan cookie yang bernama last_login untuk melihat kapan terakhir kali pengguna melakukan login. Berikut kode yang ditambahkan :
   ```python
   if user is not None:
      login(request, user)
      response = HttpResponseRedirect(reverse("main:show_main")) 
      response.set_cookie('last_login', str(datetime.datetime.now()))
      return response
   ```

3. **Menambah kode pada fungsi show_main**
   - Tambahkan potongan kode 'last_login': request.COOKIES['last_login'] ke dalam variabel context. Berikut contohnya :
   ```python
   context = {
      'name': 'Pak Bepe',
      'class': 'PBP A',
      'products': products,
      'last_login': request.COOKIES['last_login'],
   }
   ```

4. **Mengubah fungsi logout_user**
   - Ubah fungsi logout_user menjadi seperti berikut :
   ```python
   def logout_user(request):
      logout(request)
      response = HttpResponseRedirect(reverse('main:login'))
      response.delete_cookie('last_login')
      return response
   ```

5. **Menambah kode pada file main.html**
   - Tambahkan potongan kode berikut di antara tabel dan tombol logout untuk menampilkan data last login
   ```html
   <h5>Sesi terakhir login: {{ last_login }}</h5>
   ```

## Menghubungkan Model Product dengan User

1. **Menambah import pada file models.py yang ada di subdirektori main**
   - Tambahkan import berikut ini
   ```python
   from django.contrib.auth.models import User
   ```

2. **Menambah kode di model product**
   - Tambahkan kode berikut ini
   ```python
   class Product(models.Model):
      user = models.ForeignKey(User, on_delete=models.CASCADE)
   ```

3. **Memodifikasi kode di file views.py**
   - Ubah kode pada fungsi create_product menjadi sebagai berikut:
   ```python
   def create_product(request):
   form = ProductForm(request.POST or None)

   if form.is_valid() and request.method == "POST":
      product = form.save(commit=False)
      product.user = request.user
      product.save()
      return HttpResponseRedirect(reverse('main:show_main'))
   ```

4. **Mengubah fungsi show_main**
   - Ubah fungsi show_main sebagai berikut:
   ```python
   def show_main(request):
      products = Product.objects.filter(user=request.user)

      context = {
         'name': request.user.username,
      ...
   ...
   ```

5. **Simpan semua perubahan kemudian lakukan migrasi model dengan python manage.py makemigrations**

6. **Pilih 1 untuk menetapkan default value untuk field user pada semua row yang telah dibuat pada basis data**

7. **Ketik angka 1 kembali untuk menetapkan user dengan ID 1 (yang sudah kita buat sebelumnya) pada model yang sudah ada**

8. **Lakukan python manage.py migrate untuk mengaplikasikan migrasi yang sudah dilakukan sebelumnya**

## Tugas 5

# Manfaat dari setiap element selector dan waktu yang tepat untuk menggunakannya

Berikut adalah panduan penggunaan selector dalam CSS beserta manfaat dan waktu yang tepat untuk menggunakannya.

## 1. Selector Universal (`*`)

**Manfaat:**
- Memilih semua elemen pada halaman
- Untuk mengatur gaya default pada seluruh elemen

**Kapan Menggunakannya:**
- Penggunaan selector universal dapat mempengaruhi semua elemen di halaman sehingga harus hati-hati dalam penggunaannya.
- Bisa digunakan untuk mengatur margin dan padding secara global.

**Contoh Penggunaan:**
```css
* {
    margin: 0;
    padding: 0;
}
```

## 2. Selector Elemen (Tag)

**Manfaat:**
- Memilih semua elemen dengan tag yang sesuai.
- Untuk mengganti gaya elemen-elemen yang memiliki tag yang sama.

**Kapan Menggunakannya:**
- Ketika ingin mengubah gaya elemen HTML dengan tag tertentu.

**Contoh Penggunaan:**
```css
p {
    font-size: 16px;
}
```

## 3. Selector Kelas (.kelas)

**Manfaat:**
- Memilih elemen-elemen dengan atribut class tertentu.
- Dapat digunakan untuk elemen dengan kelas yang sama di berbagai bagian halaman.

**Kapan Menggunakannya:**
- Ketika ingin mengganti gaya elemen dengan kelas tertentu.

**Contoh Penggunaan:**
```css
.button {
    background-color: #007bff;
    color: #fff;
}
```

## 4. Selector ID (#id)

**Manfaat:**
- Memilih elemen dengan atribut id tertentu.
- Harus unik di seluruh halaman.

**Kapan Menggunakannya:**
- Ketika ingin mengubah gaya elemen yang memiliki ID tertentu.

**Contoh Penggunaan:**
```css
#header {
    font-size: 24px;
}
```

## 5. Selector Attribute

**Manfaat:**
- Memilih elemen dengan atribut tertentu.
- Pemilihan elemen dengan nilai atribut tertentu.
- Pemilihan elemen dengan atribut spesifik.

**Kapan Menggunakannya:**
- Ketika ingin mengganti gaya elemen dengan nilai atribut tertentu.

**Contoh Penggunaan:**
```css
a[href^="http"] {
    color: #FF0000;
}
```

## 6. Selector Pseudo-Class (:pseudo-class)

**Manfaat:**
- Memilih elemen berdasarkan keadaan atau interaksi user.
- Berguna untuk mengubah gaya elemen saat hover atau saat berada dalam keadaan tertentu.

**Kapan Menggunakannya:**
- Ketika ingin mengganti gaya elemen berdasarkan interaksi pengguna.

**Contoh Penggunaan:**
```css
a:hover {
    color: #ff0000;
}
```

## 7. Selector Pseudo-Element (::pseudo-element)

**Manfaat:**
- Memilih bagian spesifik dari elemen.
- Digunakan untuk mengubah gaya elemen seperti teks yang pertama atau elemen yang terakhir.

**Kapan Menggunakannya:**
- Ketika ingin mengganti gaya elemen tertentu dalam elemen lain.

**Contoh Penggunaan:**
```css
p::first-line {
    font-weight: bold;
}
```

**Sumber**: [petanikode](https://www.petanikode.com/css-selektor/)

## Tag HTML5

**1. <header>**
Digunakan untuk mengelompokkan elemen-elemen yang berada di bagian atas sebuah halaman atau bagian dari halaman. Biasanya berisi judul, logo, dan elemen-elemen navigasi.

```html
<header>
    <h1>Halaman Utama</h1>
    <nav>
        <ul>
            <li><a href="#">Beranda</a></li>
            <li><a href="#">Tentang Kami</a></li>
            <li><a href="#">Kontak</a></li>
        </ul>
    </nav>
</header>
```

**2. <nav>**
Mengelompokkan elemen-elemen yang berisi menu navigasi atau tautan ke halaman-halaman terkait.

```html
<nav>
    <ul>
        <li><a href="#">Beranda</a></li>
        <li><a href="#">Produk</a></li>
        <li><a href="#">Kontak</a></li>
    </ul>
</nav>
```

**3. <main>**
Digunakan untuk mengelompokkan konten utama dari sebuah halaman web. Biasanya hanya ada satu elemen <main> dalam satu halaman.

```html
<main>
    <h1>Selamat Datang di Blog Kami</h1>
    <p>Ini adalah artikel terbaru kami...</p>
</main>
```

**4. <article>**
Mengelompokkan konten yang berdiri sendiri dan dapat berdiri sendiri, seperti artikel berita atau posting blog.

```html
<article>
    <h2>10 Tips untuk Mengoptimalkan Performa Website</h2>
    <p>Di dalam artikel ini, kami akan berbagi tips...</p>
</article>
```

**5. <section>**
Mengelompokkan konten terkait dalam sebuah halaman. Bisa digunakan untuk membuat bagian-bagian dalam artikel atau halaman.

```html
<section>
    <h2>Bagian 1</h2>
    <p>Ini adalah bagian pertama dari artikel kami...</p>
</section>
<section>
    <h2>Bagian 2</h2>
    <p>Ini adalah bagian kedua dari artikel kami...</p>
</section>
```

**6. <aside>**
Digunakan untuk mengelompokkan konten sampingan yang terkait dengan konten utama. Biasanya digunakan untuk sidebar atau iklan.

```html
<aside>
    <h3>Artikel Terpopuler</h3>
    <ul>
        <li><a href="#">10 Tips SEO</a></li>
        <li><a href="#">Cara Membuat Website</a></li>
    </ul>
</aside>
```

**7. <footer>**
Digunakan untuk mengelompokkan elemen-elemen yang berada di bagian bawah halaman atau bagian dari halaman. Biasanya berisi informasi hak cipta, tautan-tautan sosial, atau informasi kontak.

```html
<footer>
    <p>&copy; 2023 Nama Perusahaan. Hak Cipta Dilindungi.</p>
    <ul>
        <li><a href="#">Facebook</a></li>
        <li><a href="#">Twitter</a></li>
    </ul>
</footer>
```

## Perbedaan Antara Margin dan Padding dalam CSS

**Margin**
- margin adalah ruang di sekitar elemen, yaitu ruang antara elemen dengan elemen lain di sekitarnya.
- margin tidak memiliki latar belakang dan tidak berpengaruh pada tampilan elemen tersebut.
- margin digunakan untuk mengatur jarak antara elemen dengan elemen lain di sekitarnya, sehingga memengaruhi tata letak keseluruhan halaman.
- Mengubah margin akan memengaruhi elemen bersangkutan dan elemen lain di sekitarnya.

**Contoh penggunaan margin:**
```css
div {
    margin: 10px;
}
```

**Padding**
- Padding adalah ruang di dalam elemen, yaitu ruang antara konten elemen dan batas elemen tersebut.
- Padding dapat memiliki latar belakang dan berpengaruh pada tampilan elemen tersebut.
- Padding digunakan untuk mengatur jarak antara konten elemen dan batas elemen tersebut, sehingga memengaruhi tampilan elemen itu sendiri.
- Mengubah padding hanya akan memengaruhi elemen bersangkutan, tanpa memengaruhi elemen lain di sekitarnya.

**Contoh penggunaan padding:**
```css
div {
    padding: 10px;
}
```

## Perbedaan Antara Framework CSS Tailwind dan Bootstrap

**1. Pengertian:**

- CSS Tailwind adalah framework "utility-first," yang berfokus pada penggunaan kelas CSS yang dapat digunakan secara langsung dalam HTML untuk membangun tampilan. Hal ini memberikan fleksibilitas tinggi tetapi memerlukan lebih banyak penulisan kode HTML.

- Bootstrap adalah framework "component-first," yang berfokus pada komponen siap pakai yang dapat dengan mudah dimasukkan ke dalam proyek. Hal ini menghasilkan kode HTML yang lebih bersih tetapi mungkin memiliki sedikit kurang fleksibilitas.

**2. Penggunaan Kelas CSS:**

CSS Tailwind:
- Memerlukan penggunaan banyak kelas CSS dalam HTML untuk mengatur tampilan elemen. Hal ini memungkinkan tingkat kustomisasi tinggi tetapi dapat membuat markup HTML menjadi besar dan sulit dibaca.

Bootstrap:
- Menggunakan lebih sedikit kelas CSS dalam HTML karena komponennya sudah memiliki kelas-kelas yang telah ditentukan. Hal ini menghasilkan markup yang lebih bersih tetapi mungkin kurang fleksibel.

**3. Tingkat Kustomisasi:**

CSS Tailwind:
- Memberikan tingkat kustomisasi yang sangat tinggi. Anda dapat menyesuaikan setiap detail tampilan dengan mengedit konfigurasi atau menambahkan kelas tambahan sesuai kebutuhan.

Bootstrap:
- Lebih mudah digunakan untuk membangun situs web dengan tampilan yang konsisten karena komponennya sudah dibuat sebelumnya. Kustomisasi komponen Bootstrap mungkin memerlukan lebih banyak pekerjaan daripada Tailwind.

**4. Ukuran File:**

Tailwind CSS:
- File CSS lebih besar karena menghasilkan banyak kelas yang harus di-render oleh browser.

Bootstrap:
- File CSS lebih kecil karena hanya memuat komponen yang digunakan dalam proyek.

## Kapan Sebaiknya Menggunakan Bootstrap daripada Tailwind, dan Sebaliknya?

**Gunakan Bootstrap Ketika:**
- Ingin mengembangkan proyek dengan cepat dan memerlukan komponen siap pakai yang dapat disesuaikan serta menginginkan tampilan yang konsisten dan memiliki desain yang sudah dirancang dengan baik.
- Tidak ingin terlalu banyak menulis kode HTML dan CSS kustom.

**Gunakan Tailwind CSS Ketika:**
- Ingin tingkat kustomisasi yang sangat tinggi untuk tampilan program.
- Suka mengontrol setiap detail tampilan program melalui kelas-kelas CSS.
- Ingin menghindari file CSS yang besar dan hanya menghasilkan kode CSS yang dibutuhkan.