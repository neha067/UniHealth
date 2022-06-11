# Generated by Django 4.0.4 on 2022-06-11 05:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_availabledocs_specialist_remove_doctordetails_id_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('regNo', models.IntegerField()),
                ('appDate', models.DateField(blank=True, null=True)),
                ('timeSlot', models.CharField(max_length=20)),
                ('tokenNo', models.AutoField(primary_key=True, serialize=False)),
                ('problem', models.CharField(max_length=200)),
                ('deptName', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='deptName', to='home.doctordetails')),
                ('docName', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='docName', to='home.doctordetails')),
            ],
        ),
        migrations.DeleteModel(
            name='specialist',
        ),
        migrations.DeleteModel(
            name='availableDocs',
        ),
    ]
