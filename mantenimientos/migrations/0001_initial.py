import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('camaras', '0002_camara_created_at_camara_updated_at'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mantenimiento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('camara', models.ForeignKey(
                    on_delete=django.db.models.deletion.CASCADE,
                    related_name='mantenimientos',
                    to='camaras.camara',
                    verbose_name='Cámara',
                )),
                ('limpieza_lente', models.BooleanField(default=False, verbose_name='Limpieza de lente')),
                ('limpieza_interior', models.BooleanField(default=False, verbose_name='Limpieza interior')),
                ('verificacion_conector', models.BooleanField(default=False, verbose_name='Verificación de conector')),
                ('verificacion_alimentacion', models.BooleanField(default=False, verbose_name='Verificación de alimentación')),
                ('fecha_mantenimiento', models.DateField(verbose_name='Fecha de mantenimiento')),
                ('proxima_fecha', models.DateField(verbose_name='Próxima fecha')),
                ('observaciones', models.TextField(blank=True, verbose_name='Observaciones')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Mantenimiento',
                'verbose_name_plural': 'Mantenimientos',
                'ordering': ['-fecha_mantenimiento'],
            },
        ),
    ]
