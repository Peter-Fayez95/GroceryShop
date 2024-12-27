# Generated by Django 4.2.8 on 2024-12-27 20:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('userprofile', '0001_initial'),
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('status', models.IntegerField(choices=[(0, 'Fullfield'), (1, 'Unfullfield'), (2, 'Canceled'), (3, 'Refunded')], default=0)),
                ('email', models.EmailField(max_length=254)),
                ('checkout_token', models.CharField(default='', max_length=36)),
                ('note', models.TextField(blank=True, default='')),
                ('total', models.FloatField()),
                ('total_discount', models.FloatField(default=0)),
                ('shipping', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='userprofile.addresses')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='OrderLine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=255)),
                ('product_price', models.FloatField()),
                ('sku', models.CharField(max_length=50)),
                ('quantity', models.PositiveIntegerField()),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orderlines', to='order.order')),
                ('product', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='orderlines', to='product.product')),
            ],
        ),
    ]
