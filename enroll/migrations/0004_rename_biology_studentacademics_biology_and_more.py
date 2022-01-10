# Generated by Django 4.0.1 on 2022-01-08 17:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('enroll', '0003_alter_studentinfo_mobile'),
    ]

    operations = [
        migrations.RenameField(
            model_name='studentacademics',
            old_name='Biology',
            new_name='biology',
        ),
        migrations.RenameField(
            model_name='studentacademics',
            old_name='Chemistry',
            new_name='chemistry',
        ),
        migrations.RenameField(
            model_name='studentacademics',
            old_name='English',
            new_name='english',
        ),
        migrations.RenameField(
            model_name='studentacademics',
            old_name='Math',
            new_name='math',
        ),
        migrations.RenameField(
            model_name='studentacademics',
            old_name='Physics',
            new_name='physics',
        ),
        migrations.RenameField(
            model_name='studentinfo',
            old_name='Address',
            new_name='address',
        ),
        migrations.RenameField(
            model_name='studentinfo',
            old_name='Class',
            new_name='class_name',
        ),
        migrations.RenameField(
            model_name='studentinfo',
            old_name='Mobile',
            new_name='mobile',
        ),
        migrations.RenameField(
            model_name='studentinfo',
            old_name='Name',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='studentinfo',
            old_name='Rollno',
            new_name='roll_no',
        ),
        migrations.RenameField(
            model_name='studentinfo',
            old_name='School',
            new_name='school',
        ),
        migrations.RemoveField(
            model_name='studentacademics',
            name='Rollno',
        ),
        migrations.AddField(
            model_name='studentacademics',
            name='roll_no',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to='enroll.studentinfo'),
            preserve_default=False,
        ),
    ]
