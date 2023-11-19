# Generated by Django 4.1.10 on 2023-11-18 19:22

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bio', models.TextField()),
                ('image', models.ImageField(default='def_cute.png', upload_to='profile', validators=[django.core.validators.FileExtensionValidator(['png', 'jpg', 'jpeg'])])),
                ('follows', models.ManyToManyField(blank=True, related_name='followed_by', to='Profile.profile')),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
