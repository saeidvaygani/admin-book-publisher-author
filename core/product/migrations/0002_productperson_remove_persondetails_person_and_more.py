# Generated by Django 4.2 on 2023-04-21 06:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("product", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="ProductPerson",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("name", models.CharField(max_length=100)),
                ("age", models.IntegerField()),
                ("email", models.EmailField(max_length=254)),
            ],
        ),
        migrations.RemoveField(model_name="persondetails", name="person",),
        migrations.RemoveField(model_name="personemails", name="person",),
        migrations.CreateModel(
            name="ProductDetails",
            fields=[
                (
                    "person",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        primary_key=True,
                        serialize=False,
                        to="product.productperson",
                    ),
                ),
                ("age", models.IntegerField()),
            ],
            options={"verbose_name_plural": "ProductDetails",},
        ),
        migrations.DeleteModel(name="Person",),
        migrations.DeleteModel(name="PersonDetails",),
        migrations.DeleteModel(name="PersonEmails",),
    ]
