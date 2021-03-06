# Generated by Django 3.1.7 on 2021-04-02 11:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('poll', '0002_auto_20210402_1357'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='answer',
            name='choice_type',
        ),
        migrations.RemoveField(
            model_name='answer',
            name='user',
        ),
        migrations.RemoveField(
            model_name='choice',
            name='text_choice',
        ),
        migrations.AddField(
            model_name='answer',
            name='value',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='choice',
            name='value',
            field=models.CharField(default='Enter value', max_length=100),
        ),
        migrations.AlterField(
            model_name='answer',
            name='choice',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='poll.choice'),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='UserVoter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('poll', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='poll.poll')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='answer',
            name='user_voter',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='answers', to='poll.uservoter'),
            preserve_default=False,
        ),
    ]
