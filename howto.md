## Download UCLA weather data and make plots

1. Open an empty text file (Windows: Notepad; Mac: TextEdit; Linux: `vim` in the terminal).
2. Download *today*'s UCLA weather data. Go to <https://weather.atmos.ucla.edu/today.php>, select all the text (`Ctrl + A` for Windows and Linux, and `Cmd + A` for Mac), and paste it to the opened text file.
3. Save the text file as `ucla_weather.csv` in the same directory of the python script `plot_weather.py`. Make sure it is saved as a CSV file with extension `.csv`, not `.csv.txt`.
4. Run the python script `plot_weather.py` in the terminal. First type `python3` followed by a space, then drag the file to the terminal window, it will append the file path of the script to the current command. Press `Enter` to run it.
   For example, if the script is placed on the Desktop, by dragging it to the terminal you may see
```bash
python3 /Users/<your_name>/Desktop/plot_weather.py
```
5. Check the directory of the script, see if you get a plot named `ucla_weather.png`.
