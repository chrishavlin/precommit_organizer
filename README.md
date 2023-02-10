# precommit_organizer

tired of managing precommit across repos? me too.


This package will copy precommit and linting related config files
from one repository to another (overwriting any that are found)

```python
from precommit_organizer import Organizer
pco = Organizer()

print(pco.repo_list)

pco.add_new_repo("myrepo", "/full/path/to/repo")
pco.add_new_repo("myrepo2", "/full/path/to/repo2")
```

To copy from `"myrepo"` to `"myrepo2"`:

```python
pco.copy_files_to_repo("my_repo", "my_repo2")
```

Repositories are saved between python sessions using a config file. The default file is:
```
~/.config/precommit_organizer/precommit_organizer.toml
```

## Assumed directory structure

when copying files, the following files will be copied if found:

* `.flake8`
* `.isort.cfg`
* `.pre-commit-config.yaml`
* `tests/lint_requirements.txt`

any config within general files is ignored (`pyproject.toml`, `setup.cfg`, etc.)

