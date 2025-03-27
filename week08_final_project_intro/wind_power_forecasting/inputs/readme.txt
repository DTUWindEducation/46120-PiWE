About Dataset:

This dataset is a unique compilation of field-based meteorological observations and wind power generation data, collected directly from a company's operational sites. The dataset represents a detailed hourly record, starting from January 2, 2017. This rich dataset provides real-world insights into the interplay between various weather conditions and wind energy production.

Context and Inspiration:
The dataset was conceived out of the necessity to understand the dynamic relationship between meteorological variables and their impact on wind power generation. By collecting data directly from the field and the wind turbine installations, we aim to provide a comprehensive and authentic dataset that can be instrumental for industry-specific research, operational optimization, and academic purposes.

Data Collection:
Data was meticulously gathered using state-of-the-art equipment installed at the site. The meteorological instruments measured temperature, humidity, dew point, and wind characteristics at different heights, while power generation data was recorded from the wind turbines' output.
This dataset is a unique compilation of field-based meteorological observations and wind power generation data, collected directly from one of our company's operational sites. The dataset represents a detailed hourly record, starting from January 2, 2017. This rich dataset provides real-world insights into the interplay between various weather conditions and wind energy production.

Potential Uses:
This dataset is ideal for industry experts, researchers, and data scientists exploring renewable energy, especially wind power. It can aid in developing predictive models for power generation, studying environmental impacts on renewable energy sources, and enhancing operational efficiency in wind farms.


------------------------------------
------------------------------------
About the data format:

The columns in the data are as follows:

Time - Hour of the day when readings occurred
temperature_2m - Temperature in degrees Fahrenheit at 2 meters above the surface
relativehumidity_2m - Relative humidity (as a percentage) at 2 meters above the surface
dewpoint_2m - Dew point in degrees Fahrenheit at 2 meters above the surface
windspeed_10m - Wind speed in meters per second at 10 meters above the surface
windspeed_100m - Wind speed in meters per second at 100 meters above the surface
winddirection_10m - Wind direction in degrees (0-360) at 10 meters above the surface (see notes)
winddirection_100m - Wind direction in degrees (0-360) at 100 meters above the surface (see notes)
windgusts_10m - Wind gusts in meters per second at 100 meters above the surface
Power - Turbine output, normalized to be between 0 and 1 (i.e., a percentage of maximum potential output)

Notes:
	1) Likely many of these variables will not be very relevant. They are included here but do not need to be included in the final models.
	2) Degrees are measured from 0 to 360. Since 0 and 360 represent the same spot on a circle, consider transforming these using sine and/or cosine. Also consider converting them to radians, instead of degrees.
	3) Each location can have a different model. There is no reason to build one model to work for all locations.


-------------------------------------
-------------------------------------
About the data source:

This dataset is from a openly available dataset on the internet, it is a "CC0 1.0 Universal" license, i.e., the dataset is on the public domain and without copyrights. Check details on the license here: https://creativecommons.org/publicdomain/zero/1.0/
