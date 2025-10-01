
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

--- 


# Tugas 5 PBP

### Jika terdapat beberapa CSS selector untuk suatu elemen HTML, jelaskan urutan prioritas pengambilan CSS selector tersebut!
---


Urutan prioritas CSS selector mengikuti konsep **specificity** (kekhususan), dimana semakin spesifik suatu selector, semakin tinggi prioritasnya. Berikut adalah urutan prioritas dari yang tertinggi ke terendah:

1. **Inline styles** - CSS yang ditulis langsung di atribut `style` pada elemen HTML memiliki prioritas tertinggi
   ```html
   <div style="color: red;">Text</div>
   ```

2. **ID selector** - Selector dengan tanda `#` memiliki prioritas tinggi
   ```css
   #header { color: blue; }
   ```

3. **Class, attribute, dan pseudo-class selector** - Selector dengan `.`, `[]`, atau `:` 
   ```css
   .nav-item { color: green; }
   [type="text"] { border: 1px solid; }
   a:hover { color: purple; }
   ```

4. **Element dan pseudo-element selector** - Selector berdasarkan tag HTML
   ```css
   div { color: black; }
   p::first-line { font-weight: bold; }
   ```

5. **Universal selector** - Selector `*` memiliki prioritas paling rendah
   ```css
   * { margin: 0; }
   ```

**Perhitungan Specificity:**
- Inline style: 1000 points
- ID selector: 100 points  
- Class/attribute/pseudo-class: 10 points
- Element/pseudo-element: 1 point

**Contoh perhitungan:**
```css
/* Specificity: 1 (1 element) */
div { color: red; }

/* Specificity: 10 (1 class) */
.container { color: blue; }

/* Specificity: 100 (1 ID) */
#main { color: green; }

/* Specificity: 111 (1 ID + 1 class + 1 element) */
#main .container div { color: purple; }
```

**Catatan penting:** 
- Jika specificity sama, maka aturan yang ditulis terakhir yang akan digunakan
- `!important` dapat mengoverride semua aturan specificity, tapi sebaiknya dihindari karena membuat CSS sulit di-maintain

### Mengapa responsive design menjadi konsep yang penting dalam pengembangan aplikasi web? Berikan contoh aplikasi yang sudah dan belum menerapkan responsive design, serta jelaskan mengapa!
---

Responsive design adalah konsep penting dalam pengembangan web modern karena beberapa alasan krusial:

**Alasan Penting Responsive Design:**

- **Diversitas Device** = User mengakses website dari berbagai perangkat dengan ukuran layar yang berbeda dan bervariasi (smartphone 5", tablet 10", laptop 15", desktop 27", dll)

-  **Mobile-First Era** = Lebih dari 60% traffic internet global berasal dari mobile devices, sehingga pengalaman mobile yang buruk akan kehilangan banyak user


-  **Cost Efficiency** = Satu codebase yang responsive lebih efisien dibanding maintain website terpisah untuk mobile dan desktop

-  **User Experience** = User expect seamless experience across devices, website yang tidak responsive akan meningkatkan bounce rate dan membuat user tidak tertarik

**Contoh Aplikasi yang Sudah Menerapkan Responsive Design:**

**BolaBelishop (Project ini):**
- Navbar yang collapse menjadi hamburger menu di mobile
- Grid layout product cards yang adjust dari 3 columns (desktop) ke 1 column (mobile)
- Form input yang stretch full-width di mobile
- Touch friendly button sizes di mobile devices

**YouTube:**
- Video player yang resize sesuai layar
- Navigation yang berubah dari sidebar (desktop) ke bottom navigation (mobile)
- Thumbnail grid yang adaptive

**Twitter/X:**
- Timeline yang adjust antara multi-column (desktop) dan single column (mobile)
- Sidebar yang hide di mobile dan muncul sebagai drawer menu
- Compose tweet button yang float di mobile

**Contoh Aplikasi yang Belum Menerapkan Responsive Design:**

