#!/usr/bin/python3
"""
Fabric script to distribute an archive to your web servers.
"""

from fabric.api import env, put, run, local
from os.path import exists

env.hosts = ['34.227.93.64', '3.85.54.154']
env.user = 'ubuntu'
env.key_filename = '~/.ssh/id_rsa'

def do_deploy(archive_path):
    """Deploys an archive to the web servers."""
    if not exists(archive_path):
        return False

    try:
        put(archive_path, '/tmp/')

        archive_filename = archive_path.split('/')[-1]
        archive_name = archive_filename.split('.')[0]

        run('mkdir -p /data/web_static/releases/{}/'.format(archive_name))

        run('tar -xzf /tmp/{} -C /data/web_static/releases/{}/'.format(
            archive_filename, archive_name))

        run('rm /tmp/{}'.format(archive_filename))

        run('mv /data/web_static/releases/{}/web_static/* \
            /data/web_static/releases/{}/'.format(archive_name, archive_name))

        run('rm -rf /data/web_static/releases/{}/web_static'.format(
            archive_name))

        run('rm -rf /data/web_static/current')

        run('ln -s /data/web_static/releases/{}/ /data/web_static/current'
            .format(archive_name))

        print("New version deployed!")
        return True
    except Exception:
        return False
