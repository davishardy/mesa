
import sys
import mesa_api


# Parse name argument
# arg = sys.argv[1]
# print(arg)
arg = "monty"
show_obj = mesa_api.Create()
show_obj.show_element("modset", "set", arg)
