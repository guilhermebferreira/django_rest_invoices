# Generated by Django 3.1.2 on 2020-10-24 02:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Invoice',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('reference_month', models.IntegerField()),
                ('reference_year', models.IntegerField()),
                ('document', models.CharField(max_length=14)),
                ('description', models.CharField(blank=True, max_length=256, null=True)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=16)),
                ('is_active', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(editable=False)),
                ('deactive_at', models.DateTimeField(null=True)),
            ],
        ),
    ]
