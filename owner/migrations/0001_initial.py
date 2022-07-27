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
            name='VehicleOwner',
            fields=[
                ('baseusermodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='userManager.baseusermodel')),
            ],
            bases=('userManager.baseusermodel',),
        ),
        migrations.CreateModel(
            name='Vehicle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vehicle_id', models.CharField(blank=True, max_length=10)),
                ('vehicle_name', models.CharField(max_length=50)),
                ('vehicle_make', models.CharField(max_length=20)),
                ('vehicle_model', models.CharField(max_length=20)),
                ('plate_number', models.CharField(max_length=10)),
                ('vehicle_owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='owner.vehicleowner')),
            ],
        ),
        migrations.CreateModel(
            name='Driver',
            fields=[
                ('baseusermodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='userManager.baseusermodel')),
                ('employer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='owner.vehicleowner')),
            ],
            bases=('userManager.baseusermodel',),
        ),
    ]