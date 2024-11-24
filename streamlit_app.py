import streamlit as st
from dotenv import load_dotenv
from main import get_response  # main.py dosyasındaki fonksiyonu import ediyoruz

# .env dosyasını yükle
load_dotenv()

# Streamlit için başlık ve açıklamalar
st.set_page_config(page_title="LangGraph-Mystic", page_icon="🌙")
st.title("LangGraph-Mystic - Rüya Yorumlayıcı")

# Konuşma geçmişi için bir oturum durumu oluşturuyoruz (session state)
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Kullanıcının sorusunu girmesi için bir mesaj kutusu
user_query = st.text_input("Rüyanız nedir?", key="user_input")

# Eğer kullanıcı bir soru girdiyse, yanıt al
if user_query:
    # Kullanıcı sorusunu chat geçmişine ekleyelim
    st.session_state.chat_history.append({"role": "human", "message": user_query})

    # Uygulamanın yanıtını alıyoruz (input'u doğru formatta gönderiyoruz)
    response = get_response(user_query)  # Burada sadece user_query'yi geçiyoruz

    # Yanıtı chat geçmişine ekleyelim
    st.session_state.chat_history.append({"role": "ai", "message": response})


# Konuşma geçmişini ekranda göster
for chat in st.session_state.chat_history:
    if chat["role"] == "human":
        with st.chat_message("human"):
            st.markdown(chat["message"])
    else:
        with st.chat_message("ai"):
            st.markdown(chat["message"])
