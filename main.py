import streamlit as st
import random

# ==============================
# PAGE CONFIG
# ==============================
st.set_page_config(page_title="A Wild Request Appears!", page_icon="❤️")

# ==============================
# SESSION STATE
# ==============================
if "answered_yes" not in st.session_state:
    st.session_state.answered_yes = False

if "nay_count" not in st.session_state:
    st.session_state.nay_count = 0

# ==============================
# VALENTINE GATE
# ==============================
if not st.session_state.answered_yes:
    st.title("💌 A Special Message...")
    st.subheader("I have an important question for you.")

    # 🔥 EXPONENTIAL GROWTH
    scale = 1.25 ** st.session_state.nay_count
    yay_font = 24 + (st.session_state.nay_count * 12)
    yay_padding = 12 + (st.session_state.nay_count * 8)
    nay_font = max(16 - (st.session_state.nay_count * 2), 1)
    nay_opacity = max(1 - (st.session_state.nay_count * 0.15), 0.05)

    # PERBAIKAN: Pastikan string HTML rata kiri di dalam st.markdown
    st.markdown(f"""
<style>
    div[data-testid="stButton"] button {{
        transition: all 0.2s ease-in-out;
    }}
    div[data-testid="stButton"] button[kind="primary"] {{
        font-size: {yay_font}px !important;
        padding: {yay_padding}px {yay_padding*2}px !important;
        transform: scale({scale});
        background-color: #ff4b4b !important;
        color: white !important;
        border: 3px solid white !important;
        border-radius: 15px !important;
    }}
    .nay-btn-style button {{
        font-size: {nay_font}px !important;
        opacity: {nay_opacity};
        background-color: #808080 !important;
        border-radius: 10px !important;
    }}
</style>
""", unsafe_allow_html=True)

    st.write("### Do you want to be my Valentine?")
    col_yay, col_nay_area = st.columns([2, 1])

    with col_yay:
        if st.button(f"YES{'!' * st.session_state.nay_count}", key="yay_btn", type="primary"):
            st.session_state.answered_yes = True
            st.balloons()
            st.rerun()

    with col_nay_area:
        for _ in range(random.randint(0, 15)):
            st.write("")
        inner_cols = st.columns([1, 1, 1])
        with inner_cols[random.randint(0, 2)]:
            st.markdown('<div class="nay-btn-style">', unsafe_allow_html=True)
            if st.button("Nay", key="nay_btn"):
                st.session_state.nay_count += 1
                st.rerun()
            st.markdown("</div>", unsafe_allow_html=True)

# ==============================
# AFTER YES
# ==============================
else:
    st.balloons()
    st.title("Pokémon Valentine's Quest")
    st.success("Successfully Caught! You are now in my Party forever.")

    # PERBAIKAN: HTML juga diratakan kiri
    st.markdown("""
<div style="background-color: white; padding: 20px; border-radius: 15px; border: 4px solid #ffde00; box-shadow: 0 4px 12px rgba(0,0,0,0.2);">
    <h3 style="color: black; margin-bottom:10px;">Keff Chan The Elite Trainer Profile</h3>
    <p style="color: black; font-size:16px;"><b>Status:</b> Level 100 Boyfriend</p>
    <p style="color: black; font-size:16px;"><b>Ability:</b> Best Hugs / Always Cute and Horny :p</p>
</div>
""", unsafe_allow_html=True)

    st.write("---")
    if st.button("Open your Valentine Gift 🎁"):
        st.success("I love you more than Pikachu loves Ketchup!")
        # Pastikan file gambar ada di folder yang sama
        try:
            st.image("me and keff.jpeg", caption="You caught my heart! ❤️", width=700)
        except:
            st.warning("Gambar 'me and keff.jpeg' tidak ditemukan.")
        st.write("It's me again! I am the gifttt, our love story has been extended forever")

    st.write("---")
    st.caption("Made with ❤️ for my favorite Trainer.")
