# Generated by Django 4.0.3 on 2022-07-27 15:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('userManager', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ClientModel',
            fields=[
                ('baseusermodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='userManager.baseusermodel')),
                ('date_created', models.TimeField(auto_now=True)),
            ],
            bases=('userManager.baseusermodel',),
        ),
    ]