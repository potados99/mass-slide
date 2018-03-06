#-*- coding: utf-8 -*-

import templateModule
import textModule


raw = templateModule.get_raw_list()

processed = textModule.process_gospel(raw["복음"])

for i in processed:
	print i
