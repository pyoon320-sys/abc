import streamlit as st

# 타이틀 표시
st.title("간단한 계산기")

# 사용자로부터 두 개의 숫자 입력 받기
num1 = st.number_input("첫 번째 숫자를 입력하세요:", min_value=0)
num2 = st.number_input("두 번째 숫자를 입력하세요:", min_value=0)

# 계산 버튼 추가
if st.button('계산하기'):
    sum_result = num1 + num2
    st.write(f'두 숫자의 합은 {sum_result}입니다.')

# 추가적인 설명
st.write('Streamlit을 사용하여 간단한 계산기를 만들었습니다!')
