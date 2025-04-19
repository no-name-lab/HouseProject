from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField


class UserProfile(AbstractUser):
    phone_number = PhoneNumberField(null=True, blank=True, region='KG')
    ROLE_CHOICES = [
        ('admin', 'admin'),
        ('seller', 'seller'),
        ('buyer', 'buyer')
    ]
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='buyer')
    preferred_languages = models.CharField(max_length=100)


class Region(models.Model):
    region_name = models.CharField(max_length=100)

    def __str__(self):
        return self.region_name


class City(models.Model):
    city_name = models.CharField(max_length=100)

    def __str__(self):
        return self.city_name


class District(models.Model):
    district_name = models.CharField(max_length=100)

    def __str__(self):
        return self.district_name



class Property(models.Model):
    PROPERTY_CHOICES = (
        ('apartment', 'Квартира'),
        ('house', 'Дом'),
        ('commercial', 'Коммерческая недвижимость'),
        ('room', 'Комната'),
        ('land', 'Участок'),
        ('dacha', 'Дача'),
        ('parking', 'Паркинг/гараж'),
    )
    TRANSACTION_TYPE = (
        ('buy', 'Купить'),
        ('Rent', 'Снять'),
    )
    CONDITION_TYPE = (
        ('New', 'Новое'),
        ('Good', 'Хорошее'),
        ('Needs renovation', 'Требует ремонта')
    )
    DOCUMENT_TYPES = (
        ('ownership_certificate', 'Свидетельство о праве собственности'),
        ('technical_passport', 'Технический паспорт'),
        ('no_documents', 'Без документов'),
        ('other', 'Другие документы'),
    )
    transaction_type = models.CharField(max_length=50, choices=TRANSACTION_TYPE)
    property_type = models.CharField(max_length=50, choices=PROPERTY_CHOICES, default='apartment')
    condition_type = models.CharField(max_length=50, choices=CONDITION_TYPE, default='New')
    document_type = models.CharField(max_length=50, choices=DOCUMENT_TYPES, default='other')
    title = models.CharField(max_length=100)
    description = models.TextField()
    region = models.ForeignKey(Region, on_delete=models.CASCADE, related_name='region_property')
    city = models.ForeignKey(City, on_delete=models.CASCADE, related_name='city_property')
    district = models.ForeignKey(District, on_delete=models.CASCADE, related_name='district_property')
    address = models.CharField(max_length=100)
    area = models.DecimalField(max_digits=10, decimal_places=2)
    price = models.DecimalField(max_digits=12, decimal_places=2)
    floor = models.PositiveIntegerField(null=True, blank=True)
    total_floors = models.PositiveIntegerField(null=True, blank=True)
    seller = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='property_seller')


class PropertyImage(models.Model):
    property = models.ForeignKey(Property, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='property_images/')


class Review(models.Model):
    author = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='author_review')
    seller = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='seller_review')
    rating = models.PositiveSmallIntegerField(choices=[(i, i) for i in range(1, 6)], null=True, blank=True)
    comment = models.TextField()

