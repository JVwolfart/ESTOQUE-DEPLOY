# Generated by Django 4.0.3 on 2022-04-21 17:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produtos', '0012_produto_ativo'),
    ]

    operations = [
        migrations.AddField(
            model_name='historico',
            name='excluido',
            field=models.BooleanField(default=False),
        ),
    ]