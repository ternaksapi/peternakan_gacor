Nama           : Muhammad Yusuf Haikal

NPM            : 2206081490

Kelas          : PBP F

Link Adapable  :https://peternakan-gacor.adaptable.app/

# Tugas 2

## Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
Berikut adalah penjelasan cara implementasi  unuk masing - masing step pada checklist:

### Membuat sebuah proyek Django baru & membuat aplikasi dengan nama main pada proyek tersebut
- Untuk membuat sebuah proyek Django baru, buat sebuah direktori untuk proyek. Untuk tugas ini, direktori utama akan dinamakan ```peternakan_gacor```.
- Pada tugas ini, saya mengaktifkan virtual environment dengan cara pertama - tama buat virtual environment dengan menjalankan perintah ```python -m venv env``` lalu jalankan virtual environtment dengan menjalankan perintah ```env\Scripts\activate.bat```.
- Untuk proyek ini, buat file yang bernama ```requirements.txt``` yang berisikan dependencies yang akan diinstal dan kemudian digunakan pada proyek. Berikut isi dari file :
```
django
gunicorn
whitenoise
psycopg2-binary
requests
urllib3
```
- Install dependencies dengan menjalankan perintah ```pip install -r requirements.txt```

- Buat proyek Django dengan menjalankan command ```django-admin startproject peternakan_gacor```

- Sebelum membuat aplikasi ```main```, edit file ```settings.py``` dengan menambahkan ```ALLOWED_HOSTS = ["*"]``` untuk menambahkan akses untuk semua host, memudahkan proses deployment.

- Buat aplikasi main dengan menjalankan ```python manage.py startapp main``` lalu daftarkan aplikasi main kedalam file ```settings.py```.
```
    INSTALLED_APPS = [
    ...,
    'main',
    ...
]
```

### Melakukan routing pada proyek agar dapat menjalankan aplikasi main. 
- Routing pada proyek dilakukan dengan menambahkan rute URL kedalam file `urls.py` yang terdapat dalam direktori ** proyek ** yang kemudian dihubungkan ke tampilan main. Tambahkan pola url ke dalam `urlpatterns`.
```
from django.contrib import admin
from django.urls import path, include
from main.views import show_main

urlpatterns = [
    path('admin/', admin.site.urls),
    path('main/', include('main.urls')),
    path('', show_main, name='show_main')
]
```
- Pada kode diatas, saya menambahkan dua baris kode, yaitu `path('main/', include('main.urls'))` dan `path('', show_main, name='show_main')` yang bertujuan untuk menertapkan rute dasar untuk app `main`.

### Membuat model pada aplikasi main dengan nama Item
- Buat `models.py` yang memiliki atribut sesuai dengan kebutuhan aplikasi saya. Dalam kasus ini, terdapat 4 atribut yang saya masukkan, `name`, `amount`, dan `description`.
```
from django.db import models

class Items(models.Model):
    name = models.CharField(max_length=255)
    amount = models.IntegerField()
    description = models.TextField()
```
- Lakukan migrasi lalu aplikasikan ke basis data dengan menjalankan perintah 
```
python manage.py makemigrations
```
lalu 
```
python manage.py migrate
```

### Membuat sebuah fungsi pada views.py untuk dikembalikan ke dalam sebuah template HTML yang menampilkan nama aplikasi serta nama dan kelas.
-  Siapkan template HTML yang akan ditempilkan pada halaman aplikasi. Buat folder bernama `template` dalam direktori `main`, lalu buat file yang bernama `template.html`. Pada proyek ini, template yang akan saya gunakan seperti berikut:
```
<h1>Welcome to Peternakan Gacor!</h1>
<h4>Peternakan terbaik se-kukusan</h4>
<br>
{% for product in products %}
    <div>
        <h5>Nama Barang:</h5>
        <p>{{ product.name }}</p>
        <h5>Deskripsi Barang:</h5>
        <p>{{ product.description }}</p>
        <h5>Jumlah Barang:</h5>
        <p>{{ product.amount }} buah</p>
    </div>
    <br>
    <br>
{% endfor %}

<h5>Muhammad Yusuf Haikal PBP F 22060801490</h5>
```

