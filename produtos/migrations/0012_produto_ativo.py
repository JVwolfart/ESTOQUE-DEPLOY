# Generated by Django 4.0.3 on 2022-04-21 13:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produtos', '0011_alter_produto_foto'),
    ]

    operations = [
        migrations.AddField(
            model_name='produto',
            name='ativo',
            field=models.BooleanField(default=True),
        ),
    ]
