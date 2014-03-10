# xplay.py
Sick and tired of waiting for your PI to render your XBMC filelist?

## Dependencies
```
pip install requests-futures
```

## Usage
Set config in config.json
```
./client.py "Search string"
./client.py stop
./client.py play
./client.py pause
```

### Coming
```
./client.py jumpto
```

## Testing
Run python -m unittest discover -s tests/