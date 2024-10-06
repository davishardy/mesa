# mkshow.py
# Version 1.0.0
# 2024-10-5
# Davis Hardy

# Create show

# Import Modules
import os
import mkutils as mku

def create_show():
    show, show_root = mku.get_show()
    
    mod_dirs = ["modchars", "modsets", "modprops"]

    if os.path.isdir(os.path.join(show_root, "show")) == True:
        for dir in mod_dirs:
            if os.path.isdir(os.path.join(show_root, "show", dir)) == False:
                os.mkdir(os.path.join(show_root, "show", dir))

create_show()

