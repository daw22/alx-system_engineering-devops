#!/usr/bin/env ruby
puts ARGV[0].scan(/\[form:(.*?)\]\s\[to:(.*?)\]\s\[flags:(.*?)\]/).join(',')