- Buat fungsi pada file `views.py` yang akan menyajikan data kedalam template. Pada file ini, terdapat data yang disimpan dalam list of dictionaries yang bernama `products_data`. Kemudian, fungsi `show_main` akan mengambil data pada list `products_data` yang kemudian akan di-* render * ke tampilan HTML.
```
from django.shortcuts import render

# Create your views here.
products_data = [
    {
        'name': 'Padi',
        'description': 'Tanaman padi (Oryza sativa L.) adalah tanaman penghasil beras yang merupakan sumber karbohidrat bagi sebagian penduduk dunia',
        'amount': 30,
    },
    {
        'name': 'Jagung',
        'description': 'Tanaman jagung (Zea mays) adalah salah satu tanaman serealia penting di dunia dan digunakan untuk berbagai keperluan.',
        'amount': 40,
    },
    {
        'name': 'Daging Wagyu',
        'description': 'Daging wagyu adalah daging sapi yang berasal dari Jepang. Daging ini memiliki tekstur yang lembut dan lemak yang melimpah.',
        'amount': 5,
    },
    {
        'name': 'Susu Kambing',
        'description': 'Susu kambing adalah susu yang dihasilkan oleh kambing. Susu kambing memiliki kandungan nutrisi yang lebih tinggi dibandingkan dengan susu sapi.',
        'amount' : 0,
    },
    {
        'name': 'Telur Ayam',
        'description': 'Telur ayam adalah telur yang dihasilkan oleh ayam. Telur ayam memiliki kandungan nutrisi yang tinggi dan dapat dikonsumsi dalam berbagai bentuk.',
        'amount' : 60
    }
]

def show_main(request):
    context = {
        'products' : products_data,
    }

    return render(request, "main.html", context)
```

### Membuat sebuah routing pada urls.py aplikasi main untuk memetakan fungsi yang telah dibuat pada views.py.
- Pada tahap ini, lakukan perubahan pada file `urls.py` pada direktori ** main **. Ini dilakukan untuk mengatur rute URL yang terkait dengan aplikasi main itu sendiri. 
```
from django.urls import path
from main.views import show_main

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
]
```

### Melakukan deployment ke Adaptable terhadap aplikasi yang sudah dibuat
- Untuk melakukan deployment, pertama lakukan push kedalam repository github yang kita gunakan untuk proyek ini. Lakukan `add`, `commit`, `push`.
- Selanjutnya, untuk tugas ini kita akan menggunakan platform Adaptable untuk melakukan deployment. Login menggunakan akun github yang terkait dengan repository yang telah dibuat. Ikuti instruksi yang disediakan pada website.

### Membuat sebuah README.md yang berisi tautan menuju aplikasi Adaptable yang sudah di-deploy
- Buat file README.md pada direktori proyek yang berisi tentang penjelasan masing - masing step, serta link menuju aplikasi. Terdapat sedikit kendala yaitu akun Adaptable seluruh mahasiswa UI telah didisable oleh pembuat website Adaptable, sehingga saya tidak dapt menyimpan tautan menuju aplikasi saya.


## Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html
![Ilustrasi bagan](bagan.png)

- Disini, terdapat 2 file `urls.py`, yang satu terdapat pada direktori app `main` yang menghubungkan rute setiap aplikasi dengan fungsi `views` yang sesuai, dan yang satu terdapat pada  direktori proyek yang berfungsi sebagai penghubung rute dasar dengan rute yang telah didefiniskan pada `urls.py` pada direktori `main`.
- `views.py` berisi fungsi yang mengatur tampilan data dari model yang kemudian dihubungkan dengan template.
- `models.py` berisi basis data dari aplikasi.
- Berkas html, dalam hal ini `template.html` menjadi penentu tampilan yang akan muncul pada aplikasi.

## Jelaskan mengapa kita menggunakan virtual environment? Apakah kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment?
Secara singkat, kita menggunakan virtual environment untuk mengisolasi linkgungan dari proyek yang kita buat, agar dependencies yang kita ingin gunakan tidak saling bertabrakan dengan dependencies yang sebelumnya mungkin sudah ada sebelumnya. Kita tetap bisa membuat aplikasi web tanpa menggunakan virtual environment, hanya saja kemungkinan terjadinya kendala besar karena masalah dependencies tadi.

## Jelaskan apakah itu MVC, MVT, MVVM dan perbedaan dari ketiganya.
- MVC atau Model-View-Controller merupakan pola desain pengembangan perangkat lunak yang menggunakan Model, View, dan Controller sebagai kerangka dasar pengembangan.
- MVT atau Model-View-Template merupakan pola desain pengembangan perangkat lunak yang menggunakan Model, View, dan Template sebagai kerangka dasar pengembangannya.
- MVVM atau Model-View-ViewModel merupakan pola desain pengembangan perangkat lunak.

Perbedaan dari ketiganya terdapat pada peran dan hubungan antara komponen tersebut,
MVC memiliki Controller yang mengatur logika aplikasi.
MVT menggantikan Controller dengan Template yang mengatur tampilan.
MVVM menggunakan ViewModel sebagai perantara antara Model dan View untuk mengisolasi logika tampilan.
