# Generated by Django 4.0.4 on 2022-08-18 13:47

import django.core.serializers.json
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import ipam.fields
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ('extras', '0073_journalentry_tags_custom_fields'),
        ('ipam', '0057_created_datetimefield'),
        ('netbox_bgp', '0022_netbox_bgp'),
    ]

    operations = [
        migrations.CreateModel(
            name='PrefixList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('last_updated', models.DateTimeField(auto_now=True, null=True)),
                ('custom_field_data', models.JSONField(blank=True, default=dict, encoder=django.core.serializers.json.DjangoJSONEncoder)),
                ('name', models.CharField(max_length=100)),
                ('description', models.CharField(blank=True, max_length=200)),
                ('family', models.CharField(max_length=10)),
                ('tags', taggit.managers.TaggableManager(through='extras.TaggedItem', to='extras.Tag')),
            ],
            options={
                'verbose_name_plural': 'Prefix Lists',
                'unique_together': {('name', 'description', 'family')},
            },
        ),
        migrations.CreateModel(
            name='PrefixListRule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('last_updated', models.DateTimeField(auto_now=True, null=True)),
                ('custom_field_data', models.JSONField(blank=True, default=dict, encoder=django.core.serializers.json.DjangoJSONEncoder)),
                ('index', models.PositiveIntegerField()),
                ('action', models.CharField(max_length=30)),
                ('prefix_custom', ipam.fields.IPNetworkField(blank=True, null=True)),
                ('ge', models.PositiveSmallIntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(128)])),
                ('le', models.PositiveSmallIntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(128)])),
                ('prefix', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='ipam.prefix')),
                ('prefix_list', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='prefrules', to='netbox_bgp.prefixlist')),
                ('tags', taggit.managers.TaggableManager(through='extras.TaggedItem', to='extras.Tag')),
            ],
            options={
                'ordering': ('prefix_list', 'index'),
                'unique_together': {('prefix_list', 'index')},
            },
        ),
    ]
