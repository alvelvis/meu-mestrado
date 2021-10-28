import os, re, sys, shutil
from datetime import datetime

if len(sys.argv) != 2 or not os.path.isfile(sys.argv[1]) or not sys.argv[1].endswith(".txt"):
    raise Exception("Commits file not found.")
commits_file = sys.argv[1]

folder_to_save_changelog = commits_file.rsplit("/", 1)[0]
repo_name = "alvelvis/meu-mestrado"
with open(commits_file) as f:
    commits = [x.strip() for x in f.read().splitlines() if x.strip() and not x.strip().startswith("#")]

patch_folder_name = "patch_{}".format(os.path.basename(commits_file).rsplit(".", 1)[0])
patches_folder = "{}/{}".format(
    folder_to_save_changelog, 
    patch_folder_name)

if not commits:
    raise Exception("Commits list is empty.")

if not os.path.isdir(folder_to_save_changelog):
    raise Exception("Folder where to save changelog does not exist.")
if os.path.isdir(patches_folder):
    shutil.rmtree(patches_folder)
os.mkdir(patches_folder)

now_date = datetime.now()
now_date = "{}_{}_{}_{}:{}:{}".format(
    now_date.year,
    now_date.month,
    now_date.day,
    now_date.hour,
    now_date.minute,
    now_date.second)
changelog = "# {}\n\nLast update: {}".format(os.path.basename(commits_file).rsplit(".", 1)[0], now_date.replace("_", "-"))
changelog_filename = os.path.basename(commits_file).rsplit(".", 1)[0] + ".md"

months = {
    'Jan': 1, 'Feb': 2, 'Mar': 3, 'Apr': 4, 'May': 5, 'Jun': 6,
    'Jul': 7, 'Aug': 8, 'Sep': 9, 'Oct': 10, 'Nov': 11, 'Dec': 12}

for commit in commits:
    author = ""
    if '-' in commit:
        author = commit.split("-")[1]
    commit = commit.split("-")[0]
    log = re.sub(r"Merge:\s.*?\n", "", os.popen("git show {}".format(commit)).read())
    if not log.strip():
        raise Exception("Commit does not exist ({}).".format(commit))
    if not author:
        author = log.splitlines()[1]    
    date = log.splitlines()[2]
    date_formatted = "{}_{}_{}_{}".format(
        date.split()[5],
        months[date.split()[2]],
        date.split()[3],
        date.split()[4])
    message = "\n".join([x.strip() for 
        x in log.split("Date:")[1].split("diff --git")[0].splitlines()[1:] if 
        x.strip()])
    patch_filename = "{}-{}.patch".format(
        date_formatted.replace(":", "-"),
        commit)
    with open("{}/{}".format(patches_folder, patch_filename), "w") as f:
        f.write(log)
    changelog += "\n\n## {0}\n\n* {3}\n* {1}\n* Lines changed: {4}\n* Commit: [{2}](https://github.com/{8}/commit/{2})\n* Patch file: [{5}]({9}/{5})\n\n{6}\n\n```diff\n{7}\n```".format(
        message.strip().splitlines()[0],
        date,
        commit,
        author,
        log.count("\n+")-1,
        patch_filename,
        message,
        "\n".join([x for x in log.split("@@")[2].splitlines() if x.strip()]),
        repo_name,
        patch_folder_name)

with open("{}/{}".format(folder_to_save_changelog, changelog_filename), "w") as f:
    f.write(changelog)
os.system("xdg-open '{}/{}'".format(folder_to_save_changelog, changelog_filename))
