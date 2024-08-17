import streamlit as st
import plotly.express as px
import pandas as pd
import warnings

warnings.filterwarnings("ignore")

# Head : Dataset name as Title, and add some discription about the dataset
# Your information: Name, and some bio
# check for null values, there was no null values
# Add hypothesis questoins before graphs, and title axis for the graphs
# some cleanups for analysis
# Conclusion (short summary)
st.title("Silicon Starlings")
st.write("Abhijit Geetaumesh: Lives in Bay Area, age 16")
st.write("Leon Zhou: Lives in the Bay Area, age 15")

st.title("Star Type Classifications --- Nasa")
st.header("Intro")
st.write(
  "This dataset describes the data from a couple hundred stars studied by NASA, each with information relating to the brightness, size, and color. We plan to identify and analyze the relationships between each category of data, to try and come to some sort of conclusion about the stars studied."
)

stars_dataframe = pd.read_csv("Stars.csv")

st.markdown("---")

st.header("Inspection")
st.write("Head")
st.table(stars_dataframe.head())
st.write("Tail")
st.table(stars_dataframe.tail())
st.write("Shape")
st.write(stars_dataframe.shape)
st.write("Columns")
st.write(stars_dataframe.columns)
st.write("Basic Statistics")
st.table(stars_dataframe.describe())

st.markdown("---")

# Clean the data -> Leon
numnull = stars_dataframe.isna().sum()
dropped_columns = ['Type']
cleanstars_dataframe = stars_dataframe.drop(dropped_columns,
                                            axis=1,
                                            inplace=False)
cleanstars_dataframe.describe()

st.header("Cleaning the data")
st.write("Number of null rows: ")
st.write(numnull)
st.write(
  "The data cleaning process involved checking for null values as well as the the final column. The column 'Type' was removed because of it's irrelevance to the processing, and no null values were found."
)
st.write("Post-processing Head")
st.table(cleanstars_dataframe.head())
st.write("Post-processing Tail")
st.table(cleanstars_dataframe.tail())
st.write("Post-processing Shape")
st.write(cleanstars_dataframe.shape)
st.write("Post-processing Columns")
st.write(cleanstars_dataframe.columns)
st.write("Post-processing Basic Statistics")
st.table(cleanstars_dataframe.describe())

st.markdown("---")

st.header(
  "Hypothesis 1: What's the relation between relative luminosity and relative radius of the stars?"
)
fig1 = px.scatter(x=cleanstars_dataframe["L"],
                  y=cleanstars_dataframe["R"],
                  labels={
                    "L": "Relative Luminosity",
                    "R": "Relative Radius"
                  })
fig1.update_layout(title_text="Relative Luminosity vs. Relative  Radius",
                   xaxis_title="Relative Luminosity",
                   yaxis_title="Relative Radius")
st.plotly_chart(fig1, use_container_width=True)

st.write(
  "Two main groupings of stars: those with small relative radii and a range of different luminosities, and those with large relative radii and a range of different luminosities. The latter is far more spread out in terms of radii, rather than being 'squished' down near the x-axis for the former. While the graph has loose form, it does indicate that stars tend to either have small or large relative radii, with little inbetween, alongside a range of luminosities."
)

st.write(
  "Why is there a split in the grouping of stars, and what kinds of stars make up the groups with large and small radii?"
)

st.write(
  "This can be answered by color coding the stars different colors based on star color and spectral class, alongside online research of stars with abnormally high radii."
)

fig1a = px.scatter(x=cleanstars_dataframe["L"],
                   y=cleanstars_dataframe["R"],
                   color=cleanstars_dataframe["Color"],
                   labels={
                     "L": "Relative Luminosity",
                     "R": "Relative Radius"
                   })
fig1a.update_layout(title_text="Relative Luminosity vs. Relative  Radius",
                    xaxis_title="Relative Luminosity",
                    yaxis_title="Relative Radius")
st.plotly_chart(fig1a, use_container_width=True)

st.write(
  "By color coding the data based on spectral class, we can figure out that many stars in the large relative radius class are cool, red stars, while stars in the small relative radius class are hot, blue stars, but there is still significant variation in star color in stars with both large and small radii. We will talk more about star color and temperature later on."
)

st.markdown("---")

