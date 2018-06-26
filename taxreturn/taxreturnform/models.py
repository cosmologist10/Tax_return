from django.db import models
import datetime

# Create your models here.

class TaxProperties(models.Model):
    """ Dashboard Components. """

    YEAR_CHOICES = []
    for r in range(2011, (datetime.datetime.now().year+1)):
        YEAR_CHOICES.append((r,r))

    TERM_CHOICES = (
            ('MONTHLY', 'Monthly'),
            ('QUATERLY', 'Quaterly'),
            ('ANNUALLY', 'Annually'),
            )

    TYPE_CHOICES = (
            ('DIRECT', 'Direct'),
            ('INDIRECT', 'Indirect'),
            ('OTHER', 'Other'),
            )

    SUBTYPE_CHOICES = (
            ('GSTR1', 'GSTR1'),
            ('GSTR2', 'GSTR2'),
            ('ADVANCETAX', 'Advace Tax'),
            ('TDSRETURN', 'TDS Return'),
            ('CORPORATETAX', 'Corporate Tax'),
            ('GSTR8', 'GSTR8'),
            ('AOC', 'AOC'),
            ('MGT7', 'MGT7'),
            ('AGM', 'AGM'),
            ('TDSCHALLENGE', 'TDS Challenge'),
            ('GSTR3B', 'GSTR 3B'),
            ('CTR', 'CTR'),
            ('GM', 'GM'),
            ('GSTR9', 'GSTR9'),
            )


    year = models.IntegerField('Year',choices=YEAR_CHOICES,default=datetime.datetime.now().year)
    term = models.CharField(max_length = 8,choices=TERM_CHOICES,default='MONTHLY')
    types= models.CharField(max_length = 8, choices = TYPE_CHOICES,default='DIRECT')
    subtype =  models.CharField(max_length = 12,choices = SUBTYPE_CHOICES, null=True)
    files = models.FileField(upload_to ='documents/')
    remarks = models.CharField(max_length=100, blank=True, null = True)