**Website Pemerintah Lama:**
- Masih banyak website instansi pemerintah yang fixed-width
- Text terlalu kecil untuk dibaca di mobile
- Button terlalu kecil untuk di-tap dengan jari
- Horizontal scrolling yang mengganggu UX

**Old Banking Websites:**
- Layout yang break di mobile
- Table data yang overflow dan tidak scrollable
- Form yang sulit diisi karena tidak ter-optimize untuk mobile keyboard


**Mengapa aplikasi lama belum menerapkan:**
- Dibuat sebelum era mobile dominan
- Budget terbatas untuk redesign
- Technical debt yang besar untuk migration (terutama di Indonesia)
- Kurangnya awareness tentang importance of mobile UX


### Jelaskan perbedaan antara margin, border, dan padding, serta cara untuk mengimplementasikan ketiga hal tersebut!
---


Margin, border, dan padding adalah tiga komponen dalam **CSS Box Model** yang mengatur spacing dan layout elemen HTML. Perbedaannya:

**1. Margin (Ruang Luar)**
- Space di **luar** border elemen
- Membuat jarak antara elemen dengan elemen lain di sekitarnya
- Bersifat transparan (tidak memiliki warna background)
- Dapat memiliki nilai negatif
- Margin collapse bisa terjadi (vertical margins dapat merge)

**2. Border (Garis Tepi)**
- Garis yang mengelilingi padding dan content
- Berada di antara margin dan padding
- Dapat dikustomisasi (warna, style, thickness)
- Menambah dimensi total elemen

**3. Padding (Ruang Dalam)**
- Space di **dalam** border, antara border dan content
- Membuat jarak antara content dengan border elemen
- Mengikuti warna background elemen
- Tidak bisa memiliki nilai negatif
- Menambah area clickable elemen

**Visualisasi Box Model:**
```
+------------------------------------------+
|           Margin (transparan)            |
|  +------------------------------------+  |
|  |    Border (colored line)           |  |
|  |  +------------------------------+  |  |
|  |  |  Padding (bg-color)          |  |  |
|  |  |  +------------------------+  |  |  |
|  |  |  |      Content           |  |  |  |
|  |  |  +------------------------+  |  |  |
|  |  +------------------------------+  |  |
|  +------------------------------------+  |
+------------------------------------------+
```

**Cara Implementasi:**

**A. Shorthand Property (Semua Sisi Sekaligus):**

```css
/* Margin */
.element {
    margin: 20px;                    /* semua sisi 20px */
    margin: 10px 20px;               /* vertical 10px, horizontal 20px */
    margin: 10px 20px 30px;          /* top 10px, horizontal 20px, bottom 30px */
    margin: 10px 20px 30px 40px;     /* top, right, bottom, left (clockwise) */
}

/* Border */
.element {
    border: 2px solid black;         /* width style color */
    border: 1px dashed #ccc;
}

/* Padding */
.element {
    padding: 15px;                   /* semua sisi 15px */
    padding: 10px 20px;              /* vertical 10px, horizontal 20px */
    padding: 10px 20px 30px 40px;    /* top, right, bottom, left */
}
```

**B. Individual Properties:**

```css
.element {
    /* Margin per sisi */
    margin-top: 10px;
    margin-right: 20px;
    margin-bottom: 15px;
    margin-left: 25px;
    
    /* Border per sisi dan property */
    border-top: 2px solid red;
    border-right-color: blue;
    border-bottom-style: dashed;
    border-left-width: 3px;
    
    /* Padding per sisi */
    padding-top: 5px;
    padding-right: 10px;
    padding-bottom: 8px;
    padding-left: 12px;
}
```

**C. Contoh Praktis dalam BolaBelishop:**

