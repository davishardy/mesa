"""
Create a show with the proper config
"""

import mesa_api
# Testings path func
"""
cur_show = mesa_api.path.Path()
cur_show.find_sequences()
print(cur_show.find_shots(cur_show.seqs[0]))
"""

cur_show_two = mesa_api.Create()
cur_show_two.show()
cur_show_two.sequence("020")
cur_show_two.shot("020", "0010")