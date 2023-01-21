# Generated by Django 3.1.1 on 2023-01-18 23:15

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Produto',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid1, editable=False, primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=45)),
                ('marca', models.CharField(max_length=20)),
                ('preco', models.FloatField()),
                ('quantidade', models.IntegerField()),
            ],
        ),
    ]