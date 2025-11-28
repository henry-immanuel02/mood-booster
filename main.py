# Cheer-up Streamlit app (English + 中文混合)
# Save as: cheer_up_wife_streamlit.py
# Run: streamlit run cheer_up_wife_streamlit.py

import streamlit as st
import random

st.set_page_config(page_title="Mood Booster 💌", page_icon="💖", layout="centered")

jokes = [
    "Why is rice never badmood? Because it always has side dishes. 米饭永远不孤单！🍚",
    "Clouds are romantic because they always wait for the sunset. 云朵超会谈恋爱。☁️🌇",
    "Your mood offline only. Try reboot your heart? 重启一下心情吧~ 🔁",
    "You're like WiFi — when your signal strong, my world peaceful. 📶💖",
    "Time: 'What time is it?' Me: 'Time to love you.' 时间：是爱你的时间。😏"
]

compliments = [
    "You look cute even without filters. 天生自带滤镜。",
    "Your smile works better than morning coffee. 你的笑比咖啡更提神。",
    "You + calm energy = unbeatable. 你很稳，我更稳。",
    "When you're angry, still adorable. 生气也很好看。",
    "You are the whole package. 完整配置。"
]

excuses = [
    "Sorry, I misplaced my mood today. 今天把心情忘在办公室了。",
    "I promise to improve — like, seriously. 我会努力升级的。",
    "I forgot to celebrate how lucky I am to have you. 忘了感恩你。抱一下补回。",
]

st.markdown("**Made with love by Henry ❤️ (来自 Henry 的心意)**")

st.title("Mood Booster for My Lovely Wife 💌 妻子的快乐加油站")
st.subheader("Click the buttons to heal your mood. 点点按钮，快乐多一点。")

st.markdown("### Choose your booster 选择你的心情补给:")

if st.button("🎭 Joke / 笑话"):
    st.markdown(f"**{random.choice(jokes)}**")

if st.button("🌸 Compliment / 夸夸你"):
    st.markdown(f"**{random.choice(compliments)}**")

if st.button("🧸 Cute Cat / 可爱小猫"):
    st.image("https://placekitten.com/600/400", caption="If this doesn't work, I'll find cuter cats. 如果没笑，我再换更可爱的猫。")

if st.button("🙇 Apology / 道歉"):
    st.markdown(f"**Sorry my love. 对不起宝贝。{random.choice(excuses)}**")
    st.balloons()

if st.button("🎵 Chill / 放松一下"):
    st.write("Take a deep breath... inhale... exhale... 深呼吸一下，轻松一点。")
    st.write("Ice cream available upon request. 想吃冰淇淋我请你。")

st.divider()

st.header("Forgiveness Generator 原谅生成器 ⚙️")
name_from = st.text_input("Sender 发件人", "Your husband 你的老公")
reason = st.text_input("Why apologizing 道歉理由", "being silly 太笨了")

if st.button("Generate Letter 生成小信件"):
    text = [
        f"Hey love, this is {name_from}. 这是我。",
        f"Sorry because {reason}. 对不起因为 {reason}。",
        "You can stay upset for a bit, but I'm here ready with hugs. 你生气我抱抱。",
        "Signature: a kiss & a promise. 签名：亲亲 + 改进承诺。💋",
    ]
    st.markdown("

".join(["**" + t + "**" for t in text]))
    st.balloons()

st.caption("Made with love & panic. 带着爱和一点慌张做的。")
