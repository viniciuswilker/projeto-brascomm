from django.core.management.base import BaseCommand
from django.contrib.auth.models import User

class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        if not User.objects.filter(username='admin').exists():
            User.objects.create_superuser('admin', 'admin@email.com', 'admin123')
            self.stdout.write(self.style.SUCCESS('Admin criado com sucesso (admin/admin123)'))
        else:
            self.stdout.write(self.style.WARNING('Admin já existe'))