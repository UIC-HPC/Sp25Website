#!/usr/bin/env ruby
require 'yaml'

# Check if a directory path was provided as an argument
unless ARGV.length > 0
  puts "Usage: ruby #{__FILE__} path/to/image_directory"
  exit
end

image_directory = ARGV[0]
directory_name = File.basename(image_directory)

# Select jpg and jpeg files from the given directory
image_files = Dir.children(image_directory).select { |f| f.match?(/.*\.(jpg|jpeg)$/i) }
image_list = image_files.map { |filename| File.join(directory_name, filename) }

# Write the list to a YAML file named after the final directory
File.write("./_data/#{directory_name}.yml", image_list.to_yaml)
