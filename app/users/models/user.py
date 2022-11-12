from django.db.models import ForeignKey, CASCADE, EmailField
from django.contrib.auth.models import AbstractUser, Group


class User(AbstractUser):
    groups = ForeignKey(Group, on_delete=CASCADE)
    email = EmailField(max_length=50, unique=True)

    REQUIRED_FIELDS = ['groups_id', 'email']

    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'

    def get_full_name(self):
        return '%s %s' % (self.first_name, self.last_name)

    def get_short_name(self):
        return self.first_name

    def __str__(self):
        return self.username
