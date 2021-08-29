#!/usr/bin/python3
"""distributes an archive to your web servers, using the function do_deploy"""
from fabric.api import local, put, run, env
from os.path import isfile

env.user = "ubuntu"
env.hosts = ["35.229.27.8", "54.83.116.20"]


def do_deploy(archive_path):
    """distributes an archive to your web servers"""

    if not isfile(archive_path):
        return False

    f = archive_path.split('/')[1]
    d = "/data/web_static/releases/{}/".format(f.split('.')[0])

    try:
        put(archive_path, "/tmp/")
        run('sudo mkdir -p {}'.format(d))
        run('sudo tar -xzf /tmp/{} -C {}'.format(f, d))
        run('sudo rm /tmp/{}'.format(f))
        run('sudo mv {}web_static/* {}'.format(d, d))
        run('sudo rm -rf {}web_static'.format(d))
        run('sudo rm -rf /data/web_static/current')
        run('sudo ln -s {} /data/web_static/current'.format(d))
    except Exception:
        return False

    return True
