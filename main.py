import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(layout="wide")

dropdown_options = ["min(1 less OR cap 15)", "min(2 less OR cap 14)", "min(2 less OR cap 13)", "cap 20",
                    "1 less", "none"]

with st.form("input_form"):
    with st.container(border=True):
        col1, col2, col3 = st.columns(3, gap="large")
        with col1:
            st.write("**North Tower**")
            n_5n_vas = st.selectbox("5N Vascular", dropdown_options, index=None)
            n_5n_vasnbt = st.selectbox("5N Vascular/ NBT overflow", dropdown_options, index=None)
            n_7n_heart_1 = st.selectbox("7N Heart Failure 1", dropdown_options, index=None)
            n_7n_heart_2 = st.selectbox("7N Heart Failure 2", dropdown_options, index=None)
            n_8n_neuro = st.selectbox("8N Neuro/Trauma Stepdown", dropdown_options, index=None)
            n_10n_neuro = st.selectbox("10N Neurostroke", dropdown_options, index=None)
            n_10n_overflow = st.selectbox("10N overflow/Beds N1029-32", dropdown_options, index=None)
            n_11n_gen = st.selectbox("11N Gen Surg/Trauma/Bariatrics", dropdown_options, index=None)
            n_12n_ortho = st.selectbox("12N Ortho and Spine Trauma", dropdown_options, index=None)
            n_14n_ortho = st.selectbox("14N Ortho and Spine Elective", dropdown_options, index=None)
        with col2:
            st.write("**South Tower**")
            s_2c_obs = st.selectbox("2C OBS unit", dropdown_options, index=None)
            s_3c_icc = st.selectbox("3C ICC", dropdown_options, index=None)
            s_5a_med = st.selectbox("5A Med/Surg", dropdown_options, index=None)
            s_5c_med_1 = st.selectbox("5C Med/Surg 1", dropdown_options, index=None)
            s_5c_med_2 = st.selectbox("5C Med/Surg 2", dropdown_options, index=None)
            s_6a_med = st.selectbox("6A Medical PCU", dropdown_options, index=None)
            s_6c_med = st.selectbox("6C Medical PCU", dropdown_options, index=None)
            s_7c_neuro = st.selectbox("7C Neuro Med/Surg", dropdown_options, index=None)
            s_8a_med = st.selectbox("8A Medical PCU", dropdown_options, index=None)
            s_8c_med = st.selectbox("8C Medical PCU", dropdown_options, index=None)
            s_8a8c_med = st.selectbox("8A/8C Medical PCU/ 2c/3c overflow", dropdown_options, index=None)
        with col3:
            st.write("**LP Tower/B-Wing**")
            lp_7a_cardiac = st.selectbox("7A Cardiac PCU/ 5B/7B overflow", dropdown_options, index=None)
            lp_7lp_med = st.selectbox("7LP Medical Oncology", dropdown_options, index=None)
            lp_8lp_bmt = st.selectbox("8LP BMT", dropdown_options, index=None)
            lp_9lp_surg = st.selectbox("9LP Surgical Oncology", dropdown_options, index=None)
            lp_10lp_colo = st.selectbox("10LP Colorectal Surgery and Surg Onc", dropdown_options, index=None)
            lp_11lp_dhi = st.selectbox("11LP DHI / Urology", dropdown_options, index=None)
            lp_11lp_dhiover = st.selectbox("11LP DHI overflow", dropdown_options, index=None)
            lp_5b_cardiac = st.selectbox("5B Cardiac Intervention", dropdown_options, index=None)
            lp_7b_cardiac = st.selectbox("7B Cardiac Stepdown", dropdown_options, index=None)

    # Every form must have a submit button.
    submitted = st.form_submit_button("Submit")
    if submitted:
        col1, col2, col3 = st.columns(3, gap="large")
        with col1:
            st.write("**North Tower**")
            n_df = pd.DataFrame(
                {
                    "name": ["5N Vascular", "5N Vascular/ NBT overflow", "7N Heart Failure 1", "7N Heart Failure 2",
                             "8N Neuro/Trauma Stepdown", "10N Neurostroke", "10N overflow/Beds N1029-32",
                             "11N Gen Surg/Trauma/Bariatrics", "12N Ortho and Spine Trauma",
                             "14N Ortho and Spine Elective"],
                    "count": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
                }
            )
            st.dataframe(
                n_df,
                column_config={
                    "name": "Patient Unit",
                    "count": "# Patients"
                },
                hide_index=True,
            )
        with col2:
            st.write("**South Tower**")
            s_df = pd.DataFrame(
                {
                    "name": ["2C OBS unit", "3C ICC", "5A Med/Surg", "5C Med/Surg 1", "5C Med/Surg 2",
                             "6A Medical PCU", "6C Medical PCU", "7C Neuro Med/Surg", "8A Medical PCU",
                             "8C Medical PCU", "8A/8C Medical PCU/ 2c/3c overflow"],
                    "count": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11],
                }
            )
            st.dataframe(
                s_df,
                column_config={
                    "name": "Patient Unit",
                    "count": "# Patients"
                },
                hide_index=True,
                height=int(35.2*(11+1))
            )
        with col3:
            st.write("**LP Tower/B-Wing**")
            lp_df = pd.DataFrame(
                {
                    "name": ["7A Cardiac PCU/ 5B/7B overflow", "7LP Medical Oncology", "8LP BMT",
                             "9LP Surgical Oncology", "10LP Colorectal Surgery and Surg Onc",
                             "11LP DHI / Urology", "11LP DHI overflow", "5B Cardiac Intervention",
                             "7B Cardiac Stepdown"],
                    "count": [1, 2, 3, 4, 5, 6, 7, 8, 9],
                }
            )
            st.dataframe(
                lp_df,
                column_config={
                    "name": "Patient Unit",
                    "count": "# Patients"
                },
                hide_index=True,
            )
