### Imports
# Standard library

# Third-party libraries
import matplotlib.pyplot as plt

# Local files


# Matplotlib style config
plt.style.use("ggplot")


def plot_histogram(
        data: dict[str, list[int | float]],
        title: str = "Histogram", 
        xlabel: str = "X label",
        ylabel: str = "Y label"
    ) -> None:
    """
    Plots a histogram from a dictionary of keys and their corresponding values.

    Parameters
    ----------
        data: A dictionary object.
        title: The title of the histogram. Defaults to `Histogram`.
        xlabel: The label for the x-axis. Defaults to `X label`.
        ylabel: The label for the y-axis. Defaults to `Y label`.

    """
    keys = list(data.keys())
    values = list(data.values())
    plt.bar(keys, values, color=COLOR_SCHEME[0])
    plt.title(title, fontsize=10)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()
    
    
def plot_lineplot(
        data: dict[str, list[int | float]],
        title: str = "Line-plot", 
        xlabel: str = "X label",
        ylabel: str = "Y label"
    ) -> None:
    """
    Plots a line-plot from a dictionary of keys and their corresponding values.

    Parameters
    ----------
        data: A dictionary object.
        title: The title of the line-plot. Defaults to `Line-plot`.
        xlabel: The label for the x-axis. Defaults to `X label`.
        ylabel: The label for the y-axis. Defaults to `Y label`.

    """
    for i, (key, value) in enumerate(data.items()):
        plt.plot(value, label=key, color=COLOR_SCHEME[i])
    plt.title(title, fontsize=9)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.xticks(rotation=45)
    plt.legend()
    plt.tight_layout()
    plt.show()
