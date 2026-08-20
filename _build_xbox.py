#!/usr/bin/env python
import dependencies.buildark.buildark as buildark

buildark.build_ark(
	["./_ark", ["./_songs/songs_ng", "/songs"]],
	"./_build/xbox/gen/",
	"./.temp_ark_xbox",
	"patch_xbox",
	"rb1_patch",
	[
		r".*\.bik$",
		r".*\..*_wii$",
		r".*\..*_ps2$",
		r".*\.xbvwii$",
		r".*\..*_ps3$",
		r".*_out\/.*",
		r".*_dbg\.milo.*",
		r".*_rt\.milo.*",
		r".*\.bak$",
		r".*\.png$",
		r".*\.jpg$",
		r".*\.dds$",
		r".*\.xcf$",
		r".*\.sh$",
		r".*\.py$"
	]
)
