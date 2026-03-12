import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('camaras', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='camara',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='camara',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterModelOptions(
            name='camara',
            options={
                'ordering': ['-created_at'],
                'verbose_name': 'Camara',
                'verbose_name_plural': 'Camaras',
            },
        ),
    ]
