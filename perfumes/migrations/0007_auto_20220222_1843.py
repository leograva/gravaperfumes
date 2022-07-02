# Generated by Django 2.2.12 on 2022-02-22 21:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('perfumes', '0006_auto_20220222_1835'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tamanho',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(choices=[('1', '100ML'), ('2', '200ML'), ('3', 'Unissex'), ('1', '100ML')], max_length=1)),
            ],
        ),
        migrations.AlterField(
            model_name='genero',
            name='nome',
            field=models.CharField(max_length=25),
        ),
    ]
