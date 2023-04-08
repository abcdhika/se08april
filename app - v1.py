#library
import streamlit as st

#write
st.title ('software perkalian')
st.subheader ('ini adalah aplikasi untuk mengalikan bilangan bulat')

#input bilangan pertama
number1 = st.number_input ('masukkan bilangan pertama')
st.write (f'Bilangan pertama adalah {number1}')

#input bilangan pertama
number2 = st.number_input ('masukkan bilangan kedua')
st.write (f'Bilangan kedua adalah {number2}')

#hasil kali
hasil = number1*number2

#tombol
if st.button ('Hitung'):
    st.write (f'Hasil kali antara {number1} dan {number2} adalah {hasil}')
else:
    st.write ('silakan tekan tombol hitung!')