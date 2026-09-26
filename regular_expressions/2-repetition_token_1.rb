#!/usr/bin/env ruby

input = ARGV[0].to_s
matches = input.scan(/hb?tn/)
puts matches.join
