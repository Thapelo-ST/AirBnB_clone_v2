#!/usr/bin/python3
"""Fabric script to distribute an archive to web servers"""
from fabric.api import *
from os import path
from datetime import datetime

env.user = 'ubuntu'
env.hosts = ['34.227.93.64', '3.85.54.154']


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

def deploy():
    """Full deployment process"""
    archive_path = do_pack()
    if not archive_path:
        return False
    return do_deploy(archive_path)
