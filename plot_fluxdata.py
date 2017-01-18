"""
Read a sample FluxNet dataset and generate plots.

"""
import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

plt.style.use('ggplot')
plt.rcParams.update({'mathtext.default': 'regular'})  # sans-serif math
plt.rcParams['axes.color_cycle'] = ['k', 'firebrick', 'dodgerblue', 'orange',
                                    'forestgreen', 'darkorchid', 'turquoise']

current_dir = os.path.dirname(os.path.abspath(__file__))
flux_data_fname = current_dir + '/fluxdata_br-sa1.csv'

df_flux = pd.read_csv(flux_data_fname, sep=',', comment='#', na_values=-9999)

# convert timestamps to ISO standard datetime format
# first convert timestamps from `int64` type to unicode string type
df_flux[['TIMESTAMP_START', 'TIMESTAMP_END']] = \
    df_flux[['TIMESTAMP_START', 'TIMESTAMP_END']].astype('U12')
# then reformat timestamp strings to `numpy.datetime64` string
# 'yyyy-mm-dd{T}hh:mm'
for i in range(df_flux.shape[0]):
    ts_start_str = df_flux.loc[i, 'TIMESTAMP_START']
    ts_end_str = df_flux.loc[i, 'TIMESTAMP_END']
    dt_start_str = '%s-%s-%sT%s:%s' % (ts_start_str[0:4], ts_start_str[4:6],
                                       ts_start_str[6:8], ts_start_str[8:10],
                                       ts_start_str[10:12])
    dt_end_str = '%s-%s-%sT%s:%s' % (ts_end_str[0:4], ts_end_str[4:6],
                                     ts_end_str[6:8], ts_end_str[8:10],
                                     ts_end_str[10:12])
    df_flux = df_flux.set_value(i, 'TIMESTAMP_START', dt_start_str)
    df_flux = df_flux.set_value(i, 'TIMESTAMP_END', dt_end_str)

# finally, convert timestamps to `numpy.datetime64` array
df_flux['TIMESTAMP_START'] = df_flux['TIMESTAMP_START'].astype(np.datetime64)
df_flux['TIMESTAMP_END'] = df_flux['TIMESTAMP_END'].astype(np.datetime64)

# refer to the data variable list for the meaning of columns
# please see <http://ameriflux.lbl.gov/data/aboutdata/data-variables/>

# subset the dataframe
# modify `plot_time_start` and `plot_time_end` to select the plotted period
# must follow the format 'yyyy-mm-dd{T}hh:mm'
plot_time_start = np.datetime64('2010-01-01T00:00')
plot_time_end = np.datetime64('2010-07-01T00:00')
df_flux_subset = df_flux.loc[
    (df_flux['TIMESTAMP_START'] >= plot_time_start) &
    (df_flux['TIMESTAMP_START'] < plot_time_end), :]


fig, axes = plt.subplots(6, 1, figsize=(12, 12))
axes[0].plot(df_flux_subset['TIMESTAMP_START'], df_flux_subset['NEE_PI'],
             '.', label='net ecosystem exchange')
axes[0].plot(df_flux_subset['TIMESTAMP_START'], df_flux_subset['RECO_PI'],
             '.', label='ecosystem respiration')

axes[1].plot(df_flux_subset['TIMESTAMP_START'], df_flux_subset['NETRAD'],
             '-', lw=0.5, label='net radiation')
axes[1].plot(df_flux_subset['TIMESTAMP_START'], df_flux_subset['H'],
             '-', lw=0.5, label='sensible heat flux')
axes[1].plot(df_flux_subset['TIMESTAMP_START'], df_flux_subset['LE'],
             '-', lw=0.5, label='latent heat flux')

# no valid soil heat flux data
# axes[1].plot(df_flux_subset['TIMESTAMP_START'], df_flux_subset['G'],
#              '-', lw=0.5, label='soil heat flux')

axes[2].plot(df_flux_subset['TIMESTAMP_START'], df_flux_subset['TA'],
             '-', lw=0.5, label='air temperature')


axes[3].plot(df_flux_subset['TIMESTAMP_START'], df_flux_subset['RH'],
             '-', lw=0.5, label='relative humidity')

axes[4].plot(df_flux_subset['TIMESTAMP_START'], df_flux_subset['VPD_PI'],
             '-', lw=0.5, label='vapor pressure deficit')

# no valid soil measurements
# axes[3].plot(df_flux_subset['TIMESTAMP_START'], df_flux_subset['TS_1'],
#              '-', lw=0.5, label='soil temperature #1')
# axes[3].plot(df_flux_subset['TIMESTAMP_START'], df_flux_subset['TS_1'],
#              '-', lw=0.5, label='soil temperature #2')
# axes[3].plot(df_flux_subset['TIMESTAMP_START'], df_flux_subset['SWC_1'],
#              '-', lw=0.5, label='soil moisture #1')
# axes[3].plot(df_flux_subset['TIMESTAMP_START'], df_flux_subset['SWC_2'],
#              '-', lw=0.5, label='soil moisture #2')

axes[5].plot(df_flux_subset['TIMESTAMP_START'], df_flux_subset['PPFD_IN'],
             '-', lw=0.5, label='incoming photosynthetic photon flux density')

# axes[5].plot(df_flux_subset['TIMESTAMP_START'], df_flux_subset['PPFD_OUT'],
#              '-', lw=0.5, label='outgoing PPFD')
# axes[5].plot(df_flux_subset['TIMESTAMP_START'], df_flux_subset['PPFD_DIF'],
#              '-', lw=0.5, label='diffuse incoming PPFD')

for i in range(6):
    axes[i].legend(loc='best', frameon=True, fontsize=10, ncol=4)

axes[0].set_ylabel('Carbon fluxes\n($\mu$mol m$^{-2}$ s$^{-1}$)')
axes[1].set_ylabel('Heat fluxes\n(W m$^{-2}$)')
axes[2].set_ylabel('Air temperature\n($\degree$C)')
axes[3].set_ylabel('RH (%)')
axes[4].set_ylabel('VPD (kPa)')
axes[5].set_ylabel('PPFD\n($\mu$mol m$^{-2}$ s$^{-1}$)')

fig.tight_layout()

fig.savefig(current_dir + '/fluxdata_br-sa1.png', dpi=300)
