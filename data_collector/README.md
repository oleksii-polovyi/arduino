# Data collector with Python and Arduino

1. Load `data_collector.ino` using Arduino IDE.
2. Update `port` and `baudrate` in `data_collector.ino` and `data_collector.py` (COM4 and 9600 used in this example).
3. Run the program in CLI with `python data_collector.py`.
4. Run `tail -f data.txt` in separate CLI to show the latest data written to the `data.txt` file.
5. Use `CTRL+C` to stop the python and/or tail process.
