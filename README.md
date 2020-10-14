```
 ____  _                     ____ _____         _
/ ___|| | ___   _ _ __   ___|___ \_   _|____  _| |_
\___ \| |/ / | | | '_ \ / _ \ __) || |/ _ \ \/ / __|
 ___) |   <| |_| | |_) |  __// __/ | |  __/>  <| |_
|____/|_|\_\\__, | .__/ \___|_____||_|\___/_/\_\\__|
            |___/|_|
```

# Skype2Text

Skype2Text is a simple one-file python script which extracts
the conversation with a user specified as a command line argument
from a skype .db file and saves it in an IRC-like format in a .txt
file.

usage : `skype2text.py <file.db> <partner's skype ID> [output file name]`

The conversation will be saved as `<partner's ID>.txt` in the same directory
by default, or in the specified output path. If `-` is specified as the
output path, stdout will be used instead.

### Dependencies

None, just make sure you have sqlite and xml support enabled in your python install.

### License

The Unlicense (unlicense.org)
