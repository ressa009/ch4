from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Company(models.Model):
    com_id = models.CharField(primary_key=True, max_length=50)
    com_name = models.CharField(max_length=50)
    com_location = models.CharField(max_length=800, blank=True, null=True)
    com_employees = models.CharField(max_length=300, blank=True, null=True)
    com_size = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'company'


class Cv(models.Model):
    cv_id = models.CharField(primary_key=True, max_length=50)
    cv_company = models.CharField(max_length=50, blank=True, null=True)
    cv_spec = models.CharField(max_length=1000, blank=True, null=True)
    cv_question = models.CharField(max_length=5000, blank=True, null=True)
    cv_answer = models.CharField(max_length=5000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cv'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Interview(models.Model):
    int_id = models.CharField(primary_key=True, max_length=50)
    int_com_id = models.CharField(max_length=50)
    name_list = models.CharField(max_length=50)
    int_difficulty = models.CharField(max_length=50, blank=True, null=True)
    int_date = models.CharField(max_length=50, blank=True, null=True)
    int_question = models.CharField(max_length=5000, blank=True, null=True)
    int_answer = models.CharField(max_length=5000, blank=True, null=True)
    int_result = models.CharField(max_length=50, blank=True, null=True)
    int_post_date = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'interview'


class News(models.Model):
    news_id = models.CharField(primary_key=True, max_length=50)
    news_com_id = models.CharField(max_length=50, blank=True, null=True)
    news_title = models.CharField(max_length=500)
    news_href = models.CharField(max_length=500, blank=True, null=True)
    news_date = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'news'


class Post(models.Model):

    post_id = models.CharField(primary_key=True, max_length=50)
    post_com_id = models.CharField(max_length=50)
    post_com_name = models.CharField(max_length=500, blank=True, null=True)
    post_title = models.CharField(max_length=500)
    post_career = models.CharField(max_length=500)
    post_location = models.CharField(max_length=800, blank=True, null=True)
    post_emp_types = models.CharField(max_length=500, blank=True, null=True)
    post_dday = models.CharField(max_length=50, blank=True, null=True)
    post_pay = models.CharField(max_length=100, blank=True, null=True)
    post_href = models.CharField(max_length=500)

    class Meta:
        managed = False
        db_table = 'post'


class Review(models.Model):
    rev_id = models.CharField(primary_key=True, max_length=50)
    rev_com_id = models.CharField(max_length=50)
    rev_com_name = models.CharField(max_length=500)
    rev_rate = models.CharField(max_length=50, blank=True, null=True)
    rev_title = models.CharField(max_length=1000)
    rev_date = models.CharField(max_length=50, blank=True, null=True)
    rev_part = models.CharField(max_length=200, blank=True, null=True)
    rev_now = models.CharField(max_length=200, blank=True, null=True)
    rev_strength = models.CharField(max_length=5000, blank=True, null=True)
    rev_weakness = models.CharField(max_length=5000, blank=True, null=True)
    rev_wish = models.CharField(max_length=5000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'review'


class Users(models.Model):
    user_id = models.CharField(primary_key=True, max_length=50)
    pwd = models.CharField(max_length=100)
    email = models.CharField(max_length=200)
    phone = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'users'