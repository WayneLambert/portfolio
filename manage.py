#!/usr/bin/env python
import os
import sys


if __name__ == '__main__':
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'aa_project.settings')

    try:
        from django.conf import settings
        from django.core.management import execute_from_command_line

        if settings.DEBUG and (
                os.environ.get('RUN_MAIN') or os.environ.get('WERKZEUG_RUN_MAIN')):
            import ptvsd
            ptvsd.enable_attach(address=('0.0.0.0', 8890))
            print("Attached remote debugger to Docker container")
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)
