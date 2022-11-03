# Generated by Django 4.1.3 on 2022-11-02 13:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
# когда создали приложения мы его зарегестрировали написали модели и сделали миграцию,
# для того чтобы django принял изменения и занес в базу данных

class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Art',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('body', models.TextField()),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
