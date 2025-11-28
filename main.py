# FINAL CLEAN VERSION — FOR WORK-RELATED BAD MOOD (NO SYNTAX ERRORS)
# Save as: mood_booster.py
# Run: streamlit run mood_booster.py

import streamlit as st
import random

st.set_page_config(page_title="Mood Booster 💌", page_icon="💖", layout="centered")

# ------------------ HEADER ------------------
st.markdown("""
<div style='text-align:center; font-size:24px; font-weight:600; margin-top:10px;'>
    Made with ❤️ by Henry<br>来自 Henry 的心意
</div>
""", unsafe_allow_html=True)

# ------------------ DATA ------------------
jokes = [
    "Work stressful? Here's a joke: Why don't programmers like nature? Too many bugs. 自然界太多 bug。😂",
    "Clouds are romantic because they wait for sunset. You should rest too. 🌇",
    "Your mood offline only. Try reboot your heart? 重启一下心情吧~ 🔁",
    "You're like WiFi — when your signal strong, my world peaceful. 📶💖",
]

comforts = [
    "You're doing amazing, even if today feels heavy. 今天真的辛苦你了。",
    "You deserve rest, not stress. 你值得好好休息。",
    "Work tough, but you tougher. 工作难，你更强。",
    "Even warriors need breaks — you're one of them. 战士也要休息。",
]

warm_words = [
    "I’m here to cheer for you. 我在这边给你打气。",
    "Take your time, breathe, I'm with you. 慢慢来，我陪着你。",
    "It’s okay to feel tired. 今天可以不坚强。",
]

# ------------------ UI ------------------
st.title("Mood Booster for My Lovely Wife, Keff Chan💌 妻子的心情加油站")
st.subheader("Your work is tough — let me lighten it a bit. 工作累了，让我来逗你笑。")

st.markdown("### Choose your booster 选择你的心情补给:")

if st.button("🎭 Joke / 笑一下"):
    st.markdown(f"**{random.choice(jokes)}**")

if st.button("🌸 Comfort / 安慰你"):
    st.markdown(f"**{random.choice(comforts)}**")

if st.button("🧸 Cute Cat / 小猫治愈"):
    st.image("https://placekitten.com/600/400", caption="Cat therapy activated. 猫咪治疗启动。🐾")

if st.button("💛 Warm Words / 暖心话"):
    st.markdown(f"**{random.choice(warm_words)}**")
    st.balloons()

if st.button("🎵 Chill / 放松一下"):
    st.write("Inhale... exhale... 深呼吸。你可以休息一下。")
    st.write("I’ll get you snacks if needed. 想吃什么我去买。")

st.divider()

# ------------------ Encouragement Letter ------------------
st.header("Encouragement Generator 鼓励生成器 ⚙️")

name_from = st.text_input("Sender 发件人", "Henry")
reason = st.text_input("Reason 理由", "you had a tough workday 工作太累了")

if st.button("Generate Letter 生成小信"):
    text = [
        f"Hey love, it's {name_from}. 这是我。",
        f"I know today was hard because {reason}. 今天真的不容易。",
        "I'm proud of you for getting through it. 我以你为荣。",
        "Come here, let me comfort you. 抱一个吧。💛",
    ]
    st.markdown("\n\n".join([f"**{t}**" for t in text]))
    st.balloons()

st.caption("Made with love, care, and zero syntax errors. 🧸💛")
