# Generated by Django 3.2.3 on 2021-05-28 14:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Admins',
            fields=[
                ('admin_id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('fullname', models.CharField(max_length=100)),
                ('number', models.DecimalField(decimal_places=0, max_digits=11)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('password', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='BusinessLForm',
            fields=[
                ('business_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=150)),
                ('dob', models.DateField()),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('number', models.DecimalField(decimal_places=0, max_digits=11)),
                ('hom_addr', models.CharField(max_length=200)),
                ('maritalS', models.BooleanField()),
                ('busiz_name', models.TextField()),
                ('offc_email', models.EmailField(max_length=254, unique=True)),
                ('offc_numb', models.DecimalField(decimal_places=0, max_digits=11)),
                ('busiz_regno', models.CharField(max_length=200)),
                ('busiz_nature', models.TextField()),
                ('acct_no', models.DecimalField(decimal_places=0, max_digits=11)),
                ('bank_name', models.CharField(max_length=200)),
                ('branch', models.CharField(max_length=200)),
                ('bvn', models.DecimalField(decimal_places=0, max_digits=10)),
                ('loan_amount', models.DecimalField(decimal_places=2, max_digits=20)),
                ('loan_descrp', models.TextField()),
                ('tenor_of_loan', models.CharField(max_length=200)),
                ('prev_loan', models.BooleanField()),
                ('collecterials', models.TextField(unique=True)),
                ('guar_name', models.CharField(max_length=150)),
                ('house_addr', models.CharField(max_length=200)),
                ('offc_addr', models.CharField(max_length=200)),
                ('numb', models.DecimalField(decimal_places=0, max_digits=11)),
                ('monthly_income', models.DecimalField(decimal_places=2, max_digits=15)),
                ('guar_collecterials', models.TextField(unique=True)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('gur_id_1', models.ImageField(upload_to='uploads/images')),
                ('guar_name2', models.CharField(max_length=150)),
                ('house_addr2', models.CharField(max_length=200)),
                ('offc_addr2', models.CharField(max_length=200)),
                ('numb2', models.DecimalField(decimal_places=0, max_digits=11)),
                ('monthly_income2', models.DecimalField(decimal_places=2, max_digits=15)),
                ('guar_collecterials2', models.TextField(unique=True)),
                ('date2', models.DateTimeField(auto_now_add=True)),
                ('gur_id_2', models.ImageField(upload_to='uploads/images')),
            ],
        ),
        migrations.CreateModel(
            name='ConsumerLForm',
            fields=[
                ('consumer_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=150)),
                ('dob', models.DateField()),
                ('number', models.DecimalField(decimal_places=0, max_digits=11)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('hom_addr', models.CharField(max_length=200)),
                ('maritalS', models.BooleanField()),
                ('emplym_info', models.TextField()),
                ('offc_email', models.EmailField(max_length=254, unique=True)),
                ('offc_numb', models.DecimalField(decimal_places=0, max_digits=11)),
                ('monthly_income', models.DecimalField(decimal_places=2, max_digits=20)),
                ('salary', models.DecimalField(decimal_places=2, max_digits=15)),
                ('acct_name', models.CharField(max_length=200, unique=True)),
                ('bank_name', models.CharField(max_length=200)),
                ('acct_no', models.DecimalField(decimal_places=0, max_digits=11)),
                ('bvn', models.DecimalField(decimal_places=0, max_digits=10)),
                ('acct_name2', models.CharField(max_length=200, unique=True)),
                ('bank_name2', models.CharField(max_length=200)),
                ('acct_no2', models.DecimalField(decimal_places=0, max_digits=10)),
                ('loan_words', models.CharField(help_text='Please write amount in words', max_length=200)),
                ('loan_figure', models.DecimalField(decimal_places=2, help_text='Please write amount in figures', max_digits=9)),
                ('loan_descrp', models.TextField()),
                ('signature', models.ImageField(upload_to='uploads/images')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('id_upload', models.ImageField(upload_to='uploads/images')),
            ],
        ),
        migrations.CreateModel(
            name='PaymentFromConsumer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('transac_id', models.IntegerField(unique=True)),
                ('payment_date', models.DateField()),
                ('amount_paid', models.DecimalField(decimal_places=2, max_digits=10)),
                ('laon_amount', models.DecimalField(decimal_places=2, max_digits=20)),
                ('amount_remains', models.DecimalField(decimal_places=2, max_digits=10)),
                ('remark', models.CharField(default='pending', max_length=20)),
                ('consumer_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.consumerlform')),
            ],
        ),
        migrations.CreateModel(
            name='PaymentFromBusiness',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('transac_id', models.IntegerField(unique=True)),
                ('payment_date', models.DateField()),
                ('amount_paid', models.DecimalField(decimal_places=2, max_digits=10)),
                ('amount_remains', models.DecimalField(decimal_places=2, max_digits=10)),
                ('remark', models.CharField(default='pending', max_length=20)),
                ('business_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.businesslform')),
                ('laon_amount', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.consumerlform')),
            ],
        ),
        migrations.CreateModel(
            name='LoanGiven',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('transac_id', models.IntegerField(unique=True)),
                ('date_given', models.DateTimeField(auto_now_add=True)),
                ('amount_given', models.DecimalField(decimal_places=2, max_digits=15)),
                ('admin_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.admins')),
                ('consumer_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.consumerlform')),
            ],
        ),
    ]