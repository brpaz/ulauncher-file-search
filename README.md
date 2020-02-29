# ulauncher-file-search

[![Ulauncher Extension](https://img.shields.io/badge/Ulauncher-Extension-green.svg?style=for-the-badge)](https://ext.ulauncher.io/-/github-brpaz-ulauncher-file-search)
[![GitHub license](https://img.shields.io/github/license/brpaz/file-search.svg?style=for-the-badge)](https://github.com/brpaz/ulauncher-file-search/blob/master/LICENSE)

> Quick Search files and directories from [Ulauncher](https://ulauncher.io) using [fd](https://github.com/sharkdp/fd).

## Demo

![demo](demo.gif)

## Requirements

- Ulauncher 5+
- Python 3+
- [fd](https://github.com/sharkdp/fd) - A simple, fast and user-friendly alternative to 'find'.

## Install

Open ulauncher preferences window -> extensions -> add extension and paste the following url:

```
https://github.com/brpaz/ulauncher-file-search
```

## Usage

This extension provides the following keywords:

- fd -> Search files and directories
- ff -> Search Files
- fdir -> Search directories

To search, input one of the previous keywords to trigger the extension and start typing your search criteria. Ulauncher will call "fd" under the hood to perform your search and it will display a list of results.

### Result items Actions

- Press "Enter" - Open the file / folder using the default system action
- Press "Alt+Enter" - On a folder, it will open the respective folder in a Terminal window.

### Extension settings

- **Terminal Emulator** -> Sets the terminal emulator to use when opening directories.
- **Base dir** -> The base directory to start your searches. By detault, its the root folder "/" but you can set to your home directory, for example. Note, that only absolute paths are supported.
## Development

```
git clone https://github.com/brpaz/ulauncher-file-search
make link
```

The `make link` command will symlink the cloned repo into the appropriate location on the ulauncher extensions folder.

Make sure Ulauncher is not running and from command line run:

```sh
ulauncher --no-extensions --dev -v |& grep "file-search"
```

This will start ulauncher with all the extensions disable which will make it easier to look for logs.

You then have to start the Circle CI extension manually. In the output of the previous command you should find something similar to this:

```sh
VERBOSE=1 ULAUNCHER_WS_API=ws://127.0.0.1:5054/file-search PYTHONPATH=/usr/lib/python3/dist-packages /usr/bin/python3 /home/bruno/.cache/ulauncher_cache/extensions/file-search/main.py
``` 

Copy and run that command in another terminal window.

Your extension should now be running. To see your changes, just Ctrl+C and re-run the last command.

## Contributing

All contributions are welcome. Just open an issue and/or create a PR.

If you like my work, feel free to "Buy me a Coffee".

<a href="https://www.buymeacoffee.com/Z1Bu6asGV" target="_blank"><img src="https://www.buymeacoffee.com/assets/img/custom_images/orange_img.png" alt="Buy Me A Coffee" style="height: auto !important;width: auto !important;" ></a>

## Links

* [Ulauncher Extensions](https://ext.ulauncher.io/)
* [Ulauncher 5.0 (Extension API v2.0.0) — Ulauncher 5.0.0 documentation](http://docs.ulauncher.io/en/latest/)

## License

MIT &copy; [Bruno Paz](http://brunopaz.net)
