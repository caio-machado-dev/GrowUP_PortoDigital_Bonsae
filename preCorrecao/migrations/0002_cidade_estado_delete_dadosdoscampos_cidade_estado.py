# Generated by Django 5.1.2 on 2024-10-15 04:30

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("preCorrecao", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Cidade",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nome", models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name="Estado",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("sigla", models.CharField(max_length=2, unique=True)),
            ],
        ),
        migrations.DeleteModel(
            name="DadosDosCampos",
        ),
        migrations.AddField(
            model_name="cidade",
            name="estado",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="cidades",
                to="preCorrecao.estado",
            ),
        ),
    ]
