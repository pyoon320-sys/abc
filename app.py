operation = st.selectbox("연산을 선택하세요:", ["합", "뺄셈", "곱셈", "나눗셈"])

if operation == "합":
    result = num1 + num2
elif operation == "뺄셈":
    result = num1 - num2
elif operation == "곱셈":
    result = num1 * num2
elif operation == "나눗셈":
    if num2 != 0:
        result = num1 / num2
    else:
        result = "0으로 나눌 수 없습니다."

st.write(f"결과: {result}")
