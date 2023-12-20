# Generated by Django 4.2.8 on 2023-12-20 13:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('aluguel', '0002_carro_foto_carro_preco_alter_carro_ano'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aluguel',
            name='cliente',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='Cliente',
        ),
    ]
