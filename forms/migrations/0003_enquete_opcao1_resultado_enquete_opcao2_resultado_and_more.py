# Generated by Django 4.2.8 on 2023-12-06 22:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forms', '0002_enquete_finalizado'),
    ]

    operations = [
        migrations.AddField(
            model_name='enquete',
            name='opcao1_resultado',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='enquete',
            name='opcao2_resultado',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='enquete',
            name='opcao3_resultado',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='enquete',
            name='opcao4_resultado',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='enquete',
            name='opcao5_resultado',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='enquete',
            name='opcao6_resultado',
            field=models.IntegerField(default=0),
        ),
    ]
