# Generated by Django 4.2.1 on 2023-05-21 23:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_allocateequipements_status_alter_equipement_location_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='allocateequipements',
            name='status',
            field=models.CharField(choices=[('active', 'Active'), ('panding', 'Panding')], default='panding', editable=False, max_length=250),
        ),
        migrations.CreateModel(
            name='Accept',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('request', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.allocateequipements')),
            ],
        ),
    ]
