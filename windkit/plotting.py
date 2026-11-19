"""Plot helpers."""
import matplotlib.pyplot as plt


def plot_mean_field(field, ax=None, title="Mean wind speed"):
    ax = ax or plt.gca()
    im = ax.imshow(field.mean(axis=0), cmap="viridis", origin="lower")
    ax.set_title(title)
    plt.colorbar(im, ax=ax, label="m/s")
    return ax


def plot_timeseries(field, ax=None, title="Domain-mean wind speed per hour"):
    ax = ax or plt.gca()
    ax.plot(range(field.shape[0]), field.mean(axis=(1, 2)), marker="o")
    ax.set_title(title)
    ax.set_xlabel("Hour")
    ax.set_ylabel("m/s")
    return ax
