from django.db import models

# Create your models here.

class Category(models.Model):
	name = models.CharField("Название", max_length=100, unique=True)
	slug = models.SlugField(max_lenght=120, unique=True)
	order_number = models.SmallIntegerField(blank=True, null=True)
	icon = models.ImageField(upload_to="category/imgs/")

	class Meta:
		verbose_name = "Категория"
		verbose_name_prular = "Категории"
		ordering = ["=order_number"]

	def __str__(self): # Имя записи #Возврашает имя объекта
		return self.name

class Product(models.Model):
	name = models.CharField("Название", max_lenght=200)
	description = models.CharField("Описание ")
	image = models.ImageField("Фото", upload_to="/product.imgs")
	price = models.DecimalField("Цена", max_digits=10, decimal_places=2) # Максимальное количество символов после запятой 
	category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
	is_available = models.BooleanField(default=True)

	class Meta:
		verbose_name = "Блюдо"
		verbose_name_plural = "Блюда"
		ordering = ["-category", "is_available"]

	def __str__(self) -> str:
		return self.name 
