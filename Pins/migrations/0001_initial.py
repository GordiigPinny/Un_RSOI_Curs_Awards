# Generated by Django 3.0.4 on 2020-03-13 17:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('descr', models.CharField(blank=True, max_length=1024, null=True)),
                ('ptype', models.CharField(choices=[('p', 'Место'), ('u', 'Юзер')], max_length=2)),
                ('price', models.IntegerField()),
                ('pin_pic_link', models.URLField(blank=True, null=True)),
                ('created_dt', models.DateTimeField(auto_now_add=True)),
                ('deleted_flg', models.BooleanField(default=False)),
            ],
        ),
    ]
