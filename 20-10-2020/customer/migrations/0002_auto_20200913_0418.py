# Generated by Django 2.2.7 on 2020-09-12 22:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='uploads',
            name='criteria',
            field=models.CharField(default='', max_length=300),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='uploads',
            name='custo_type',
            field=models.CharField(default='Salaried', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='uploads',
            name='loan_amt',
            field=models.BigIntegerField(default=2000000),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='uploads',
            name='loan_type',
            field=models.CharField(default='Personal', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='uploads',
            name='remark',
            field=models.CharField(default='', max_length=1500),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='uploads',
            name='tenure',
            field=models.IntegerField(default=12),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='uploads',
            name='age',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='uploads',
            name='cibil_score',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='uploads',
            name='company_yrs',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='uploads',
            name='current_exp',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='uploads',
            name='gross_sal',
            field=models.CharField(max_length=15),
        ),
        migrations.AlterField(
            model_name='uploads',
            name='net_sal',
            field=models.CharField(max_length=15),
        ),
        migrations.AlterField(
            model_name='uploads',
            name='paid_up_cap',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='uploads',
            name='retire_age',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='uploads',
            name='total_exp',
            field=models.CharField(max_length=50),
        ),
        migrations.CreateModel(
            name='loan_details',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bank', models.CharField(max_length=500)),
                ('product', models.CharField(max_length=500)),
                ('loan', models.FloatField()),
                ('emi', models.FloatField()),
                ('roi', models.FloatField()),
                ('emi_start', models.DateField()),
                ('emi_end', models.DateField()),
                ('bounces', models.CharField(max_length=500)),
                ('moratorium', models.CharField(max_length=500)),
                ('loan_belong', models.CharField(max_length=500)),
                ('uid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='loan_details', to='customer.uploads')),
            ],
        ),
        migrations.CreateModel(
            name='credit_details',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bank', models.CharField(max_length=500)),
                ('credit_limit', models.CharField(max_length=500)),
                ('limit_utilize', models.CharField(max_length=500)),
                ('card_age', models.CharField(max_length=500)),
                ('payment_delay', models.CharField(max_length=500)),
                ('moratorium', models.CharField(max_length=500)),
                ('card_belong', models.CharField(max_length=500)),
                ('uid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='credit_details', to='customer.uploads')),
            ],
        ),
    ]
