# Generated by Django 2.1 on 2018-08-18 06:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254)),
                ('username', models.CharField(max_length=200)),
                ('password', models.CharField(max_length=400)),
                ('user_type', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Manager',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.FileField(blank=True, upload_to='')),
                ('grade', models.CharField(blank=True, max_length=200)),
                ('date', models.DateField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Outlets',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('lat', models.CharField(max_length=400)),
                ('long', models.CharField(max_length=400)),
                ('date', models.DateField(auto_now=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Sales.Account')),
            ],
        ),
        migrations.AddField(
            model_name='manager',
            name='outlet',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Sales.Outlets'),
        ),
        migrations.AddField(
            model_name='manager',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Sales.Account'),
        ),
    ]