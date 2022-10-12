# import package 


from os import stat
import streamlit as st

import pandas as pd 
import plotly.offline as pyo
import plotly.graph_objs as go


from sklearn.utils import estimator_html_repr


import plotly.express as px  
import numpy as np
import plotly.figure_factory as ff
import chart_studio.plotly as py
#from plotly.offline import init_notebook_mode,iplot



# setting page layout 
st.set_page_config(layout="wide")
st.title("Streamlit Application...")

st.markdown("""**Hello**  and **welcome** to my first streamlit application in MSBA325 course!

In this application, I used three datasets.  The first is **Sales Data** to study sales by products, customers, and region.

The second is: **Graduate Admission Prediction** to study the factors that increase the chance for graduate studies admission. 

The third is **Life Expectancy** to see the difference in age expectancy among countries.""")

df = pd.read_excel(r"C:\Users\BC\Documents\Daniel Streamlit\Assignment #2 - Daniel Raydan - ID 202371151\2- Bubble chart\sales.xlsx")

st.title("Sales Dataset")

# Load dataset
if st.checkbox("Preview Dataset"):
        data =df
        if st.button ("ALL Dataset"):
            st.dataframe(data)
        elif st.button("Head"):
            st.write(data.head())
        elif st.button("Tail"):
            st.write(data.tail())

# Show Column Name
if st.checkbox ("Show Column Name"):
        data=df
        st.write(data.columns)


st.subheader("Profit vs Sales")


ax2=px.scatter(df,x="Sales",y="Profit", color="Order Priority")
ax2.update_layout(
    #title = "Sales vs Profit",
    xaxis = dict(title = "Sales"),
    xaxis_range = [0 , 30000],
    yaxis = dict(title = "Profit"),
    yaxis_range = [-15000 , 20000],
    hovermode = "closest"
)
st.plotly_chart(ax2, use_container_width=True)
st.write('<p style="font-size:130%">This scatter plot shows the variation of profit with sales of orders with different priorities</p>', unsafe_allow_html=True)

col1, col2= st.columns(2)   
val_count11  = df['Product Category'].value_counts(normalize=True, ascending=False)
        
fig11=px.pie(val_count11, values= val_count11.values , hole =0.3, names= val_count11.index)
fig11.update_layout({
        'plot_bgcolor': 'rgba(0,0,0,0)'})
fig11.update_layout(yaxis_visible=False, yaxis_showticklabels=False)
col1.subheader("Order by Product Category")       
col1.plotly_chart(fig11, use_container_width=True) 

val_count3 = df['Product Sub-Category'].value_counts(normalize=True, ascending=False)
    
fig3=px.pie(val_count3, values= val_count3.values , hole =0.3, names= val_count3.index, labels=dict(x=" percentage(%)", y=" "))
fig3.update_layout({
    'plot_bgcolor': 'rgba(0,0,0,0)'})
fig3.update_layout(yaxis_visible=False, yaxis_showticklabels=False)
           
col2.subheader("Order by Product Sub_Category")  
col2.plotly_chart(fig3,use_container_width=True)

st.write('<p style="font-size:130%">These pie charts show the distribution of product category and product sub_category among orders</p>', unsafe_allow_html=True)

st.subheader("Sales by Product Category and Product Subcategory")
fig=px.sunburst(df, values="Sales", color="Sales", path=["Product Category","Product Sub-Category"])
ax=fig.update_layout(
    margin = dict(t=25, l=30, r=25, b=30)
)
st.plotly_chart(ax,use_container_width=True)
st.write('<p style="font-size:130%">This sunburst shows sales by product category and product sub_category</p>', unsafe_allow_html=True)


countryord = df.groupby(['Region'])['Order Quantity'].sum().reset_index().sort_values(by='Order Quantity')
countrysales = df.groupby(['Region'])['Sales'].sum().reset_index().sort_values(by='Sales')
st.subheader("QUANTITY ORDERED AND SALES BY Region")
col1, col2= st.columns(2) 
col1.subheader("QUANTITY ORDERED")
col2.subheader("Sales")
fig5= px.bar(x=countryord['Order Quantity'], y=countryord['Region'], orientation='h',
                    )
fig5.update_layout({
    'plot_bgcolor': 'rgba(0,0,0,0)'})
col1.plotly_chart(fig5,use_container_width=True)

st.write('<p style="font-size:130%">These bar plots show the order quantity and sales in each region</p>', unsafe_allow_html=True)

