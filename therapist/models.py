from django.db import models
from django.contrib.auth.models import User
from django.core.validators import EmailValidator
from django.core.exceptions import ValidationError
from django.db.models import Avg

class DailyInput(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="daily_inputs")
    date = models.DateTimeField(auto_now_add=True, db_index=True)
    text = models.TextField()
    emotion = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return f"{self.user.username} - {self.date.strftime('%Y-%m-%d %H:%M:%S')}"

    class Meta:
        ordering = ['-date']

    @staticmethod
    def get_daily_average(user, selected_date):
        return DailyInput.objects.filter(user=user, date__date=selected_date).aggregate(Avg('emotion'))

    def save(self, *args, **kwargs):
        self.text = self.text.strip()
        if self.emotion:
            self.emotion = self.emotion.lower()
        super().save(*args, **kwargs)


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=30, default="First_Name")
    last_name = models.CharField(max_length=30, default="Last_Name")
    address = models.CharField(max_length=100, blank=True, null=True)
    parent_email = models.EmailField(validators=[EmailValidator()])
    doctor_email = models.EmailField(validators=[EmailValidator()])

    def __str__(self):
        return self.user.username

    def clean(self):
        if self.parent_email == self.doctor_email:
            raise ValidationError("Parent email and doctor email cannot be the same.")
