# Generated by Django 5.1.1 on 2024-09-25 11:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ethereal', '0003_about_work_testimonial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=225, null=True)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('message', models.TextField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.RenameField(
            model_name='about',
            old_name='message',
            new_name='bio',
        ),
        migrations.RemoveField(
            model_name='about',
            name='email',
        ),
        migrations.RemoveField(
            model_name='about',
            name='name',
        ),
        migrations.AddField(
            model_name='about',
            name='bio_2',
            field=models.TextField(blank=True, null=True),
        ),
    ]
