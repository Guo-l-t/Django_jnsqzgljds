# Generated by Django 3.2.9 on 2022-01-02 21:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Btpr',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('xuhao', models.CharField(max_length=10)),
                ('xingming', models.CharField(max_length=100)),
                ('leixing', models.CharField(max_length=255)),
                ('f1', models.CharField(max_length=255)),
                ('f2', models.CharField(max_length=255)),
                ('f3', models.CharField(max_length=255)),
                ('f4', models.CharField(max_length=255)),
                ('f5', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='count_youxiu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('xuhao', models.CharField(max_length=10)),
                ('leixing', models.CharField(max_length=100)),
                ('count_youxiu', models.CharField(max_length=255)),
                ('f1', models.CharField(max_length=255)),
                ('f2', models.CharField(max_length=255)),
                ('f3', models.CharField(max_length=255)),
                ('f4', models.CharField(max_length=255)),
                ('f5', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('username', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('zhanghao', models.CharField(max_length=255)),
                ('password', models.CharField(max_length=100)),
                ('user_level', models.CharField(max_length=100)),
                ('danwei', models.CharField(max_length=255)),
                ('zkjsz', models.CharField(max_length=255)),
                ('fkjsz', models.CharField(max_length=255)),
                ('sjgjjz', models.CharField(max_length=255)),
                ('yejjz', models.CharField(max_length=255)),
                ('ssjjz', models.CharField(max_length=255)),
                ('yejjy', models.CharField(max_length=255)),
                ('jggq', models.CharField(max_length=255)),
                ('sjb', models.CharField(max_length=255)),
                ('f1', models.CharField(max_length=255)),
                ('f2', models.CharField(max_length=255)),
                ('f3', models.CharField(max_length=255)),
                ('f4', models.CharField(max_length=255)),
                ('f5', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Vote_session',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('voter', models.CharField(max_length=255)),
                ('voting_object', models.CharField(max_length=100)),
                ('voting_results', models.CharField(max_length=100)),
                ('voting_object_type', models.CharField(max_length=100)),
                ('voting_time', models.CharField(max_length=100)),
                ('voting_update_time', models.CharField(max_length=100)),
                ('f1', models.CharField(max_length=255)),
                ('f2', models.CharField(max_length=255)),
                ('f3', models.CharField(max_length=255)),
                ('f4', models.CharField(max_length=255)),
                ('f5', models.CharField(max_length=255)),
            ],
        ),
    ]
