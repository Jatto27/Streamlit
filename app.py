import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Medals Visualization", layout="wide")
st.title("Medals Visualization")

#dropdown menu
medal = st.selectbox("Medal type", ["gold", "silver", "bronze"])

#checkboxes

show_bar = st.checkbox("Show Bar Chart", value=True)
show_pie = st.checkbox("Show Pie Chart", value=True)

#two-col structure
col1,col2 = st.columns(2)

#load the medal wide data set
df = px.data.medals_wide()

#plot bar chart
if show_bar:
  fig_bar = px.bar(df, x="nation", y = f"{medal}", title = f"Medals Count ({medal})", t)
  
fig_bar.update_layout(
  title_x=0.5,
  xaxis_title="Country",
  yaxis_title="Count",
  width = 300, height = 400
)


if show_pie:
  fig_pie = px.pie(
      df, values=f"{medal}", names="nation", title=f"Medals Count ({medal})")

  fig_pie.update_layout(
      title_x=0.5, width=300, height=400
  )
                      

  col1.plotly_chart(fig_bar, use_container_width=True)
