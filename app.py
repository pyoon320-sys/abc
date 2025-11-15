import streamlit as st

st.title("🧩 미로 탈출 게임")

# 미로(벽=1, 길=0, 목표=2)
maze = [
    [1,1,1,1,1,1,1],
    [1,0,0,0,1,0,1],
    [1,0,1,0,0,0,1],
    [1,0,1,1,1,0,1],
    [1,0,0,0,1,0,1],
    [1,1,1,0,0,2,1],
    [1,1,1,1,1,1,1]
]

# 플레이어 시작 위치
if "player" not in st.session_state:
    st.session_state.player = [1,1]  # (y,x)

player_y, player_x = st.session_state.player

# 미로 출력
def draw_maze():
    display = ""
    for y, row in enumerate(maze):
        for x, cell in enumerate(row):
            if [y,x] == st.session_state.player:
                display += "🙂 "         # 플레이어 위치
            elif cell == 1:
                display += "⬛ "         # 벽
            elif cell == 2:
                display += "🏁 "         # 목표
            else:
                display += "⬜ "
        display += "\n"
    st.text(display)

draw_maze()

# 이동 함수
def move(dy, dx):
    new_y = st.session_state.player[0] + dy
    new_x = st.session_state.player[1] + dx

    if maze[new_y][new_x] != 1:   # 벽이 아니면 이동
        st.session_state.player = [new_y, new_x]

# 버튼 UI
col1, col2, col3 = st.columns(3)
with col2:
    if st.button("⬆️ 위"):
        move(-1, 0)

with col1:
    if st.button("⬅️ 왼쪽"):
        move(0, -1)

with col3:
    if st.button("➡️ 오른쪽"):
        move(0, 1)

col1, col2, col3 = st.columns(3)
with col2:
    if st.button("⬇️ 아래"):
        move(1, 0)

# 승리 체크
if maze[player_y][player_x] == 2:
    st.success("🎉 탈출 성공!")
    if st.button("게임 다시 시작"):
        st.session_state.player = [1,1]
