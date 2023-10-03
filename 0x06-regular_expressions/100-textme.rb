#!/usr/bin/env ruby

# Define the regular expression pattern to match sender, receiver, and flags
pattern = /\[from:(.*?)\] \[to:(.*?)\] \[flags:(.*?)\]/i

# Check if a log entry argument is provided
if ARGV.length != 1
  puts "Usage: #{$PROGRAM_NAME} <log_entry>"
  exit 1
end

# Get the log entry from the command-line arguments
log_entry = ARGV[0]

# Extract sender, receiver, and flags using the regular expression
match_data = log_entry.match(pattern)

if match_data
  sender = match_data[1]
  receiver = match_data[2]
  flags = match_data[3]
  puts "#{sender},#{receiver},#{flags}"
else
  puts "Invalid log entry format."
end
