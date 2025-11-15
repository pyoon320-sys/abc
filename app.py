import streamlit as st
import random
import time

st.set_page_config(page_title="러너 게임", layout="centered")
st.title("🏃 러너 게임 (Temple Run 간단 버전)")

# 초기화
if "player_pos" not in st.session_state:
    st.session_state.player_pos = 1  # 0=왼쪽, 1=중앙, 2=오른쪽

if "obstacles" not in st.session_state:
    st.session_state.obstacles = []  # (lane)
    
if "score" not in st.session_state:
    st.session_state.score = 0

if "game_over" not in st.session_state:
    st.session_state.game_over = False

# 장애물 생성
def spawn_obstacle():
    lane = random.choice([0,1,2])
    st.session_state.obstacles.append(lane)

# 장애물 진행
def update_obstacles():
    if len(st.session_state.obstacles) > 6:
        st.session_state.obstacles.pop(0)

# 충돌 체크
def check_collision():
    if len(st.session_state.obstacles) > 0:
        last_lane = st.session_state.obstacles[-1]
        if last_lane == st.session_state.player_pos:
            st.session_state.game_over = True

# 게임 화면 출력
def render_game():
    display = ""

    lanes = ["⬜", "⬜", "⬜"]
    lanes[st.session_state.player_pos] = "🙂"

    display += " | ".join(lanes) + "\n\n"
    display += "▼ 장애물 ▼\n"

    # 장애물 표시
    for i, lane in enumerate(reversed(st.session_state.obstacles)):
        row = [" ", " ", " "]
        row[lane] = "⬛"
        display += " | ".join(row) + "\n"

    st.text(display)

# 버튼 UI
col1, col2, col3 = st.columns(3)

with col1:
    if st.button("⬅️ 왼쪽"):
        st.session_state.player_pos = max(0, st.session_state.player_pos - 1)

with col3:
    if st.button("➡️ 오른쪽"):
        st.session_state.player_pos = min(2, st.session_state.player_pos + 1)

# 게임 루프
if not st.session_state.game_over:
    spawn_obstacle()
    update_obstacles()
    check_collision()
    st.session_state.score += 1

render_game()

st.write(f"🏆 점수: **{st.session_state.score}**")

if st.session_state.game_over:
    st.error("💥 충돌! 게임 오버!")
    if st.button("다시 시작"):
        st.session_state.player_pos = 1
        st.session_state.obstacles = []
        st.session_state.score = 0
        st.session_state.game_over = False
