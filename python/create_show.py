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
seq_list = ["010", "020", "030", "040", "050", "060", "070"]
shot_list = ["0010", "0020", "0030", "0040"]
for seq in seq_list:
    cur_show_two.sequence(seq)
    for shot in shot_list:
        cur_show_two.shot(seq, shot)