# Generated by Django 5.1.1 on 2024-11-15 20:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0002_alter_cliente_direccion_alter_direccion_provincia'),
    ]

    operations = [
        migrations.AlterField(
            model_name='direccion',
            name='provincia',
            field=models.CharField(choices=[('BA', 'Buenos Aires'), ('CABA', 'Ciudad Autónoma de Buenos Aires'), ('CT', 'Catamarca'), ('CC', 'Chaco'), ('CH', 'Chubut'), ('CB', 'Córdoba'), ('CR', 'Corrientes'), ('ER', 'Entre Ríos'), ('FO', 'Formosa'), ('JY', 'Jujuy'), ('LP', 'La Pampa'), ('LR', 'La Rioja'), ('MZ', 'Mendoza'), ('MI', 'Misiones'), ('NQ', 'Neuquén'), ('RN', 'Río Negro'), ('SA', 'Salta'), ('SJ', 'San Juan'), ('SL', 'San Luis'), ('SC', 'Santa Cruz'), ('SF', 'Santa Fe'), ('SE', 'Santiago del Estero'), ('TF', 'Tierra del Fuego'), ('TM', 'Tucumán')], max_length=25, null=True),
        ),
    ]
