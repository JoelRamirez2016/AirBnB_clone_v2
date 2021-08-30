#!/usr/bin/python3
"""
Define Funtion do_pack and
distributes an archive to your web servers, using the function do_deploy
"""
from datetime import datetime
import os
from fabric.api import local, put, run, env
from os.path import isfile

env.user = "ubuntu"
env.hosts = ["35.229.27.8", "54.83.116.20"]


def do_pack():
    """
    Generates a .tgz archive from the contents of the web_static folder
    of your AirBnB Clone repo, using the function do_pack.
    """
    dt = datetime.now()
    f = "versions/web_static_{}.tgz".format(dt.strftime("%Y%m%d%H%M%S"))

    if not os.path.isdir("versions") and local("mkdir -p versions").failed:
        return None

    if local("tar -cvzf {} web_static".format(f)).failed:
        return None

    return f


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


def deploy():
    """creates and distributes an archive to your web"""
    f = do_pack()

    if not f:
        return False

    return do_deploy(f)
