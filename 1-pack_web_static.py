#!/usr/bin/python3
from fabric.api import local
from datetime import datetime

def do_pack():
    """Generates a .tgz archive from the web_static folder."""
    try:
        current_time = datetime.now()
        archive_name = "web_static_{}{}{}{}{}{}.tgz".format(
            current_time.year, current_time.month, current_time.day,
            current_time.hour, current_time.minute, current_time.second)

        local("mkdir -p versions")

        result = local("tar -czvf versions/{} web_static".format(archive_name))

        if result.succeeded:
            return "versions/{}".format(archive_name)
        else:
            return None
    except Exception:
        return None
