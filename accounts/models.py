from django.db import models

# Create your models here.
class Customer(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    contact_no = models.CharField(max_length=13)
    email = models.EmailField()
    password = models.CharField(max_length=500)

    def rgstr(self):
        self.save()

    def ifAlreadyExists(self):
        if Customer.objects.filter(email = self.email):
            return True
        return False

    def validateCustomer(self):
        err_msg = None
        if not self.first_name:
            err_msg = "First Name Required!"
        elif len(self.contact_no) != 10 :
            err_msg = "Pone Number must be of 10 Digits!"
        elif self.ifAlreadyExists():
            err_msg = "User Already Registered!"
        return err_msg
    @staticmethod
    def get_customer_by_email(email):
        try:
            return Customer.objects.get(email = email)
        except:
            return False