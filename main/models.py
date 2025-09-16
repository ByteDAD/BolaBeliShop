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
    name = models.CharField(max_length=255)  # nama item
    price = models.IntegerField()  # harga item
    description = models.TextField()  # deskripsi item
    thumbnail = models.URLField(blank=True, null=True)  # gambar item
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, default='jersey')
    is_featured = models.BooleanField(default=False)  # unggulan atau tidak

    # Atribut tambahan opsional
    stock = models.PositiveIntegerField(default=0)  # stok barang
    brand = models.CharField(max_length=100, blank=True, null=True)  # merk barang
    
    # Field untuk created date dan views
    created_at = models.DateTimeField(auto_now_add=True)  # tanggal dibuat
    product_views = models.PositiveIntegerField(default=0)  # jumlah views

    def __str__(self):
        return f"{self.name} ({self.category})"
    
    def increment_views(self):
        """Method untuk menambah view count"""
        self.product_views += 1
        self.save()