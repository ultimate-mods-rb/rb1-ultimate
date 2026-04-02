import os
import platform
import shutil
import re
import subprocess

def build_ark(srcs, dest, temp_ark, ark_name, game, excludes):
	# init exec locations
	# maybe just like run from path cuz uh this is terrible
	# dont do as i do, do i as i say.
	match platform.system():
		case "Windows":
			arkhelper_path = "./dependencies/arkhelper"
		case "Linux":
			arkhelper_path = "./dependencies/linux/arkhelper"
		case "Darwin":
			arkhelper_path = "./dependencies/macos/arkhelper"

	# delete temp path if it exists
	if os.path.exists(temp_ark):
		shutil.rmtree(temp_ark)

	os.mkdir(temp_ark)

	# create temp ark folder with only relevant files
	for path in srcs:
		for dirpath, dirnames, filenames in os.walk(path):
			for name in filenames:
				file = os.path.join(dirpath, name)
				include = True

				# match file through all regex paterns
				# idk python maybe optize this with like while or something
				for exclude in excludes:
					if re.search(exclude, file):
						include = False

				if include:
					file_temp = file.replace(path, temp_ark)
					dirpath_temp = dirpath.replace(path, temp_ark)

					# make dirs and copy/link files
					os.makedirs(dirpath_temp, exist_ok=True)
					if platform.system() == "Windows":
						shutil.copy(file, file_temp)
					else:
						subprocess.run(["ln", file, file_temp, "-f"])

	# build ark
	run = [arkhelper_path, "dir2ark",  temp_ark, dest, "-n", ark_name, "-s", "2147483647"]
	match game:
		case "rb1":
			run.extend(["-e", "-v", "4"])
		case "rb1_patch":
			run.extend(["-e", "-v", "4", "-f"])
		case "rb2":
			run.extend(["-e", "-v", "5"])
		case "rb3":
			run.extend(["-e", "-v", "6"])
	subprocess.run(run)

	# delete temp path
	shutil.rmtree(temp_ark)
