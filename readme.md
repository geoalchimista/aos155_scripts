# AOS 155, Winter 2017

## Download UCLA weather data and make plots

1. Open an empty text file (Windows: Notepad; Mac: TextEdit; Linux: `vim` in the terminal).
2. Download *today*'s UCLA weather data. Go to <https://weather.atmos.ucla.edu/today.php>, select all the text (`Ctrl + A` for Windows and Linux, and `Cmd + A` for Mac), and paste it to the opened text file.
3. Save the text file as `ucla_weather.txt` in the same directory of the python script `plot_weather.py`.
4. Run the python script `plot_weather.py` in the terminal. First type `python3` followed by a *space*, then drag the file to the terminal window, it will append the file path of the script to the current command. Press `Enter/Return` to run it.
    For example, if the script is on the Desktop, by dragging it to the terminal you may see:
        ```python3 /Users/<your_name>/Desktop/plot_weather.py```
5. It will pop up a window showing the plot. After you close the pop-up window, it saves the figure to the same directory of the script, named `ucla_weather.png`.

## Download FLUXNET data and make plots

1. Download the plotting script `plot_fluxdata.py` and the data file `fluxdata_br-sa1.csv.zip` in this repository.
2. Unzip the data file, and copy the extracted **CSV** file to the *same* directory of `plot_fluxdata.py`.
3. Run the Python script `plot_fluxdata.py` in the terminal. First type `python3` followed by a *space*, then drag the Python script file to the terminal window. Press `Enter/Return` to run it.
4. Once it's done, see if you get a plot `fluxdata_br-sa1.png` for the time series of some major meteorological and flux variables, for example, net ecosystem exchange of carbon, air temperature, et cetera.
5. The dataset is from 1 Jan 2002 to 31 Dec 2011, and the plotted period is the first half of the year 2010. If you'd like to plot a different period, open the Python script `plot_fluxdata.py` in a text editor and modify the variables `plot_time_start` and `plot_time_end`. Be sure to follow the same format (`yyyy-mm-dd{T}hh:mm`).
