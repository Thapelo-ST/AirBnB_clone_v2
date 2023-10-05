#!/usr/bin/python3
"""
Fabric script to distribute an archive to your web servers.
"""

from fabric.api import *
from os import path

env.user = 'ubuntu'
env.hosts = ['34.227.93.64', '3.85.54.154']


def do_deploy(archive_path):
    """Deploys an archive to the web servers."""
    if not path.exists(archive_path):
        return False

    try:
        archive_name = archive_path.split("/")[-1]
        archive_no_ext = archive_name.replace(".tgz", "")
        remote_tmp = "/tmp/{}".format(archive_name)
        remote_dest = "/data/web_static/releases/{}/".format(archive_no_ext)

        put(archive_path, remote_tmp)
        run("mkdir -p {}".format(remote_dest))
        run("tar -xzf {} -C {}".format(remote_tmp, remote_dest))
        run("rm {}".format(remote_tmp))
        run("mv {}web_static/* {}".format(remote_dest, remote_dest))
        run("rm -rf {}web_static".format(remote_dest))
        run("rm -rf /data/web_static/current")
#        print("Symbolic link")
        run("ln -s {} /data/web_static/current".format(remote_dest))
        print("New version deployed!")
        return True
    except Exception:
        # print ("Deployment failed:", str(e))
        return False
