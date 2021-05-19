import os, re, sys
from datetime import datetime

folder_to_save_changelog = "Petroles_3"
repo_name = "alvelvis/meu-mestrado"
commits = \
    '''
7ad921ca7b0026a8d96285f76a37097fbc5d7dda
3983c05dde4b414d6a7b400afeb89ad2a9e63603
cada8310640e99453c71506dac6c337a584fd1f5
53d707a5cf2507383795458666e33450730e6012
b7f3d42913ca7db33f3c2927609ba56ecc3efa5c
725b3da4d82a47ed5757524c3bb8fd4d2048b127
ad450c4185a5c03beff93a817b997a7963165059
fd9f01fe910ed8a9b7d23f66181b65939a961906-Maria Clara Castro
4dfd6de383be7b49ffb7005907919a1096bf3855-Tatiana Cavalcanti
    '''
commits = [x.strip() for x in commits.splitlines() if x.strip()]

patches_folder = "{}/{}".format(
    folder_to_save_changelog, 
    "patch")

if not commits:
    raise Exception("Commits list is empty.")

if not os.path.isdir(folder_to_save_changelog):
    raise Exception("Folder does not exist.")
if not os.path.isdir(patches_folder):
    os.mkdir(patches_folder)

git_log = os.popen("git log --all").read()
for file in os.listdir(patches_folder):
    if (file.endswith(".patch") 
    and not " {}\n".format(file.rsplit("-", 1)[1].split(".patch")[0]) in git_log):
        with open("{}/{}".format(patches_folder, file)) as f:
            print(f.read())
        delete = input("\nCommit not found in repository history ({}). Delete this patch? (y/N): ".format(file))
        if delete.lower().strip() == "y":
            os.remove("{}/{}".format(patches_folder, file))

for file in os.listdir(folder_to_save_changelog):
    if file.endswith(".md") and 'changelog' in file:
        with open("{}/{}".format(folder_to_save_changelog, file)) as f:
            md = f.read()
        for commit in commits:
            if commit.split("-")[0] in md:
                delete = input("Commit is already documented in a changelog file ({}), delete it? (Y/n): ".format(file))
                if delete.lower().strip() == "y" or not delete.strip():
                    os.remove("{}/{}".format(folder_to_save_changelog, file))
                break

now_date = datetime.now()
now_date = "{}_{}_{}_{}:{}:{}".format(
    now_date.year,
    now_date.month,
    now_date.day,
    now_date.hour,
    now_date.minute,
    now_date.second)
changelog = "# Changelog ({})".format(now_date.replace("_", " "))
changelog_filename = "changelog-{}.md".format(
    now_date)

months = {
    'Jan': 1, 'Feb': 2, 'Mar': 3, 'Apr': 4, 'May': 5, 'Jun': 6,
    'Jul': 7, 'Aug': 8, 'Sep': 9, 'Oct': 10, 'Nov': 11, 'Dec': 12}

for commit in commits:
    author = ""
    if '-' in commit:
        author = commit.split("-")[1]
    commit = commit.split("-")[0]
    for file in os.listdir(patches_folder):
        if commit in file:
            delete = input("Commit already has a patch file ({}), delete it? (Y/n): ".format(file))
            if delete.lower().strip() == "y" or not delete.strip():
                os.remove("{}/{}".format(patches_folder, file))
    log = re.sub(r"Merge:\s.*?\n", "", os.popen("git show {}".format(commit)).read())
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
        date_formatted,
        commit)
    with open("{}/{}".format(patches_folder, patch_filename), "w") as f:
        f.write(log)
    changelog += "\n\n## {0}\n\n* {3}\n* {1}\n* Lines changed: {4}\n* Commit: [{2}](https://github.com/{8}/commit/{2})\n* Patch file: [{5}](patch/{5})\n\n{6}\n\n```diff\n{7}\n```".format(
        message.strip().splitlines()[0],
        date,
        commit,
        author,
        log.count("\n+"),
        patch_filename,
        message,
        "\n".join([x for x in log.split("@@")[2].splitlines() if x.strip()]),
        repo_name)

with open("{}/{}".format(folder_to_save_changelog, changelog_filename), "w") as f:
    f.write(changelog)
os.system("xdg-open '{}/{}'".format(folder_to_save_changelog, changelog_filename))