```css
/* Card Product */
.product-card {
    margin: 20px;              /* jarak antar card */
    border: 1px solid #e5e7eb; /* garis tepi card */
    padding: 20px;             /* ruang dalam card */
    border-radius: 8px;        /* rounded corners */
}

/* Button */
.btn-primary {
    margin: 10px 5px;          /* jarak button dengan elemen lain */
    border: 2px solid #8b5cf6; /* border ungu */
    padding: 12px 24px;        /* ruang dalam button */
}

/* Form Input */
.form-input {
    margin-bottom: 16px;       /* jarak antar input field */
    border: 2px solid #d1d5db; /* border abu-abu */
    padding: 12px;             /* ruang dalam input */
}
```


### Jelaskan konsep flex box dan grid layout beserta kegunaannya!
---

**Flexbox (Flexible Box Layout)** dan **Grid Layout** adalah dua sistem layout modern di CSS yang mempermudah pembuatan layout yang complex dan responsive.



## 1. Flexbox

**Konsep:**
Flexbox adalah sistem layout satu dimensi (1D) yang mengatur elemen dalam satu arah, baik horizontal (row) atau vertical (column). Flexbox sangat cocok untuk mengatur komponen dalam satu baris atau satu kolom.

**Karakteristik Flexbox:**
- One dimensional layout (row atau column)
- Distribusi space yang fleksibel
- Alignment yang mudah (center, space-between, dll)
- Order elemen dapat diubah tanpa mengubah HTML

**Properties Utama:**

**Container Properties:**
```css
.flex-container {
    display: flex;
    
    /* Direction */
    flex-direction: row | column | row-reverse | column-reverse;
    
    /* Wrapping */
    flex-wrap: nowrap | wrap | wrap-reverse;
    
    /* Horizontal alignment */
    justify-content: flex-start | center | flex-end | space-between | space-around;
    
    /* Vertical alignment */
    align-items: stretch | flex-start | center | flex-end | baseline;
    
    /* Multiple rows alignment */
    align-content: flex-start | center | flex-end | space-between | space-around;
    
    /* Gap between items */
    gap: 20px;
}
```

**Item Properties:**
```css
.flex-item {
    /* Grow factor */
    flex-grow: 1;
    
    /* Shrink factor */
    flex-shrink: 1;
    
    /* Base size */
    flex-basis: 200px;
    
    /* Shorthand */
    flex: 1 1 200px; /* grow shrink basis */
    
    /* Individual alignment */
    align-self: auto | flex-start | center | flex-end | stretch;
    
    /* Order */
    order: 2;
}
```

**Penggunaan Cases Flexbox:**
1. Navbar dengan menu items yang distribute evenly
2. Card layout dalam satu row yang responsive
3. Centering content vertical dan horizontal
4. Button groups dengan equal width
5. Form layouts dengan label dan input alignment

**Contoh Implementasi di BolaBelishop:**

```css
/* Navbar dengan Flexbox */
.navbar {
    display: flex;
    justify-content: space-between;  /* logo kiri, menu kanan */
    align-items: center;             /* vertical center */
    padding: 1rem;
}

/* Filter Buttons */
.filter-section {
    display: flex;
    gap: 12px;                       /* jarak antar button */
    flex-wrap: wrap;                 /* wrap ke baris baru jika sempit */
}

/* Card Footer dengan Flexbox */
.card-footer {
    display: flex;
    justify-content: space-between;  /* "Read more" kiri, "Edit/Delete" kanan */
    align-items: center;
    padding-top: 16px;
    border-top: 1px solid #e5e7eb;
}
```



## 2. Grid Layout

**Konsep:**
Grid adalah sistem layout dua dimensi (2D) yang mengatur elemen dalam rows dan columns sekaligus. Grid sangat powerful untuk membuat layout halaman yang complex.

**Karakteristik Grid:**
- Two-dimensional layout (rows dan columns)
- Precise placement control
- Complex layouts dengan code yang simple
- Responsive grid dengan media queries

**Properties Utama:**

