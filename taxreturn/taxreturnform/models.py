from django.db import models
import datetime

# Create your models here.

def year_choices():
    return [r for r in range(2011, datetime.date.today().year)]

def current_year():
    return datetime.date.today().year

class TaxProperties(models.Model):
    """ Dashboard Components. """

    TERM_CHOICES = (
            (MONTHLY, 'Monthly'),
            (QUATERLY, 'Quaterly'),
            (ANNUALLY, 'Annually'),
            )

    TYPE_CHOICES = (
            (DIRECT, 'Direct'),
            (INDIRECT, 'Indirect'),
            (OTHER, 'Other'),
            )

    SUBTYPE_CHOICES = (
            (GSTR1, 'GSTR1'),
            (GSTR2, 'GSTR2'),
            (ADVANCETAX, 'Advace Tax'),
            (TDSRETURN, 'TDS Return'),
            (CORPORATETAX, 'Corporate Tax'),
            (GSTR8, 'GSTR8'),
            (AOC, 'AOC'),
            (MGT7, 'MGT7'),
            (AGM, 'AGM'),
            (TDSCHALLENGE, 'TDS Challenge'),
            (GSTR3B, 'GSTR 3B'),
            (CTR, 'CTR'),
            (GM, 'GM'),
            (GSTR9, 'GSTR9'),
            )


    assessment_year = models.IntegerField(choices = year_choices,default=current_year)
    term = models.CharField(max_length = 8,choices = TERM_CHOICES,default=MONTHLY)
    types= models.CharField(max_length = 8, choices = TYPE_CHOICES,
            default=DIRECT)
    subtype =  models.CharField(max_length = 12,choices = SUBTYPE_CHOICES, null=True)
    files = models.FileField(upload_to ='documents/')
    remarks = models.CharField(max_length=100, blank=True, null = True)

