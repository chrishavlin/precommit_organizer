import os

import tomli
import tomli_w

_template = "[precommit_organizer]\n\n"

def create_empty_config(config_file):
    with open(config_file,"w") as f:
        f.write(_template)

class Repo:

    attrs_to_write = ["repo_path", ]
    def __init__(self, repo_name: str, repo_path: os.PathLike):
        self.repo_name = repo_name
        self.repo_path = repo_path

        self.repo_path_orig = repo_path
        self.repo_path = str(repo_path)
        self.repo_entry = f"\n\n[{repo_name}]"

    @property
    def entry(self) -> dict:
        return {self.repo_name: {"repo_path" : self.repo_path}}

    @property
    def toml_str(self) -> str:
        return tomli_w.dumps(self.entry)



class Config:
    def __init__(self, config_file):
        self.config_file = config_file
        self.reload()

    def reload(self):
        with open(self.config_file, "rb") as f:
            config = tomli.load(f)
        self.config = config

    def append_str_to_disk(self, new_entry):
        with open(self.config_file, "a") as f:
            f.write(new_entry)

    def add_new_repo(self, repo_name: str, repo_path: os.PathLike):
        new_repo = Repo(repo_name, repo_path)
        self.config[repo_name] = new_repo.entry[repo_name]
        self.rewrite_full()
        self.reload()

    def rewrite_full(self):
        with open(self.config_file, 'wb') as f:
            tomli_w.dump(self.config, f)

    def remove_repo(self, repo_name: str):
        if repo_name in self.config:
            self.config.pop(repo_name)
            self.rewrite_full()
            self.reload()



