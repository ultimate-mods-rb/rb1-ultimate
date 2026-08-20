#!/usr/bin/env python
import dependencies.buildark.buildark as buildark

buildark.build_ark(
	[
		"./_ext/ps2",
		"./_ark",
		["./_songs/songs_ps2", "/songs"]
	],
	"./_build/ps2/GEN",
	"./.temp_ark_ps2",
	"MAIN",
	"rb1",
	[
		r".*\..*_ps3$",
		r".*\..*_wii$",
		r".*\.xbv$",
		r".*\.xbvwii$",
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
	],
	split_size = "4123741823"
)
