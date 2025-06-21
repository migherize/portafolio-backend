from django.contrib import admin

# Register your models here.
from apps.users.models import (
    Educations,
    Experiences,
    Imagenes,
    ImagenesProject,
    Languages,
    NetworksType,
    Profiles,
    ProjectLanguages,
    ProjectLinks,
    ProjectRoles,
    ProjectTools,
    Projects,
    Roles,
    SocialNetworks,
    Tools,
    Users,
)

admin.site.register(Educations)
admin.site.register(Experiences)
admin.site.register(Imagenes)
admin.site.register(ImagenesProject)
admin.site.register(Languages)
admin.site.register(NetworksType)
admin.site.register(Profiles)
admin.site.register(ProjectLanguages)
admin.site.register(ProjectLinks)
admin.site.register(ProjectRoles)
admin.site.register(ProjectTools)
admin.site.register(Projects)
admin.site.register(Roles)
admin.site.register(SocialNetworks)
admin.site.register(Tools)
admin.site.register(Users)
