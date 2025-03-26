# Wind power forecasting using machine learning
This is one of the three pre-defined final projects in [46120 Scientific
Programming for Wind Energy](https://kurser.dtu.dk/course/46120), a MSc course
in DTU Wind. 

The objective of this project is to develop a Python package for short-term 
wind power forecasting using machine learning (ML) techniques. You and your
group will leverage a real-world dataset containing meteorological observations 
and wind power generation to build predictive models. The library will 
preprocess data, train ML algorithms (e.g., regression, decision trees, neural 
networks), and evaluate forecast accuracy.

## Background
Wind power forecasting is critical for grid stability, energy market 
participation, and operational efficiency in wind farms. Accurate predictions 
help balance supply and demand, reduce curtailment, and optimize maintenance 
schedules. Traditional physical models (e.g., numerical weather prediction) are 
computationally expensive, while data-driven ML approaches offer a flexible 
alternative by learning patterns directly from historical data.

### Machine learning in general
Machine learning (ML) is a subset of artificial intelligence (AI) that enables 
systems to learn patterns from data without being explicitly programmed. By 
training algorithms on historical data, ML models can make predictions, 
classify information, or identify trends. Key categories include:

* **Supervised Learning**: Models learn from labeled data (e.g., predicting
  power output from weather variables).
    * Common algorithms: Linear regression, decision trees, random forests, 
        neural networks.

* **Unsupervised Learning**: Models discover hidden patterns in unlabeled data 
(e.g., clustering similar wind regimes).

* **Reinforcement Learning**: Models learn by interacting with an environment 
to maximize rewards (less common in wind energy forecasting).

ML excels in handling nonlinear relationships, high-dimensional data, and 
real-time adaptability, making it ideal for complex problems like wind power 
forecasting.

You can learn more about the basics of ML in the following videos:

* [**What is Machine Learning?**](https://www.youtube.com/watch?v=HcqpanDadyQ) 

* [**The 7 steps of machine learning**](https://www.youtube.com/watch?v=nKW8Ndu7Mjw) 


You may also go through the [foundational courses](
https://developers.google.com/machine-learning/foundational-courses) on Machine 
Learning provided by Google, especially the first two ones: 
* [**Introduction to Machine Learning**](
    https://developers.google.com/machine-learning/intro-to-ml)

* [**Machine Learning Crash Course**](
    https://developers.google.com/machine-learning/crash-course)

### Wind power forecasting: importance and challenges
Wind power is inherently variable due to the stochastic nature of wind. 
Accurate forecasting is critical for:

* **Grid Stability**: Balancing supply and demand to avoid blackouts.

* **Energy Markets**: Enabling wind farm operators to bid competitively in 
day-ahead markets.

* **Operational Efficiency**: Optimizing maintenance schedules and reducing 
turbine wear.

* **Reducing Curtailment**: Minimizing wasted energy by aligning production 
with grid capacity.

**Key Challenges** 
* **Intermittency**: Rapid changes in wind condition due to weather fronts, 
turbulence, or terrain effects.

* **Spatiotemporal Complexity**: Wind patterns vary by location, height, and 
time (diurnal/seasonal cycles).

* **Data Quality**: Noise, missing values, and sensor errors in real-world 
datasets.

* **Physical Constraints**: Turbine cut-in/cut-out speeds, blade pitch 
adjustments, power curves and turbine availability.

### Traditional forecasting methods
**Physical Models**:

* Use numerical weather prediction (NWP) systems to simulate atmospheric 
physics and generate wind speed forecasts.

* Strengths: Long-term accuracy (24–72 hours).

* Weaknesses: Computationally expensive, limited resolution (~1–10 km), and 
struggles with short-term variability.

**Statistical Models**:

* Persistence Model: Assumes future power equals current power (naive baseline).

* Auto-Regressive (AR) Models: Use historical power data (e.g., ARIMA).

* Strengths: Simple, fast, and effective for very short-term forecasts.

* Weaknesses: Ignores weather variables, fails to capture nonlinear dynamics.

### Machine learning in wind power forecasting
ML bridges the gap between physical and statistical models by leveraging 
historical data to learn complex relationships between meteorological 
variables and power output.

**Current Practices**
* **Data Sources**:

    * **Historical SCADA Data**: Turbine power output, wind speed/direction at 
    hub height.

    * **Meteorological Data**: NWP outputs, on-site sensors, or reanalysis data
    (e.g., ERA5).

    * **Temporal Features**: Time of day, day of year, holidays.

* **Common ML Approaches**

    * **Short-Term Forecasting (1–6 hours)**:

        * **Random Forests/Gradient Boosting**: Handle nonlinear interactions 
        and feature importance.

        * **Support Vector Machines (SVM)**: Effective for small datasets.

    * **Medium-Term Forecasting (6–24 hours)**:

        * **Neural Networks (NNs)**: Feedforward NNs for static forecasts.

        * **Long Short-Term Memory (LSTM) Networks**: Capture temporal 
        dependencies in time-series data.

        * **Hybrid Models**: Combine NWP outputs with ML corrections to improve 
        accuracy.

**Industry Trends**

* **Feature Engineering**: Cyclical encoding (e.g., sine/cosine for wind 
direction), lagged variables, rolling statistics.

* **Probabilistic Forecasting**: Quantile regression or Bayesian methods to 
estimate uncertainty (e.g., 95% prediction intervals).

* **Transfer Learning**: Pre-train models on data-rich regions and fine-tune 
for new sites.

* **Edge Computing**: Deploy lightweight models on turbines for real-time 
predictions.

### Limitations and Open Challenges
* **Data Scarcity**: Limited high-quality data for new or offshore sites.

* **Model Interpretability**: "Black-box" models like neural networks hinder 
trust in critical applications.

* **Dynamic Conditions**: Aging turbines, changing landscapes, or climate 
shifts degrade model performance over time.



## Provided data
The provided dataset is a unique compilation of field-based meteorological 
observations and wind power generation data, collected directly from a 
company's operational sites. The dataset represents a detailed hourly record, 
starting from January 2, 2017 to December 31, 2021. This rich dataset provides 
real-world insights into the interplay between various weather conditions and 
wind energy production.

### Context and Inspiration
The dataset was conceived out of the necessity to understand the dynamic 
relationship between meteorological variables and their impact on wind power 
generation. By collecting data directly from the field and the wind turbine 
installations, the provider of the dataset aims to provide a comprehensive and 
authentic dataset that can be instrumental for industry-specific research, 
operational optimization, and academic purposes.

### Data Collection
Data was meticulously gathered using state-of-the-art equipment installed at 
the site. The meteorological instruments measured temperature, humidity, 
dew point, and wind characteristics at different heights, while power 
generation data was recorded from the wind turbines' output.

### Potential Uses
This dataset is ideal for industry experts, researchers, and data scientists 
exploring renewable energy, especially wind power. It can aid in developing 
predictive models for power generation, studying environmental impacts on 
renewable energy sources, and enhancing operational efficiency in wind farms.

### Data format
Four csv files for 4 locations are found in `inputs` folder, namded as 
`Location[x].csv`, where `[x]` denotes the index of the location.

The columns in the data are as follows:
* **Time** - Hour of the day when readings occurred

* **temperature_2m** - Temperature in degrees Fahrenheit at 2 meters above the 
surface

* **relativehumidity_2m** - Relative humidity (as a percentage) at 2 meters 
above the surface

* **dewpoint_2m** - Dew point in degrees Fahrenheit at 2 meters above the 
surface

* **windspeed_10m** - Wind speed in meters per second at 10 meters above the 
surface

* **windspeed_100m** - Wind speed in meters per second at 100 meters above the 
surface

* **winddirection_10m** - Wind direction in degrees (0-360) at 10 meters above 
the surface (see notes)

* **winddirection_100m** - Wind direction in degrees (0-360) at 100 meters 
above the surface (see notes)

* **windgusts_10m** - Wind gusts in meters per second at 100 meters above the 
surface

* **Power** - Turbine output, normalized to be between 0 and 1 (i.e., a 
percentage of maximum potential output)

**Notes**:
1. Likely many of these variables will not be very relevant. They are included 
here but do not need to be included in the final models.

2. Degrees are measured from 0 to 360. Since 0 and 360 represent the same spot 
on a circle, consider transforming these using sine and/or cosine. Also 
consider converting them to radians, instead of degrees.

3.  Each location can have a different model. There is no reason to build one 
model to work for all locations.


### About the data source:

This dataset is from a openly available dataset on the internet, it is a 
"CC0 1.0 Universal" license, i.e., the dataset is on the public domain and 
without copyrights. Check details on the license here: 
https://creativecommons.org/publicdomain/zero/1.0/



## Requirements to pass
### Functional requirements
As a minimal, your package should be able to:
1. Load and parse the provided input data

2. Plot timeseries of a selected variable (like **wind_speed_100m** or 
**Power**) for a given site (site 1, 2, 3 or 4) within a specific 
perid, i.e., a function with variable_name, site_index, starting_time 
and ending_time as inputs.

3. Compute mean squared error (MSE), mean absolute error (MAE), and root mean 
square error (RMSE) for a forecasted time series against the corresponding 
real time series.

4. Split the dataset into training dataset and test dataset.

5. Predict one hour ahead power output for a given site (site 1, 2, 3, or 4) 
using the persistence model, which assumes one hour ahead power output equals
the current power output.

6. Predict one hour ahead power output for a given site (site 1, 2, 3 or 4) 
using two different ML models (like support vector machine or neural network)

7. Plot predicted against real timeseries of power for a given site (site 1,
 2, 3 or 4) within a specific period with a specified forecasting model.


**Important note**: 
* Your package should also implement at least two extra functions besides the required ones listed above.
* If the training process is time consuming, you can save and load your trained
models using `pickle`.

### Formal requirements
Check the general requirements defined for all final projects.

### Other tips
* You are recommended to use `scikit-learn` to develop this package. 
* You may want to check the relevant examples provided by `scikit-learn`: 
    * [**Lagged features for time series forecasting**](https://scikit-learn.org/stable/auto_examples/applications/plot_time_series_lagged_features.html#sphx-glr-auto-examples-applications-plot-time-series-lagged-features-py)
    * [**Time-related feature engineering**](https://scikit-learn.org/stable/auto_examples/applications/plot_cyclical_feature_engineering.html#sphx-glr-auto-examples-applications-plot-cyclical-feature-engineering-py)
* You may consider extending your models to work for longer forecasting
horizon, like 6 hours or 12 hours.
* You may implement more ML models.
* You may try other tools, like `Keras`



## References
* Giebel, G. and Kariniotakis, G., (2017). Wind power forecasting — a review of 
the state of the art. *Renewable energy forecasting*, pp.59-109. DOI:
[10.1016/B978-0-08-100504-0.00003-2](
    https://doi.org/10.1016/B978-0-08-100504-0.00003-2)

* Feng, J., (2019). *Artificial Intelligence for Wind Energy (AI4Wind): A state 
of the art report*. DTU Wind Energy E Vol. 0180 (Available at: 
https://orbit.dtu.dk/files/169036158/AI4Wind_state_of_the_art_report.pdf)



## Recommended materials
To learn more about the topic of this project, the following materials are
recommended:

* [**Masterclass on Wind Power Forecasting (Part I)**](
    https://youtu.be/j-5xq3ZyMk0) by Gregor Giebel

* [**Masterclass on Wind Power Forecasting (Part II)**](
    https://youtu.be/xO_AIU0m9vY) by Gregor Giebel

* [**Lesson 1: Introduction to renewable energy forecasting**](
    https://youtu.be/RZi5RjDKAH0) by Henrik Madsen

* [**Lesson 2: Point forecasts of wind and solar power production**](
    https://youtu.be/RZi5RjDKAH0) by Henrik Madsen

* [**Lesson 3: Probabilistic and full stochastic forecasting**](
    https://youtu.be/Z-E_TDLIx8c) by Henrik Madsen

* DTU course: [**46765 Machine learning for energy systems**](
    https://kurser.dtu.dk/course/46765)

* DTU course: [**02960 Time Series Analysis - with a focus on Modelling and 
Forecasting in Energy Systems**](
    https://kurser.dtu.dk/course/02960)
    

