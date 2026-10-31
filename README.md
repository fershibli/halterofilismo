# Halterofilismo

A two-player weightlifting game for the Windows console, with ASCII-art lifters, played over the network with UDP sockets: each player mashes keys to build power and lift the bar before the other. Made in 2014.

## History

`Halterofilismo_Redes_1` to `4b` (May-Jun 2014): from the first UDP exchange to win counters, matches and the ASCII animations in `ascii_art_musculacao*.txt`.

## Play in the browser

**[https://fershibli.github.io/halterofilismo/](https://fershibli.github.io/halterofilismo/)** (open it on two computers, or in two tabs)

The page runs `web/game/halterofilismo.py` (a Python 3 copy made with 2to3) on Pyodide inside an xterm.js terminal. `web/green.py` turns the keyboard, energy and network threads into cooperative tasks, since browsers have no threads, and `web/netsock.py` replaces the UDP sockets with a WebRTC data channel (PeerJS). The ports the game asks for no longer matter, and the "IP" it shows and asks for is a room code. Published by `.github/workflows/pages.yml`.

## Author

Fernando Luiz Neme Chibli ([@fershibli](https://github.com/fershibli))

## Releases

Builds are made by GitHub Actions (`.github/workflows/release.yml`) for Windows only. Push a tag such as `v1.0` (or run the workflow by hand) and the zipped builds are attached to a GitHub release.

The game reads the keyboard with `msvcrt`, which only exists on Windows, so there are no macOS or Linux builds.

To play from source: `python2.7 halterofilismo.py`.

Both players run the game, type the input/output ports and the friend's IP.
