import streamlit as st
import time

# --- Page Configuration ---
st.set_page_config(page_title="For My Love Ishta ❤️", page_icon="💖", layout="wide")

# --- BGM aur Styles (Isse screen blank nahi hogi) ---
st.markdown("""
    <style>
    /* Music player ko hidden rakhne ke liye */
    .hidden-audio {
        display: none;
    }
    .stApp { background-color: #fff5f5; }
    .stButton>button {
        background-color: #FF69B4;
        color: white;
        border-radius: 20px;
        font-weight: bold;
        width: 100%;
        border: none;
        padding: 10px;
    }
    /* Falling Hearts Animation */
    @keyframes hearts-fall {
        0% { top: -10%; transform: translateX(0) rotate(0deg); }
        100% { top: 100%; transform: translateX(100px) rotate(360deg); }
    }
    .heart {
        position: fixed;
        color: #ff4b4b;
        font-size: 25px;
        user-select: none;
        z-index: 1000;
        animation: hearts-fall 4s linear infinite;
    }
    </style>
    """, unsafe_allow_html=True)

# Falling hearts function
def falling_hearts():
    heart_html = ""
    for i in range(25):
        left = (i * 7) % 100
        delay = i * 0.3
        heart_html += f'<div class="heart" style="left: {left}%; animation-delay: {delay}s;">❤️</div>'
    st.markdown(heart_html, unsafe_allow_html=True)

# --- Session State ---
if 'page' not in st.session_state:
    st.session_state.page = 'envelope_back'

# --- Music Logic (Sirf start ke baad bajega) ---
if st.session_state.page != 'envelope_back' and st.session_state.page != 'angry_teddy':
    # Ye YouTube link music play karega bina screen disturb kiye
    st.markdown('<div class="hidden-audio"><iframe width="0" height="0" src="https://www.youtube.com/embed/H5v3kku4y6Q?autoplay=1&loop=1&playlist=H5v3kku4y6Q" frameborder="0" allow="autoplay"></iframe></div>', unsafe_allow_html=True)

