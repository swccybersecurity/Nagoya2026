import streamlit as st
import requests
import json
import os
from datetime import datetime, date

st.set_page_config(page_title="名古屋親子遊 2026", page_icon="🎒", layout="centered")

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Noto+Sans+TC:wght@400;500;700&family=DM+Serif+Display&display=swap');
html, body, [class*="css"] { font-family: 'Noto Sans TC', sans-serif; }
.stApp { background: linear-gradient(135deg, #fdf6ec 0%, #fcebd7 50%, #f9e0c0 100%); min-height: 100vh; }
h1 { font-family: 'DM Serif Display', serif; color: #7c3a1e; letter-spacing: 0.02em; }
h2, h3 { color: #7c3a1e; }
.weather-card { background: linear-gradient(135deg, #1a6fa3, #0d4f7a); border-radius: 16px; padding: 16px 20px; color: white; margin-bottom: 16px; box-shadow: 0 4px 15px rgba(13,79,122,0.3); }
.weather-card .temp { font-size: 2.2rem; font-weight: 700; color: white; }
.weather-card .rain { font-size: 0.9rem; opacity: 0.85; margin-top: 4px; color: white; }
.weather-card .advice { background: rgba(255,255,255,0.15); border-radius: 8px; padding: 8px 12px; margin-top: 10px; font-size: 0.85rem; color: white; }
.spot-card { background: white; border-radius: 16px; overflow: hidden; margin-bottom: 4px; box-shadow: 0 2px 12px rgba(124,58,30,0.08); border: 1px solid #f0d9c4; }
.spot-card-img { width: 100%; height: 160px; object-fit: cover; display: block; }
.spot-card-body { padding: 14px 16px 16px; }
.spot-card-title { font-size: 1.05rem; font-weight: 700; color: #7c3a1e; margin-bottom: 4px; }
.spot-card-time { font-size: 0.82rem; color: #e8855a; font-weight: 600; margin-bottom: 6px; }
.spot-card-detail { font-size: 0.88rem; color: #555; line-height: 1.6; }
.spot-card-done { opacity: 0.5; }
.transport-row { display: flex; align-items: center; gap: 8px; padding: 4px 8px; color: #888; font-size: 0.82rem; margin: 2px 0 2px 8px; }
.transport-line { width: 2px; height: 24px; background: #e0c9b8; margin-right: 4px; }
.stProgress > div > div > div > div { background: linear-gradient(90deg, #e8855a, #c9572c) !important; }
[data-testid="stMetricValue"] { color: #c9572c; font-weight: 700; }
.stButton > button { background: linear-gradient(135deg, #e8855a, #c9572c); color: white; border: none; border-radius: 10px; font-weight: 500; }
.stButton > button:hover { background: linear-gradient(135deg, #c9572c, #a8421e); color: white; }
hr { border-color: #f0d9c4; }
</style>
""", unsafe_allow_html=True)

itinerary = {
    "Day 1 (7/13) - 抵達與安頓": {"tasks": [
        {"id": "d1_1", "task": "✈️ 抵達名古屋 NGO", "time": "15:30",
         "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/3/38/Chubu_Centrair_International_Airport_Aerial_photograph_2015.jpg/640px-Chubu_Centrair_International_Airport_Aerial_photograph_2015.jpg",
         "detail": "航班 CX530。領行李、過海關、裝網卡。", "map": "",
         "transport_after": {"icon": "🚆", "label": "名鐵特急", "duration": "28 分鐘"}},
        {"id": "d1_2", "task": "🏨 入住 HOTEL LiVEMAX BUDGET", "time": "17:20",
         "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/2/24/Nagoya_Station_Towers_from_Sasashima_20100904.jpg/640px-Nagoya_Station_Towers_from_Sasashima_20100904.jpg",
         "detail": "位於太閤通口。記得確認嬰兒推車是否方便進出電梯。", "map": "https://maps.google.com/?q=HOTEL+LiVEMAX+BUDGET+名古屋",
         "transport_after": {"icon": "🚶", "label": "步行", "duration": "5 分鐘"}},
        {"id": "d1_3", "task": "🍜 ESCA 地下街晚餐", "time": "18:30",
         "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/e/e9/Miso_katsu_Nagoya.jpg/640px-Miso_katsu_Nagoya.jpg",
         "detail": "推薦：矢場味噌豬排、鳥開親子丼、吉田麵。", "map": "https://maps.google.com/?q=名古屋+ESCA+地下街",
         "transport_after": None},
    ]},
    "Day 2 (7/14) - 經典市區": {"tasks": [
        {"id": "d2_1", "task": "🏯 名古屋城散步", "time": "09:30",
         "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/4/4a/Nagoya_Castle_20100530.jpg/640px-Nagoya_Castle_20100530.jpg",
         "detail": "搭地鐵名城線至「市役所站」。平坦好推推車，慢慢散步拍照。", "map": "https://maps.google.com/?q=名古屋城",
         "transport_after": {"icon": "🚇", "label": "地鐵名城線", "duration": "20 分鐘"}},
        {"id": "d2_2", "task": "🛍️ 榮町商圈午餐 / 逛街", "time": "12:00",
         "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/1/17/Sakae%2C_Nagoya_01.jpg/640px-Sakae%2C_Nagoya_01.jpg",
         "detail": "百貨公司多，有舒適冷氣和育嬰室。", "map": "https://maps.google.com/?q=名古屋+榮商圈",
         "transport_after": {"icon": "🚶", "label": "步行", "duration": "5 分鐘"}},
        {"id": "d2_3", "task": "🌃 綠洲21 夜景", "time": "18:30",
         "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/8/8e/Oasis21-2.jpg/640px-Oasis21-2.jpg",
         "detail": "宇宙船造型建築，晚上點燈很美，小孩可在底層廣場活動。", "map": "https://maps.google.com/?q=Oasis+21",
         "transport_after": None},
    ]},
    "Day 3 (7/15) - 港區放電": {"tasks": [
        {"id": "d3_1", "task": "🐠 名古屋港水族館", "time": "10:00",
         "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/8/89/Nagoya_port_aquarium01s3200.jpg/640px-Nagoya_port_aquarium01s3200.jpg",
         "detail": "搭地鐵名港線至「名古屋港站」。必看：海豚秀、小白鯨、企鵝。", "map": "https://maps.google.com/?q=名古屋港水族館",
         "transport_after": {"icon": "🚶", "label": "步行", "duration": "3 分鐘"}},
        {"id": "d3_2", "task": "🚢 南極觀測船富士號", "time": "14:00",
         "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/5/55/Fuji_icebreaker_Nagoya.jpg/640px-Fuji_icebreaker_Nagoya.jpg",
         "detail": "就在水族館旁邊，視小孩體力決定是否登船。", "map": "https://maps.google.com/?q=南極觀測船+富士號",
         "transport_after": {"icon": "🚇", "label": "地鐵名港線", "duration": "35 分鐘"}},
        {"id": "d3_3", "task": "🍽️ 港區周邊晚餐", "time": "18:00",
         "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/e/e9/Miso_katsu_Nagoya.jpg/640px-Miso_katsu_Nagoya.jpg",
         "detail": "在水族館周邊商場解決晚餐，避開市區下班人潮。", "map": "",
         "transport_after": None},
    ]},
    "Day 4 (7/16) - 童話合掌村": {"tasks": [
        {"id": "d4_1", "task": "🚌 出發一日遊巴士", "time": "08:00",
         "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/b/b5/Takayama_Sanmachi_Suji_2009.jpg/640px-Takayama_Sanmachi_Suji_2009.jpg",
         "detail": "太閤通口集合。攜帶：輕便傘車、小孩安撫零食/玩具。", "map": "",
         "transport_after": {"icon": "🚌", "label": "遊覽車", "duration": "約 2.5 小時"}},
        {"id": "d4_2", "task": "🥩 飛驒高山老街散步", "time": "10:30",
         "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/b/b5/Takayama_Sanmachi_Suji_2009.jpg/640px-Takayama_Sanmachi_Suji_2009.jpg",
         "detail": "必吃：飛驒牛握壽司、五平餅。", "map": "https://maps.google.com/?q=飛驒高山老街",
         "transport_after": {"icon": "🚌", "label": "遊覽車", "duration": "約 1 小時"}},
        {"id": "d4_3", "task": "🛖 白川鄉合掌村", "time": "13:30",
         "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/5/5d/Shirakawa-go_Gassho-zukuri_Village%2C_Ogi-machi%2C_Shirakawa%2C_Gifu.jpg/640px-Shirakawa-go_Gassho-zukuri_Village%2C_Ogi-machi%2C_Shirakawa%2C_Gifu.jpg",
         "detail": "世界遺產打卡！觀景台需轉搭接駁車，推車需收折。", "map": "https://maps.google.com/?q=白川鄉合掌村",
         "transport_after": {"icon": "🚌", "label": "遊覽車返回", "duration": "約 2.5 小時"}},
        {"id": "d4_4", "task": "🏨 返回飯店", "time": "18:30",
         "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/2/24/Nagoya_Station_Towers_from_Sasashima_20100904.jpg/640px-Nagoya_Station_Towers_from_Sasashima_20100904.jpg",
         "detail": "預計 18:30-19:00 回到名古屋車站，在周邊吃晚餐。", "map": "",
         "transport_after": None},
    ]},
    "Day 5 (7/17) - 樂高日": {"tasks": [
        {"id": "d5_1", "task": "🧱 名古屋樂高樂園", "time": "10:00",
         "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/3/3e/LEGOLAND_Japan_Resort_entrance.jpg/640px-LEGOLAND_Japan_Resort_entrance.jpg",
         "detail": "搭青波線至「金城埠頭站」。專為 2-12 歲設計，先下載官方 App 查等待時間。", "map": "https://maps.google.com/?q=LEGOLAND+Japan",
         "transport_after": {"icon": "🚶", "label": "步行", "duration": "5 分鐘"}},
        {"id": "d5_2", "task": "🚄 磁浮鐵道館（彈性）", "time": "15:00",
         "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/a/a3/SCMaglev_and_Railway_Park_20120611.jpg/640px-SCMaglev_and_Railway_Park_20120611.jpg",
         "detail": "在樂高樂園旁邊。小孩還有體力的話，進去看超大新幹線！", "map": "https://maps.google.com/?q=磁浮鐵道館+名古屋",
         "transport_after": None},
    ]},
    "Day 6 (7/18) - 麵包超人": {"tasks": [
        {"id": "d6_1", "task": "🍞 麵包超人兒童博物館", "time": "10:00",
         "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/d0/Anpanman_Nagoya.jpg/640px-Anpanman_Nagoya.jpg",
         "detail": "前往長島度假村，學齡前幼童的天堂！", "map": "https://maps.google.com/?q=名古屋麵包超人兒童博物館",
         "transport_after": {"icon": "🚶", "label": "步行", "duration": "5 分鐘"}},
        {"id": "d6_2", "task": "🛍️ 三井 Outlet 爵士之夢長島", "time": "13:00",
         "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/6/66/Mitsui_Outlet_Park_Jazz_Dream_Nagashima.jpg/640px-Mitsui_Outlet_Park_Jazz_Dream_Nagashima.jpg",
         "detail": "日本最大級 Outlet，爸媽輪流顧小孩去逛！", "map": "https://maps.google.com/?q=三井Outlet+Park+爵士之夢長島",
         "transport_after": {"icon": "🚌", "label": "巴士返回", "duration": "約 1 小時"}},
    ]},
    "Day 7 (7/19) - 悠閒散步": {"tasks": [
        {"id": "d7_1", "task": "⛩️ 大須觀音參拜", "time": "10:00",
         "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/1/11/Osu_Kannon_Temple_Nagoya_2009.jpg/640px-Osu_Kannon_Temple_Nagoya_2009.jpg",
         "detail": "搭地鐵鶴舞線至「大須觀音站」。", "map": "https://maps.google.com/?q=大須觀音",
         "transport_after": {"icon": "🚶", "label": "步行", "duration": "2 分鐘"}},
        {"id": "d7_2", "task": "🍡 大須商店街逛街", "time": "10:30",
         "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/1/11/Osu_Kannon_Temple_Nagoya_2009.jpg/640px-Osu_Kannon_Temple_Nagoya_2009.jpg",
         "detail": "有巨大雨棚，推嬰兒車很舒服。買藥妝、吃炸雞、糰子。", "map": "https://maps.google.com/?q=大須商店街",
         "transport_after": {"icon": "🚇", "label": "地鐵", "duration": "15 分鐘"}},
        {"id": "d7_3", "task": "🌳 久屋大通公園", "time": "15:00",
         "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/f/f9/Hisaya-odori_Park_Nagoya.jpg/640px-Hisaya-odori_Park_Nagoya.jpg",
         "detail": "讓小孩跑跳放電，大人坐著喝咖啡。", "map": "https://maps.google.com/?q=久屋大通公園",
         "transport_after": None},
    ]},
    "Day 8 (7/20) - 網美與採買": {"tasks": [
        {"id": "d8_1", "task": "📸 則武森林 (Noritake Garden)", "time": "10:00",
         "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/e/e9/Noritake_Garden01.jpg/640px-Noritake_Garden01.jpg",
         "detail": "極美的紅磚建築群，適合拍全家福。", "map": "https://maps.google.com/?q=則武森林",
         "transport_after": {"icon": "🚶", "label": "步行", "duration": "3 分鐘"}},
        {"id": "d8_2", "task": "📚 AEON Mall 則武新町", "time": "12:00",
         "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/2/24/Nagoya_Station_Towers_from_Sasashima_20100904.jpg/640px-Nagoya_Station_Towers_from_Sasashima_20100904.jpg",
         "detail": "育嬰設施完善。必拍絕美蔦屋書店大書牆。", "map": "https://maps.google.com/?q=AEON+Mall+則武新町",
         "transport_after": {"icon": "🚶", "label": "步行", "duration": "10 分鐘"}},
        {"id": "d8_3", "task": "🎁 車站周邊最後採買", "time": "16:00",
         "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/2/24/Nagoya_Station_Towers_from_Sasashima_20100904.jpg/640px-Nagoya_Station_Towers_from_Sasashima_20100904.jpg",
         "detail": "高島屋或名鐵百貨補齊伴手禮（小倉吐司餅乾、青柳外郎糕）。", "map": "https://maps.google.com/?q=名鐵百貨店+本店",
         "transport_after": None},
    ]},
    "Day 9 (7/21) - 準備回家": {"tasks": [
        {"id": "d9_1", "task": "☕ 名古屋特色早餐", "time": "08:00",
         "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/0/09/Komeda_Coffee_morning_set.jpg/640px-Komeda_Coffee_morning_set.jpg",
         "detail": "Komeda 咖啡：點飲料送小倉吐司，名古屋限定文化！", "map": "https://maps.google.com/?q=Komeda+Coffee+名古屋車站",
         "transport_after": {"icon": "🚶", "label": "步行", "duration": "10 分鐘"}},
        {"id": "d9_2", "task": "🧳 飯店退房", "time": "10:00",
         "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/2/24/Nagoya_Station_Towers_from_Sasashima_20100904.jpg/640px-Nagoya_Station_Towers_from_Sasashima_20100904.jpg",
         "detail": "10:00 前退房。清點行李件數。", "map": "",
         "transport_after": {"icon": "🚆", "label": "名鐵 μ-SKY", "duration": "28 分鐘"}},
        {"id": "d9_3", "task": "✈️ 航班 CX531 返台", "time": "16:40",
         "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/3/38/Chubu_Centrair_International_Airport_Aerial_photograph_2015.jpg/640px-Chubu_Centrair_International_Airport_Aerial_photograph_2015.jpg",
         "detail": "中部國際機場。建議 13:30 前抵達！", "map": "",
         "transport_after": None},
    ]},
}

TRIP_START = date(2026, 7, 13)
PROGRESS_FILE = "progress.json"

def load_progress():
    if os.path.exists(PROGRESS_FILE):
        try:
            with open(PROGRESS_FILE, "r") as f:
                return json.load(f)
        except Exception:
            pass
    return {"checked": [], "notes": {}}

def save_progress(data):
    with open(PROGRESS_FILE, "w") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

if "data" not in st.session_state:
    st.session_state.data = load_progress()

@st.cache_data(ttl=3600)
def fetch_weather(days_ahead):
    if days_ahead > 14:
        return "TOO_FAR"
    url = (
        "https://api.open-meteo.com/v1/forecast"
        "?latitude=35.1815&longitude=136.9066"
        "&daily=weathercode,temperature_2m_max,temperature_2m_min,precipitation_probability_max"
        "&timezone=Asia%2FTokyo"
        "&forecast_days=14"
    )
    try:
        resp = requests.get(url, timeout=8)
        resp.raise_for_status()
        return resp.json()
    except Exception:
        return None

def wmo_to_emoji(code):
    if code == 0:            return "☀️", "晴天"
    elif code in (1, 2):     return "🌤️", "多雲時晴"
    elif code == 3:          return "☁️", "陰天"
    elif code in (45, 48):   return "🌫️", "有霧"
    elif code in (51,53,55): return "🌦️", "毛毛雨"
    elif code in (61,63,65): return "🌧️", "有雨"
    elif code in (80,81,82): return "⛈️", "陣雨"
    elif code in (95,96,99): return "⛈️", "雷雨"
    else:                    return "🌈", "不明"

def rain_advice(prob, max_temp):
    tips = []
    if prob >= 60:       tips.append("☔ 降雨機率高，務必帶傘")
    elif prob >= 30:     tips.append("🌂 帶把折疊傘備用")
    if max_temp >= 35:   tips.append("🥵 高溫警報！多補水")
    elif max_temp >= 32: tips.append("☀️ 炎熱，注意防曬與幼兒補水")
    if not tips:         tips.append("✅ 天氣不錯，出門愉快！")
    return "　".join(tips)

all_tasks   = [t for day in itinerary.values() for t in day["tasks"]]
total_tasks = len(all_tasks)
checked     = st.session_state.data["checked"]
pct         = int(len(checked) / total_tasks * 100) if total_tasks else 0

st.title("🎒 名古屋親子遊 2026")

today     = date.today()
days_left = (TRIP_START - today).days
trip_day  = (today - TRIP_START).days

col1, col2 = st.columns([2, 1])
with col1:
    if days_left > 0:
        st.info(f"🚀 距離出發還有 **{days_left}** 天！")
    elif 0 <= trip_day <= 8:
        st.success(f"✨ 旅程第 **{trip_day + 1}** 天，正在進行中！")
    else:
        st.warning("🏠 旅程已圓滿結束，感謝這段美好回憶 🌸")
with col2:
    st.metric("完成度", f"{pct}%")
    st.progress(pct)

st.divider()
mode = st.radio("📋 顯示模式", ["每日行程", "總覽模式"], horizontal=True)
st.divider()

weather_data = fetch_weather(days_left)

if mode == "每日行程":
    days_list    = list(itinerary.keys())
    default_idx  = max(0, min(trip_day, len(days_list)-1)) if 0 <= trip_day <= 8 else 0
    selected_day = st.selectbox("📅 選擇天數", days_list, index=default_idx)
    day_index    = days_list.index(selected_day)

    if weather_data == "TOO_FAR":
        st.info("ℹ️ 距離出發日大於 14 天，目前尚無精準天氣預報。")
    elif weather_data:
        try:
            w_idx = min(day_index, len(weather_data["daily"]["weathercode"]) - 1)
            d = weather_data["daily"]
            emoji, desc = wmo_to_emoji(d["weathercode"][w_idx])
            t_max  = d["temperature_2m_max"][w_idx]
            t_min  = d["temperature_2m_min"][w_idx]
            rain_p = d["precipitation_probability_max"][w_idx]
            advice = rain_advice(rain_p, t_max)
            st.markdown(f"""
            <div class="weather-card">
                <div style="display:flex;justify-content:space-between;align-items:center;">
                    <div>
                        <div style="font-size:1rem;opacity:0.8;">名古屋天氣預報</div>
                        <div class="temp">{emoji} {t_max:.0f}° / {t_min:.0f}°C</div>
                        <div class="rain">🌧 降雨機率 {rain_p}% ｜ {desc}</div>
                    </div>
                    <div style="font-size:3rem;">{emoji}</div>
                </div>
                <div class="advice">{advice}</div>
            </div>
            """, unsafe_allow_html=True)
        except Exception:
            pass
    else:
        st.info("⚠️ 天氣預報需要網路連線")

    st.subheader(selected_day)
    tasks = itinerary[selected_day]["tasks"]

    for i, task_info in enumerate(tasks):
        tid     = task_info["id"]
        is_done = tid in checked
        opacity = "spot-card-done" if is_done else ""
        map_btn = f'　<a href="{task_info["map"]}" target="_blank" style="text-decoration:none; font-weight:bold; color:#e8855a;">📍 導航</a>' if task_info.get("map") else ""

        st.markdown(f"""
        <div class="spot-card {opacity}">
            <img class="spot-card-img" src="{task_info['image']}" onerror="this.style.display='none'" alt="">
            <div class="spot-card-body">
                <div class="spot-card-time">🕐 {task_info['time']}</div>
                <div class="spot-card-title">{"✅ " if is_done else ""}{task_info['task']}</div>
                <div class="spot-card-detail">{task_info['detail']}{map_btn}</div>
            </div>
        </div>
        """, unsafe_allow_html=True)

        new_val = st.checkbox("完成此站", value=is_done, key=f"ck_{tid}")
        if new_val and tid not in checked:
            checked.append(tid)
            save_progress(st.session_state.data)
            st.rerun()
        elif not new_val and tid in checked:
            checked.remove(tid)
            save_progress(st.session_state.data)
            st.rerun()

        if task_info.get("transport_after") and i < len(tasks) - 1:
            t = task_info["transport_after"]
            st.markdown(f"""
            <div class="transport-row">
                <div class="transport-line"></div>
                {t['icon']} {t['label']}　⏱ {t['duration']}
            </div>
            """, unsafe_allow_html=True)

    st.divider()
    st.subheader("📝 今日筆記（花費 / 紀錄）")
    note_key     = f"note_{selected_day}"
    notes        = st.session_state.data.setdefault("notes", {})
    current_note = st.text_area("在這裡紀錄想說的話...", value=notes.get(note_key, ""), height=100, key=f"note_{note_key}")
    if current_note != notes.get(note_key, ""):
        notes[note_key] = current_note
        save_progress(st.session_state.data)

else:
    for idx, (day_name, day_data) in enumerate(itinerary.items()):
        tasks       = day_data["tasks"]
        done_count  = sum(1 for t in tasks if t["id"] in checked)
        total_count = len(tasks)
        all_done    = done_count == total_count

        weather_str = ""
        # 由於總覽模式無法確定每天都是未來的哪一天，這裡做個簡單防呆，不抓取太遠的天氣
        if weather_data and weather_data != "TOO_FAR":
            try:
                w_idx = min(idx, len(weather_data["daily"]["weathercode"]) - 1)
                d = weather_data["daily"]
                emoji, _ = wmo_to_emoji(d["weathercode"][w_idx])
                t_max    = d["temperature_2m_max"][w_idx]
                rain_p   = d["precipitation_probability_max"][w_idx]
                weather_str = f"　{emoji} {t_max:.0f}°C　🌧 {rain_p}%"
            except Exception:
                pass

        header = f"{'✅' if all_done else '📅'} {day_name}{weather_str}　({done_count}/{total_count})"
        with st.expander(header, expanded=False):
            for task in tasks:
                tid     = task["id"]
                is_done = tid in checked
                
                if is_done:
                    st.success(f"✅ {task['time']} {task['task']}")
                else:
                    st.markdown(f"⬜ {task['time']} {task['task']}")

    st.divider()
    if st.button("🗑️ 重置所有打卡紀錄", use_container_width=True):
        st.session_state.data = {"checked": [], "notes": {}}
        save_progress(st.session_state.data)
        st.rerun()
