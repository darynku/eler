# Generated by Django 4.2.7 on 2023-12-25 05:55

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django_jsonform.models.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(verbose_name='Название')),
            ],
            options={
                'verbose_name': 'Курс',
                'verbose_name_plural': 'Курсы',
            },
        ),
        migrations.CreateModel(
            name='CourseType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Название')),
            ],
            options={
                'verbose_name': 'Тип курса',
                'verbose_name_plural': 'Типы курсов',
            },
        ),
        migrations.CreateModel(
            name='Level',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.course', verbose_name='Курс')),
            ],
            options={
                'verbose_name': 'Уровень',
                'verbose_name_plural': 'Уровни',
            },
        ),
        migrations.CreateModel(
            name='Tutorial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('course', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='courses.course')),
            ],
            options={
                'verbose_name': 'Обучение',
                'verbose_name_plural': 'Обучения',
            },
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=1000, verbose_name='Текст вопроса')),
                ('choise', django_jsonform.models.fields.ArrayField(base_field=models.CharField(), size=4, verbose_name='Выбор')),
                ('correct', models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(4)], verbose_name='Номер правильного выбора')),
                ('level', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.level', verbose_name='Уровень')),
            ],
            options={
                'verbose_name': 'Вопрос',
                'verbose_name_plural': 'Вопросы',
            },
        ),
        migrations.AddField(
            model_name='course',
            name='coursetype',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.coursetype', verbose_name='Тип курса'),
        ),
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('correct', models.BooleanField(verbose_name='Правильно')),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.question', verbose_name='Вопрос')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.student', verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'Ответ',
                'verbose_name_plural': 'Ответы',
            },
        ),
    ]