
---

# ⚽️ Tugas PBP – BolaBeliShop

## Implementasi Checklist

Proyek ini dibuat pada branch **master**. **main** hanya sebagai README

Link Tugas : https://dimas-abyan-bolabelishop.pbp.cs.ui.ac.id

Aku mengerjakan proyek ini dengan beberapa langkah:

1. **Membuat Proyek & Aplikasi**

   * Aku buat project bernama `bolabelishop` dan app `main`.
   * Tambahkan `main` ke `INSTALLED_APPS` di `settings.py`.

2. **Membuat Model**
   Aku mendefinisikan `Product` di `models.py`. Atribut wajib: `name`, `price`, `description`, `thumbnail`, `category`, `is_featured`. Atribut tambahan: `stock`, `brand`.

   ```python
   import uuid
   from django.db import models

   class Product(models.Model):
       CATEGORY_CHOICES = [
           ('jersey', 'Jersey'),
           ('sepatu', 'Sepatu'),
           ('bola', 'Bola'),
           ('aksesoris', 'Aksesoris'),
       ]

       id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
       name = models.CharField(max_length=255)
       price = models.IntegerField()
       description = models.TextField()
       thumbnail = models.URLField(blank=True, null=True)
       category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, default='jersey')
       is_featured = models.BooleanField(default=False)

       stock = models.PositiveIntegerField(default=0)
       brand = models.CharField(max_length=100, blank=True, null=True)

       def __str__(self):
           return f"{self.name} ({self.category})"
   ```

   Setelah itu jalanin:

   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

3. **Views & Template**
   Di `views.py`, aku bikin fungsi `show_main` untuk menampilkan identitas dan nama shop.
   Lalu di `main.html`, aku tampilkan datanya.

4. **Routing**
   Bikin `urls.py` di app `main` lalu hubungkan ke `urls.py` di project.

5. **Testing**
   Aku menambahkan `tests.py` untuk memastikan URL, template, dan model bekerja.

   ```python
   from django.test import TestCase, Client
   from .models import Product

   class MainTest(TestCase):
       def test_main_url_is_exist(self):
           response = Client().get('/')
           self.assertEqual(response.status_code, 200)

       def test_main_using_main_template(self):
           response = Client().get('/')
           self.assertTemplateUsed(response, 'main.html')

       def test_nonexistent_page(self):
           response = Client().get('/halaman_yang_tidak_ada/')
           self.assertEqual(response.status_code, 404)

       def test_product_creation(self):
           product = Product.objects.create(
               name="Sepatu Bola",
               price=500000,
               description="Sepatu bola edisi terbatas",
               category="sepatu",
               is_featured=True,
               stock=10,
               brand="Nike"
           )
           self.assertEqual(product.name, "Sepatu Bola")
           self.assertEqual(product.category, "sepatu")
           self.assertTrue(product.is_featured)

       def test_product_default_values(self):
           product = Product.objects.create(
               name="Jersey Random",
               price=200000,
               description="Jersey tim bola misterius"
           )
           self.assertEqual(product.category, "jersey")
           self.assertEqual(product.stock, 0)
           self.assertFalse(product.is_featured)
   ```

**Kesimpulan Step 1**: Django enak dipakai karena struktur jelas, meskipun awalnya ribet. Dengan step-by-step, semua checklist bisa dikerjakan rapi.

---

## Soal 2 – Bagan Aplikasi

Struktur aplikasi yang kugunakan:

Pertama, klien (misalnya pengguna lewat browser) mengirimkan sebuah request melalui URL. Request ini masuk ke server, lalu diteruskan ke Django. Django kemudian mengecek pola URL yang sudah didefinisikan di urls.py. Jika cocok, Django akan memanggil fungsi yang ada di views.py.

