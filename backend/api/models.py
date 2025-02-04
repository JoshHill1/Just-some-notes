# from django.db import models

# class Subject(models.Model):
#     title = models.CharField(max_length=200, help_text="A short title for the subject")
#     slug = models.SlugField(unique=True, help_text="Unique URL-friendly identifier")
#     header = models.CharField(max_length=200, help_text="The header text to display")
#     content = models.TextField(help_text="The paragraph text for the subject")
#     image = models.ImageField(upload_to='subject_images/', blank=True, null=True, help_text="Optional image for the subject")
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)

#     def __str__(self):
#         return self.title


from django.db import models

class Page(models.Model):
    PAGE_CHOICES = (
        (1, "Page 1"),
        (2, "Page 2"),
        (3, "Page 3"),
        (4, "Page 4"),
    )
    page_number = models.IntegerField(choices=PAGE_CHOICES, unique=True)
    header = models.CharField(max_length=200)
    content = models.TextField()
    image1 = models.ImageField(upload_to='page_images/', blank=True, null=True)
    image2 = models.ImageField(upload_to='page_images/', blank=True, null=True)

    def __str__(self):
        return f"Page {self.page_number} - {self.header}"
