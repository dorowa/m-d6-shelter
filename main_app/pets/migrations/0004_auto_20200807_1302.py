# Generated by Django 2.2.13 on 2020-08-07 13:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pets', '0003_kind_kind_link'),
    ]

    operations = [
        migrations.AlterField(
            model_name='petspecie',
            name='pet_gender',
            field=models.CharField(choices=[('M', 'мальчик'), ('F', 'девочка')], default='M', max_length=1),
        ),
    ]
