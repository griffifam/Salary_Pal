# Generated by Django 2.1.5 on 2019-01-06 06:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_auto_20190106_0203'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='company',
            options={'ordering': ['level_of_microaggressions'], 'verbose_name': 'Company', 'verbose_name_plural': 'Companies'},
        ),
        migrations.AlterModelOptions(
            name='offer',
            options={'ordering': ['adie_id'], 'verbose_name': 'Offer', 'verbose_name_plural': 'Offers'},
        ),
        migrations.AlterField(
            model_name='company',
            name='adies_present',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='company',
            name='level_of_microaggressions',
            field=models.CharField(choices=[('NONE', 'one comment'), ('LOW', 'two comments'), ('MODERATE', 'comments and attitude'), ('HIGH', 'uncomfortable at the start')], max_length=20),
        ),
        migrations.AlterField(
            model_name='company',
            name='startup',
            field=models.BooleanField(default=False),
        ),
    ]
