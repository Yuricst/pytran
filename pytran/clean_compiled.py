"""
Clean compiled files
"""

import os

def clean_compiled(extensions="all"):
	"""Remove compiled files"""
	if extensions=="all":
		ext_list = ["so", "exe", "out"]
	else:
		ext_list = [extensions]
	for ext in ext_list:
		os.system(f"rm *.{ext}")
		print(f"Removed .{ext} files!")
	return