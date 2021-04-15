from django.db import models

class VladExelModels(models.Model):
    file_name = models.FileField(upload_to='vlad_exel_file')
    user_name = models.CharField(max_length=100)
    data = models.DateField(auto_now=True)
    phone_number = models.CharField(max_length=20)

    def __str__(self):
       return f'{self.user_name}, {self.phone_number}'




