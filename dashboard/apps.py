from django.apps import AppConfig

def create_group(sender, **kwargs):
    from django.contrib.auth.models import Group

    group_names = ['ADMIN_TU',"KASUBBAG_TU","USER"]

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
