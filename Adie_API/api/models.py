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

    def __str__(self):
        return '\nAge: %s\nGender: %s\nRace: %s\nSexual Orientation: %s\nTransplant?: %s\nLocation: %s, %s' % (self.age, self.gender, self.race, self.orientation, self.transplant, self.location_city, self.location_state)


class Company(models.Model):
    MICROAGGRESSIONS = (
        ('NONE', 'one comment'),
        ('LOW', 'two comments'),
        ('MODERATE', 'comments and attitude'),
        ('HIGH', 'uncomfortable at the start'),
    )
    startup = models.BooleanField(default=False)
    org_size = models.IntegerField()
    location_city = models.CharField(max_length=20)
    location_state = models.CharField(max_length=20)
    industry = models.CharField(max_length=128)
    adies_present = models.BooleanField(default=False)
    level_of_microaggressions = models.CharField(max_length=20, choices=MICROAGGRESSIONS)

    class Meta:
        verbose_name = 'Company'
        verbose_name_plural = 'Companies'
        ordering = ['level_of_microaggressions']

    def __str__(self):
        return '\nStartup?: %s\nOrg Size: %s\nLocation: %s,  %s\nIndustry: %s\nAdies Present?: %s\nLevel of Microaggressions?: %s\n' % (self.startup, self.org_size, self.location_city, self.location_state, self.industry, self.adies_present, self.level_of_microaggressions)


class Offer(models.Model):
    adie_id = models.ForeignKey(Adie, on_delete=models.CASCADE)
    base_amount = models.IntegerField()
    signing_bonus = models.IntegerField()
    relocation_package = models.IntegerField()
    health_insurance = models.IntegerField()
    retirement = models.CharField(max_length=128)
    vacation_days = models.IntegerField()
    company_id = models.ForeignKey(Company, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Offer'
        verbose_name_plural = 'Offers'
        ordering = ['adie_id']

    def __str__(self):
        return '\nAdie: %s\nCompany: %s\nBase Pay: %s \nSigning Bonus: %s\nHealth Insurance: %s\n # of Vacation Days: %s\nRetirement: %s\nRelocation Compensation: %s' % (self.adie_id, self.company_id, self.base_amount, self.signing_bonus, self.health_insurance, self.vacation_days, self.retirement, self.relocation_package)