Di dalam views.py, logika aplikasi dijalankan. Jika data dibutuhkan, views.py akan melakukan query ke models.py yang sudah terhubung dengan database. Models bertugas mengelola data (menyimpan, mengambil, atau mengupdate). Setelah data diperoleh, views.py akan mengirimkan data tersebut ke template (misalnya file main.html). Template ini berfungsi untuk menampilkan data dalam bentuk halaman web yang rapi.

Hasil render dari template kemudian dikembalikan lagi ke Django, diteruskan ke server, dan akhirnya dikirim kembali ke klien sebagai sebuah halaman web utuh.

**Kesimpulan:**
- `urls.py` bertugas mengarahkan request ke view yang sesuai.
- `views.py` menjadi jembatan utama yang mengatur logika antara models (data) dan template (tampilan).
- `models.py` fokus pada manajemen data.
- `templates` bertugas menampilkan data dalam bentuk HTML yang bisa dipahami pengguna.
Dengan alur ini, Django memisahkan peran tiap komponen dengan jelas, sehingga aplikasi lebih terstruktur dan mudah dikembangkan.


**Kesimpulan Step 2**: Django sudah menyediakan struktur standar, sehingga aplikasi bisa berkembang rapi tanpa bingung taruh file di mana.

---

## Soal 3 – Alur `settings.py`, `urls.py`, `views.py`

* **`settings.py`**: mendaftarkan app dan konfigurasi global.
* **`urls.py` (proyek)**: mengarahkan URL utama ke `main/urls.py`.
* **`urls.py` (app)**: mengarahkan URL spesifik ke fungsi di `views.py`.
* **`views.py`**: menyiapkan data dan memanggil template.
* **`main.html`**: menampilkan hasilnya.

**Kesimpulan Step 3**: 
File settings.py adalah pusat konfigurasi dari sebuah proyek Django. Semua pengaturan seperti daftar aplikasi yang dipakai, database, middleware, sampai ALLOWED_HOSTS ada di sana. Bisa dibilang ini fondasi proyek Django.
Lalu, urls.py berperan sebagai "tempat masuk” aplikasi. Setiap kali pengguna mengetikkan URL, Django akan mengecek apakah ada pola yang sesuai. Kalau ada, request diteruskan ke fungsi tertentu di views.py.
Views.py kemudian bertugas mengolah data yang dibutuhkan. Jika perlu akses database, ia akan memanggil models.py. Setelah itu hasilnya dikirim ke template (HTML) agar bisa ditampilkan.

---

## Soal 4 – Perbedaan `makemigrations` dan `migrate`

* `makemigrations`: menyiapkan file perubahan model blueprint.
* `migrate`: benar-benar menerapkan perubahan ke database.

**Kesimpulan Step 4**: `makemigrations` adalah langkah membuat catatan perubahan model. Django menyimpannya dalam file migration sebagai blueprint. Setelah itu, `migrate` digunakan untuk benar-benar mengeksekusi perubahan blueprint tadi ke dalam database.

---

## Soal 5 – Alasan Menggunakan Django

Aku memilih Django karena:

* Sudah lengkap (ORM, template engine, auth).
* Struktur proyek rapi.
* Banyak dokumentasi & komunitas yang beginner.

**Kesimpulan Step 5**: Django dipilih karena menggunakan Python, bahasa yang sudah familiar sejak awal kuliah di FASILKOM UI. Django juga punya framework yang sudah menyediakan banyak fitur bawaan: ORM untuk database, template engine, autentikasi, hingga keamanan.


---

## Step 6 – Feedback Asdos

Menurutku asdos membantu banget, penjelasan singkat tapi jelas. Masalah kecil saja seperti kurangnya koma tetap dibantu dengan baik dan tanpa merendahkan mahasiswa yang kesulitan.

---

# Tugas 3 PBP

### 1. Mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform?

Data delivery diperlukan agar data dapat diakses di berbagai tempat dan platform. Data yang dikirim dari client ke server dapat disimpan ke database, kemudian data tersebut bisa dilihat dan digunakan di platform yang berbeda seperti web, mobile app, atau sistem lain yang membutuhkan data tersebut.

