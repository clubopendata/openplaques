import json
import os
import sys
import urllib.request

from datetime import datetime


def get_json():
    """get the Open Plaques JSON"""
    request = ('https://dl.dropboxusercontent.com/u/21695507/openplaques/' +
               'open-plaques-United-Kingdom-2016-05-22.json')
    response = urllib.request.urlopen(request)
    str_response = response.read().decode('utf-8')
    return json.loads(str_response)


def get_file_path():
    """Get the path to the current file"""
    return os.path.dirname(os.path.dirname(os.path.realpath(sys.argv[0])))


def make_out_dir(out_root):
    """Make a '/data' dir in .."""
    out_path = os.path.join(out_root, 'data')
    if not os.path.exists(out_path):
        os.makedirs(out_path)
    return out_path


def str_dt():
    """Return a string representation of today's date
    without commas, colons or spaces. Ideal for adding to
    filenames as a form of version control"""
    return (str(datetime.now())
            .replace('-', '')
            .replace(':', '')
            .replace(' ', '')
            .split('.')[0])


def make_out_file():
    out_root = get_file_path()
    out_directory = make_out_dir(out_root)
    return os.path.join(
        out_directory,
        '{}_open_plaques_uk.json'.format(str_dt())
    )

if __name__ == "__main__":
    obj = get_json()
    out_file = make_out_file()
    with open(out_file, 'w') as fp:
        json.dump(obj, fp)
