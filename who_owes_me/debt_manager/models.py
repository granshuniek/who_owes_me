from django.db import models
from django.urls import reverse
from .managers import CreditorsAndDebtorsManager
from django.contrib.auth.models import AbstractUser

def upload_path_handler_creditors(instance, filename):
    import os.path
    fn, ext = os.path.splitext(filename)
    return "{{ MEDIA_URL }}/debt_manager/avatars/users/{id}/{fn}{ext}".format(id=instance.pk, fn=fn,ext=ext)

class UserProfile(AbstractUser):
    """
        Model represents people who are owe money.
    """
    user = models.ForeignKey(User, unique=True, related_name='profile')
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    avatar = models.ImageField(upload_to=upload_path_handler_creditors, null=True)

    USERNAME_FIELD = 'username'

    # Model Save override used when image is uploaded
    def save(self, *args, **kwargs):
        if self.id is None:
            saved_image = self.avatar
            self.avatar = None
            super(UserProfile, self).save(*args, **kwargs)
            self.avatar = saved_image
        super(UserProfile, self).save(*args, **kwargs)

class Debtors(models.Model):
    """
        Model represents people who are owe money.
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    objects = CreditorsAndDebtorsManager()

    def __str__(self):
        """
            String representation of model.
        """
        return '{0} {1}'.format(self.first_name, self.last_name)
    
    def get_absolute_url(self):
        return reverse('debtors-detail', args=[str(self.id)])

class Creditors(models.Model):
    """
        Model represents people who are creditors.
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    objects = CreditorsAndDebtorsManager()

    def __str__(self):
        """
            String representation of model.
        """
        return '{0} {1}'.format(self.first_name, self.last_name)
    
    def get_absolute_url(self):
        return reverse('creditors-detail', args=[str(self.id)])

class Debts(models.Model):
    """
        Model represents all debts.
    """
    debtor = models.ForeignKey('Debtors', on_delete=models.CASCADE)
    creditor = models.ForeignKey('Creditors', on_delete=models.CASCADE)
    amount = models.FloatField()
    for_what = models.CharField(max_length=250)
    description = models.TextField(max_length=1000)
    date = models.DateTimeField()

    def __str__(self):
        return "{0} - {1} (date: {2}): {3}".format(self.amount, self.for_what, self.date ,self.description)

    def get_absolute_url(self):
        return reverse('debts-detail', args=[str(self.id)])