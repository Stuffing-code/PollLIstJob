# Generated by Django 3.1.7 on 2021-04-02 12:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('poll', '0004_auto_20210402_1510'),
    ]

    operations = [
        migrations.AddField(
            model_name='answer',
            name='type_question',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='poll.question'),
            preserve_default=False,
        ),
    ]
