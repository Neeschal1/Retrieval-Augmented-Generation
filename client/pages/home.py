import streamlit as st
from ui.home.page_config import page_config
from ui.home.hero import hero_section
from ui.home.description import description_section
from ui.home.features import features_section
from ui.home.cta import cta_section
from constants.footer import footer

page_config()
hero_section()
st.divider()
description_section()
st.divider()
features_section()
st.divider()
cta_section()
st.divider()
footer()