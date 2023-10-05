# Install

`cp logging.yml.example logging.yml`

If you want the logs to be stored in a file, open logging.yml and uncomment the third line below :

```yaml
handlers:
    - console
    # - line
```

Also change the log file directory:

```yaml
handlers:
    file:
        class: logging.handlers.WatchedFileHandler
        # Change the path to your liking
        filename: /home/yourname/.myproject/logs/runtime.log
```

If you just want to run it:

`pip install .`

If you want to dev/contribute:

`pip install ".[dev]"`


# See available make commands

`make help`

```
format              Format the project codebase and fix linter issues 
install             Install dependencies required to run the project 
install-dev         Install dependencies + dev dependencies 
lint                Run project linter 
```