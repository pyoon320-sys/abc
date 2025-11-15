import streamlit as st
import random

st.title("인스타그램 아이디 추천기 ✨ (단어 2개 + 숫자 버전)")

# 사용자 입력
word1 = st.text_input("첫 번째 단어를 입력하세요 (예: travel)")
word2 = st.text_input("두 번째 단어를 입력하세요 (예: coffee)")
number = st.number_input("숫자를 입력하세요 (예: 7, 21, 99)", min_value=0, max_value=9999)

# 추천 버튼
if st.button("아이디 추천받기"):
    if word1.strip() and word2.strip():
        # 패턴 생성
        patterns = [
            f"{word1}{word2}{number}",
            f"{word1}_{word2}_{number}",
            f"{word1}.{word2}{number}",
            f"{word1}{number}_{word2}",
            f"{word2}{word1}{number}",
            f"{word1}_{number}_{word2}",
            f"its_{word1}_{word2}",
            f"{word1}_{word2}_official",
            f"{word1}{word2}_vibes",
            f"{word1}{word2}_{random.randint(1,999)}",   # 랜덤 한 개 끼워 넣기
        ]

        st.subheader("추천 아이디 👍")
        for p in patterns[:6]:   # 6개만 보여줌
            st.write(f"👉 **{p.lower()}**")

    else:
        st.warning("단어 2개를 모두 입력해주세요!")
