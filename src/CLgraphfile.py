# CLgraphfile.py written for Python 2.7
#
# This Python program reads a file describing a graph 
# and creates the concrete ILP for the maximum clique problem,
# for that graph.
# DG October 9, 2017

# Note, for anyone new to programming: This looks very cluttered, but
# everything to the right of the hash mark (#) on any line (such as this one) is a comment
# ignored by python. It is to help humans understand the program.


#import sys  # this imports the module called `sys', which is a collection of programs
            # that facilitate system calls

def MClique(graph_file, lp_file):
  #arg1 = graph_file    # assign the first argument (graph189.txt) to the variable arg1
  #arg2 = lp_file   # assign the second argument (graph189.lp) to the variable arg2
                        # The values in arg1 and arg2 are strings.

  INFILE = open(graph_file, "r")  # open the file specified by the value of arg1, to read from the file.
  OUTFILE = open(lp_file, "w") # open the file specified by the value of arg2, to write to the file.

  constraints = "such that \n\n"  # assign the string `such that \n\n' to the variable `constraints'
  listC = ""                      # assign the empty string to the variable `listC'
  binaries = "binary \n"          # assign the string `binary \n' to the variable `binaries'

  i = 0
  for line in INFILE:  # read in the lines from INFILE, one line at a time
      i = i + 1   # increment i to keep track of the line number just read in.
      listC = listC + "+ C(%d) " % i   # concatenate the string "+ C(i) " to the variable 'listC'
      binaries = binaries + "C(%d)\n" % i # and concatenate "+ C(i) \n" to the variable 'binaries'

      j = 0    
      for char in line:   # for each character in the line just read in:
         j = j + 1    # increment j to keep track of the character position being examined.
         if char == '0' and (i < j):  # if the char is a '0', create the next string. But we don't
                                      # want to generate the same inequality twice, so we only
                                      # do it if i < j.
            string = "C(%d) + C(%d) <= 1\n" % (i,j)  # create the needed inequality for i and j
            constraints = constraints + string   # concatenate that inequality to the variable 'constraints'

  INFILE.close()
  OUTFILE.write("Maximize \n") # write to file the string (word) 'Maximize' and move to a new line (because of '\n')
  OUTFILE.write(listC + "\n")  # write to file the value of variable 'listC' and move to a new line
  OUTFILE.write (constraints)  # write to file the value of variable 'constraints'
  OUTFILE.write (binaries)     # write to file the value of the variable 'binaries'
  OUTFILE.write ("end")        # write to file the string (word) 'end'
  OUTFILE.close()