# --- 1. Envelope Page ---
if st.session_state.page == 'envelope_back':
    st.image("https://ih1.redbubble.net/image.1118155160.0784/st,small,507x507-pad,600x600,f8f8f8.jpg", use_container_width=True) 
    st.image("https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExaTAwYTN6ZjEweHRucGl3bzQwOThzc2MybTczdXBubTRzOWl5eGR1MiZlcD12MV9naWZzX3NlYXJjaCZjdD1n/eDYW3Ey6iuL4YLo9PO/giphy.gif", width=150) 
    st.markdown("<h2 style='text-align: center;'>Pls accept the gift Ishri Pishri ❤️</h2>", unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    with col1:
        if st.button("YES ✅"):
            st.session_state.page = 'gift_selection'
            st.rerun()
    with col2:
        if st.button("NO ❌"):
            st.session_state.page = 'angry_teddy'
            st.rerun()

# --- 2. Angry Teddy ---
elif st.session_state.page == 'angry_teddy':
    st.image("https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExaTAwYTN6ZjEweHRucGl3bzQwOThzc2MybTczdXBubTRzOWl5eGR1MiZlcD12MV9naWZzX3NlYXJjaCZjdD1n/eabb0SQsYllO0DxAqF/giphy.gif", width=300) 
    st.header("Why did u click NO?? 😠")
    if st.button("Try Again"):
        st.session_state.page = 'envelope_back'
        st.rerun()

# --- 3. Gift Selection ---
elif st.session_state.page == 'gift_selection':
    st.header("Gift for you! 🎁")
    st.write("Click any gift to open:")
    col1, col2, col3 = st.columns(3)
    box_url = "https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExMWJlMHB0bHI3c291ejVoeHdoMW9sMHFkYXV3M3JueXljNmQ3cWJkMSZlcD12MV9naWZzX3NlYXJjaCZjdD1n/VIe5NOnlPxJ9FcONBq/giphy.gif"
    
    with col1:
        st.image(box_url)
        if st.button("🎁 Gift 1"):
            st.session_state.page = 'gift1'
            st.rerun()
    with col2:
        st.image(box_url)
        if st.button("🎁 Gift 2"):
            st.session_state.page = 'gift2'
            st.rerun()
    with col3:
        st.image(box_url)
        if st.button("🎁 Gift 3"):
            st.session_state.page = 'gift3'
            st.rerun()

# --- Box 1: New Year Wish ---
elif st.session_state.page == 'gift1':
    placeholder = st.empty()
    for i in range(3, 0, -1):
        placeholder.title(f"Opening in... {i}")
        time.sleep(1)
    placeholder.empty()
    st.balloons()
    st.title("HAPPY NEW YEAR MY LOVE! 🎊")
    st.image("https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExb3RoZHMzM204ZzF1bTAyczNjbDN0ajlvNHN2NG91OThpdml5OG9scSZlcD12MV9naWZzX3NlYXJjaCZjdD1n/8oTQu4lwKLrsA/giphy.gif", width=400)
    st.write("Har saal bas ek hi dua hai — tum mere saath raho. Let's make this year amazing! ❤️")
    if st.button("Back"):
        st.session_state.page = 'gift_selection'
        st.rerun()

# --- Box 2: Certificate ---
elif st.session_state.page == 'gift2':
    st.markdown(f"""
        <div style="border: 10px solid #FFD700; padding: 30px; text-align: center; background-color: white; border-radius: 15px; font-family: 'Georgia';">
            <h1 style="color: #FF4B4B; margin-bottom: 10px;">🏆 OFFICIAL CERTIFICATE 🏆</h1>
            <hr style="border: 1px solid #eee;">
            <p style="font-size: 20px; color: #555;">This is proudly presented to:</p>
            <h1 style="color: #2c3e50; text-decoration: underline;">Ishta Pathak</h1>
            <p style="font-size: 22px; color: #555; font-style: italic;">For being the</p>
            <h2 style="color: #FF4B4B;">✨ WORLD'S BEST BOYFRIEND ✨</h2>
            <p style="font-size: 18px; color: #7f8c8d;">Issued by: Diksha ❤️</p>
        </div>
    """, unsafe_allow_html=True)
    if st.button("Back to Gifts 🔙"):
        st.session_state.page = 'gift_selection'
        st.rerun()

# --- Box 3: Donkey ---
elif st.session_state.page == 'gift3':
    st.image("https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExaTAwYTN6ZjEweHRucGl3bzQwOThzc2MybTczdXBubTRzOWl5eGR1MiZlcD12MV9naWZzX3NlYXJjaCZjdD1n/Ie4CIIvQS0bk3zwZlM/giphy.gif")
    st.header("Yahi hone wala h tmare sath,smjhe buddhu gadhe itna gift mil gya phir bhi aa gye or gift lene 😂")
    if st.button("Aage Badho"):
        st.session_state.page = 'kiss_page'
        st.rerun()

# --- 4. Kiss ---
elif st.session_state.page == 'kiss_page':
    st.image("https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExaTAwYTN6ZjEweHRucGl3bzQwOThzc2MybTczdXBubTRzOWl5eGR1MiZlcD12MV9naWZzX3NlYXJjaCZjdD1n/L2CGLm2BRDOXCe1uKz/giphy.gif", width=400)
    if st.button("💋 Click for Kiss"):
        st.audio("https://www.myinstants.com/media/sounds/mwah.mp3", autoplay=True)
        st.session_state.page = 'final_para'
        st.rerun()

# --- 5. Final Page (Hearts Falling) ---
elif st.session_state.page == 'final_para':
    falling_hearts() 
    st.write("""
    ### My Jaan,
    In this new year, I promise to love you even more. You are my happiness and my whole world. 
    Thank you for being mine. Thank you so much for coming in my life ishuu....
    
    **I love u so much Ishri Pishri ❤️**
    """)
    if st.button("Restart ❤️"):
        st.session_state.page = 'envelope_back'
        st.rerun()
