from django.db import models

class Page(models.Model):
    PAGE_CHOICES = (
        (1, "Statistics"),
        (2, "Public Speaking"),
        (3, "Business"),
        (4, "Psychology"),
    )
    page_number = models.IntegerField(choices=PAGE_CHOICES, unique=True)
    header = models.CharField(max_length=200, blank=True, null=True)
    content = models.TextField(blank=True, null=True)
    image1 = models.ImageField(upload_to='page_images/', blank=True, null=True)
    image2 = models.ImageField(upload_to='page_images/', blank=True, null=True)

    def __str__(self):
        return f"{self.get_page_number_display()} - {self.header or ''}"

    # def __str__(self):
    #     return f"Page {self.page_number} - {self.header}"
class Statistics(models.Model):
    header = models.CharField(max_length=200, blank=False, null=False)
    content = models.TextField(blank=False, null=False)
    image1 = models.ImageField(upload_to='page_images/', blank=True, null=True)
    image2 = models.ImageField(upload_to='page_images/', blank=True, null=True)

class PublicSpeaking(models.Model):
    header = models.CharField(max_length=200, blank=False, null=False)
    content = models.TextField(blank=False, null=False)
    image1 = models.ImageField(upload_to='page_images/', blank=True, null=True)
    image2 = models.ImageField(upload_to='page_images/', blank=True, null=True)

class Business(models.Model):
    header = models.CharField(max_length=200, blank=False, null=False)
    content = models.TextField(blank=False, null=False)
    image1 = models.ImageField(upload_to='page_images/', blank=True, null=True)
    image2 = models.ImageField(upload_to='page_images/', blank=True, null=True)

class Psychology(models.Model):
    header = models.CharField(max_length=200, blank=False, null=False)
    content = models.TextField(blank=False, null=False)
    image1 = models.ImageField(upload_to='page_images/', blank=True, null=True)
    image2 = models.ImageField(upload_to='page_images/', blank=True, null=True)
