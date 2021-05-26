# Generated by Django 3.2.3 on 2021-05-24 16:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_order'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='email',
            new_name='email1',
        ),
        migrations.RenameField(
            model_name='order',
            old_name='name',
            new_name='name1',
        ),
        migrations.RenameField(
            model_name='order',
            old_name='phone',
            new_name='phone1',
        ),
        migrations.RemoveField(
            model_name='order',
            name='description',
        ),
        migrations.AddField(
            model_name='order',
            name='description1',
            field=models.TextField(default='', max_length=500),
        ),
        migrations.AlterField(
            model_name='feedback',
            name='description',
            field=models.TextField(blank=True, default='', max_length=400),
        ),
        migrations.AlterField(
            model_name='order',
            name='image',
            field=models.ImageField(default='', upload_to='images'),
        ),
    ]