### 2. Mana yang lebih baik antara XML dan JSON? Mengapa JSON lebih populer?

JSON lebih populer karena:

- JSON lebih mudah dibaca oleh manusia
- JSON lebih ringan sehingga proses read/write lebih cepat
- JSON merupakan bawaan JavaScript, jadi bagi developer yang menggunakan JavaScript akan lebih mudah menggunakan JSON
- JSON menggunakan 30-40% lebih sedikit bytes dibandingkan XML untuk data yang sama. Dalam era mobile-first, setiap byte sangat berharga.

- JSON dapat langsung di-parse menjadi JavaScript object tanpa library tambahan.

- JSON lebih mudah dibaca dan ditulis oleh developer. Struktur yang bersih mengurangi kemungkinan error.

- Parsing JSON lebih cepat dibandingkan XML karena struktur yang lebih sederhana.

**Namun XML masih unggul dalam:**
- Validation yang ketat melalui XML Schema
- Metadata dan namespace support
- Document markup yang kompleks


### 3. Fungsi method `is_valid()` pada form Django

`is_valid()` berfungsi untuk memvalidasi apakah input form sudah sesuai dengan aturan field pada models maupun aturan Django tentang form tersebut.

Jika `is_valid()` tidak digunakan, maka ketika user menginput form dan data masuk ke database, bisa menyebabkan database crash karena data yang tidak sesuai format atau requirements.


### 4. Pentingnya `csrf_token` dalam form Django

CSRF atau "Cross-Site Request Forgery" adalah jenis serangan dimana penyerang mengirim request ke server saat user sedang login ke sebuah website, sehingga penyerang dapat mengirim request atas nama pengguna tersebut.

`csrf_token` dibuat agar serangan CSRF tidak terjadi, dengan cara server mengirim kode CSRF kepada client, dan ketika client melakukan request, client harus mengembalikan kode tersebut ke server.

Ketika form tidak menggunakan `csrf_token`, maka penyerang dapat melakukan request kepada server tanpa verifikasi dengan form tersebut.

**Skenario serangan tanpa CSRF protection:**
1. User login ke BolaBelishop di tab browser
2. Di tab lain, user membuka website jahat yang berisi form tersembunyi
3. Form tersebut secara otomatis submit request ke BolaBelishop untuk membuat pesanan mahal
4. Karena browser otomatis mengirim cookies, server mengira request valid dari user

**Bagaimana CSRF token bekerja:**
Django menggunakan "double submit cookie" yang menyematkan token rahasia dalam form yang harus cocok dengan yang disimpan di session. Website jahat tidak bisa mengakses token ini karena Same-Origin Policy.

**Konsekuensi tanpa CSRF protection:**
- Unauthorized actions atas nama user
- Data manipulation tanpa sepengetahuan user


**Cara penyerang memanfaatkan:**
- Malicious ads yang berisi hidden forms
- Compromised websites yang menyuntikkan malicious code

### 5. Implementasi Checklist Step-by-Step

## ✅ Dokumentasi Implementasi

### **Step 1: Membuat 4 Fungsi Views untuk Data Delivery**

**Views yang diimplementasi di `main/views.py`:**

```python
def show_xml(request):
    product_list = Product.objects.all()
    xml_data = serializers.serialize("xml", product_list)
    return HttpResponse(xml_data, content_type="application/xml")

def show_json(request):
    product_list = Product.objects.all()
    json_data = serializers.serialize("json", product_list)
    return HttpResponse(json_data, content_type="application/json")

def show_xml_by_id(request, product_id):
    product_item = Product.objects.filter(pk=product_id)
    xml_data = serializers.serialize("xml", product_item)
    return HttpResponse(xml_data, content_type="application/xml")

def show_json_by_id(request, product_id):
    product_item = Product.objects.get(pk=product_id)
    json_data = serializers.serialize("json", [product_item])
    return HttpResponse(json_data, content_type="application/json")
```

