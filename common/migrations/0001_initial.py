# Generated by Django 4.1 on 2023-07-06 12:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="AuthGroup",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=150, unique=True)),
            ],
            options={
                "db_table": "auth_group",
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="AuthGroupPermissions",
            fields=[
                ("id", models.BigAutoField(primary_key=True, serialize=False)),
            ],
            options={
                "db_table": "auth_group_permissions",
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="AuthPermission",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=255)),
                ("codename", models.CharField(max_length=100)),
            ],
            options={
                "db_table": "auth_permission",
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="AuthUser",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("password", models.CharField(max_length=128)),
                ("last_login", models.DateTimeField(blank=True, null=True)),
                ("is_superuser", models.IntegerField()),
                ("username", models.CharField(max_length=150, unique=True)),
                ("first_name", models.CharField(max_length=150)),
                ("last_name", models.CharField(max_length=150)),
                ("email", models.CharField(max_length=254)),
                ("is_staff", models.IntegerField()),
                ("is_active", models.IntegerField()),
                ("date_joined", models.DateTimeField()),
            ],
            options={
                "db_table": "auth_user",
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="AuthUserGroups",
            fields=[
                ("id", models.BigAutoField(primary_key=True, serialize=False)),
            ],
            options={
                "db_table": "auth_user_groups",
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="AuthUserUserPermissions",
            fields=[
                ("id", models.BigAutoField(primary_key=True, serialize=False)),
            ],
            options={
                "db_table": "auth_user_user_permissions",
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="Company",
            fields=[
                (
                    "com_id",
                    models.CharField(max_length=50, primary_key=True, serialize=False),
                ),
                ("com_name", models.CharField(max_length=50)),
                (
                    "com_location",
                    models.CharField(blank=True, max_length=800, null=True),
                ),
                (
                    "com_employees",
                    models.CharField(blank=True, max_length=300, null=True),
                ),
                ("com_size", models.CharField(blank=True, max_length=50, null=True)),
            ],
            options={
                "db_table": "company",
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="Cv",
            fields=[
                (
                    "cv_id",
                    models.CharField(max_length=50, primary_key=True, serialize=False),
                ),
                ("cv_company", models.CharField(blank=True, max_length=50, null=True)),
                ("cv_spec", models.CharField(blank=True, max_length=1000, null=True)),
                (
                    "cv_question",
                    models.CharField(blank=True, max_length=5000, null=True),
                ),
                ("cv_answer", models.CharField(blank=True, max_length=5000, null=True)),
            ],
            options={
                "db_table": "cv",
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="DjangoAdminLog",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("action_time", models.DateTimeField()),
                ("object_id", models.TextField(blank=True, null=True)),
                ("object_repr", models.CharField(max_length=200)),
                ("action_flag", models.PositiveSmallIntegerField()),
                ("change_message", models.TextField()),
            ],
            options={
                "db_table": "django_admin_log",
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="DjangoContentType",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("app_label", models.CharField(max_length=100)),
                ("model", models.CharField(max_length=100)),
            ],
            options={
                "db_table": "django_content_type",
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="DjangoMigrations",
            fields=[
                ("id", models.BigAutoField(primary_key=True, serialize=False)),
                ("app", models.CharField(max_length=255)),
                ("name", models.CharField(max_length=255)),
                ("applied", models.DateTimeField()),
            ],
            options={
                "db_table": "django_migrations",
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="DjangoSession",
            fields=[
                (
                    "session_key",
                    models.CharField(max_length=40, primary_key=True, serialize=False),
                ),
                ("session_data", models.TextField()),
                ("expire_date", models.DateTimeField()),
            ],
            options={
                "db_table": "django_session",
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="Interview",
            fields=[
                (
                    "int_id",
                    models.CharField(max_length=50, primary_key=True, serialize=False),
                ),
                ("int_com_id", models.CharField(max_length=50)),
                ("name_list", models.CharField(max_length=50)),
                (
                    "int_difficulty",
                    models.CharField(blank=True, max_length=50, null=True),
                ),
                ("int_date", models.CharField(blank=True, max_length=50, null=True)),
                (
                    "int_question",
                    models.CharField(blank=True, max_length=5000, null=True),
                ),
                (
                    "int_answer",
                    models.CharField(blank=True, max_length=5000, null=True),
                ),
                ("int_result", models.CharField(blank=True, max_length=50, null=True)),
                (
                    "int_post_date",
                    models.CharField(blank=True, max_length=50, null=True),
                ),
            ],
            options={
                "db_table": "interview",
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="News",
            fields=[
                (
                    "news_id",
                    models.CharField(max_length=50, primary_key=True, serialize=False),
                ),
                ("news_com_id", models.CharField(blank=True, max_length=50, null=True)),
                ("news_title", models.CharField(max_length=500)),
                ("news_href", models.CharField(blank=True, max_length=500, null=True)),
                ("news_date", models.CharField(blank=True, max_length=50, null=True)),
            ],
            options={
                "db_table": "news",
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="Post",
            fields=[
                (
                    "post_id",
                    models.CharField(max_length=50, primary_key=True, serialize=False),
                ),
                ("post_com_id", models.CharField(max_length=50)),
                (
                    "post_com_name",
                    models.CharField(blank=True, max_length=500, null=True),
                ),
                ("post_title", models.CharField(max_length=500)),
                ("post_career", models.CharField(max_length=500)),
                (
                    "post_location",
                    models.CharField(blank=True, max_length=800, null=True),
                ),
                (
                    "post_emp_types",
                    models.CharField(blank=True, max_length=500, null=True),
                ),
                ("post_dday", models.CharField(blank=True, max_length=50, null=True)),
                ("post_pay", models.CharField(blank=True, max_length=100, null=True)),
                ("post_href", models.CharField(max_length=500)),
            ],
            options={
                "db_table": "post",
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="Review",
            fields=[
                (
                    "rev_id",
                    models.CharField(max_length=50, primary_key=True, serialize=False),
                ),
                ("rev_com_id", models.CharField(max_length=50)),
                ("rev_com_name", models.CharField(max_length=500)),
                ("rev_rate", models.CharField(blank=True, max_length=50, null=True)),
                ("rev_title", models.CharField(max_length=1000)),
                ("rev_date", models.CharField(blank=True, max_length=50, null=True)),
                ("rev_part", models.CharField(blank=True, max_length=200, null=True)),
                ("rev_now", models.CharField(blank=True, max_length=200, null=True)),
                (
                    "rev_strength",
                    models.CharField(blank=True, max_length=5000, null=True),
                ),
                (
                    "rev_weakness",
                    models.CharField(blank=True, max_length=5000, null=True),
                ),
                ("rev_wish", models.CharField(blank=True, max_length=5000, null=True)),
            ],
            options={
                "db_table": "review",
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="Users",
            fields=[
                (
                    "user_id",
                    models.CharField(max_length=50, primary_key=True, serialize=False),
                ),
                ("pwd", models.CharField(max_length=100)),
                ("email", models.CharField(max_length=200)),
                ("phone", models.CharField(max_length=50)),
            ],
            options={
                "db_table": "users",
                "managed": False,
            },
        ),
    ]
