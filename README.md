# Disclamer

These scripts are inspired by Pyheartbeat from Python Cookbook. The core idea is the same however some custom configurations are also added.

Credits to: Nicola Larosa

# PyHeartbeat

PyHeartBeat is made up of two files: PyHBClient.py sends UDP packets, while PyHBServer.py listens for such packets and detects inactive clients. The client program, running on any number of computers, periodically sends an UDP packet to the server program that runs on one central computer. In the server program, one thread dynamically builds and updates a dictionary that stores the IP numbers of the client computers and the timestamp of the last packet received from each. At the same time, the main thread of the server program periodically checks the dictionary, noting whether any of the timestamps is older than a defined timeout.

# Configurations

All the configuration options are stored in the `config.ini` file, such as the server ip, port, the timeout of the heartbeats, the timeout after which the server checks the status of the clients etc.

# Running the scripts

It is recommended to run the scripts in the background. For linux systems it can be done by:

```bash
$ pyton PyHBserver.py &
```

Also by default the scripts log to stdout. It is recommended to specifiy a log file in `config.ini`.

To stop the scripts simply get the pid of the script using ps or some other process utility and kill it.
