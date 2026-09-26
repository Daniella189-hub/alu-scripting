#!/usr/bin/env ruby

input = ARGV[0].to_s
matches = input.scan(/hbt{1,5}n/)
puts matches.join