**Container Properties:**
```css
.grid-container {
    display: grid;
    
    /* Define columns */
    grid-template-columns: 200px 1fr 2fr;
    grid-template-columns: repeat(3, 1fr);
    grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
    
    /* Define rows */
    grid-template-rows: 100px auto 50px;
    
    /* Gap between items */
    gap: 20px;
    row-gap: 20px;
    column-gap: 10px;
    
    /* Alignment */
    justify-items: start | center | end | stretch;
    align-items: start | center | end | stretch;
    
    /* Grid areas (template) */
    grid-template-areas:
        "header header header"
        "sidebar content content"
        "footer footer footer";
}
```

**Item Properties:**
```css
.grid-item {
    /* Span multiple columns/rows */
    grid-column: 1 / 3;        /* dari line 1 ke line 3 */
    grid-row: 2 / 4;
    
    /* Shorthand */
    grid-column: span 2;       /* span 2 columns */
    grid-row: span 3;          /* span 3 rows */
    
    /* Named areas */
    grid-area: header;
    
    /* Individual alignment */
    justify-self: start | center | end | stretch;
    align-self: start | center | end | stretch;
}
```

**Use Cases Grid:**
1. Page layout (header, sidebar, content, footer)
2. Photo gallery dengan item sizes yang berbeda
3. Dashboard dengan widgets
4. Magazine-style layouts
5. Product catalog dengan responsive columns

**Contoh Implementasi di BolaBelishop:**

```css
/* Product Grid - Responsive */
.product-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
    gap: 24px;
    padding: 2rem;
}

/* Responsive breakpoints */
@media (min-width: 768px) {
    .product-grid {
        grid-template-columns: repeat(2, 1fr);
    }
}

@media (min-width: 1024px) {
    .product-grid {
        grid-template-columns: repeat(3, 1fr);
    }
}

/* Dashboard Layout */
.dashboard {
    display: grid;
    grid-template-areas:
        "header header header"
        "sidebar main main"
        "footer footer footer";
    grid-template-columns: 250px 1fr 1fr;
    grid-template-rows: auto 1fr auto;
    min-height: 100vh;
}

.header { grid-area: header; }
.sidebar { grid-area: sidebar; }
.main { grid-area: main; }
.footer { grid-area: footer; }
```

---

## Perbandingan Flexbox vs Grid

| Aspek | Flexbox | Grid |
|-------|---------|------|
| Dimensi | 1D (row atau column) | 2D (row dan column) |
| Use Case | Component-level layout | Page-level layout |
| Control | Content-based sizing | Track-based sizing |
| Best For | Navigation, cards dalam row | Complete page layouts, galleries |
| Learning Curve | Lebih mudah | Lebih complex |

**Kapan Menggunakan Apa:**
- **Flexbox**: Untuk layout komponen kecil, alignment sederhana, distribusi space dalam satu arah
- **Grid**: Untuk layout halaman utuh, gallery, dashboard, atau layout yang membutuhkan control yang presisi di 2 dimensi

**Kombinasi Flexbox + Grid:**
Dalam praktik, sering kita kombinasikan keduanya:
```css
/* Grid untuk overall layout */
.page-layout {
    display: grid;
    grid-template-columns: 250px 1fr;
}

/* Flexbox untuk navbar di dalam grid */
.navbar {
    display: flex;
    justify-content: space-between;
}

/* Grid untuk product cards */
.product-list {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
}

/* Flexbox untuk content dalam card */
.product-card {
    display: flex;
    flex-direction: column;
    justify-content: space-between;
}
```

### Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial)!
---


### 1. Implementasi Fungsi Edit dan Delete Product

**Step 1: Membuat Fungsi Edit di `views.py`**

```python
@login_required(login_url='/login')
def edit_products(request, id):
    # Get product by ID, return 404 if not found
    product = get_object_or_404(Product, pk=id)
    
    # Security: Pastikan user hanya bisa edit product miliknya
    if product.user != request.user:
        messages.error(request, 'You are not authorized to edit this product.')
        return redirect('main:show_main')
    
    # Create form with existing product data
    form = ProductForm(request.POST or None, instance=product)
    
    if form.is_valid() and request.method == 'POST':
        form.save()
        messages.success(request, 'Product updated successfully!')
        return redirect('main:show_main')

    context = {
        'form': form,
        'product': product
    }
    return render(request, "edit_products.html", context)
```

