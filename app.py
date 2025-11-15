iimport streamlit as st
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
    display += "▼ 장애물