fig6= px.bar(x=countrysales['Sales'], y=countrysales['Region'], orientation='h',
                    )
fig6.update_layout({
    'plot_bgcolor': 'rgba(0,0,0,0)'})
col2.plotly_chart(fig6,use_container_width=True)

st.subheader('MONTHLY SALES BY Customer Segment')
prodsales = df.groupby(['Customer Segment','Ship Month'])['Sales'].sum().reset_index()
fig = px.bar(prodsales, x='Sales', y='Customer Segment',
             orientation='h', height=600, 
            animation_frame="Ship Month", animation_group="Customer Segment",  template="seaborn")
fig.layout.updatemenus[0].buttons[0].args[1]["frame"]["duration"] = 1000
st.plotly_chart(fig,use_container_width=True)
st.write('<p style="font-size:130%">This bar graph shows the monthly sales obtained from each customer segment</p>', unsafe_allow_html=True)

st.sidebar.write("**Contact** **Details:**")
st.sidebar.write("Done By: **Daniel** **Raydan**")
st.sidebar.write("Email:dmr05@mail.aub.edu")


df1 = pd.read_csv(r"C:\Users\BC\Downloads\Admission_Predict.csv")

st.title("Graduate Admission Dataset")

# Load dataset
if st.checkbox("View Dataset"):
        data =df1
        if st.button ("ALL Dataset"):
            st.dataframe(data)
        elif st.button("Head"):
            st.write(data.head())
        elif st.button("Tail"):
            st.write(data.tail())

# Show Column Name
if st.checkbox ("Column Name"):
        data=df1
        st.write(data.columns)
        

st.subheader("Choose a Score")
pages_names = ("CGPA","TOEFL Score", "GRE Score")
page=st.radio('Navigation',pages_names)




if page == "CGPA" :
 st.subheader("Chance of Admit by CGPA ")
 ax=px.scatter(df1,x="CGPA",y="Chance of Admit ", color="LOR ", size_max=10, hover_name="Serial No.")
 st.plotly_chart(ax, use_container_width=True)
if page =="TOEFL Score" :
    st.subheader("Chance of Admit by TOEFL Score ")
    ax=px.scatter(df1,x="TOEFL Score",y="Chance of Admit ", color="LOR ", size_max=10, hover_name="Serial No.")
    st.plotly_chart(ax, use_container_width=True)
if page ==  "GRE Score" :
    st.subheader("Chance of Admit by GRE Score ")
    ax=px.scatter(df1,x="GRE Score",y="Chance of Admit ", color="LOR ", size_max=10, hover_name="Serial No.")
    st.plotly_chart(ax, use_container_width=True)

st.write('<p style="font-size:130%">This scatter plots shows the variation of chance of admission according to the exams scores </p>', unsafe_allow_html=True)



st.title("Life Expectancy Dataset")
df3=pd.read_csv(r"C:\Users\BC\Downloads\Life_expectancy_dataset.csv",encoding='latin-1')

if st.checkbox('Show Life Expectancy Data'):
    st.subheader('Life Expectancy Data')
    st.write(df3)

df4=df3.groupby("Continent",as_index=False)[["Overall Life","Male Life", "Female Life"]].mean()


st.subheader("Life Expectancy by Continent")

select = st.selectbox('Select a Continent',df4['Continent'])

#get the state selected in the selectbox
state_data = df4[df4['Continent'] == select]



def get_total_dataframe(dataset):
    total_dataframe = pd.DataFrame({
    'Status':['Overall Life', 'Male Life', 'Female Life'],
    'Number of cases':(dataset.iloc[0]['Overall Life'],
    dataset.iloc[0]['Male Life'], 
    dataset.iloc[0]['Female Life'])})
    return total_dataframe
state_total = get_total_dataframe(state_data)

#if st.checkbox("Show Analysis by Continent", True, key=2):
st.markdown("## **Level analysis**" + " in %s " % (select))
#st.markdown("### Overall Life, Male Life ,and Female Life " +
   # " in %s " % (select))
   # if not st.checkbox('Hide Graph', False, key=1):
state_total_graph = px.bar(
        state_total, 
        x='Status',
        y='Number of cases',
        labels={'Number of cases':'Number of cases in %s' % (select)},
        color='Status')
st.plotly_chart(state_total_graph, use_container_width=True)

st.write('<p style="font-size:130%">This bar graph shows the overall , male, and female life expectancy in each continent </p>', unsafe_allow_html=True)
