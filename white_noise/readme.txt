## to convert input mp3 to a format readable by python library 
ffmpeg -i input.mp3 -codec:a libmp3lame -qscale:a 2 output.mp3

