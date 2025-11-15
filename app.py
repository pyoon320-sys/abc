import streamlit as st
import random

st.title("인스타그램 아이디 추천기 ✨")

# 키워드 입력
keyword = st.text_input("사용하고 싶은 키워드를 입력하세요 (예: travel, coffee, cat 등)")

# 추천 버튼
if st.button("아이디 추천받기"):
    if keyword.strip():
        # 아이디 패턴 리스트
        patterns = [
            f"{keyword}_{random.randint(1,999)}",
            f"{keyword}{random.randint(10,99)}",
            f"real_{keyword}",
            f"{keyword}_official",
            f"{keyword}.daily",
            f"{keyword}.life",
            f"its_{keyword}",
            f"{keyword}_vibes",
            f"{keyword}world",
            f"{keyword}_studio"
        ]

        st.subheader("추천 아이디 👍")
        for p in patterns[:5]:
            st.write(f"👉 **{p.lower()}**")
    else:
        st.warning("키워드를 입력해주세요!")
