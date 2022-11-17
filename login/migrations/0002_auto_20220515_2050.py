# Generated by Django 3.2 on 2022-05-15 17:50

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='client',
            old_name='city',
            new_name='county',
        ),
        migrations.RenameField(
            model_name='shop',
            old_name='shop_name',
            new_name='Industry',
        ),
        migrations.RenameField(
            model_name='shop',
            old_name='city',
            new_name='county',
        ),
        migrations.RemoveField(
            model_name='client',
            name='gender',
        ),
        migrations.RemoveField(
            model_name='client',
            name='id',
        ),
        migrations.RemoveField(
            model_name='shop',
            name='id',
        ),
        migrations.AddField(
            model_name='client',
            name='building',
            field=models.CharField(default='', max_length=21),
        ),
        migrations.AddField(
            model_name='client',
            name='location_id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
        migrations.AddField(
            model_name='client',
            name='street',
            field=models.CharField(default='', max_length=21),
        ),
        migrations.AddField(
            model_name='shop',
            name='building',
            field=models.CharField(default='', max_length=21),
        ),
        migrations.AddField(
            model_name='shop',
            name='location_id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
        migrations.AddField(
            model_name='shop',
            name='street',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='user',
            name='first_name',
            field=models.CharField(blank=True, max_length=150, verbose_name='first name'),
        ),
        migrations.AlterField(
            model_name='user',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
