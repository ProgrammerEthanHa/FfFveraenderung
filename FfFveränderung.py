import streamlit as st
import pandas as pd
import altair as alt

st.header("Kann Fridays for Future etwas verändern?")
st.subheader("Glaubst du, dass die Bewegung etwas verändert?")

source = pd.DataFrame({
        'Anteil(%)': [26, 51, 23],
        'Antwort': ['Nein', 'Ja', 'Kann ich nicht einschätzen']
     })
 
bar_chart = alt.Chart(source).mark_bar().encode(
        y='Anteil(%):Q',
        x='Antwort:O',
    )
st.altair_chart(bar_chart, use_container_width=True)


txt = st.text_area('', '''
    Basis n=1002; Nur Jugendliche, die FfF kennen
    ''')
st.text("Klicke an die Balken um die Daten genauer anzuschauen. Du kannst auch die Diagramm vergrößern und ein Bild davon machen")
st.text("Quelle: SINUS-Institut")