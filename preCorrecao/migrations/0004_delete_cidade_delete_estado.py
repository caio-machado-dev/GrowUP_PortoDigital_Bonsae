# Generated by Django 5.1.2 on 2024-10-16 19:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("preCorrecao", "0003_rename_nome_cidade_nomecidades"),
    ]

    operations = [
        migrations.DeleteModel(
            name="Cidade",
        ),
        migrations.DeleteModel(
            name="Estado",
        ),
    ]