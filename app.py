import streamlit as st

st.title("🎧 감성 플레이리스트 추천기 – 확장 버전")
st.write("오늘의 기분에 맞는 노래를 더 다양하게 추천해드릴게요 ☁️💖")

# 더욱 다양한 플레이리스트 데이터
playlists = {
    "설레는 느낌 ✨": [
        "IVE - LOVE DIVE",
        "NewJeans - Super Shy",
        "세븐틴 - 아주 NICE",
        "NCT DREAM - Candy",
        "STAYC - ASAP",
        "르세라핌 - Perfect Night",
        "선미 - 보름달",
        "오마이걸 - 살짝 설렜어",
        "TXT - Our Summer",
        "아이유 - Blueming",
    ],
    "힐링하고 싶어 🍀": [
        "아이유 - Love Poem",
        "적재 - 별 보러 가자",
        "폴킴 - 비",
        "태연 - 그대라는 시",
        "멜로망스 - 선물",
        "백예린 - Maybe It's Not Our Fault",
        "경서 - 밤하늘의 별을",
        "치즈 - Mood Indigo",
        "우효(Oohyo) - 꿀차",
        "정준일 - 안아줘",
    ],
    "감성에 잠기고 싶어 🌙": [
        "아이유 - 밤편지",
        "디오 - 별 떨어진다",
        "백예린 - Square",
        "정승환 - 너였다면",
        "도영 - 고백",
        "10cm - 폰서트",
        "우원재 - 시차",
        "크러쉬 - 가끔",
        "딘 - instagram",
        "백예린 - Bye bye my blue",
    ],
    "신나게 달리고 싶어 🔥": [
        "BLACKPINK - Pink Venom",
        "LE SSERAFIM - ANTIFRAGILE",
        "NewJeans - ETA",
        "지코 - 아무노래",
        "NCT WISH - WISH",
        "STRAY KIDS - S-Class",
        "ITZY - Dalla Dalla",
        "aespa - Spicy",
        "TWICE - Talk That Talk",
        "제시 - 눈누난나",
    ],
    "비 오는 날 듣기 좋은 노래 🌧": [
        "헤이즈 - 비도 오고 그래서",
        "아이유 - Rain Drop",
        "폴킴 - 모든 날, 모든 순간",
        "한요한 - 비",
        "윤하 - 사건의 지평선",
        "로이킴 - 봄봄봄",
        "루시 - 개화",
        "정키 - 부담이 돼",
        "소유 - I Miss You",
        "스탠딩에그 - 오래된 노래"
    ],
}

# 기분 선택
mood = st.selectbox("지금 당신의 기분은?", list(playlists.keys()))

if st.button("플레이리스트 추천받기 🎵"):
    st.subheader(f"'{mood}'에 맞춘 플레이리스트 🎶")
    for song in playlists[mood]:
        st.write(f"💚 {song}")
