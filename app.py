import streamlit as st
import pandas as pd
import numpy as np


## Welcome
# st.write("Hello World!")


## table
# st.write("Here's our first attempt at using data to create a table:")
# st.write(pd.DataFrame({
#     'first column': [1, 2, 3, 4],
#     'second column': [10, 20, 30, 40]
# }))


## chart
# chart_data = pd.DataFrame(
#      np.random.randn(20, 3),
#      columns=['a', 'b', 'c'])

# st.line_chart(chart_data)

## slider
x = st.slider('x')  # 👈 this is a widget
st.write(x, 'squared is', x * x)


## text input
# st.text_input("Your name", key="name")

# # You can access the value at any point with:
# st.write(f"Hello {st.session_state.name}")


## checkbox
# if st.checkbox('Show dataframe'):
#     chart_data = pd.DataFrame(
#        np.random.randn(20, 3),
#        columns=['a', 'b', 'c'])

#     chart_data


## sidebar
# # Add a selectbox to the sidebar:
# add_selectbox = st.sidebar.selectbox(
#     'How would you like to be contacted?',
#     ('Email', 'Home phone', 'Mobile phone')
# )

# # Add a slider to the sidebar:
# add_slider = st.sidebar.slider(
#     'Select a range of values',
#     0.0, 100.0, (25.0, 75.0)
# )


## layout
# left_column, right_column = st.columns(2)
# # You can use a column just like st.sidebar:
# left_column.button('Press me!')

# # Or even better, call Streamlit functions inside a "with" block:
# with right_column:
#     chosen = st.radio(
#         'Language',
#         ("Python", "C++", "Java", "R"))
#     st.write(f"You selected {chosen}.")
