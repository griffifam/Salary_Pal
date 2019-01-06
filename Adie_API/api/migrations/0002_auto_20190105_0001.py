# Generated by Django 2.1.5 on 2019-01-05 00:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('startup', models.BooleanField(null=True)),
                ('size', models.IntegerField()),
                ('location_city', models.CharField(max_length=20)),
                ('location_state', models.CharField(max_length=20)),
                ('industry', models.CharField(max_length=128)),
                ('adies_present', models.BooleanField(null=True)),
                ('level_of_microaggressions', models.CharField(choices=[('NONE', 'no encounters'), ('LOW', 'one or two encounters'), ('MODERATE', 'more than three encounters'), ('HIGH', 'almost weekly encounters')], max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Offer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('base_amount', models.IntegerField()),
                ('signing_bonus', models.IntegerField()),
                ('relocation_package', models.IntegerField()),
                ('health_insurance', models.IntegerField()),
                ('retirement', models.CharField(max_length=128)),
                ('vacation_days', models.IntegerField()),
            ],
        ),
        migrations.RemoveField(
            model_name='adie',
            name='sex',
        ),
        migrations.AlterField(
            model_name='adie',
            name='gender',
            field=models.CharField(choices=[('female', 'female'), ('non-binary', 'non-binary'), ('trans', 'transgender'), ('two-spirited', 'two-spirited'), ('male', 'male')], max_length=10),
        ),
        migrations.AlterField(
            model_name='adie',
            name='orientation',
            field=models.CharField(choices=[('straight', 'straight'), ('queer', 'lesbian'), ('queer', 'gay'), ('queer', 'bisexual'), ('asexual', 'asexual')], max_length=20),
        ),
        migrations.AlterField(
            model_name='adie',
            name='race',
            field=models.CharField(choices=[('Black', 'African American'), ('Latinx', 'Hispanic'), ('Latinx', 'Latino'), ('White', 'European American'), ('White', 'Caucasian'), ('Asian', 'Asian American'), ('Indigenous', 'Native'), ('Indigenous', 'Native American'), ('Indigenous', 'Alaska Native'), ('Pacific Islander', 'Native Hawaiian')], max_length=15),
        ),
        migrations.AddField(
            model_name='offer',
            name='adie_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Adie'),
        ),
        migrations.AddField(
            model_name='offer',
            name='company_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Company'),
        ),
        migrations.AddField(
            model_name='company',
            name='adies',
            field=models.ManyToManyField(through='api.Offer', to='api.Adie'),
        ),
    ]
