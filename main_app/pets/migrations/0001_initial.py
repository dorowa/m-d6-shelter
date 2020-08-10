# Generated by Django 2.2.13 on 2020-08-04 15:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Breed',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('breed_name', models.TextField()),
                ('breed_info', models.TextField()),
            ],
            options={
                'verbose_name': 'Порода',
                'verbose_name_plural': 'Породы',
            },
        ),
        migrations.CreateModel(
            name='Kind',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kind_name', models.TextField()),
                ('kind_info', models.TextField()),
            ],
            options={
                'verbose_name': 'Вид',
                'verbose_name_plural': 'Виды',
            },
        ),
        migrations.CreateModel(
            name='PetAction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pa_action', models.CharField(max_length=20)),
                ('pa_date', models.DateField()),
                ('pa_info', models.TextField()),
            ],
            options={
                'verbose_name': 'Передача',
                'verbose_name_plural': 'Передачи',
            },
        ),
        migrations.CreateModel(
            name='Volunteer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vol_name', models.TextField()),
                ('vol_phone', models.CharField(max_length=11)),
                ('vol_rating', models.SmallIntegerField(default=1)),
            ],
            options={
                'verbose_name': 'Владелец',
                'verbose_name_plural': 'Владельцы',
            },
        ),
        migrations.CreateModel(
            name='PetSpecie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pet_name', models.TextField()),
                ('pet_birthdate', models.DateField()),
                ('pet_register_date', models.DateField()),
                ('pet_img', models.ImageField(blank=True, null=True, upload_to='pet_imgs/')),
                ('breed', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='breeds', to='pets.Breed')),
                ('kind', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='kinds', to='pets.Kind')),
                ('volunteer', models.ManyToManyField(blank=True, related_name='volunteers', through='pets.PetAction', to='pets.Volunteer')),
            ],
            options={
                'verbose_name': 'Животное',
                'verbose_name_plural': 'Животные',
            },
        ),
        migrations.AddField(
            model_name='petaction',
            name='petspecie',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='taken_pet', to='pets.PetSpecie'),
        ),
        migrations.AddField(
            model_name='petaction',
            name='volunteer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='took_volunteer', to='pets.Volunteer'),
        ),
        migrations.AddField(
            model_name='breed',
            name='kind',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pets.Kind'),
        ),
    ]