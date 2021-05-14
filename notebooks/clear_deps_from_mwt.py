#%%
path = "../330TEM"
if os.path.isdir(path):
    files = ["{}/{}".format(path, x) for x in os.listdir(path)]
elif os.path.isfile(path):
    files = [path]
else:
    exit()
for file in files:
    with open(file) as f:
        conllu = f.read().splitlines()
    for l, line in enumerate(conllu):
        if line.count("\t") == 9 and '-' in line.split("\t")[0]:
            line = line.split("\t")
            line[8] = "_"
            conllu[l] = "\t".join(line)
    with open(file, "w") as f:
        f.write("\n".join(conllu))