**Penjelasan implementasi:**
- Menggunakan `serializers.serialize()` dari Django untuk konversi object ke XML/JSON
- Content-type headers yang tepat untuk response
- Error handling untuk ID yang tidak ditemukan
- Konsisten menggunakan `product_id` sebagai parameter

### **Step 2: Membuat Routing URL**

**URL patterns di `main/urls.py`:**

```python
urlpatterns = [
    path('', show_main, name='show_main'),
    path('create-product/', create_product, name='create_product'),
    path('product/<str:id>/', show_product, name='show_product'),
    path('xml/', show_xml, name='show_xml'),
    path('json/', show_json, name='show_json'),
    path('xml/<str:product_id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<str:product_id>/', show_json_by_id, name='show_json_by_id'),
]
```

**Perbaikan yang dilakukan:**
- Mengganti parameter `news_id` menjadi `product_id` untuk konsistensi
- Struktur URL yang RESTful dan intuitif
- Proper naming convention untuk URL names

### **Step 3: Halaman dengan Tombol "Add" dan "Detail"**

**Implementation di `main.html`:**

```html
<!-- Tombol Add Product -->
<a href="{% url 'main:create_product' %}">
  <button>+ Add Product</button>
</a>

<!-- Loop untuk setiap produk -->
{% for product in product_list %}
<div>
  <h2><a href="{% url 'main:show_product' product.id %}">{{ product.name }}</a></h2>
  <p><b>{{ product.get_category_display }}</b>{% if product.is_featured %} | 
    <b>Featured</b>{% endif %} | <i>{{ product.created_at|date:"d M Y H:i" }}</i> 
    | Views: {{ product.product_views }}</p>
  
  {% if product.thumbnail %}
  <img src="{{ product.thumbnail }}" alt="thumbnail" width="150" height="100">
  {% endif %}
  
  <p>{{ product.description|truncatewords:25 }}...</p>
  <p><a href="{% url 'main:show_product' product.id %}"><button>Read More</button></a></p>
</div>
{% endfor %}
```

**Fitur yang diimplementasi:**
- Navigation button ke form create product
- Clickable product names yang mengarah ke detail
- Display kategori, featured status, dan view count
- Thumbnail support dengan conditional rendering
- Truncated description untuk overview yang bersih

### **Step 4: Halaman Form untuk Menambah Objek**

**Form definition di `main/forms.py`:**

```python
class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ["name", "price", "description", "category", "thumbnail", "is_featured"]
```

**View untuk handle form di `views.py`:**

```python
def create_product(request):
    form = ProductForm(request.POST or None)
    
    if form.is_valid() and request.method == "POST":
        form.save()
        return redirect('main:show_main')
    
    context = {'form': form}
    return render(request, "create_product.html", context)
```

**Template `create_product.html`:**

```html
{% extends 'base.html' %} 
{% block content %}
<h1>Add Product</h1>

<form method="POST">
  {% csrf_token %}
  <table>
    {{ form.as_table }}
    <tr>
      <td></td>
      <td><input type="submit" value="Add Product" /></td>
    </tr>
  </table>
</form>
{% endblock %}
```

**Flow yang diimplementasi:**
1. GET request → Tampilkan form kosong
2. POST request → Validasi data → Simpan → Redirect ke homepage
3. CSRF protection dengan `{% csrf_token %}`
4. Form validation dengan `form.is_valid()`

### **Step 5: Halaman Detail Objek Model**

**View untuk detail product:**

```python
def show_product(request, id):
    product = get_object_or_404(Product, pk=id)
    product.increment_views()  # Auto increment view counter
    
    context = {'product': product}
    return render(request, "product_detail.html", context)
```

**Template `product_detail.html`:**

