import pandas as pd
import os
import matplotlib.pyplot as plt

plt.style.use('ggplot')
plt.rcParams.update({'mathtext.default': 'regular'})  # sans-serif math

current_dir = os.path.dirname(os.path.abspath(__file__))
met_data_fname = current_dir + ('/ucla_weather.csv')

df_met = pd.read_csv(
    met_data_fname, sep='\\s+|\\u2003', header=0,
    names=['year', 'month', 'day', 'hour', 'minute', 'wind_dir',
           'wind_speed', 'gust', 'T_air', 'T_air_min', 'T_air_max',
           'RH', 'RH_min', 'RH_max', 'T_dew', 'T_wetbulb',
           'p_atm_0', 'precip_hour', 'precip_day'], engine='python')

# define time in hour, used as the x variable in the plots
time = df_met['hour'].values + df_met['minute'].values / 60.

fig, axes = plt.subplots(2, 2)
axes[0, 0].plot(time, df_met['T_air'], 'k-', lw=2, label='air temp')
axes[0, 0].plot(time, df_met['T_dew'], '-', c='dodgerblue', lw=2,
                label='dew temp')
axes[0, 0].legend(loc='upper left', frameon=False)
axes[0, 1].plot(time, df_met['wind_speed'], 'k-', lw=2)
axes[1, 0].plot(time, df_met['RH'], 'k-', lw=2)
axes[1, 1].plot(time, df_met['p_atm_0'], 'k-', lw=2)
axes[1, 1].ticklabel_format(useOffset=False)

axes[0, 0].set_ylabel('Temperature ($\degree$F)')
axes[0, 1].set_ylabel('Wind speed (m s$^{-1}$)')
axes[1, 0].set_ylabel('Relative humidity (%)')
axes[1, 1].set_ylabel('Sea level pressure (hPa)')

for i in range(4):
    axes[i // 2, i % 2].set_xlabel('Time (hour)')

fig.tight_layout()
plt.show()

fig.savefig(current_dir + '/ucla_weather.png', dpi=300)
