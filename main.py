import streamlit as st
from pages.regression import mainRegression
from st_pages import show_pages_from_config

# --- Page Content Functions ---
def home_page():
    mainRegression()

def tutorial_page():
    st.title("Tutorial")
    st.write("This is the Tutorial page. Add your tutorial content here.")  # Placeholder

def about_us_page():
    st.title("About Us")
    st.write("This is the About Us page. Tell users about your team/project.")  # Placeholder

# --- Main App ---
def main():
    # Theme is now applied within mainRegression() (assuming it's handled there)

    # Sidebar Navigation
    st.sidebar.title("Menu")
    selection = st.sidebar.radio("Navigate to", ["Home", "Tutorial", "About Us"])  # Updated labels

    # Display Selected Page
    if selection == "Home":
        home_page()
    elif selection == "Tutorial":
        tutorial_page()
    elif selection == "About Us":
        about_us_page()

if __name__ == "__main__":
    main()
