from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    @property
    def product_count(self):
        return self.product_set.count()

class Tag(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Product(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    tag = models.ManyToManyField(Tag, blank=True, null=True)

    def __str__(self):
        return self.title

    @property
    def rating(self):
        stars = [review.stars for review in self.reviews.all() if review.stars is not None]
        if not stars:
            return 0
        else:
            return round(sum(stars) / len(stars), 2)

STAR_CHOICES = (
    (1, '* '),
    (2, 2 * '* '),
    (3, 3 * '* '),
    (4, 4 * '* '),
    (5, 5 * '* ')
)

class Review(models.Model):
    text = models.TextField()
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    stars = models.IntegerField(default=0, choices=STAR_CHOICES)

    def __str__(self):
        return self.text