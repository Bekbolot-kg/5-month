from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)

    @property
    def products_count(self):
        return self.products.all().count()

    def __str__(self):
        return self.name


class Color(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Product(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, related_name='products')
    colors = models.ManyToManyField(Color)
    created_at = models.DateTimeField(auto_now_add=True, null=True)

    def get_category_name(self):
        return self.category.name if self.category else None

    @property
    def get_rating(self):
        total_reviews = self.reviews.count()
        if total_reviews == 0:
            return 0
        sum_rating = 0
        for i in self.reviews.all():
            sum_rating += i.stars

        return sum_rating / total_reviews

    def __str__(self):
        return self.title


class Review(models.Model):
    text = models.TextField()
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='reviews')
    stars = models.PositiveIntegerField(choices=((1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')), null=True)

    def __str__(self):
        return self.text


