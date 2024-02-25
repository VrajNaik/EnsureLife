from django.db import models

# Create your models here.
class Policy(models.Model):
    policy_name = models.CharField(max_length=50)
    high_premium = models.BooleanField()
    accidental_cover = models.BooleanField()
    surrender_value = models.BooleanField()
    market_risk = models.BooleanField()
    age_group = models.CharField(max_length=50)
    term_period = models.CharField(max_length=50)
    premium_wavier = models.BooleanField()
    maturity = models.CharField(max_length=50)

    def get_policy_by_name(policy_name):
        try:
            return Policy.objects.get(policy_name = policy_name)
        except:
            return False