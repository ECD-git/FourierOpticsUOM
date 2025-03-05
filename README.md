# FourierOpticsUOM
A small module of code developed in conjunction with the Fourier Optics lab experiment at UOM, third year physics.
Developed for personal use, more functions and their explanations will be added here over time.
Requres numpy, scipy, PIL, matplotlib, random, all of which are readily available on Spyder,
where it is reccomended to run this program

## Function Descriptions
- unflatten(array: list, linelength: int):
    - Unflattens a 1D array into a 2d array of width linelength.
- normalise(array: list):
    - Normalises an array height to have max value at 1
- sample(data: list, samplesize: int)
    - Returns an array of random x and y values within the bounds of the input array.
- abs2(x):
    - gets the absolute value of an nomalised imaginary number x
- openimage(name: str)
    - Opens an image file, returns a 2D array of pixel intensity data.
- displayhorizontalline(data: list, row: int, norm: bool)
    - Plots a horizontal line segment of the inputted image's intensity.
    - Plot can be normalised if norm is set to true.
- displayverticalline(data: list, colm: int, norm: bool)
    - Plots a vertical line segment of the inputted image's intensity.
    - Plot can be normalised if norm is set to true.
- get_period(inpdata: list, full: bool)
    - Uses the scipi get_peaks function to get the average distance between 2 peaks, for periodic input data.
    - Indexes and heights of peaks can be returned in full is set to true.
    - Warning, untested on not strictly horizontal or vertical data.
- stderrormean(oneDdata: list)
    - Gets the statistical standard error on the mean for an array of floats.


## v0.1
- Initial commit, taken directly from person code directory
- Added docstrings to functions

