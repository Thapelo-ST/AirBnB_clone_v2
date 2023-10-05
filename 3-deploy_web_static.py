#!/usr/bin/python3
"""Fabric script to distribute an archive to web servers"""
from fabric.api import env, put, run
from os import path
from datetime import datetime

env.user = "ubuntu"
env.hosts = ['<IP web-01>', '<IP web-02>']


def do_pack():
    """Create a tarball of the web_static folder"""
    timestamp = datetime.now().strftime('%Y%m%d%H%M%S')
    archive_path = "versions/web_static_{}.tgz".format(timestamp)
    local("mkdir -p versions")
    result = local("tar -czvf {} web_static".format(archive_path))
    if result.failed:
        return None
    return archive_path


def do_deploy(archive_path):
    """Distribute and deploy the web_static archive"""
    if not path.exists(archive_path):
        return False

    try:
        put(archive_path, "/tmp/")
        filename = path.basename(archive_path)
        no_ext = filename.replace(".tgz", "")
        run("mkdir -p /data/web_static/releases/{}/".format(no_ext))
        run("tar -xzf /tmp/{} -C /data/web_static/releases/{}/".format(
            filename, no_ext))
        run("rm /tmp/{}".format(filename))
        run("mv /data/web_static/releases/{}/web_static/* \
            /data/web_static/releases/{}/".format(no_ext, no_ext))
        run("rm -rf /data/web_static/current")
        run("ln -s /data/web_static/releases/{}/ /data/web_static/current".format(no_ext))

        return True
    except Exception as e:
        return False


def deploy():
    """Full deployment process"""
    archive_path = do_pack()
    if not archive_path:
        return False
    return do_deploy(archive_path)
