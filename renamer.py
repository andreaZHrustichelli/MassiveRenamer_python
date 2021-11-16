import os
    
print("Program STARTED")
lines_in = [line_in.rstrip('\n') for line_in in open("IN.txt")]
print(lines_in)
print(len(lines_in))
lines_out = [line_out.rstrip('\n') for line_out in open("OUT.txt")]
print(lines_out)
print(len(lines_out))

    i=0
    while i < len(lines_in):
         nome_file_in=lines_in[i]
         nome_file_out=lines_out[i]
         print("Rename from " + nome_file_in + " to " + nome_file_out)
         os.system("mv " + nome_file_in + " " + nome_file_out)
         i=i+1  