st.header(
  "Hypothesis 2: What's the relation between relative luminosity and temperature of the stars?"
)
fig7 = px.scatter(x=cleanstars_dataframe['L'],
                  y=cleanstars_dataframe['Temperature'],
                  labels={
                    "L": "Relative Luminosity",
                    "Temperature": "Temperature (k)"
                  },
                  title="Relative Luminosity vs. Temperature  (k)")
fig7.update_layout(xaxis_title="Relative Luminosity",
                   yaxis_title="Temperature (k)")
fig2 = px.scatter(x=cleanstars_dataframe['L'],
                  y=cleanstars_dataframe['Temperature'],
                  labels={
                    "L": "Relative Luminosity",
                    "Temperature": "Temperature (k)"
                  },
                  title="Relative Luminosity vs. Temperature  (k)",
                  log_x=True,
                  range_x=[0.00001, 1000000])
fig2.update_layout(xaxis_title="Relative Luminosity",
                   yaxis_title="Temperature (k)")
st.plotly_chart(fig2, use_container_width=True)

st.write(
  "Even after the removal of outliers (Luminosity {<1, >70000}), there seems to be little correlation between the luminosity and temperature of the stars. Within the dataset, most of the points are below 1 and above 10000, with a large variation in luminosity. This can be largely attributed to the nature of the relative luminosity value. It's formula is simply a constant multiplied by the size of the star and the temperature raised to the fourth power. When adjusted to a logarithmic scale (10^x), the graph seems to conform to the exponential growth curve with two clusters of outliers, similar to the relationship between temperature and absolute magnitude that follows."
)

st.markdown("---")

st.header(
  "Hypothesis 3: What's the relation between absolute magnitude and temperature of the stars? "
)
fig3 = px.scatter(x=cleanstars_dataframe["A_M"],
                  y=cleanstars_dataframe["Temperature"],
                  labels={
                    "A_M": "Absolute Magnitude",
                    "Temperature": "Temperature (k)"
                  })
fig3.update_layout(title_text="Absolute Magnitude vs. Temperature",
                   xaxis_title="Absolute Magnitude",
                   yaxis_title="Temperature (k)")
st.plotly_chart(fig3, use_container_width=True)

st.write(
  "There is a general curve of stars that looks like an exponential decay curve. In general, the higher the absolute magnitude (lower the brightness), the lower the temperature, which makes sense intuitively. However, there are two groups of outliers. The first group is located when the absolute magnitude is less than -5. Despite their low absolute magnitudes (high brightness), they have incredibly low temperatures. The second group is located with the absolute magnitude is greater than 10. Despite their high absolute magnitudes (low brightness), they have incredibly high temperatures."
)

st.write("What makes the stars from each outlier group special?")

st.write(
  "This can be answered by color coding the stars different colors based on star color and spectral class, alongside online research of stars with abnormally high brightness and low temperatures and stars with low brightness and high temperatures."
)

fig3a = px.scatter(x=cleanstars_dataframe["A_M"],
                   y=cleanstars_dataframe["Temperature"],
                   color=cleanstars_dataframe["Color"],
                   labels={
                     "A_M": "Absolute Magnitude",
                     "Temperature": "Temperature (k)"
                   })
fig3a.update_layout(title_text="Absolute Magnitude vs. Temperature",
                    xaxis_title="Absolute Magnitude",
                    yaxis_title="Temperature (k)")
st.plotly_chart(fig3a, use_container_width=True)

st.markdown("---")

st.header(
  "What is the relationship between relative luminosity and absolute magnitude?"
)

fig4 = px.scatter(x=cleanstars_dataframe["L"],
                  y=cleanstars_dataframe["A_M"],
                  labels={
                    "L": "Relative Luminosity",
                    "A_M": "Absolute Magnitude"
                  })
fig4.update_layout(xaxis_title="Relative Luminosity",
                   yaxis_title="Absolute Magnitude")
st.plotly_chart(fig4, use_container_width=True)

st.write(
  "As you may have noticed, the graphs of relative luminosity (logorithm) and temperature and absolute magnitude and temperature are pretty similar (the biggest difference is absolute magnitude is reversed due to it because the negative log). Both relative luminosity and absolute magnitude are measures of brightness, which is why they produce similar graphs. Most datapoints that are outliers in this graph are also outliers in the absolute magnitude vs temperature graph, suggesting a relationship between absolute magnitude and luminosity as seen by the correlation in fig. 4."
)

