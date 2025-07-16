import streamlit as st
import random

# -----------------------
# 응원 메시지 리스트
# -----------------------
messages = [
    "🍓 아롬아! 오늘도 충분히 잘하고 있어. 돼끼는 늘 응원해!",
    "🍑 힘들 땐 잠깐 쉬어가도 괜찮아. 돼끼는 항상 네 편이야!",
    "🍉 회사는 회사고, 아롬이는 소중한 존재야. 잊지 말기!",
    "🍒 작지만 확실한 성취들, 돼끼는 다 보고 있어! 잘하고 있어!",
    "🍋 오늘도 출근한 너, 너무 대단해. 진심으로 응원해!",
    "🥝 사람들에게 친절한 아롬이, 자신에게도 조금 더 친절해줘!",
    "🍇 힘들었던 하루 끝에 돼끼가 보낸 포근한 위로 한 스푼 💌",
    "🍊 일은 잠깐 잊고, 돼끼랑 웃어보자! 아롬이는 빛나는 사람이야!",
    "🍏 모두가 아롬이를 몰라도 돼끼는 알아. 넌 진짜 멋져!",
    "🥥 오늘도 무사히 버틴 너에게, 돼끼가 주는 칭찬 한 박스 🎁"
]

# -----------------------
# 앱 설정 및 초기화
# -----------------------
st.set_page_config(page_title="돼끼의 응원편지", page_icon="🐷")
st.title("🐷 돼끼의 응원편지")
st.write("친구 아롬이를 위한 💌 돼끼의 랜덤 응원 메시지를 받아보세요!")

# -----------------------
# 세션 상태를 통한 메시지 관리
# -----------------------
if "current_message" not in st.session_state:
    st.session_state.current_message = ""

# -----------------------
# 버튼 동작 정의
# -----------------------
def get_new_message():
    st.session_state.current_message = random.choice(messages)

# -----------------------
# 버튼 UI
# -----------------------
if st.session_state.current_message == "":
    if st.button("💌 돼끼의 편지 받기"):
        get_new_message()
else:
    st.success(st.session_state.current_message)
    if st.button("🔁 또다른 메시지 받기"):
        get_new_message()

