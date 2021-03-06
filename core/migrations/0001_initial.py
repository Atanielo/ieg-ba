# Generated by Django 3.0.4 on 2020-03-08 03:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contato',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=40, verbose_name='nome')),
                ('email', models.EmailField(max_length=40, unique=True, verbose_name='email')),
                ('telefone', models.CharField(max_length=15, verbose_name='telefone')),
                ('mensagem', models.TextField()),
            ],
        ),
    ]
