
from django.db import migrations
from api.user.models import CustomUser
import django.contrib.auth.models
import django.utils.timezone


class Migration(migrations.Migration):
    def seed_data(apps, schema_editor):
        user = CustomUser(  name="khaled",
                            email="khaledjjkh@gmail.com",
                            is_staff=True,
                            is_superuser=True,
                            phone="09123456789",
                            gender="Male"
                            )
        user.set_password('123456789')
        user.save()
    dependencies = []
    operations = [
        migrations.RunPython(seed_data),
     ]
    
