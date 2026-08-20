#!/usr/bin/env python
import dependencies.buildark.buildark as buildark

buildark.build_ark(
	[
		"./_ext/wii",
		"./_ark",
		["./_songs/songs_wii", "/songs"]
	],
	"./_build/wii/files/gen",
	"./.temp_ark_wii",
	"main",
	"rb1",
	[
		r".*\..*_ps3$",
		r".*\..*_ps2$",
		r".*\.xbv$",
		r".*\..*_xbox$",
		r".*_out\/.*",
		r".*_dbg\.milo.*",
		r".*_rt\.milo.*",
		r"..*ulti\/updates.*",
		r".*\.bak$",
		r".*\.png$",
		r".*\.jpg$",
		r".*\.dds$",
		r".*\.xcf$",
		r".*\.sh$",
		r".*\.py$"
	]
)
