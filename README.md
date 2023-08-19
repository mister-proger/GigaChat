
# General info
Our goal is to combine the advantages of all the most popular social networks in one application, while keeping off their disadvantages. Also, for the sake of performance, we develop in native code for each platform. Of course, it is highly unlikely that someone would be interested in a school project, but we welcome any sort of help ;)

# Installation
While components are not ready, we advice against trying to install anything

## Server
--no information--

## Linux client
### Build prerequisites:
- Of course, linux
- Qt 6 or higher
- g++ compiler
- GNU make 
- GHC Haskell compiler (not necessary yet)
- ghc-static (not necessary yet)
- patience

### Build steps: 
1. clone the repository & navigate to GigaChat/client/desktop/linux-x11/source
2. `haskell/build-shared.sh` or `cd haskell && ghc -dynamic -shared -fPIE <did not finish the command lol>`  (not necessary yet)
3. run `qmake GigaQt.pro && make`
4. Pray. for it to work.

## Windows client
--no information--

## Android client
--no information--

