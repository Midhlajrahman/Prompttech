# Generated by Django 5.0 on 2024-01-02 05:37

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [('web', '0006_testimonail')]

    operations = [
        migrations.CreateModel(
            name='Enquiry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('contact', models.CharField(max_length=15)),
                ('email', models.EmailField(max_length=254)),
                ('details', models.TextField()),
            ],
        )
    ]
