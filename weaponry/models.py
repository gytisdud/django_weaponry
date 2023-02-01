import uuid
from datetime import date
from PIL import Image
from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from tinymce.models import HTMLField
from django.views.generic.edit import CreateView
# Create your models here.

class Weapon(models.Model):
    name = models.CharField('Name', max_length=50)
    country = models.CharField('Country', max_length=50)
    # description = models.TextField('Description', max_length=1000, help_text='Weapon description')
    description = HTMLField()
    cover = models.ImageField('Cover', upload_to='covers', null=True)

    def __str__(self):
        return self.name


    def get_absolute_url(self):
        return reverse('weapon-detail', args=[str(self.id)])

class WeaponUnit(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text='Unique ID of a weapon')
    weapon = models.ForeignKey('Weapon', on_delete=models.SET_NULL, null=True)
    due_back = models.DateField('Date', null=True, blank=True)
    # soldier = models.ForeignKey('Soldier', on_delete=models.SET_NULL, null=True)
    operator = models.ForeignKey('Soldier', on_delete=models.SET_NULL, null=True, blank=True)
    @property
    def is_overdue(self):
        if self.due_back and date.today() > self.due_back:
            return True
        return False

    LOAN_STATUS = (
        ('a', 'Assigned'),
        ('n', 'Not assigned'),
    )

    status = models.CharField(
        max_length=1,
        choices=LOAN_STATUS,
        blank=True,
        default='a',
        help_text='Status',
    )

    admin = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    class Meta:
        ordering = ['due_back']

    def __str__(self):
        return f'{self.id} ({self.weapon.name} {self.operator} )'


class Soldier(models.Model):
    rank = models.CharField('Rank', max_length=50)
    first_name = models.CharField('Name', max_length=100)
    last_name = models.CharField('Last name', max_length=100)
    # description = HTMLField(default="")
    # description = models.TextField('Description', max_length=2000, default='')
    description = HTMLField()
    @property
    def display_weapons(self):
        return ', '.join(weapon.name for weapon in self.weapons.all()[:3])

    # display_weapons.short_descriptiopn = 'Weapons'
    class Meta:
        ordering = ['rank', 'first_name', 'last_name']

    def get_absolute_url(self):
        return reverse('soldier-detail', args=[str(self.id)])

    def __str__(self):
        return f'{self.rank}. {self.last_name}, {self.first_name}'






