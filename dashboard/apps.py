from django.apps import AppConfig

def create_group(sender, **kwargs):
    from django.contrib.auth.models import Group

    group_names = ['TU_SET_ADMIN',"TU_SET_KASUBBAG","USER","ADMIN_TU"]

    # Check if the group already exists to avoid duplicates
    for group_name in group_names:
        if not Group.objects.filter(name=group_name).exists():
            Group.objects.create(name=group_name)



class DashboardConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'dashboard'

    def ready(self):
         # Connect the post_migrate signal to the create_groups function
        from django.db.models.signals import post_migrate
        post_migrate.connect(create_group, sender=self)