**Step 2: Membuat Fungsi Delete di `views.py`**

```python
@login_required(login_url='/login')
def delete_product(request, id):
    # Get product by ID
    product = get_object_or_404(Product, pk=id)
    
    # Security: Pastikan user hanya bisa delete product miliknya
    if product.user != request.user:
        messages.error(request, 'You are not authorized to delete this product.')
        return redirect('main:show_main')
    
    # Delete product
    product.delete()
    messages.success(request, 'Product deleted successfully!')
    
    return HttpResponseRedirect(reverse('main:show_main'))
```

**Step 3: Menambahkan URL Routing di `urls.py`**

```python
urlpatterns = [
    # existing paths...
    path('product/<uuid:id>/edit', edit_products, name='edit_products'),
    path('product/<uuid:id>/delete', delete_product, name='delete_product'),
]
```

**Step 4: Menambahkan Button Edit & Delete di `card_product.html`**

```html
{% if user.is_authenticated and product.user == user %}
  <div class="flex items-center justify-between pt-4 border-t border-purple-100">
    <a href="{% url 'main:show_product' product.id %}" class="text-purple-600">
      Read more
    </a>
    <div class="flex space-x-2">
      <a href="{% url 'main:edit_products' product.id %}" class="text-blue-600">
        Edit
      </a>
      <a href="{% url 'main:delete_product' product.id %}" 
         onclick="return confirm('Are you sure?')" 
         class="text-red-600">
        Delete
      </a>
    </div>
  </div>
{% endif %}
```

**Penjelasan:**
- Menggunakan `get_object_or_404()` untuk handling error jika product tidak ditemukan
- Authorization check memastikan user hanya bisa edit/delete product miliknya sendiri
- Confirmation dialog pada delete untuk mencegah accidental deletion
- Messages untuk user feedback setelah action berhasil

---

### 2. Kustomisasi Desain dengan Tailwind CSS

**Step 1: Setup Tailwind di `base.html`**

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    {% block meta %} {% endblock meta %}
    
    <!-- Tailwind CSS CDN -->
    <script src="https://cdn.tailwindcss.com"></script>
    
    <!-- Custom CSS -->
    <link rel="stylesheet" href="{% static 'css/global.css' %}"/>
</head>
<body>
    {% block content %} {% endblock content %}
</body>
</html>
```

**Step 2: Kustomisasi Login Page**

Menggunakan gradient background dan card-based design:

```html
<div class="bg-gradient-to-br from-blue-50 to-indigo-50 w-full min-h-screen flex items-center justify-center">
  <div class="max-w-md w-full">
    <div class="bg-white rounded-lg border border-gray-200 p-8 shadow-lg">
      <h1 class="text-2xl font-bold text-gray-900 mb-2">Sign In</h1>
      <p class="text-gray-600 mb-8">Welcome back to BolaBelishop</p>
      
      <!-- Form here -->
    </div>
  </div>
</div>
```

**Step 3: Customize Register Page**

Similar design dengan login tapi dengan additional fields:

```html
<div class="bg-gradient-to-br from-blue-50 to-indigo-50 min-h-screen flex items-center justify-center">
  <div class="max-w-md w-full">
    <div class="bg-white border border-gray-200 rounded-lg p-8 shadow-lg">
      <h2 class="text-2xl font-semibold text-gray-900 mb-2">Join Us</h2>
      <p class="text-gray-500 mb-8">Create your BolaBelishop account</p>
      
      <!-- Form here -->
    </div>
  </div>