```html
{% extends 'base.html' %}
{% block content %}
<p><a href="{% url 'main:show_main' %}"><button>← Back to Product List</button></a></p>

<h1>{{ product.name }}</h1>
<p><b>{{ product.get_category_display }}</b>{% if product.is_featured %} | 
    <b>Featured</b>{% endif %} | <b>Price: Rp {{ product.price }}</b></p>

{% if product.thumbnail %}
<img src="{{ product.thumbnail }}" alt="Product thumbnail" width="300">
{% endif %}

<p>{{ product.description }}</p>
<p><b>Price:</b> Rp {{ product.price }}</p>
{% if product.brand %}
<p><b>Brand:</b> {{ product.brand }}</p>
{% endif %}
<p><b>Stock:</b> {{ product.stock }} items</p>
{% endblock content %}
```

**Fitur yang diimplementasi:**
- Back navigation ke product list
- Complete product information display
- Conditional rendering untuk optional fields
- Auto view counter increment
- Responsive image display

## 🔗 URL Endpoints yang Dapat Diakses

| URL | Fungsi | Output Format |
|-----|--------|---------------|
| `/` | Homepage dengan daftar produk | HTML |
| `/create-product/` | Form tambah produk | HTML |
| `/product/<id>/` | Detail produk | HTML |
| `/xml/` | Semua produk | XML |
| `/json/` | Semua produk | JSON |
| `/xml/<product_id>/` | Produk spesifik | XML |
| `/json/<product_id>/` | Produk spesifik | JSON |

## 🏗️ Struktur Project

```
BolaBelishop/
├── BolaBelishop/
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
├── main/
│   ├── models.py          # Product model dengan UUID
│   ├── views.py           # 7 views (3 HTML + 4 API)
│   ├── urls.py            # URL routing
│   ├── forms.py           # ProductForm
│   ├── tests.py           # Unit tests
│   └── templates/
│       ├── main.html           # Homepage
│       ├── create_product.html # Form page
│       └── product_detail.html # Detail page
├── templates/
│   └── base.html          # Base template
└── manage.py
```

Screenshot URL di postman.

