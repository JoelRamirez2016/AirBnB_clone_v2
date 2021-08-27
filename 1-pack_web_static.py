#!/usr/bin/python3
"""
Define Funtion do_pack
"""
from datetime import datetime
from fabric.api import local


def do_pack():
    """
    Generates a .tgz archive from the contents of the web_static folder
    of your AirBnB Clone repo, using the function do_pack.
    """
    dt = datetime.now()
    f = "versions/web_static_{}.tgz".format(dt.strftime("%Y%m%d%H%M%S"))

    if local("tar -cvzf {} web_static".format(f)).failed:
        return None
    return f
