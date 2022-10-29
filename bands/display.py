import matplotlib.pyplot as plt

def show_bands(band) -> None:
    """
    Function plots given satellite band.
    """
    plt.figure(figsize=(12, 12))
    plt.imshow(band, cmap='gray')
    plt.plot()