#!/usr/bin/env ruby

# Define the regular expression pattern to match sender, receiver, and flags
pattern = /^(?:Message from (\S+) to (\S+):|Text from (\S+) to (\S+):)\s*(.*?)\s*$/i

# Check if a log file argument is provided
if ARGV.length != 1
  puts "Usage: #{$PROGRAM_NAME} <log_file>"
  exit 1
end

# Get the log file path from the command-line arguments
log_file_path = ARGV[0]

# Check if the log file exists
if File.exist?(log_file_path)
  # Open and read the log file line by line
  File.foreach(log_file_path) do |line|
    match_data = line.match(pattern)
    if match_data
      sender = match_data[1] || match_data[3]
      receiver = match_data[2] || match_data[4]
      flags = match_data[5].scan(/#\w+/).join(',') # Extract and join flags
      puts "#{sender},#{receiver},#{flags}"
    end
  end
else
  puts "The log file '#{log_file_path}' does not exist."
end
