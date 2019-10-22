from django.db import models

class BookInfo(models.Model):
    book_name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=200, decimal_places=3)
    publish_date = models.DateField()

    def __str__(self):
        return self.book_name

class BookSold(models.Model):
    book_id = models.ForeignKey(BookInfo, on_delete = models.CASCADE)
    qty_sold = models.IntegerField(default=0)

    def __str__(self):
        return self.book_id.book_name