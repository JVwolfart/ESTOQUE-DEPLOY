# Generated by Django 4.0.3 on 2022-04-19 19:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produtos', '0005_produto_medida'),
    ]

    operations = [
        migrations.AddField(
            model_name='produto',
            name='informacoes',
            field=models.TextField(blank=True, null=True),
        ),
    ]
