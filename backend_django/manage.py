#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    """Run administrative tasks."""
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc

    # react 템플릿 
    # try:
    #     if sys.argv == 'react':
    #         project_root = os.getcwd()
    #         os.system("npm run build")
    #         os.chdir(project_root)
    #         sys.argv.pop(2)
    # except IndexError:
    #     execute_from_command_line(sys.argv)
    # else:
    #     execute_from_command_line(sys.argv)
    # 여기까지     
    execute_from_command_line(sys.argv)


if __name__ == "__main__":
    main()
