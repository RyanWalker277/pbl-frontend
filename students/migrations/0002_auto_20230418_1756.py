# Generated by Django 2.2.27 on 2023-04-18 17:56

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='student_date_of_birth',
            field=models.DateField(default=datetime.date(2023, 4, 18)),
        ),
    ]
