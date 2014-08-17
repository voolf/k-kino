#!/usr/bin/env python
import os
import sys
# manage.py startapp article создает новые модуль проект в консоли
if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "KmKProject.settings")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
