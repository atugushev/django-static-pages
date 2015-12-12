import codecs
import os
import shutil

from django.conf import settings
from django.core.management import CommandError
from django.test import SimpleTestCase
from django.test.utils import override_settings
from django.utils.encoding import force_text

from static_pages.management.commands import generate_static_pages
from django.utils.six import StringIO


class GenerateStaticPagesCase(SimpleTestCase):

    def setUp(self):
        self.command = generate_static_pages.Command()

    def tearDown(self):
        shutil.rmtree(settings.STATIC_PAGES_DIR, ignore_errors=True)

    def get_file(self, filepath):
        assert filepath, 'filepath is empty.'
        filepath = os.path.join(settings.STATIC_PAGES_DIR, filepath)
        with codecs.open(filepath, "r", "utf-8") as f:
            return f.read()

    def assertFileEqual(self, filepath, text):
        file_text = self.get_file(force_text(filepath))
        self.assertEqual(
            text,
            file_text,
            "'%s' not '%s'" % (text, file_text),
        )

    def test_command(self):
        self.command.execute()
        self.assertFileEqual('index.html', 'Hello, World!')
        self.assertFileEqual('about.html', 'I am the static pages generator')

    @override_settings(STATIC_PAGES_DIR=None)
    def test_setting_dir_required(self):
        self.assertRaises(CommandError, self.command.execute)

    @override_settings(STATIC_PAGES_DIR='relative/path/')
    def test_trailing_slash(self):
        self.assertRaises(CommandError, self.command.execute)

    @override_settings(STATIC_PAGES_LIST=None)
    def test_setting_pages_list_none(self):
        # noinspection PyCallingNonCallable
        stdout = StringIO()
        self.command.execute(stdout=stdout)
        self.assertEqual(stdout.getvalue(), "Nothing to generate\n")
