# Generated by Django 4.2 on 2023-05-02 18:17

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Book",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("title", models.CharField(max_length=255)),
                ("author", models.CharField(max_length=255)),
                ("year_published", models.IntegerField()),
                ("genres", models.CharField(max_length=255)),
            ],
        ),
    ]
