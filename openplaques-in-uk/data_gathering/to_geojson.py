import json
import os

from get_data import str_dt

os.chdir(os.path.dirname(__file__))
print(os.getcwd())

with open('../data/20160609102653_open_plaques_uk.json') as fp:
    data = json.load(fp)

geojson = {
    "type": "FeatureCollection",
    "features": [
        {
            "type": "Feature",
            "geometry": {
                "type": "Point",
                "coordinates": [d["longitude"], d["latitude"]],
            },
            "properties": d,
        } for d in data]}

with open('../data/{}_open_plaques_uk.geojson'.format(str_dt()), 'w') as out:
    json.dump(geojson, out)