</div>
```

**Step 4: Kustomisasi Form Pages (Create & Edit Product)**

```html
<div class="bg-gradient-to-br from-slate-800 via-purple-900 to-slate-900 min-h-screen">
  <div class="max-w-3xl mx-auto px-4 py-8">
    <div class="bg-white rounded-lg border border-gray-200 p-8">
      <h1 class="text-2xl font-bold text-gray-900 mb-2">Create New Product</h1>
      <p class="text-gray-600 mb-8">Share your football product</p>
      
      <form method="POST" class="space-y-6">
        {% csrf_token %}
        <!-- Form fields -->
        
        <div class="flex gap-4 pt-6 border-t">
          <a href="{% url 'main:show_main' %}" 
             class="px-6 py-3 border rounded-md">Cancel</a>
          <button type="submit" 
                  class="flex-1 bg-purple-600 text-white px-6 py-3 rounded-md">
            Publish Product
          </button>
        </div>
      </form>
    </div>
  </div>
</div>
```

**Step 5: Custom CSS untuk Form Styling di `global.css`**

```css
.form-style form input, form textarea, form select {
    width: 100%;
    padding: 0.5rem;
    border: 2px solid #bcbcbc;
    border-radius: 0.375rem;
}

.form-style form input:focus, form textarea:focus, form select:focus {
    outline: none;
    border-color: #2563eb;
    box-shadow: 0 0 0 3px rgba(37, 99, 235, 0.1);
}

.form-style input[type="checkbox"]:checked {
    background-color: #2563eb;
    border-color: #2563eb;
}
```

---

### 3. Kustomisasi Halaman Daftar Product

**Step 1: Responsive Product Grid**

```html
<div class="bg-gradient-to-br from-slate-800 via-purple-900 to-slate-900 pt-16 min-h-screen">
  <div class="max-w-7xl mx-auto px-4 py-8">
    
    <!-- Header -->
    <div class="mb-8">
      <h1 class="text-3xl font-bold text-white mb-2">Latest Football Product</h1>
      <p class="text-gray-300">Stay updated with the latest football products</p>
    </div>

    <!-- Filter Section -->
    <div class="flex justify-between mb-8 bg-gradient-to-r from-purple-50 to-pink-50 rounded-lg border p-4">
      <div class="flex space-x-3">
        <a href="?" class="{% if request.GET.filter == 'all' or not request.GET.filter %} bg-purple-600 text-white {% else %} bg-white text-gray-700 border {% endif %} px-4 py-2 rounded-md">
          All Product
        </a>
        <a href="?filter=my" class="{% if request.GET.filter == 'my' %} bg-purple-600 text-white {% else %} bg-white text-gray-700 border {% endif %} px-4 py-2 rounded-md">
          My Product
        </a>
      </div>
      
      {% if user.is_authenticated %}
        <div class="text-sm text-gray-300">
          Last login: {{ last_login }}
        </div>
      {% endif %}
    </div>

    <!-- Product Grid -->
    {% if not product_list %}
      <div class="bg-gradient-to-br from-purple-50 to-pink-50 rounded-lg border p-12 text-center">
        <div class="w-32 h-32 mx-auto mb-4">
          <img src="{% static 'image/no-product.gif' %}" alt="No product" class="w-full h-full object-contain">
        </div>
        <h3 class="text-lg font-medium text-gray-900 mb-2">No product found</h3>
        <p class="text-gray-500 mb-6">Be the first to share football product</p>
        <a href="{% url 'main:create_product' %}" class="inline-flex px-4 py-2 bg-purple-600 text-white rounded-md">
          Create product
        </a>
      </div>
    {% else %}
      <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
        {% for product in product_list %}
          {% include 'card_product.html' with product=product %}
        {% endfor %}
      </div>
    {% endif %}
  </div>
