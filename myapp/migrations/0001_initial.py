# Generated by Django 3.2.21 on 2024-01-16 17:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=100)),
                ('place', models.CharField(max_length=100)),
                ('latitude', models.CharField(max_length=100)),
                ('longitude', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='fuel_wage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fuel_type', models.CharField(max_length=100)),
                ('wage_per_km', models.CharField(max_length=100)),
                ('fuel_price', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='login',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=100)),
                ('usertype', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='route',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('latitude', models.CharField(max_length=100)),
                ('longitude', models.CharField(max_length=100)),
                ('From', models.CharField(max_length=100)),
                ('To', models.CharField(max_length=100)),
                ('date', models.CharField(max_length=100)),
                ('no_of_requests', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='user',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=100)),
                ('photo', models.CharField(max_length=100)),
                ('COMPANY', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='myapp.company')),
                ('LOGIN', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='myapp.login')),
            ],
        ),
        migrations.CreateModel(
            name='user_request',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.CharField(max_length=100)),
                ('status', models.CharField(max_length=100)),
                ('latitude', models.CharField(max_length=100)),
                ('longitude', models.CharField(max_length=100)),
                ('amount', models.CharField(max_length=100)),
                ('ROUTE', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='myapp.route')),
                ('USER', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='myapp.user')),
            ],
        ),
        migrations.CreateModel(
            name='transaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('payment_status', models.CharField(max_length=100)),
                ('amount', models.CharField(max_length=100)),
                ('date', models.CharField(max_length=100)),
                ('USER', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='myapp.user')),
                ('USERREQUEST', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='myapp.user_request')),
            ],
        ),
        migrations.AddField(
            model_name='route',
            name='USER',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='myapp.user'),
        ),
        migrations.CreateModel(
            name='feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('feedback', models.CharField(max_length=200)),
                ('feedback_date', models.CharField(max_length=100)),
                ('USER', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='USER', to='myapp.user')),
                ('driver', models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, related_name='driver', to='myapp.user')),
            ],
        ),
        migrations.CreateModel(
            name='complaint',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('complaint', models.CharField(max_length=100)),
                ('complaint_date', models.CharField(max_length=100)),
                ('reply', models.CharField(max_length=100)),
                ('reply_date', models.CharField(max_length=100)),
                ('USER', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='u', to='myapp.user')),
                ('driver', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='d', to='myapp.user')),
            ],
        ),
        migrations.AddField(
            model_name='company',
            name='LOGIN',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='myapp.login'),
        ),
    ]
