#!/usr/bin/env ruby

input = ARGV[0].to_s
matches = input.scan(/^h.n$/)
puts matches.join
