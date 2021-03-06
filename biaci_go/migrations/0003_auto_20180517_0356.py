# Generated by Django 2.0.5 on 2018-05-17 03:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('biaci_go', '0002_biblioteca_ejemplar'),
    ]

    operations = [
        migrations.CreateModel(
            name='Revista',
            fields=[
                ('recurso_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='biaci_go.Recurso')),
                ('numero', models.IntegerField()),
                ('serie', models.CharField(max_length=10)),
            ],
            bases=('biaci_go.recurso',),
        ),
        migrations.RemoveField(
            model_name='biblioteca',
            name='id',
        ),
        migrations.AlterField(
            model_name='biblioteca',
            name='codigo',
            field=models.CharField(max_length=4, primary_key=True, serialize=False),
        ),
    ]
