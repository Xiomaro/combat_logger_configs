# Combat Logger
A tool for Black Desert Online to log combat messages.

Visualize your captured logs with this [website](http://war-analyzer.oracle-tools.site/)

## Prerequisites
- [Npcap](https://npcap.com/#download)
- (optional) [Wireshark](https://www.wireshark.org/download.html)

## Installation
### Bundled executable
You can download the already bundled executable and the current working config [here](https://github.com/sch-28/combat_logger/releases).
### Building from source
requires Python (tested on 3.10.1)
```
git clone https://github.com/sch-28/combat_logger
cd combat_logger
install
```

## Usage

Start the executable while the game is running.
When combat messages are received, the program will write them to `<date>.log` (if the output name is not specified).

If you do not want to [risk losing data](#problems), you can also run Wireshark to record the BDO network as a backup.
Running the executable with the --file argument allows you to parse a recorded `*.pcap` file.

## Problems
Bdo changes its network structure after each weekly patch. Consequently, the [config](https://github.com/sch-28/combat_logger/blob/main/config.ini) needs to be adjusted accordingly.
If the config is not updated yet, but you still need to log a fight, then you can record it with Wireshark. After the config has been updated, you can run the logger on the `*.pcap` file.

Running the executable with an old config will **not yield any results**.
## Options
```
-h, --help                    show this help message and exit
-f FILE, --file FILE          instead of sniffing for bdo packages, it will use the given *.pcap file
-o OUTPUT, --output OUTPUT    custom output file    
```
