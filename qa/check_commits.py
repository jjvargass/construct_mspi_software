import os
from git import Repo
import logging


path = os.getcwd()
repo = Repo(path)
commits_list = list(repo.iter_commits())

for i in range(len(commits_list)):
    commit = commits_list[i]
    print(commit.hexsha)
    print(commit.author)
    print(commit.message)
