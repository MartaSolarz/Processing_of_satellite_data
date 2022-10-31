import matplotlib.pyplot as plt

def show_bands(band: str) -> None:
    """
    Function plots given satellite band.
    
    Parameters:
        band [str];
    Return:
        None.
    """
    plt.figure(figsize=(12, 12))
    plt.imshow(band, cmap='gray')
    plt.plot()
