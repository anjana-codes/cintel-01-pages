#Import libraries
import matplotlib.pyplot as plt
import numpy as np
from shiny.express import ui, input, render
from scipy.stats import norm

# Add page options for Shiny
ui.page_opts(title="PyShiny App with Plot", fillable=True)

# Create a sidebar with a slider input
with ui.sidebar():
    # A a slider for the specifying nunber of bins in the histogram
    # The ui.input_slider function is called with five arguments:
    # A string id ("selected_number_of_bins") that uniquely identifies this input value. 
    # A string label ("Number of Bins") to be displayed alongside the slider.
    # An integer representing the minimum number of bins (0).
    # An integer representing the maximum number of bins (100).
    # An integer representing the initial value of the slider (35).
    # A string id ("selected_number_of_bins") that uniquely identifies this input value. 
    ui.input_slider("selected_number_of_bins", "Number of Bins", 0, 100, 35)

# Define a plot function for rendering a histogram
@render.plot(alt="A histogram")
def histogram():
   
    # Set a random seed for reproducibility
    np.random.seed(3)

    # Generate random data for the histogram
    x = 100 + 15 * np.random.randn(437)

    # Plot the histogram using the specified number of bins and change the color to brown
    plt.hist(x, input.selected_number_of_bins(), density=True, color='brown')
    
    # Plot the PDF.
    mu, std = norm.fit(x) 
    xmin, xmax = plt.xlim()
    x = np.linspace(xmin, xmax, 100)
    p = norm.pdf(x, mu, std)
    plt.plot(x, p, 'k', linewidth=2)
