# Generated by Django 3.2.9 on 2021-11-18 17:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('foodapp', '0002_alter_dish_cuisine'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dish',
            name='cuisine',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='foodapp.cuisine'),
        ),
    ]
