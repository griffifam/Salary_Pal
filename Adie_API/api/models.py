from django.db import models

# Create your models here.
class Adie(models.Model):
    RACE = (
        ('Black', 'African American'),
        ('Latinx', 'Hispanic'),
        ('Latinx', 'Latino'),
        ('White', 'European American'),
        ('White', 'Caucasian'),
        ('Asian', 'Asian American'),
        ('Indigenous', 'Native'),
        ('Indigenous', 'Native American'),
        ('Indigenous', 'Alaska Native'),
        ('Pacific Islander', 'Native Hawaiian'),
    )
    GENDER = (
        ('female','female'),
        ('non-binary','non-binary'),
        ('trans', 'transgender'),
        ('two-spirited', 'two-spirited'),
        ('male', 'male'),
    )
    ORIENTATION = (
        ('straight', 'straight'),
        ('queer', 'lesbian'),
        ('queer', 'gay'),
        ('queer', 'bisexual'),
        ('asexual', 'asexual'),
    )
    age = models.IntegerField()
    gender = models.CharField(max_length=20, choices=GENDER)
    race = models.CharField(max_length=20, choices=RACE)
    orientation = models.CharField(max_length=20, choices=ORIENTATION)
    transplant = models.BooleanField(default=False)
    location_city = models.CharField(max_length=20)
    location_state = models.CharField(max_length=20)

    class Meta:
        verbose_name = 'adie'
        verbose_name_plural = 'adies'
        ordering = ['race']


class Company(models.Model):
    MICROAGGRESSIONS = (
        ('NONE', 'no encounters'),
        ('LOW', 'one or two encounters'),
        ('MODERATE', 'more than three encounters'),
        ('HIGH', 'almost weekly encounters'),
    )
    startup = models.BooleanField(null=True)
    org_size = models.IntegerField()
    location_city = models.CharField(max_length=20)
    location_state = models.CharField(max_length=20)
    industry = models.CharField(max_length=128)
    adies_present = models.BooleanField(null=True)
    adies = models.ManyToManyField(Adie, through='Offer')
    level_of_microaggressions = models.CharField(max_length=20, choices=MICROAGGRESSIONS)


class Offer(models.Model):
    adie_id = models.ForeignKey(Adie, on_delete=models.CASCADE)
    base_amount = models.IntegerField()
    signing_bonus = models.IntegerField()
    relocation_package = models.IntegerField()
    health_insurance = models.IntegerField()
    retirement = models.CharField(max_length=128)
    vacation_days = models.IntegerField()
    company_id = models.ForeignKey(Company, on_delete=models.CASCADE)
