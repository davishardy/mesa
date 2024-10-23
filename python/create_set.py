
import json
import mesa_api

test_file = "/Users/davishardy/SCAD/5_Tools/mesa/python/mesa_api/templates/modset.json"

with open(test_file, 'r') as file:
    folder_structure = json.load(file)

cur_show_two = mesa_api.Create()
cur_show_two.create_asset('/Users/davishardy/SCAD/5_Tools/Collaborativespace/ski/show/modset', "hill", folder_structure)