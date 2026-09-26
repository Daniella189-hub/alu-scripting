#!/usr/bin/env ruby


input = ARGV[0].to_s
matches = input.scan(/^\d{10}$/)
puts matches.join