- xml & xml id
  ![Alt Text](https://github.com/ByteDAD/BolaBeliShop/blob/main/XML_Pic_Normal.jpeg?raw=true)
  
  ![Alt Text](https://github.com/ByteDAD/BolaBeliShop/blob/main/XML_Pic_ID.jpeg?raw=true)
  
- json & json id
  ![Alt Text](https://github.com/ByteDAD/BolaBeliShop/blob/main/Json_Pic_Normal.jpeg?raw=true)

  ![Alt Text](https://github.com/ByteDAD/BolaBeliShop/blob/main/Json_Pic_ID.jpeg?raw=true)

--- 

# Tugas 4 PBP

### Apa itu Django AuthenticationForm? Jelaskan juga kelebihan dan kekurangannya.
---
- Django AuthenticationForm adalah form bawaan Django yang digunakan untuk proses login user, yang secara otomatis memvalidasi username dan password terhadap database. Setelah validasi berhasil, form ini akan mengembalikan user object yang sudah terautentikasi.
- Kelebihannya Django AuthenticationForm adalah form sudah siap pakai dengan built-in security (CSRF protection, password validation), mudah diimplementasikan, dan terintegrasi langsung dengan sistem authentication Django. Memiliki validasi otomatis untuk kredensial user dan penanganan error yang informatif, sehingga developer tidak perlu membuat validasi login dari nol. Dapat di-customize sesuai kebutuhan aplikasi, seperti menambahkan field tambahan atau mengubah tampilan form.
- Kekurangan Django AuthenticationForm adalah tidak menyediakan styling UI dan hanya memiliki fitur basic login, sehingga untuk fitur advanced seperti "Remember Me" atau social login perlu implementasi tambahan.

### Apa perbedaan antara autentikasi dan otorisasi? Bagaiamana Django mengimplementasikan kedua konsep tersebut?
---
- Autentikasi adalah proses pengecekan kredensial untuk membuktikan bahwa user adalah orang yang benar-benar memiliki akun tersebut, biasanya menggunakan kombinasi username/email dan password.
- Otorisasi adalah langkah selanjutnya setelah login berhasil, yaitu menentukan fitur atau data mana saja yang boleh diakses oleh user berdasarkan role atau permission yang dimilikinya.
- Django menangani autentikasi menggunakan sistem `django.contrib.auth` dengan fungsi seperti `authenticate()` untuk validasi kredensial dan `login()` untuk membuat session, ditambah middleware yang mengelola status user di setiap request.
- Untuk otorisasi, Django menyediakan sistem permission berbasis model dan group, dimana developer bisa menggunakan decorator `@login_required`, `@user_passes_test`, atau method `user.has_perm()` untuk membatasi akses ke view atau resource tertentu.
- Django secara otomatis membuat 4 permission dasar (create, read, update, delete) untuk setiap model, dan developer juga bisa membuat custom permission sesuai kebutuhan bisnis aplikasinya.

### Apa saja kelebihan dan kekurangan session dan cookies dalam konteks menyimpan state di aplikasi web?
---
- **Kelebihan** cookies adalah implementasinya sangat straightforward dan tidak membutuhkan resource server untuk penyimpanan, serta dapat bertahan lama di browser user bahkan setelah browser ditutup sehingga cocok untuk fitur "Remember Me".
- **Kekurangan cookies** meliputi batasan ukuran hanya 4KB per cookie, rentan terhadap manipulasi karena tersimpan di client-side, dan dapat menimbulkan privacy concerns karena data bisa diakses oleh JavaScript atau dicuri melalui various attack vectors.
- **Kelebihan session** adalah tingkat keamanan yang lebih tinggi karena data aktual disimpan di server dan hanya session identifier yang dikirim ke client, plus kapasitas penyimpanan yang tidak terbatas untuk data state yang bisa dibilang kompleks.
- **Kekurangan session** termasuk konsumsi memory server yang lebih besar untuk menyimpan session data, masalah *scalability* atau skalabilitas pada aplikasi multi-server, dan jika session ID tercuri maka attacker masih bisa mengakses session tersebut hingga expired.

### Apakah penggunaan cookies aman secara default dalam pengembangan web, atau apakah ada risiko potensial yang harus diwaspadai? Bagaimana Django menangani hal tersebut?
---
- Cookies memiliki kerentanan keamanan karena data tersimpan di sisi client (browser) dalam bentuk plain text, sehingga rentan terhadap serangan seperti session hijacking, XSS attacks, dan CSRF yang dapat mencuri informasi sensitif user.
- Risiko utama cookies meliputi kemungkinan data penting seperti password atau token dapat dibaca oleh script jahat, serta dapat dimanipulasi atau dicuri melalui network sniffing jika tidak menggunakan HTTPS.
- Django mengatasi masalah ini dengan implementasi session-based authentication dimana data sensitif disimpan di server, sedangkan cookie hanya berisi session key yang berfungsi sebagai penghubung antara client dan server.
- Django juga menerapkan security measures seperti CSRF protection token, secure cookie flags (httpOnly, secure), dan session expiry untuk meminimalkan risiko keamanan pada cookie yang digunakan.
- Dengan pendekatan ini, **meskipun cookie dicuri**, attacker hanya mendapatkan session ID yang memiliki masa berlaku terbatas dan tidak berisi informasi kredensial user secara langsung.


### Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
---
### 1. Implementasi Fungsi Register

**Langkah pertama**, import library yang diperlukan di `views.py`:
```python
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
```

**Kemudian buat fungsi register**:
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

Fungsi ini menggunakan `UserCreationForm` dari Django yang sudah menyediakan field Username dan Password untuk registrasi user baru. Setelah berhasil register, user akan diarahkan ke halaman login.

**Tambahkan routing** di `urls.py`:
```python
path('register/', register, name='register'),
```

**Buat template `register.html`** untuk menampilkan form registrasi.

### 2. Implementasi Fungsi Login

**Import library tambahan** di `views.py`:
```python
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login
import datetime
from django.http import HttpResponseRedirect
from django.urls import reverse
```

**Buat fungsi login_user**:
```python
def login_user(request):
   if request.method == 'POST':
      form = AuthenticationForm(data=request.POST)

      if form.is_valid():
        user = form.get_user()
        login(request, user)
        response = HttpResponseRedirect(reverse("main:show_main"))
        response.set_cookie('last_login', str(datetime.datetime.now()))
        return response

   else:
      form = AuthenticationForm(request)
   context = {'form': form}
   return render(request, 'login.html', context)
```

Fungsi ini menggunakan `AuthenticationForm` untuk validasi kredensial, kemudian menggunakan fungsi `login()` dari Django untuk membuat session. Saat login berhasil, akan disimpan cookie `last_login` untuk tracking.

**Tambahkan routing** dan **buat template `login.html`** untuk form login.

### 3. Implementasi Fungsi Logout

**Buat fungsi logout_user**:
```python
def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response
```

Fungsi ini menggunakan `logout(request)` untuk menghapus session user, kemudian redirect ke halaman login sambil menghapus cookie `last_login`.

**Tambahkan button logout di template**:
```html
<a href="{% url 'main:logout' %}">
  <button>Logout</button>
</a>
```

### 4. Menghubungkan Model Product dengan User

**Tambahkan field user di `models.py`**:
```python
from django.contrib.auth.models import User

class Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    # field lainnya...
```

**Update fungsi create_product di `views.py`**:
```python
def create_product(request):
    form = ProductForm(request.POST or None)

    if form.is_valid() and request.method == 'POST':
        product_entry = form.save(commit = False)
        product_entry.user = request.user
        product_entry.save()
        return redirect('main:show_main')

    context = {'form': form}
    return render(request, "create_product.html", context)
```

Dengan `commit=False`, object Product dibuat tapi belum disimpan ke database. Kemudian field `user` diisi dengan `request.user` (user yang sedang login) sebelum disimpan.

### 5. Menampilkan Informasi User yang Logged In

**Update context di fungsi show_main**:
```python
@login_required(login_url='/login')
def show_main(request):
    filter_type = request.GET.get("filter", "all")

    if filter_type == "all":
        product_list = Product.objects.all()
    else:
        product_list = Product.objects.filter(user=request.user)

    context = {
        'npm' : '2406432633',
        'name': 'Dimas Abyan Diasta', 
        'class': 'PBP C',
        'product_list': product_list,
        'last_login': request.COOKIES.get('last_login', 'Never')
    }

    return render(request, "main.html", context)
```

**Tambahkan di template `main.html`**:
```html
<h5>Sesi terakhir login: {{ last_login }}</h5>
```

Variable `last_login` mengambil nilai dari cookie yang di-set saat login. Jika cookie tidak ada, akan menampilkan "Never".

### 6. Menambahkan Decorator @login_required

**Tambahkan decorator pada fungsi yang memerlukan login**:
```python
from django.contrib.auth.decorators import login_required

@login_required(login_url='/login')
def show_main(request):
    # implementation...

@login_required(login_url='/login') 
def create_product(request):
    # implementation...
```

Decorator ini memastikan hanya user yang sudah login yang dapat mengakses fungsi tersebut. Jika belum login, user akan diarahkan ke halaman login.

### 7. Fitur Filtering Product

**Implementasi filter "My Articles" vs "All Articles"**:
```python
filter_type = request.GET.get("filter", "all")

if filter_type == "all":
    product_list = Product.objects.all()
else:
    product_list = Product.objects.filter(user=request.user)
```

**Tambahkan button filter di template**:
```html
<a href="?filter=all">
  <button type="button">All Articles</button>
</a>
<a href="?filter=my">
  <button type="button">My Articles</button>
</a>
```

Dengan implementasi ini, user dapat melihat semua produk atau hanya produk yang dibuat oleh user tersebut.
