# Copyright 2018 Regents of the University of Colorado. All Rights Reserved.
# Released under the MIT license.
# This software was developed at the University of Colorado's Laboratory for Atmospheric and Space Physics.
# Verify current version before use at: https://github.com/MAVENSDC/Pytplot

import pytplot
import numpy as np
from scipy import interpolate
from scipy.interpolate import interp1d

#TVAR INTERPOLATION
#interpolate tvar2 to tvar1 cadence
def tinterp(tvar1,tvar2,replace=False):

    new_tvar2 = pytplot.data_quants[tvar2].interp_like(pytplot.data_quants[tvar1])

    if replace:
        pytplot.data_quants[tvar2] = new_tvar2
        return
    else:
        return new_tvar2

    '''
    # Crop Data
    tv1, tv2 = pytplot.crop(tvar1,tvar2)
    df_index = pytplot.data_quants[tvar1].data.columns
    #interpolate to tvar1 cadence
    if interp == 'linear':
        name1 = tvar1 + "_interp"
        name2 = tvar2 + "_interp"
        new_df = []
        for i in df_index:
            tv2_col = [item[i] for item in tv2_d]
            f = interp1d(tv2_t,tv2_col,fill_value="extrapolate")
            new_df = new_df + [f(tv1_t)]
        new_df = np.transpose((list(new_df)))
    elif interp == 'cubic':
        new_df = []
        for i in df_index:
            tv2_col = [item[i] for item in tv2_d]
            f = interp1d(tv2_t,tv2_col,kind='cubic',fill_value='extrapolate')
            new_df = new_df + [f(tv1_t)]
        new_df = np.transpose((list(new_df)))
        name1 = tvar1 + "_interp"
        name2 = tvar2 + "_interp"
    elif interp == 'quad_spline':
        new_df = []
        for i in df_index:
            tv2_col = [item[i] for item in tv2_d]
            tck = interpolate.splrep(tv2_t, tv2_col, s=0,k=2)
            ynew = interpolate.splev(tv1_t, tck, der=0)
            new_df = new_df + [ynew]
        new_df = np.transpose((list(new_df)))
        name1 = tvar1 + "_interp"
        name2 = tvar2 + "_interp"
    #store interpolated tvars as 'X_interp'
    pytplot.store_data(name2, data={'x':tv1_t,'y':new_df})
    '''
    return