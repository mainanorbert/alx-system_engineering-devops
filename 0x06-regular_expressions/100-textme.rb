#!/usr/bin/env ruby
# [ used to match opening bracket and ] to match closing bracket
# \ is used to escape [ as \[ and ] as \]
puts ARGV[0].scan(/\[from:(.*?)\] \[to:(.*?)\] \[flags:(.*?)\]/).join(',')
