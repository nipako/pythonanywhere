from django.db import models

class cosmeticsType(models.Model):
    text = models.CharField(max_length=200)

    def __str__(self):
        return f'{self.text}'

class cosmetics(models.Model):
    cosmetics_Type = models.ForeignKey(cosmeticsType, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    detail = models.IntegerField()

    def __str__(self):
        return f'{self.cosmetics_Type.text} - {self.name} - {self.detail}'