import streamlit as st
import pandas as pd
from datetime import date

def load_journal():
    try:
        journal_data = pd.read_csv('journal.csv')
    except FileNotFoundError:
        journal_data = pd.DataFrame({'Date': [], 'Entry': []})
    return journal_data

def save_journal(journal_data):
    journal_data.to_csv('journal.csv', index=False)


st.title('Daily Journal App')
st.write('Write your daily journal entries here!')

# Load the existing journal data or create an empty dataframe
journal_data = load_journal()

# Display existing journal entries
st.subheader('Existing Journal Entries:')
st.dataframe(journal_data)

# Add new entry
st.subheader('Add New Entry:')
new_entry_date = st.date_input('Date', date.today())
new_entry_text = st.text_area('Journal Entry')

if st.button('Add Entry'):
    if new_entry_text:
        new_entry = pd.DataFrame({'Date': [new_entry_date], 'Entry': [new_entry_text]})
        journal_data = pd.concat([journal_data, new_entry], ignore_index=True)
        save_journal(journal_data)
        st.success('Entry added successfully!')
    else:
        st.warning('Entry text cannot be empty!')

# Delete all entries
if st.button('Clear All Entries'):
    journal_data = pd.DataFrame({'Date': [], 'Entry': []})
    save_journal(journal_data)
    st.success('All entries cleared!')
