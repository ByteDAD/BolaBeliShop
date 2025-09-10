
---

# ⚽️ Tugas PBP – BolaBeliShop

## Implementasi Checklist

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
- urls.py bertugas mengarahkan request ke view yang sesuai.
- views.py menjadi jembatan utama yang mengatur logika antara models (data) dan template (tampilan).
- models.py fokus pada manajemen data.
- templates bertugas menampilkan data dalam bentuk HTML yang bisa dipahami pengguna.
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

