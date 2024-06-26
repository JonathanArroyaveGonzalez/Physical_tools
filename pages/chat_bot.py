

import streamlit as st

pg = st.navigation([st.Page("example.py"),st.Page("example2.py")])

st.sidebar.selectbox("Group", ["A","B","C"], key="group")
st.sidebar.slider("Size", 1, 5, key="size")

pg.run()