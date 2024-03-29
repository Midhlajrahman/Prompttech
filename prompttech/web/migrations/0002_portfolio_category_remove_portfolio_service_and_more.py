# Generated by Django 5.0 on 2024-01-01 11:59

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [('web', '0001_initial')]

    operations = [
        migrations.CreateModel(
            name='Portfolio_Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                (
                    'category',
                    models.CharField(
                        choices=[
                            ('HOME_AUTOMATION', 'Home & Office Automation'),
                            ('SECURITY_SURVEILLANCE', 'Security & Surveillance'),
                        ],
                        max_length=50,
                    ),
                ),
            ],
        ),
        migrations.RemoveField(model_name='portfolio', name='service'),
        migrations.AddField(
            model_name='portfolio',
            name='Portfolio_Category',
            field=models.ForeignKey(
                blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='web.portfolio_category'
            ),
        ),
    ]
