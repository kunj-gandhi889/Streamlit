import streamlit as st
import pandas as pd
from matplotlib import pyplot as plt
import numpy as np
import time

st.set_option('deprecation.showPyplotGlobalUse', False)
st.title("SIDEBAR , NAVIGATION BAR , STATUS BAR")

# sidebar --> st.sidebar.widget --> add widget at sidebar
# navigation bar can be created in sidebar only
ch = st.sidebar.radio("Navigate",["PLOT","DATAFRAME"]) 
data = {
    "num" : [i for i in range(1,11)],
    "square" : [i**2 for i in range(1,11)],
    "twice" : [i*2 for i in range(1,11)],
    "thrice" : [i*3 for i in range(1,11)],
    "cube":[i**3 for i in range(1,11)],
    "exponential" : [np.e**i for i in range(1,11)]
}
df = pd.DataFrame(data)
if ch == "PLOT":
    plt.style.use("ggplot")
    sel = st.sidebar.selectbox("Select Column",df.columns)

    plt.plot(df["num"],df[sel])
    plt.xlabel("NUMBER")
    plt.ylabel(str(sel).upper())
    plt.title(f"PLOT BETWEEN NUM AND {str(sel).upper()}")
    st.pyplot()
else:
    st.table(df)


# status bar
st.write("# STATUS BAR")
st.error("This is Error Message")  # to display error message
st.success("This is Success")  # displays success message
st.exception(ValueError("This is ValueError Exception"))
st.info("This is important text")  # to display informational message
st.warning("This is warning message")  # displays warning msg

# progress bar

st.write("# PROGRESS BAR")
f,s =  st.columns(2)
prog_bar1 = st.progress(0)  # to display a progress bar
prog_bar2 = st.progress(0)  # to display a progress bar
with f:
    for i in range(75):
        time.sleep(0.1)
        prog_bar1.progress(i+1)
with s:
    for i in range(25):
        time.sleep(0.1)
        prog_bar2.progress(i+1)
# balloon animation
# st.balloons()  # ballon animation --> when progress bar fills up

# snow animation
st.snow()

# spinner
with st.spinner("Loading!...."):
    time.sleep(3)
st.success("Done")

# expander  --> like data hider
with st.expander("Expand This Container"):
    st.write("Superman is a superhero appearing in DC Movies and Comics. His earth alias name is  Clark Kent and his Kryptonian Name is Kal-el")
    st.image("orsrc30951.jpg")