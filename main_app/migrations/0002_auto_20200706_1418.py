# Generated by Django 3.0.7 on 2020-07-06 14:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Clothing',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('category', models.CharField(max_length=100)),
                ('brand', models.CharField(max_length=100)),
                ('size', models.CharField(choices=[('XS', 'Extra-Small'), ('S', 'Small'), ('M', 'Medium'), ('L', 'Large'), ('XL', 'Extra-Large')], default='S', max_length=2)),
                ('description', models.TextField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Shoe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('brand', models.CharField(max_length=100)),
                ('shoe_size', models.CharField(choices=[('5', 'Five'), ('6', 'Six'), ('7', 'Seven')], default=('7', 'Seven'), max_length=1)),
                ('description', models.TextField(max_length=250)),
            ],
        ),
        migrations.RemoveField(
            model_name='photo',
            name='product',
        ),
        migrations.DeleteModel(
            name='Product',
        ),
        migrations.AddField(
            model_name='clothing',
            name='shoes',
            field=models.ManyToManyField(to='main_app.Shoe'),
        ),
        migrations.AddField(
            model_name='clothing',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='photo',
            name='clothing',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='main_app.Clothing'),
            preserve_default=False,
        ),
    ]
