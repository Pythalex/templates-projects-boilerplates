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
        filename: /home/alexandre/.lifeboat/logs/lifeboat.log
```

If you just want to run it:

`pip install .`

If you want to dev/contribute:

`pip install ".[dev]"`


# Format

`make format`


# Run

`python lifeboat/main.py [ACTION]`