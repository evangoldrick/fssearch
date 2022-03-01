import parser
import sys

if len(sys.argv) != 3:
    print(f"Requires 2 arguments, you provided {len(sys.argv)}\nForm should be input_file output_file")
else:
    with open(sys.argv[1], "r") as inFile:
        with open(sys.argv[2], "w") as outFile:
            outFile.write(str(parser.makeSearchTreeFromLines(inFile.readlines()).getDict()))
