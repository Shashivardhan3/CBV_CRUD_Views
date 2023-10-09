# Generated by Django 4.2.4 on 2023-10-09 07:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='School',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Sname', models.CharField(max_length=100)),
                ('Sprincipal', models.CharField(max_length=100)),
                ('Slocation', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Stname', models.CharField(max_length=100)),
                ('Stage', models.IntegerField()),
                ('Sname', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='students', to='app.school')),
            ],
        ),
    ]
