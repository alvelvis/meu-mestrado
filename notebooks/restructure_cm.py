import argparse
import re, sys

parser = argparse.ArgumentParser(description='Pós-processamento do html de matriz de confusão do Julgamento.')
parser.add_argument('input_file', help="Caminho do html que contém uma matriz de confusão do Julgamento.")
args = parser.parse_args()

clear_file = lambda x: re.sub("<.*?>", "", re.sub('</tr>', '[line]', re.sub("</td>|</th>", "[col]", x)))

output = []
with open(args.input_file) as f:
    table = clear_file(f.read().split('<div id="DEPRELMatrix" class="tables panel panel-default" style="display: block;">')[1].split("</div>\n")[0])#.split("[col]", 1)[1]#.rsplit("[col]", 1)[0]

table = table.split("[line]")
table = [x.rsplit("[col]", 1)[0].split("[col]") for x in table if x]

columns = table[0][1:-1]
lines = [x[0] for x in table[1:] if x][1:-1]

for l in range(len(lines)):
    for c in range(len(columns)):
        output.append("{},{},{}".format(lines[l], columns[c], table[l+2][c+1]))

sys.stdout.write("\n".join(output))