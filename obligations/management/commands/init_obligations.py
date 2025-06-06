from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from obligations.models import ZonalObligation

class Command(BaseCommand):
    help = 'Initialize zonal obligations with zero values'

    def handle(self, *args, **kwargs):
        # Get or create a superuser for initial records
        superuser = User.objects.filter(is_superuser=True).first()
        if not superuser:
            self.stdout.write(self.style.ERROR('No superuser found. Please create a superuser first.'))
            return

        # Get all category choices
        categories = [choice[0] for choice in ZonalObligation.CATEGORY_CHOICES]

        # Create initial records for each category
        for category in categories:
            ZonalObligation.objects.get_or_create(
                category=category,
                defaults={
                    'current_figure': 0,
                    'projected_target': 0,
                    'created_by': superuser
                }
            )
            self.stdout.write(self.style.SUCCESS(f'Created initial record for {category}')) 