from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ('invoices', '0001_initial'),
    ]

    operations = [
        migrations.RunSQL(
            'alter table invoices_invoice modify created_at timestamp default CURRENT_TIMESTAMP not null;')
    ]
