# ulauncher-file-search

[![Build Status](https://img.shields.io/travis/com/brpaz/ulauncher-file-search.svg)](https://github.com/brpaz/ulauncher-file-search)
[![GitHub license](https://img.shields.io/github/license/brpaz/ulauncher-fd.svg)](https://github.com/brpaz/:ulauncher-file-search/blob/master/LICENSE)

> Quick Search files and directories from [Ulauncher](https://ulauncher.io) using [https://github.com/sharkdp/fd](fd).

## Demo

TODO Add demo here.

## Requirements

- Ulauncher
- Python >= 2.7
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
git clone https://github.com/brpaz/ulauncher-fd
make link
```

The `make link` command will symlink the cloned repo into the appropriate location on the ulauncher extensions folder.

To see your changes, stop ulauncher and run it from the command line with: `ulauncher -v`.

## Todo

- An support for in file search using rigrep.

## Contributing

- Fork it!
- Create your feature branch: git checkout -b my-new-feature
- Commit your changes: git commit -am 'Add some feature'
- Push to the branch: git push origin my-new-feature
- Submit a pull request :D

## License

MIT &copy; [Bruno Paz]
