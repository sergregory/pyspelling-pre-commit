pyspelling mirror
===============

Mirror of pyspelling package for pre-commit.

For pre-commit: see https://github.com/pre-commit/pre-commit

For pyspelling: see https://github.com/facelessuser/pyspelling/


### Using pyspelling with pre-commit

Add this to your `.pre-commit-config.yaml`:

```yaml
-   repo: https://github.com/sergregory/pyspelling-pre-commit
    rev: ''  # Use the sha / tag you want to point at
    hooks:
    -   id: pyspelling
```

### overriding `args`

note that this repository sets `args: [-S]`, so that pyspelling gets files to check properly.
