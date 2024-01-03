#!/usr/bin/env ruby
matching_group = ARGV[0].match(/.*\[from:(?<from>\w+|\+?\d+)\].*\[to:(?<to>\w+|\+?\d+)\].*\[flags:(?<flags>.*?)\].*/)
puts "#{matching_group[:from]}, #{matching_group[:to]}, #{matching_group[:flags]}"
