# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
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
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
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


class Certificates(models.Model):
    id_certificate = models.AutoField(primary_key=True)
    id_profile = models.ForeignKey('Profiles', models.DO_NOTHING, db_column='id_profile')
    id_imagen = models.ForeignKey('Imagenes', models.DO_NOTHING, db_column='id_imagen')
    title = models.CharField(blank=True, null=True)
    issuer = models.CharField(blank=True, null=True, db_comment='Instituto')
    issued_date = models.DateTimeField(blank=True, null=True)
    credencial_url = models.CharField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True, db_comment='Fecha de registro')
    updated_at = models.DateTimeField(blank=True, null=True, db_comment='Fecha de actualización')

    class Meta:
        managed = False
        db_table = 'certificates'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
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


class Educations(models.Model):
    id_profile = models.ForeignKey('Profiles', models.DO_NOTHING, db_column='id_profile')
    id_education = models.AutoField(primary_key=True)
    description = models.TextField(blank=True, null=True, db_comment='Grado de estudio')
    type_education = models.TextField(blank=True, null=True, db_comment='Tipo de aprendizaje en la progracion obtenida')  # This field type is a guess.
    created_at = models.DateTimeField(blank=True, null=True, db_comment='Fecha de registro')
    updated_at = models.DateTimeField(blank=True, null=True, db_comment='Fecha de actualizacion')

    class Meta:
        managed = False
        db_table = 'educations'
        db_table_comment = 'Educacion del usuario en la programacion'


class Experiences(models.Model):
    id_profile = models.ForeignKey('Profiles', models.DO_NOTHING, db_column='id_profile')
    id_experience = models.AutoField(primary_key=True)
    title = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True, db_comment='Experiencia con la programacion')
    created_at = models.DateTimeField(blank=True, null=True, db_comment='Fecha de registro')
    updated_at = models.DateTimeField(blank=True, null=True, db_comment='Fecha de actualizacion')

    class Meta:
        managed = False
        db_table = 'experiences'
        db_table_comment = 'Experiencia del usuario en la programacion'


class Imagenes(models.Model):
    id_imagen = models.AutoField(primary_key=True)
    name = models.CharField(blank=True, null=True)
    path = models.CharField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True, db_comment='Fecha de registro')
    updated_at = models.DateTimeField(blank=True, null=True, db_comment='Fecha de actualización')

    class Meta:
        managed = False
        db_table = 'imagenes'


class ImagenesProject(models.Model):
    id_project = models.OneToOneField('Projects', models.DO_NOTHING, db_column='id_project', primary_key=True)  # The composite primary key (id_project, id_imagen) found, that is not supported. The first column is selected.
    id_imagen = models.ForeignKey(Imagenes, models.DO_NOTHING, db_column='id_imagen')
    default_position = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True, db_comment='Fecha de registro')
    updated_at = models.DateTimeField(blank=True, null=True, db_comment='Fecha de actualización')

    class Meta:
        managed = False
        db_table = 'imagenes_project'
        unique_together = (('id_project', 'id_imagen'),)


class Languages(models.Model):
    id_language = models.AutoField(primary_key=True)
    name = models.CharField(unique=True, db_comment='Nombre del lenguaje')
    created_at = models.DateTimeField(blank=True, null=True, db_comment='Fecha de registro')
    updated_at = models.DateTimeField(blank=True, null=True, db_comment='Fecha de actualizacion')

    class Meta:
        managed = False
        db_table = 'languages'
        db_table_comment = 'Lenguaje de programacion utilizado en el proyecto'


class NetworksType(models.Model):
    id_network_type = models.AutoField(primary_key=True)
    name = models.CharField(blank=True, null=True)
    icon_url = models.CharField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'networks_type'
        db_table_comment = 'Tabla catalogo para redes sociales'


class Profiles(models.Model):
    id_profile = models.AutoField(primary_key=True)
    id_imagen = models.ForeignKey(Imagenes, models.DO_NOTHING, db_column='id_imagen')
    id_user = models.OneToOneField('Users', models.DO_NOTHING, db_column='id_user')
    biography = models.TextField(blank=True, null=True, db_comment='Biografia')
    created_at = models.DateTimeField(blank=True, null=True, db_comment='Fecha de registro')
    updated_at = models.DateTimeField(blank=True, null=True, db_comment='Fecha de actualizacion')

    class Meta:
        managed = False
        db_table = 'profiles'
        db_table_comment = 'Informacion del usuario'


class ProjectLanguages(models.Model):
    id_project = models.OneToOneField('Projects', models.DO_NOTHING, db_column='id_project', primary_key=True)  # The composite primary key (id_project, id_language) found, that is not supported. The first column is selected.
    id_language = models.ForeignKey(Languages, models.DO_NOTHING, db_column='id_language')
    created_at = models.DateTimeField(blank=True, null=True, db_comment='Fecha de registro')
    updated_at = models.DateTimeField(blank=True, null=True, db_comment='Fecha de actualizacion')

    class Meta:
        managed = False
        db_table = 'project_languages'
        unique_together = (('id_project', 'id_language'),)
        db_table_comment = 'Tabla intermedia para representar la relación muchos a muchos entre proyectos y lenguajes de programación'


