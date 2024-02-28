#!/usr/bin/env ruby

#Making a pattern for sender and receiver and flags
sender = /from:(.*?)\]/
receiver = /to:(.*?)\]/
flags = /flags:(.*?)\]/

input = ARGV[0]

match_sender = input.match(sender)[1]
match_receiver = input.match(receiver)[1]
match_flags = input.match(flags)[1]

puts match_sender + ',' + match_receiver + ',' + match_flags
