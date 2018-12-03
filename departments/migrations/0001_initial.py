# Generated by Django 2.1.3 on 2018-12-02 23:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('directions', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dep_description', models.CharField(max_length=140)),
                ('fkdirection', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='directions.Direction')),
            ],
        ),
    ]