class ProjectLinks(models.Model):
    id_link = models.AutoField(primary_key=True)
    id_project = models.ForeignKey('Projects', models.DO_NOTHING, db_column='id_project')
    url = models.CharField(db_comment='Enlace del proyecto')
    type = models.TextField(blank=True, null=True, db_comment='Tipo de enlace (ej. frontend, backend, demo, docs)')  # This field type is a guess.
    description = models.TextField(blank=True, null=True, db_comment='Descripción adicional del enlace')
    created_at = models.DateTimeField(blank=True, null=True, db_comment='Fecha de registro')
    updated_at = models.DateTimeField(blank=True, null=True, db_comment='Fecha de actualización')

    class Meta:
        managed = False
        db_table = 'project_links'
        db_table_comment = 'Enlaces asociados a un proyecto (frontend, backend, demo, etc.)'


class ProjectRoles(models.Model):
    id_project = models.OneToOneField('Projects', models.DO_NOTHING, db_column='id_project', primary_key=True)  # The composite primary key (id_project, id_role) found, that is not supported. The first column is selected.
    id_role = models.ForeignKey('Roles', models.DO_NOTHING, db_column='id_role')
    created_at = models.DateTimeField(blank=True, null=True, db_comment='Fecha de registro')
    updated_at = models.DateTimeField(blank=True, null=True, db_comment='Fecha de actualización')

    class Meta:
        managed = False
        db_table = 'project_roles'
        unique_together = (('id_project', 'id_role'),)
        db_table_comment = 'Rol en el proyecto'


class ProjectTools(models.Model):
    id_project = models.OneToOneField('Projects', models.DO_NOTHING, db_column='id_project', primary_key=True)  # The composite primary key (id_project, id_tool) found, that is not supported. The first column is selected.
    id_tool = models.ForeignKey('Tools', models.DO_NOTHING, db_column='id_tool')
    created_at = models.DateTimeField(blank=True, null=True, db_comment='Fecha de registro')
    updated_at = models.DateTimeField(blank=True, null=True, db_comment='Fecha de actualización')

    class Meta:
        managed = False
        db_table = 'project_tools'
        unique_together = (('id_project', 'id_tool'),)
        db_table_comment = 'Herramientas utilizadas en un proyecto (relación muchos a muchos)'


class Projects(models.Model):
    id_project = models.AutoField(primary_key=True)
    id_user = models.ForeignKey('Users', models.DO_NOTHING, db_column='id_user')
    title = models.CharField(blank=True, null=True, db_comment='Titulo del proyecto')
    description = models.TextField(blank=True, null=True, db_comment='Descripcion del proyecto')
    project_start_date = models.DateTimeField(blank=True, null=True, db_comment='Fecha del proyecto')
    created_at = models.DateTimeField(blank=True, null=True, db_comment='Fecha de registro')
    updated_at = models.DateTimeField(blank=True, null=True, db_comment='Fecha de actualizacion')

    class Meta:
        managed = False
        db_table = 'projects'
        db_table_comment = 'Proyectos realizados por el usuario'


class Roles(models.Model):
    id_role = models.AutoField(primary_key=True)
    name = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'roles'


class SocialNetworks(models.Model):
    id_social_network = models.AutoField(primary_key=True)
    id_profile = models.ForeignKey(Profiles, models.DO_NOTHING, db_column='id_profile')
    id_networks_type = models.ForeignKey(NetworksType, models.DO_NOTHING, db_column='id_networks_type')
    url = models.CharField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True, db_comment='Fecha de registro')
    updated_at = models.DateTimeField(blank=True, null=True, db_comment='Fecha de actualizacion')

    class Meta:
        managed = False
        db_table = 'social_networks'
        db_table_comment = 'Diferentes redes sociales'


class Tools(models.Model):
    id_tool = models.AutoField(primary_key=True)
    name = models.CharField(unique=True, db_comment='Nombre de la herramienta (ej. React, Tailwind, Docker)')
    created_at = models.DateTimeField(blank=True, null=True, db_comment='Fecha de registro')
    updated_at = models.DateTimeField(blank=True, null=True, db_comment='Fecha de actualización')

    class Meta:
        managed = False
        db_table = 'tools'
        db_table_comment = 'Herramientas utilizadas en el proyecto'


class Users(models.Model):
    id_user = models.AutoField(primary_key=True)
    first_name = models.CharField(blank=True, null=True, db_comment='Primer nombre')
    second_name = models.CharField(blank=True, null=True, db_comment='Segundo nombre')
    first_surname = models.CharField(blank=True, null=True, db_comment='Primer apellido')
    second_surname = models.CharField(blank=True, null=True, db_comment='Segundo apellido')
    nick_name = models.CharField(blank=True, null=True, db_comment='Avatar')
    phone = models.CharField(blank=True, null=True, db_comment='Telefono de contacto')
    email = models.CharField(unique=True, db_comment='Correo del usuario')
    gender = models.TextField(db_comment='Genero del usuario')  # This field type is a guess.
    abstract_user = models.TextField(blank=True, null=True, db_comment='Resumen biografico del usuario')
    created_at = models.DateTimeField(blank=True, null=True, db_comment='Fecha de registro')
    updated_at = models.DateTimeField(blank=True, null=True, db_comment='Fecha de actualizacion')

    class Meta:
        managed = False
        db_table = 'users'
        db_table_comment = 'Tabla para la identificacion del usuario'