st.header("Hypothesis 4: What is the frequency of each kind of star color?")
color_frequency = cleanstars_dataframe["Color"].value_counts()
fig5 = px.pie(cleanstars_dataframe,
              names='Color',
              title='Frequency of Star Colors')
fig5.update_traces(hoverinfo='percent', textinfo='value')
st.plotly_chart(fig5, use_container_width=True)

st.write(
  "Stars come in various colors, and the color of a star is primarily determined by its temperature. The temperature, in turn, affects the balance between the different wavelengths of light emitted by the star. Stars emit light across a wide spectrum, but the human eye is most sensitive to light in the green-yellow part of the spectrum. Generally, stars with higher temperatures appear bluish or white, while stars with lower temperatures appear reddish. From the temperature graph, it is evident that stars with lower temperature (<5000k) appear more often than those with higher temperatures. "
)

st.markdown("---")

st.header(
  "Hypothesis 5: What is the relationship between color and spectral class?")
fig6 = px.density_heatmap(x=cleanstars_dataframe["Color"],
                          y=cleanstars_dataframe["Spectral_Class"],
                          labels={
                            "Color": "Color",
                            "Spectral_Class": "Spectral Class"
                          })
fig6.update_layout(title_text="Color vs. Spectral Class")
fig6.update_xaxes(categoryarray=[
  "Red", "OrangeRed", "Orange", "YellowOrange", "Yellow", "YellowWhite",
  "White", "BlueWhite", "Blue"
])
fig6.update_yaxes(categoryarray=["M", "K", "G", "F", "A", "B", "O"])
fig6.update_layout(xaxis_title="Color", yaxis_title="Spectral Class")
st.plotly_chart(fig6, use_container_width=True)

st.write(
  "According to online research, the spectral classifications indicate different colors and temperatures of the star, where M is the most red and O is the most blue. We see this in the heat map, as bluer stars are of the O, B, and A spectral classes, yellower stars are part of the F and G classes, oranger stars are part of the K class, and red stars are part of the M class. Online research also indicates increasing temperature for different spectral classes, where O>B>A>F>G>K>M in terms of temperature. Because there is a direct correlation between spectral classifications and color, it must mean that color also indicates temperature--which it does. Generally, the bluer the star, the hotter it is, and the redder the star, the colder it is."
)

st.markdown("---")

st.header("Conclusion")

st.write(
  "While a correlation between radius and luminosity was observed, it is not a simple direct proportionality, as some significant group at the extremes of large and small radii was seen. But generally, stars with larger radii tend to exhibit higher luminosities, suggesting a relationship between a star's physical size and its energy output. However, it is important to consider that other factors, such as temperature and composition, can also influence a star's luminosity."
)

st.write(
  "A positive correlation was observed between luminosity and temperature. This implies that as the temperature of a star increases, so does its luminosity. This finding aligns with the well-known Stefan-Boltzmann law, which states that the luminosity of a star is directly proportional to the fourth power of its temperature."
)

st.write(
  "A similar pattern was seen between absolute magnitude and temperature. Absolute magnitude is a measure of the brightness of a star if it was 10 parsecs away from observation. When comparing relative luminosity and absolute magnitude, we found them to have a direct linear relationship."
)

st.write(
  "In terms of star color, the analysis revealed a varied frequency distribution. Stars exhibit a range of colors, with blue being the hottest and red being the coolest. However, the frequency distribution is not uniform, with the majority of stars falling within the white to red color categories. Blue stars were found to be relatively less frequent, while red stars were more commonly observed."
)

st.write(
  "There also exists a close relationship between star color and spectral class, which provides information about the surface temperature of stars. Different spectral classes, such as O, B, A, F, G, K, and M, correspond to different temperature ranges. Blue stars, associated with spectral classes O, B and A, have higher temperatures, while red stars, linked to spectral classes M and K, have lower temperatures. This connection between color and spectral class enables inferences to be made about a star's temperature based on its observed color."
)

st.write(
  "All in all, this project as taught us a lot about data management and analysis. Finding the correlation between each set of data is not as straightforwards as it seems. Some of the correlations, such as the one between Relative Luminosity and Temperature, or Absolute Magnitude and Temperature, took some processing to find a clearer trend. Outliers played a large factor in this - they often misled us and shrouded the real trend. Finally, we were able to draw conclusions about information not directly given to us, such as the relationship between absolute magntiude and relative luminosity."
)
