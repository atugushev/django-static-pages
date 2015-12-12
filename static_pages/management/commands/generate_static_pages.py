import os

from django.conf import settings
from django.core.management.base import BaseCommand, CommandError
from django.core.urlresolvers import reverse, NoReverseMatch
from django.test import Client
from django.utils import translation


class Command(BaseCommand):
    help = 'Generates static pages'

    def handle(self, *args, **options):
        # Handle settings
        pages = getattr(settings, 'STATIC_PAGES_LIST', ())
        output_dir = getattr(settings, 'STATIC_PAGES_DIR', None)
        client_kwargs = getattr(settings, 'STATIC_PAGES_CLIENT_KWARGS', {})

        # No pages -- skip
        if not pages:
            self.stdout.write('Nothing to generate')
            return

        # Required setting
        if output_dir is None:
            raise CommandError('Required to specify a path in STATIC_PAGES_DIR setting')

        # Absolute path is required
        if not output_dir.startswith('/'):
            raise CommandError('A path in STATIC_PAGES_DIR setting should be an absolute path')

        # Activate a fixed LANGUAGE_CODE locale, because by default
        # the BaseCommand.execute() method deactivates translations
        # See https://docs.djangoproject.com/en/dev/howto/custom-management-commands/#management-commands-and-locales
        translation.activate(settings.LANGUAGE_CODE)

        for url, fn in pages:
            # Trailing slash
            dest_file = output_dir
            if not output_dir.endswith('/'):
                dest_file += '/'

            dest_file += fn
            dest_dir = os.path.dirname(dest_file)

            # Make sure that destination directory is exists
            if not os.path.exists(dest_dir):
                os.makedirs(dest_dir)

            # Init client
            client = Client(**client_kwargs)

            # Try paths or view names
            try:
                page_url = reverse(url)
            except NoReverseMatch:
                page_url = url

            # Get response
            response = client.get(page_url)

            # Write output
            with open(dest_file, 'wb') as f:
                self.stdout.write('Generate static page: %(file)s (%(status_code)s)' % {
                    'file': dest_file,
                    'status_code': response.status_code
                })
                f.write(response.content)
