# Generated by Django 5.0.6 on 2024-07-07 04:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0002_rename_descripcion_producto_descripcion_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='imagen',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='producto',
            name='descripcion',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='producto',
            name='nombre',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='producto',
            name='precio',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
    ]
