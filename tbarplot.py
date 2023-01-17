import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

def bar(x, height, *args, **kwargs):

    x = np.array(x)
    height = np.array(height)
    # Remove error bar heights from arguments
    
    yerr = kwargs.pop('yerr', None)

    # Make bar plot
    bars = plt.bar(x, height, *args, **kwargs)

    # Calculate scaling for error bars
    # Get dimensions of y-axis in pixels
    ymin, ymax = plt.ylim()
    y1, y2 = plt.gca().get_window_extent().get_points()[:, 1]
    # Get unit scale
    yscale = (y2-y1)/(ymax-ymin)

    # Add error bars
    if yerr is not None:
        
        # Resize y axis to fit error bar
        ylow, yhigh = plt.ylim()
        ypos = (height + yerr)[height >= 0]
        yneg = (height - yerr)[height < 0]
        if np.min(height) < 0:
            ylow = ylow + (np.min(yneg) - np.min(height))
        if np.max(height) >= 0:
            yhigh = yhigh + (np.max(ypos) - np.max(height))
        plt.ylim(ylow, yhigh)

        # Add Ts
        for xi, yi, yerri in zip(x, height, yerr):
            if yi >= 0:
                plt.text(
                    xi, yi, 'T',
                    fontsize=yerri*yscale,
                    fontfamily='serif',
                    ha='center', va='bottom',
                )
            else:
                plt.text(
                    xi, yi, 'T',
                    fontsize=yerri*yscale,
                    fontfamily='serif',
                    ha='center', va='top', rotation=180,
                )


    return bars
