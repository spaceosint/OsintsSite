# Generated by Django 3.2.8 on 2021-12-04 07:45

from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import photo_search.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserPhoto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('user_photo', models.ImageField(null=True, upload_to='temp_photos', verbose_name='Фото')),
                ('time_create', models.DateTimeField(auto_now_add=True, verbose_name='Время создания')),
                ('result_vk', models.BigIntegerField(null=True, verbose_name='Результат по фото для вк')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'Фото пользователей',
                'verbose_name_plural': 'Фото пользователей',
                'ordering': ['id'],
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='BigData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('person_photo', models.ImageField(null=True, upload_to=photo_search.models.directory_path, verbose_name='фото')),
                ('sex', models.PositiveSmallIntegerField(null=True, verbose_name='пол')),
            ],
            options={
                'verbose_name': 'BigData',
                'verbose_name_plural': 'BigData',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Face_encodings_vk',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('encodings', models.BigIntegerField(null=True, verbose_name='encodings')),
            ],
            options={
                'verbose_name': 'Слепок пользователей вк',
                'verbose_name_plural': 'Слепок пользователей вк',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Personal_inst',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('inst_id', models.BigIntegerField(db_index=True, null=True, verbose_name='inst')),
                ('about', models.CharField(db_index=True, max_length=512, null=True, verbose_name='Статус')),
                ('time_create', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Время создания')),
            ],
            options={
                'verbose_name': 'Данные пользователей вк',
                'verbose_name_plural': 'Данные пользователей',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Personal_vk',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vk_id', models.BigIntegerField(db_index=True, null=True, verbose_name='id vk')),
                ('surname', models.CharField(db_index=True, max_length=512, null=True, verbose_name='Фамилия')),
                ('first_name', models.CharField(db_index=True, max_length=512, null=True, verbose_name='Имя')),
                ('date_birth', models.CharField(db_index=True, max_length=20, null=True, verbose_name='Дата рождения')),
                ('country', models.CharField(db_index=True, max_length=128, null=True, verbose_name='Страна')),
                ('city', models.CharField(db_index=True, max_length=128, null=True, verbose_name='Город')),
                ('instagram', models.CharField(db_index=True, max_length=512, null=True, verbose_name='id Instagram')),
                ('time_create', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Время создания')),
            ],
            options={
                'verbose_name': 'Данные пользователей вк',
                'verbose_name_plural': 'Данные пользователей',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Sale',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='TempPhoto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_img', models.ImageField(null=True, upload_to='temp_photos/pil', verbose_name='Обрезанные фото')),
                ('time_create', models.DateTimeField(auto_now_add=True, verbose_name='Время создания')),
                ('count', models.IntegerField(max_length=20)),
                ('UserPhoto_TempPhoto', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Обрезанные фото связь')),
            ],
        ),
        migrations.CreateModel(
            name='SaleImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='test/')),
                ('sale', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='photo_search.sale', verbose_name='vendita')),
            ],
        ),
        migrations.CreateModel(
            name='Photo_vk',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo_vk', models.ImageField(null=True, upload_to='photo_vk/([0-9]+)', verbose_name='база фото вк')),
                ('person_photo_face', models.ImageField(null=True, upload_to='photo_vk/([0-9]+)face([0-9]+)', verbose_name='лицо из фото')),
                ('face_encodings_vk', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='photo_search.face_encodings_vk', verbose_name='Фото слепок')),
                ('person_photo_vk', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='photo_search.bigdata', verbose_name='Ффото & BigData')),
            ],
            options={
                'verbose_name': 'Фото пользователей вк',
                'verbose_name_plural': 'Фото пользователей вк',
                'ordering': ['id'],
            },
        ),
        migrations.AddField(
            model_name='bigdata',
            name='personal_inst',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='photo_search.personal_inst', verbose_name='Персональные данные инстаграм'),
        ),
        migrations.AddField(
            model_name='bigdata',
            name='personal_vk',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='photo_search.personal_vk', verbose_name='Персональные данные вк'),
        ),
    ]