</div>
```

**Penjelasan:**
- Dark gradient background 
- Filter buttons dengan active state styling
- Conditional rendering untuk empty state dengan animated GIF
- Responsive grid: 1 column (mobile) → 2 columns (tablet) → 3 columns (desktop)

---

### 4. Desain Card Product 

**File: `card_product.html`**

```html
{% load static %}
<article class="bg-gradient-to-br from-purple-50 to-pink-50 rounded-lg border border-purple-100 hover:shadow-xl transition-all duration-300 overflow-hidden">
  
  <!-- Thumbnail Section -->
  <div class="aspect-[16/9] relative overflow-hidden">
    {% if product.thumbnail %}
      <img src="{{ product.thumbnail }}" alt="{{ product.name }}" 
           class="w-full h-full object-cover">
    {% else %}
      <div class="w-full h-full bg-gradient-to-br from-green-100 to-green-200 flex items-center justify-center">
        <svg class="w-20 h-20 text-green-300" fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" 
                d="M4 16l4.586-4.586a2 2 0 012.828 0L16 16m-2-2l1.586-1.586a2 2 0 012.828 0L20 14m-6-6h.01M6 20h12a2 2 0 002-2V6a2 2 0 00-2-2H6a2 2 0 00-2 2v12a2 2 0 002 2z"></path>
        </svg>
      </div>
    {% endif %}

    <!-- Category Badge -->
    <div class="absolute top-3 left-3">
      <span class="inline-flex items-center px-2.5 py-0.5 rounded-md text-xs font-medium bg-purple-600 text-white shadow-sm">
        {{ product.get_category_display }}
      </span>
    </div>

    <!-- Featured Badge -->
    {% if product.is_featured %}
    <div class="absolute top-3 right-3">
      <span class="inline-flex items-center px-2 py-1 rounded text-xs font-medium bg-yellow-100 text-yellow-800">
        ⭐ Featured
      </span>
    </div>
    {% endif %}
  </div>

  <!-- Content Section -->
  <div class="p-5">
    <!-- Meta Info -->
    <div class="flex items-center text-sm text-gray-500 mb-3">
      <time datetime="{{ product.created_at|date:'c' }}">
        {{ product.created_at|date:"M j, Y" }}
      </time>
      <span class="mx-2">•</span>
      <span>{{ product.product_views }} views</span>
    </div>

    <!-- Title -->
    <h3 class="text-lg font-semibold text-gray-900 mb-3 line-clamp-2">
      <a href="{% url 'main:show_product' product.id %}" 
         class="hover:text-purple-600 transition-colors">
        {{ product.name }}
      </a>
    </h3>

    <!-- Description -->
    <p class="text-gray-600 text-sm line-clamp-3 mb-4">
      {{ product.description|truncatewords:20 }}
    </p>

    <!-- Action Buttons -->
    {% if user.is_authenticated and product.user == user %}
      <div class="flex items-center justify-between pt-4 border-t border-purple-100">
        <a href="{% url 'main:show_product' product.id %}" 
           class="text-purple-600 hover:text-purple-700 font-medium text-sm">
          Read more
        </a>
        <div class="flex space-x-2">
          <a href="{% url 'main:edit_products' product.id %}" 
             class="text-blue-600 hover:text-blue-700 text-sm">
            Edit
          </a>
          <a href="{% url 'main:delete_product' product.id %}" 
             class="text-red-600 hover:text-red-700 text-sm">
            Delete
          </a>
        </div>
      </div>
    {% else %}
      <div class="pt-4 border-t border-purple-100">
        <a href="{% url 'main:show_product' product.id %}" 
           class="text-purple-600 hover:text-purple-700 font-medium text-sm">
          Read more →
        </a>
      </div>
    {% endif %}
  </div>
