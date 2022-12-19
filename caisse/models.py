from django.db import models

# Create your models here.

class Staff(models.Model):
    first_name=models.CharField("First Name",null=True,max_length=200)
    last_name = models.CharField("First Name", null=True, max_length=200)
    user_name = models.CharField("userName", null=True, max_length=200)
    email = models.CharField("Email", null=True, max_length=255)
    region=models.CharField("Region d'affectation", null=True, max_length=255)
    post = models.CharField("Post Staff", null=True, max_length=200)
    service = models.CharField("Service Staff", null=True, max_length=200)

    def __str__(self):
        return self.user_name


class TransactionCash(models.Model):
    created_at=models.DateTimeField(blank=True)
    receiver = models.CharField("userName", null=True, max_length=200,blank=True)
    ref_transaction = models.CharField("reference Transaction", null=True, max_length=30,blank=True)
    description = models.TextField("description transaction",null=True,blank=True)
    mouvement_cash = models.CharField("Cash mouvement", null=True, max_length=30,blank=True)
    detail_mouvement_cash = models.CharField("Cash mouvement", null=True, max_length=30, blank=True)
    amount = models.FloatField(null=True,blank=True)


    def __str__(self):
        return self.receiver

