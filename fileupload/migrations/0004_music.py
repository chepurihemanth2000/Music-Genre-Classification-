
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fileupload', '0003_auto_20170605_0737'),
    ]

    operations = [
        migrations.CreateModel(
            name='Music',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='audio')),
                ('slug', models.SlugField(blank=True)),
            ],
        ),
    ]
