import streamlit as st

# 타이틀 표시
st.title('간단한 스트림릿 앱')

# 사용자 입력 받기
name = st.text_input('이름을 입력하세요')

# 입력값에 따라 메시지 출력
if name:
    st.write(f'안녕하세요, {name}님!')
else:
    st.write('이름을 입력해 주세요.')
