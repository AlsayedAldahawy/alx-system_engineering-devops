#!/usr/bin/env ruby

puts ARGV[0].scan(/.+from:(\+?\w+)\].+to:(\+?\w+)\].+flags:([-110:]{5,15})\]/).join","
