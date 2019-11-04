from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=32)
    detail = models.TextField(max_length=1025)
    date_created = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def short_detail(self):
        return truncatechars(self.detail, 30)

    short_detail.admin_order_field = 'detail'
    short_detail.short_description = 'detail'

    

