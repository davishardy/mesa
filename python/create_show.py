"""
Create a show with the proper config
"""

import mesa_api

cur_show = mesa_api.path.Path()

cur_show.find_sequences()

print(cur_show.find_shots('s010'))
