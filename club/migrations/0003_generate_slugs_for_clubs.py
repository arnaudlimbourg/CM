# Generated by Django 4.1.3 on 2022-12-06 09:42

from django.db import migrations
from django.utils.text import slugify


def generate_slugs(apps, schema_editor):
    Club = apps.get_model("club", "Club")
    for club in Club.objects.all():
        club.slug = slugify(club.name)
        club.save()


class Migration(migrations.Migration):

    dependencies = [
        ('club', '0002_club_slug'),
    ]

    operations = [
        migrations.RunPython(generate_slugs,
                             reverse_code=migrations.RunPython.noop)
    ]
