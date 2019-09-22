"""User admin classes."""

from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib import admin
from django.contrib.auth.models import User
# models
from users.models import Profile

# Register your models here.
# admin.site.register(Profile) esto se puede sustituir por una class
# y un decorador

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    """Profile admin."""

    # Muestra los campos que indiquemos en la tupla
    list_display = ('user', 'phone_number', 'website', 'picture')
    # Muestra los campos indicados como links
    list_display_links = ('user',)
    # permite editarlos desde la vista lista
    list_editable = ('phone_number', 'website', 'picture')

    # Esto establece el filtro de busqueda
    search_fields = (
        'user__email',
        'user__first_name',
        'user__last_name',
        'phone_number',
    )

    # En la vista agrega un filtro
    list_filter = (
        'user__is_active',
        'user__is_staff',
        'created',
        'modified',
    )

    # Cambia el orden de aparicion de los campos en el formulario
    fieldsets = (
        # Profile es un titulo puede ser None
        ('Profile', {
            'fields': (('user', 'picture'),), # la notacion anterior ubica un campo al lado de otro
        }),
        ('Extra info', {
            'fields': (
                ('website', 'phone_number'),
                ('biography')
            )
        }),
        ('Metadata', {
            'fields': (('created', 'modified')),
        }),
    )

    # me permite agregar campos como de solo lectura
    readonly_fields = ('created', 'modified', 'user')


class ProfileInline(admin.StackedInline):
    """Profile in-line admin for users."""

    model = Profile
    can_delete = False
    verbose_name_plural = 'profiles'


class UserAdmin(BaseUserAdmin):
    """Add profile admin to base user admin."""
    inlines = (ProfileInline,)
    # modifica la vista tree de user en django (en donde se crean los nuevos usuarios)
    # y se ven los ya creados
    list_display = (
        'username',
        'email',
        'first_name',
        'last_name',
        'is_active',
        'is_staff'
    )


admin.site.unregister(User)
admin.site.register(User, UserAdmin)
