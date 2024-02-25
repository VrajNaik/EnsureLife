from django.db import models

# Create your models here.
class Insurance(models.Model):
    policy_name = models.CharField(max_length = 50)
    description = models.CharField(max_length=5000)
    info = models.CharField(max_length=50000)
    benefits1 = models.CharField(max_length=50000)
    benefits2 = models.CharField(max_length=50000)
    optbenefits = models.CharField(max_length = 50000)
    #policy_name = models.CharField(max_length = 50)
    #img = models.ImageField(upload_to='assets/images')
    #sum = models.IntegerField()
    #premium = models.IntegerField()
    #no = models.IntegerField()
    #loan = models.BooleanField()
    def get_policy_by_name(policy_name):
        try:
            return Insurance.objects.get( policy_name = policy_name)
        except:
            return False