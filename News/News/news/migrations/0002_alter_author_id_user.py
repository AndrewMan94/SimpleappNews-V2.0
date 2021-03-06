from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='id_user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='usr', to=settings.AUTH_USER_MODEL),
        ),
    ]