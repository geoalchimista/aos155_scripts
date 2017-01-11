# AOS 155, Winter 2017

## Download UCLA weather data and make plots

1. Open an empty text file (Windows: Notepad; Mac: TextEdit; Linux: `vim` in the terminal).
2. Download *today*'s UCLA weather data. Go to <https://weather.atmos.ucla.edu/today.php>, select all the text (`Ctrl + A` for Windows and Linux, and `Cmd + A` for Mac), and paste it to the opened text file.
3. Save the text file as `ucla_weather.txt` in the same directory of the python script `plot_weather.py`.
4. Run the python script `plot_weather.py` in the terminal. First type `python3` followed by a *space*, then drag the file to the terminal window, it will append the file path of the script to the current command. Press `Enter/Return` to run it.
    For example, if the script is on the Desktop, by dragging it to the terminal you may see:
        ```python3 /Users/<your_name>/Desktop/plot_weather.py```
5. It will pop up a window showing the plot. After you close the pop-up window, it saves the figure to the same directory of the script, named `ucla_weather.png`.
