from django.db import models
from django.core.validators import RegexValidator

import re

class Color(models.Model):
    color_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100, unique=True)
    year = models.PositiveSmallIntegerField()
    hex_code = models.CharField(max_length=6, unique=True, validators=[RegexValidator(regex=r'^#[A-F0-9]{6}$', message="colox hex code doesn't comply.", code='invalid_hex_code'),])
    pantone = models.CharField(max_length=7, unique=True, validators=[RegexValidator(regex=r'^\d\d\-\d{4}$', message="colox pantone doesn't comply.", code='invalid_pantone'),])

    def __str__(self):
        return self.name

    @classmethod
    def get_last_id(cls):
        return cls.objects.all().aggregate(models.Max('color_id')).get('color_id__max')

    @classmethod
    def check_year(cls, year):

        try:
            year_int = int(year)
        except:
            return False

        if year_int < 0 or year_int > 9999 : return False

        return True

    @classmethod
    def check_hex_code(cls, hex_code):

        return re.match('^#[A-F0-9]{6}$', hex_code) is not None

    @classmethod
    def check_pantone(cls, pantone):

        return re.match('^\d\d\-\d{4}$', pantone) is not None
