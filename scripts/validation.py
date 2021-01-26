# Python Native
import logging
import matplotlib.pyplot as plt
import rasterio
# 3rd Party
import gdal
import numpy
from matplotlib.offsetbox import AnchoredText

def apu_calc(data1, data2):
    '''This function compute APU metrics.
    :param data1: Array of pixel values of a single band.
    :type data1: numpy.array
    :param data2: Array of pixel values of a single band.
    :type data2: numpy.array
    '''
    assert data1.size==data2.size
    sample_size = data1.size # Total pixels

    residuals = data2 - data1 # Residuals calc

    acc = residuals.sum()/sample_size # Accuracy metric

    diff_a = numpy.power((residuals - acc), 2)
    prec = numpy.sqrt(diff_a.sum()/(sample_size-1)) # Precision metric

    residuals_square = numpy.power((residuals), 2)
    unc = numpy.sqrt(residuals_square.sum()/sample_size) # Uncertainty

    res_unc = 100 * (unc/data1.mean())

    return sample_size, acc, prec, unc, res_unc


def apu_hist_plot(hist_data, hist_min, hist_max, lines, line_names, bins, colors=['tab:pink', 'tab:red', 'tab:green', 'tab:purple'], marker=['', '+', 'x', '*'], xlabel=None, global_text=None, out_file=None):
    fig, ax = plt.subplots()
    if xlabel:
        ax.set_xlabel(xlabel)

    # Plot lines
    i=0
    for line in lines:
        ax.plot(bins, line, color=colors[i], label=line_names[i], marker=marker[i])
        i+=1

    # Instantiate a second axes that shares the same x-axis
    ax2 = ax.twinx()

    # Order of each plot (Front, Back)
    ax.set_zorder(2)
    ax2.set_zorder(1)
    ax.patch.set_visible(False)

    # Remove scientific notation
    ax2.ticklabel_format(style='plain')

    # the histogram of the data
    _, _, _ = ax2.hist(hist_data, bins, edgecolor="k", label = 'nb of points')

    if global_text is not None:
        xpos = bins[0]
        # Get text y pos
        ypos = 0
        for line in lines:
            if numpy.nanmax(line) > ypos:
                ypos = numpy.nanmax(line)*0.65
        box_text = f'APU {global_text[0]} Band {global_text[1]} \n{global_text[2]}\nnbp={global_text[3]}\nAvg Truth {global_text[4]:.2f}\nAccuracy{global_text[5]:.2f}\nPrecision{global_text[6]:.2f}\nUncertainty{global_text[7]:.2f}'
        ax.text(x = xpos, y = ypos, s = box_text)

    fig.legend(loc="upper right", bbox_to_anchor=(1,1), bbox_transform=ax.transAxes)

    if out_file:
        plt.savefig(out_file)
    else:
        plt.show()


def sug_spec_on_reflec(reflec):
    return 0.005 + 0.05 * reflec


def parcelise_data(r1, r2, bins):
    # Calculate APU per parcel
    data_bins = numpy.digitize(r1, bins)

    accuracy = list()
    precision = list()
    uncertainty = list()
    for parcel in range(1, len(bins)+1):
        parc_pos = numpy.where(data_bins == parcel)[0]
        if parc_pos is not None and len(parc_pos)>200:
            _, acc, prec, unc, _ = apu_calc(r1[parc_pos], r2[parc_pos])
        else:
            _, acc, prec, unc, _ = numpy.nan, numpy.nan, numpy.nan, numpy.nan, numpy.nan
        accuracy.append(acc)
        precision.append(prec)
        uncertainty.append(unc)
    return accuracy, precision, uncertainty


def metrics_and_plot(r1, r2, out_file=None, num_valid_observations=None):
    r1_min = numpy.nanmin(r1)
    r1_max = numpy.nanmax(r1)

    num_bins = int(numpy.ceil((r1_max - r1_min)*100))

    r1_floor = numpy.floor(r1_min*100)/100 #*100 to remove 2 decimal places and / 100 to return scale
    r1_ceil = numpy.ceil(r1_max*100)/100 #*100 to remove 2 decimal places and / 100 to return scale

    bins = numpy.linspace((r1_floor), (r1_ceil), num_bins, endpoint=False)

    # Remove from r1 and r2 observations with less than num_valid_observations on its bin
    if num_valid_observations is not None:
        data_bins = numpy.digitize(r1, bins)
        bincount = numpy.bincount(data_bins)
        valid_bins = numpy.where(bincount > num_valid_observations)

        r1_floor = bins[valid_bins[0][0]-1]
        r1_ceil = bins[valid_bins[0][-1]-1]+0.01
        num_bins = int((r1_ceil - r1_floor)*100) #End of the larger parcel - start of smallest parcel
        bins = numpy.linspace((r1_floor), (r1_ceil), num_bins, endpoint=False)

        # Check which positions from r1 do not have enough num_valid_observations
        values_to_keep = numpy.isin(data_bins, valid_bins[0])
        r1 = r1[values_to_keep]
        r2 = r2[values_to_keep]

    sug_spec = numpy.array(list(map(sug_spec_on_reflec, bins)))
    sample_size, acc, prec, unc, res_unc = apu_calc(r1, r2) # Global APU
    acc_parc, prec_parc, unc_parc = parcelise_data(r1, r2, bins) # Per parcel APU

    lines = [sug_spec, acc_parc, prec_parc, unc_parc]
    line_names = ['suggested specs', 'accuracy', 'precision', 'uncertainty']

    global_text = ['image_name', 'X', 'DatasetX', sample_size, 0, acc, prec, unc]

    apu_hist_plot(hist_data=r1, hist_min=r1_floor, hist_max=r1_ceil, lines=lines, line_names=line_names, bins=bins, xlabel='Surface Reflectance Truth', global_text=global_text, out_file=out_file)


# Run example
# from numpy import genfromtxt

# r1 = genfromtxt('/home/marujo/Marujo/Tasks/arcsi_lc8_af.csv', delimiter=',')
# r2 = genfromtxt('/home/marujo/Marujo/Tasks/reflec_lc8_af.csv', delimiter=',')
# out_file = '/home/marujo/Marujo/Tasks/hist.png'

# num_valid_observations = 200

# metrics_and_plot(r1, r2, out_file, num_valid_observations)