</article>
```

**Fitur Unik dalam Card:**
1. **Gradient Background**: Soft purple-pink gradient untuk aesthetic appeal
2. **Hover Effects**: Shadow yang meningkat saat di-hover
3. **Aspect Ratio Box**: Thumbnail dengan ratio 16:9 
4. **Fallback Image**: SVG icon jika tidak ada thumbnail
5. **Conditional Actions**: Edit/Delete buttons hanya muncul untuk owner
6. **Smooth Transitions**: Semua hover effects menggunakan transition-colors

---

### 5. Responsive Navigation Bar (Navbar)

**File: `navbar.html`**

```html
<nav class="fixed top-0 left-0 w-full bg-gradient-to-r from-slate-900 via-purple-900 to-slate-900 border-b border-purple-700 shadow-lg z-50">
  <div class="max-w-7xl mx-auto px-6">
    <div class="flex items-center justify-between h-16">
      
      <!-- Logo -->
      <div class="flex items-center">
        <h1 class="text-xl font-semibold text-white">
          <span class="text-purple-400">Bola</span>Beli<span class="text-purple-400">Shop</span>
        </h1>
      </div>
      
      <!-- Desktop Navigation -->
      <div class="hidden md:flex items-center space-x-8">
        <a href="/" class="text-gray-300 hover:text-purple-400 font-medium transition-colors">
          Home
        </a>
        <a href="{% url 'main:create_product' %}" class="text-gray-300 hover:text-purple-400 font-medium transition-colors">
          Create Product
        </a>
      </div>
      
      <!-- Desktop User Section -->
      <div class="hidden md:flex items-center space-x-6">
        {% if user.is_authenticated %}
          <div class="text-right">
            <div class="text-sm font-medium text-white">{{ name|default:user.username }}</div>
            <div class="text-xs text-gray-400">{{ npm|default:"Student" }} - {{ class|default:"Class" }}</div>
          </div>
          <a href="{% url 'main:logout' %}" class="text-red-400 hover:text-red-300 font-medium transition-colors">
            Logout
          </a>
        {% else %}
          <a href="{% url 'main:login' %}" class="text-gray-300 hover:text-white font-medium transition-colors">
            Login
          </a>
          <a href="{% url 'main:register' %}" class="bg-purple-600 hover:bg-purple-700 text-white px-4 py-2 rounded-lg font-medium transition-colors shadow-md">
            Register
          </a>
        {% endif %}
      </div>
      
      <!-- Mobile Hamburger Button -->
      <div class="md:hidden flex items-center">
        <button class="mobile-menu-button p-2 text-gray-300 hover:text-white transition-colors">
          <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h16M4 18h16"></path>
          </svg>
        </button>
      </div>
    </div>
  </div>
  
  <!-- Mobile Menu (Hidden by default) -->
  <div class="mobile-menu hidden md:hidden bg-slate-900 border-t border-purple-700">
    <div class="px-6 py-4 space-y-4">
      <!-- Mobile Navigation Links -->
      <div class="space-y-1">
        <a href="/" class="block text-gray-300 hover:text-purple-400 font-medium py-3">
          Home
        </a>
        <a href="{% url 'main:create_product' %}" class="block text-gray-300 hover:text-purple-400 font-medium py-3">
          Create Product
        </a>
      </div>
      
      <!-- Mobile User Section -->
      <div class="border-t border-purple-700 pt-4">
        {% if user.is_authenticated %}
          <div class="mb-4">
            <div class="font-medium text-white">{{ name|default:user.username }}</div>
            <div class="text-sm text-gray-400">{{ npm|default:"Student" }} - {{ class|default:"Class" }}</div>
          </div>
          <a href="{% url 'main:logout' %}" class="block text-red-400 hover:text-red-300 font-medium py-3">
            Logout
          </a>
        {% else %}
          <div class="space-y-3">
            <a href="{% url 'main:login' %}" class="block text-gray-300 hover:text-white font-medium py-3">
              Login
            </a>
            <a href="{% url 'main:register' %}" class="block bg-purple-600 hover:bg-purple-700 text-white font-medium py-3 px-4 rounded-lg text-center shadow-md">
              Register
            </a>
          </div>
        {% endif %}
      </div>
    </div>
  </div>
  
  <!-- JavaScript for Mobile Menu Toggle -->
  <script>
    const btn = document.querySelector("button.mobile-menu-button");
    const menu = document.querySelector(".mobile-menu");
  
    btn.addEventListener("click", () => {
      menu.classList.toggle("hidden");
    });
  </script>
</nav>
```


**JavaScript Toggle: (Tambahan)**
- Simple vanilla JavaScript untuk toggle class "hidden"
- Toggle mobile menu visibility


