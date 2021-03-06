# Generated by Django 3.0.5 on 2021-12-27 20:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='InvoiceUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=600)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('email', models.EmailField(max_length=900, unique=True)),
                ('address', models.TextField(blank=True, max_length=5000, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(db_index=True, max_length=600)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('cost', models.FloatField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Invoice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('tax_percent', models.FloatField(default=0)),
                ('bank_details', models.TextField(max_length=4000)),
                ('biller', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='billerinvoices', to='invoicegenerator.InvoiceUser')),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='clientinvoices', to='invoicegenerator.InvoiceUser')),
                ('services', models.ManyToManyField(related_name='serviceinvoices', to='invoicegenerator.Service')),
            ],
        ),
    ]
