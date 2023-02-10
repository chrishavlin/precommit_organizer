import os
from typing import Optional
from precommit_organizer.logging import mylogger
from pathlib import Path
import shutil

from precommit_organizer.repoconfig import create_empty_config, Config

_default_config_dir = Path(os.path.join(os.path.expanduser("~"), ".config", "precommit_organizer"))
_config_search_paths = [
    _default_config_dir,
]

_default_config_file = Path("precommit_organizer.toml")

def search_for_config():
    for possible_dir in _config_search_paths:
        if possible_dir.is_dir():
            possible_file = Path(os.path.join(possible_dir, _default_config_file))
            if possible_file.is_file():
                return possible_file

    return None


def create_config_file():
    if _default_config_dir.is_dir() is False:
        _default_config_dir.mkdir(parents=True)

    config_file = os.path.join(_default_config_dir, _default_config_file)
    create_empty_config(config_file)
    return config_file


class Organizer:
    def __init__(self, config_file: Optional[os.PathLike]=None):
        if config_file is None:
            mylogger.info("No config_file provided, searching for one...")
            config_file = search_for_config()

        if config_file is None:
            mylogger.info(f"No config_file found, creating one in {_default_config_dir}")
            config_file = create_config_file()

        if config_file is None:
            raise RuntimeError("Still no config file...")

        mylogger.info(f"Using the following config_file: {config_file}")

        self.config_file = config_file
        self.config = Config(self.config_file)

    def add_new_repo(self, repo_name: str, repo_path: os.PathLike):
        self.config.add_new_repo(repo_name, repo_path)

    def remove_repo(self):
        raise NotImplementedError("need to do this")

    @property
    def config_dict(self):
        return self.config.config

    @property
    def repo_list(self):
        return list(k for k in self.config_dict.keys() if k !='precommit_organizer')

    def get_repo(self, repo_name: str) -> dict:
        return self.config_dict[repo_name]

    def remove_repo(self, repo_name: str):
        self.config.remove_repo(repo_name)

    def copy_files_to_repo(self, src_repo: str, dest_repo: str):
        files_to_copy = [
            ".flake8",
            '.isort.cfg',
            '.pre-commit-config.yaml',
            'tests/lint_requirements.txt'
        ]
        src_path = self.get_repo(src_repo)['repo_path']
        dest_path = self.get_repo(dest_repo)['repo_path']
        if os.path.isdir(dest_path) is False:
            raise OSError(f"Destiniation repo not found at {dest_path}")
        if os.path.isdir(src_path) is False:
            raise OSError(f"Source repo not found at {src_path}")

        for fi in files_to_copy:
            fullfi = os.path.join(src_path, fi)
            if os.path.isfile(fullfi):
                mylogger.info(f"copying {fi} from {src_path} to {dest_path}")
                dest_fi = os.path.join(dest_path, fi)

                try:
                    # this will overwrite
                    shutil.copy(fullfi, dest_fi)
                except OSError:
                    raise OSError(f"Could not copy {fullfi}")



