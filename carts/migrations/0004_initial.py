# Generated by Django 4.0.3 on 2022-04-06 17:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0002_wishlist_wishlists_user_product_unq'),
        ('products', '0003_productsize_product_sizes_product_size_unq'),
        ('carts', '0003_delete_cart'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('quantity', models.IntegerField(default=0)),
                ('product_size', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.productsize')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.user')),
            ],
            options={
                'db_table': 'carts',
            },
        ),
    ]