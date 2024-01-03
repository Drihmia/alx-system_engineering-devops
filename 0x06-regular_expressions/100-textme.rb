#!/usr/bin/env ruby
matching_group = ARGV[0].match(/.*\[from:(\w+|\+?\d+)\].*\[to:(\w+|\+?\d+)\].*\[flags:(.*?)\].*/)
puts matching_group[1] + "," + matching_group[2] + "," + matching_group[3]
