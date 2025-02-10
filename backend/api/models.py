from django.db import models

class Statistics(models.Model):
    header = models.CharField(max_length=200, blank=False, null=False)
    content = models.TextField(blank=False, null=False)
    image1 = models.ImageField(upload_to='page_images/', blank=True, null=True)
    image2 = models.ImageField(upload_to='page_images/', blank=True, null=True)
    class Meta:
        verbose_name_plural = "Statistics"

class PublicSpeaking(models.Model):
    header = models.CharField(max_length=200, blank=False, null=False)
    content = models.TextField(blank=False, null=False)
    image1 = models.ImageField(upload_to='page_images/', blank=True, null=True)
    image2 = models.ImageField(upload_to='page_images/', blank=True, null=True)
    class Meta:
        verbose_name_plural = "Public Speaking"

class Business(models.Model):
    header = models.CharField(max_length=200, blank=False, null=False)
    content = models.TextField(blank=False, null=False)
    image1 = models.ImageField(upload_to='page_images/', blank=True, null=True)
    image2 = models.ImageField(upload_to='page_images/', blank=True, null=True)
    class Meta:
        verbose_name_plural = "Business"

class Psychology(models.Model):
    header = models.CharField(max_length=200, blank=False, null=False)
    content = models.TextField(blank=False, null=False)
    image1 = models.ImageField(upload_to='page_images/', blank=True, null=True)
    image2 = models.ImageField(upload_to='page_images/', blank=True, null=True)
    class Meta:
        verbose_name_plural = "Psychology"
