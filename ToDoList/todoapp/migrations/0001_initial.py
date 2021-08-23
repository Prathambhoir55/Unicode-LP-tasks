# Generated by Django 3.2.5 on 2021-08-23 13:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(default=0, primary_key=True, serialize=False)),
                ('task_name', models.CharField(max_length=100)),
                ('task_time', models.DateTimeField()),
                ('task_desc', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='TaskDone',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task_done', models.BooleanField()),
                ('task_name', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='todoapp.task')),
            ],
        ),
    ]