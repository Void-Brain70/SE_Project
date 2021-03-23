# Generated by Django 3.1.1 on 2020-09-19 11:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Product', '0002_productcart_productcategory_productreview'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productcategory',
            name='category',
        ),
        migrations.RemoveField(
            model_name='productcategory',
            name='product',
        ),
        migrations.RemoveField(
            model_name='productreview',
            name='product',
        ),
        migrations.RemoveField(
            model_name='productreview',
            name='review',
        ),
        migrations.DeleteModel(
            name='ProductCart',
        ),
        migrations.DeleteModel(
            name='ProductCategory',
        ),
        migrations.DeleteModel(
            name='ProductReview',
        ),
    ]