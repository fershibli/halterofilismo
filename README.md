# Halterofilismo

A two-player weightlifting game for the Windows console, with ASCII-art lifters, played over the network with UDP sockets: each player mashes keys to build power and lift the bar before the other. Made in 2014.

## History

`Halterofilismo_Redes_1` to `4b` (May-Jun 2014): from the first UDP exchange to win counters, matches and the ASCII animations in `ascii_art_musculacao*.txt`.

## Author

Fernando Luiz Neme Chibli ([@fershibli](https://github.com/fershibli))

## Releases

Builds are made by GitHub Actions (`.github/workflows/release.yml`) for Windows only. Push a tag such as `v1.0` (or run the workflow by hand) and the zipped builds are attached to a GitHub release.

The game reads the keyboard with `msvcrt`, which only exists on Windows, so there are no macOS or Linux builds.

To play from source: `python2.7 halterofilismo.py`.

Both players run the game, type the input/output ports and the friend's IP.
