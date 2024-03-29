# Generated by Django 2.2.6 on 2019-10-10 01:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('edificio', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Unidad',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('piso', models.IntegerField(default=10, null=True)),
                ('torre', models.IntegerField(default=10, null=True)),
                ('numero', models.IntegerField(default=10, null=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Unidades',
        ),
    ]
