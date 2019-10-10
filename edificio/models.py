from django.db import models

# Create your models here.
class Unidad(models.Model):
	created_at = models.DateTimeField(auto_now_add = True, auto_now = False)
	updated_at = models.DateTimeField(auto_now_add = True, auto_now = False)

	piso =  models.IntegerField(default=10, null=True)
	torre = models.IntegerField(default=10, null=True)
	numero = models.IntegerField(default=10, null=True)


