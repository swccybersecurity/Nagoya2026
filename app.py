import streamlit as st
import requests
import json
import os
from datetime import datetime, date

# ── 頁面設定 ──────────────────────────────────────────────

st.set_page_config(page_title="名古屋親子遊 2026", page_icon="🎒", layout="centered")

# ── 視覺主題 CSS ──────────────────────────────────────────

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Noto+Sans+TC:wght@400;500;700&family=DM+Serif+Display&display=swap');

html, body, [class*="css"] {
    font-family: 'Noto Sans TC', sans-serif;
}

/* 漸層背景 */
.stApp {
    background: linear-gradient(135deg, #fdf6ec 0%, #fcebd7 50%, #f9e0c0 100%);
    min-height: 100vh;
}

/* 標題 */
h1 { font-family: 'DM Serif Display', serif; color: #7c3a1e; letter-spacing: 0.02em; }
h2, h3 { color: #7c3a1e; }

/* 天氣卡片 */
.weather-card {
    background: linear-gradient(135deg, #1a6fa3, #0d4f7a);
    border-radius: 16px;
    padding: 16px 20px;
    color: white;
    margin-bottom: 16px;
    box-shadow: 0 4px 15px rgba(13,79,122,0.3);
}
.weather-card .temp { font-size: 2.2rem; font-weight: 700; }
.weather-card .rain { font-size: 0.9rem; opacity: 0.85; margin-top: 4px; }
.weather-card .advice { 
    background: rgba(255,255,255,0.15); 
    border-radius: 8px; 
    padding: 8px 12px; 
    margin-top: 10px; 
    font-size: 0.85rem;
}

/* Expander 樣式 */
.streamlit-expanderHeader {
    background: white !important;
    border-radius: 10px !important;
    border: 1px solid #f0d9c4 !important;
    font-weight: 500 !important;
}
.streamlit-expanderContent {
    background: #fff9f4 !important;
    border: 1px solid #f0d9c4 !important;
    border-top: none !important;
    border-radius: 0 0 10px 10px !important;
}

/* 進度條顏色 */
.stProgress > div > div > div > div {
    background: linear-gradient(90deg, #e8855a, #c9572c) !important;
}

/* 選單 */
.stSelectbox > div > div {
    background: white;
    border-radius: 10px;
    border: 1px solid #f0d9c4;
}

/* Metric 卡片 */
[data-testid="stMetricValue"] { color: #c9572c; font-weight: 700; }

/* 按鈕 */
.stButton > button {
    background: linear-gradient(135deg, #e8855a, #c9572c);
    color: white;
    border: none;
    border-radius: 10px;
    font-weight: 500;
}
.stButton > button:hover {
    background: linear-gradient(135deg, #c9572c, #a8421e);
    color: white;
}

/* 總覽完成勾勾 */
.overview-done { color: #27ae60; font-weight: 600; }
.overview-pending { color: #aaa; }

/* info / success box */
.stAlert { border-radius: 12px; }

/* divider */
hr { border-color: #f0d9c4; }
</style>
""", unsafe_allow_html=True)

# ── 行程資料庫 ────────────────────────────────────────────

itinerary = {
    "Day 1 (7/13) - 抵達與安頓": [
        {"id": "d1_1", "task": "✈️ 15:30 抵達名古屋 NGO", "detail": "航班 CX530。領行李、過海關、裝網卡。"},
        {"id": "d1_2", "task": "🚆 搭名鐵前往名古屋車站", "detail": "尋找「名鐵線」指標，搭乘 μ-SKY 或特急列車往名古屋。約 28 分鐘。"},
        {"id": "d1_3", "task": "🏨 入住 HOTEL LiVEMAX BUDGET", "detail": "位於太閤通口。記得確認嬰兒推車是否方便進出電梯。\n\n[📍 Google Map 導航](https://maps.app.goo.gl/ZvQa6cZzYkTkPFDr5)"},
        {"id": "d1_4", "task": "🍜 ESCA 地下街晚餐", "detail": "就在車站旁邊。推薦名店：矢場味噌豬排、鳥開親子丼、吉田麵。\n\n[📍 ESCA 地下街](https://maps.app.goo.gl/8Xb3s9L6pVzGeXJJ9)"},
    ],
    "Day 2 (7/14) - 經典市區": [
        {"id": "d2_1", "task": "🎒 備妥推車、尿布、水壺出門", "detail": "今天預計會走比較多路，請確認推車狀態。"},
        {"id": "d2_2", "task": "🏯 名古屋城散步", "detail": "搭乘地鐵名城線至「市役所站」。園區平坦好推推車，可慢慢散步拍照。\n\n[📍 名古屋城](https://maps.app.goo.gl/K1K1qhJbWfM4Xbaz7)"},
        {"id": "d2_3", "task": "🛍️ 榮町商圈吃午餐 / 逛街", "detail": "百貨公司多，尋找有舒適冷氣和育嬰室的百貨吃午餐。\n\n[📍 榮町](https://maps.app.goo.gl/8GZUkPaSgWExuVNa8)"},
        {"id": "d2_4", "task": "🌃 綠洲21 (Oasis 21) 夜景", "detail": "宇宙船造型建築，晚上點燈很美，小孩可在底層廣場活動。\n\n[📍 Oasis 21](https://maps.app.goo.gl/1R1UvPuiZzBGHqcn6)"},
    ],
    "Day 3 (7/15) - 港區放電": [
        {"id": "d3_1", "task": "🎒 攜帶防曬與小孩替換衣物", "detail": "今天在水族館可能會有玩水或流汗的狀況。"},
        {"id": "d3_2", "task": "🐠 名古屋港水族館", "detail": "搭乘地鐵名港線至「名古屋港站」。必看亮點：海豚秀、小白鯨、企鵝。室內避暑首選！\n\n[📍 名古屋港水族館](https://maps.app.goo.gl/eSwgWaHmYAqFgChc7)"},
        {"id": "d3_3", "task": "🚢 參觀南極觀測船富士號", "detail": "就在水族館旁邊，視小孩體力決定是否登船參觀。\n\n[📍 南極觀測船富士](https://maps.app.goo.gl/cS4CsgbmJf1ztPaD6)"},
        {"id": "d3_4", "task": "🍽️ 港區周邊吃晚餐", "detail": "可在水族館周邊商場解決晚餐，避開市區下班人潮。"},
    ],
    "Day 4 (7/16) - 童話合掌村": [
        {"id": "d4_1", "task": "🚌 08:00 太閤通口集合出發", "detail": "參加一日團。⚠️ 務必攜帶：輕便好收折的傘車、小孩安撫零食/玩具。"},
        {"id": "d4_2", "task": "🥩 飛驒高山老街散步", "detail": "中午抵達高山。必吃：飛驒牛握壽司、五平餅。\n\n[📍 飛驒高山老街](https://maps.app.goo.gl/bvbBNqBjgpCJtBuL9)"},
        {"id": "d4_3", "task": "🛖 漫步白川鄉合掌村", "detail": "世界遺產打卡！若要上觀景台需轉搭接駁車，推車需收折。\n\n[📍 白川鄉合掌村](https://maps.app.goo.gl/mwGzPezNdj4Y6TkW9)"},
        {"id": "d4_4", "task": "🚌 傍晚返回飯店解散", "detail": "預計 18:00-19:00 回到名古屋車站，直接在周邊吃晚餐。"},
    ],
    "Day 5 (7/17) - 樂高日": [
        {"id": "d5_1", "task": "🎒 準備防曬、水與滿滿體力", "detail": "前往樂高樂園。搭乘青波線至「金城埠頭站」。"},
        {"id": "d5_2", "task": "🧱 名古屋樂高樂園", "detail": "專為 2-12 歲設計，設施非常溫和。建議先下載官方 App 查看設施等待時間。\n\n[📍 名古屋樂高樂園](https://maps.app.goo.gl/KvCrJijG3rEMFuLNA)"},
        {"id": "d5_3", "task": "🚄 磁浮鐵道館 (彈性)", "detail": "在樂高樂園旁邊。如果小孩提早離開樂高還有體力，可以進去看超大新幹線。\n\n[📍 磁浮鐵道館](https://maps.app.goo.gl/EkDQhP4t3PdqhLDv8)"},
    ],
    "Day 6 (7/18) - 麵包超人": [
        {"id": "d6_1", "task": "🍞 名古屋麵包超人兒童博物館", "detail": "前往長島度假村。學齡前幼童的天堂，絕對會失心瘋！\n\n[📍 麵包超人博物館](https://maps.app.goo.gl/6J3Gfv7uQBk6Jb5o8)"},
        {"id": "d6_2", "task": "🛍️ 三井 Outlet 爵士之夢長島", "detail": "大人血拚時間！日本最大級 Outlet，爸媽可輪流顧小孩去逛。\n\n[📍 三井 Outlet 長島](https://maps.app.goo.gl/nXKDYhMmHnZreFzQ8)"},
        {"id": "d6_3", "task": "🚌 搭乘巴士返回市區", "detail": "留意末班車時間，建議不要拖太晚。"},
    ],
    "Day 7 (7/19) - 悠閒散步": [
        {"id": "d7_1", "task": "⛩️ 大須觀音參拜", "detail": "搭乘地鐵鶴舞線至「大須觀音站」。\n\n[📍 大須觀音](https://maps.app.goo.gl/AGa6uYBJfGBJuW1D6)"},
        {"id": "d7_2", "task": "🍡 大須商店街逛街", "detail": "有巨大雨棚，推嬰兒車逛街很舒服。買藥妝、吃大須小吃（如炸雞、糰子）。\n\n[📍 大須商店街](https://maps.app.goo.gl/q6FVQdUyVcFGGBGF9)"},
        {"id": "d7_3", "task": "🌳 久屋大通公園", "detail": "下午若想讓小孩在草地上跑跳放電，可以來這裡散步喝咖啡。\n\n[📍 久屋大通公園](https://maps.app.goo.gl/C5n3yDvN8bLkmr986)"},
    ],
    "Day 8 (7/20) - 網美與採買": [
        {"id": "d8_1", "task": "📸 則武森林 (Noritake Garden)", "detail": "極美的紅磚建築群與陶瓷博物館，適合拍全家福。\n\n[📍 則武森林](https://maps.app.goo.gl/GFf4Cr7eFkyHX9aQ7)"},
        {"id": "d8_2", "task": "📚 AEON Mall 則武新町店", "detail": "緊鄰則武森林。室內育嬰設施完善，必拍絕美「蔦屋書店」大書牆。\n\n[📍 AEON Mall 則武新町](https://maps.app.goo.gl/jVbNLPzEqNUm3H6S6)"},
        {"id": "d8_3", "task": "🎁 車站周邊最後採買", "detail": "回飯店前，在高島屋或名鐵百貨補齊伴手禮（小倉吐司餅乾、青柳外郎糕）。\n\n[📍 名鐵百貨](https://maps.app.goo.gl/HbL7hxbxJ4HPFnWP7)"},
    ],
    "Day 9 (7/21) - 準備回家": [
        {"id": "d9_1", "task": "☕ 體驗名古屋特色早餐", "detail": "找間飯店附近的咖啡廳（如 Komeda），體驗「點飲料送早餐 (小倉吐司)」文化。\n\n[📍 Komeda 珈琲店附近分店](https://maps.app.goo.gl/rBHc7p5h7E13spBr5)"},
        {"id": "d9_2", "task": "🧳 飯店退房與行李確認", "detail": "10:00 前退房。清點行李件數，確認沒遺忘任何東西。"},
        {"id": "d9_3", "task": "🚆 搭名鐵前往機場", "detail": "建議中午左右就出發前往中部國際機場，機場內也有很多好逛的。"},
        {"id": "d9_4", "task": "✈️ 16:40 航班 CX531", "detail": "準備登機，平安回家！"},
    ],
}

TRIP_START = date(2026, 7, 13)
TRIP_END   = date(2026, 7, 21)

# ── 打卡狀態持久化 (JSON 檔) ──────────────────────────────

PROGRESS_FILE = "progress.json"

def load_progress():
    if os.path.exists(PROGRESS_FILE):
        try:
            with open(PROGRESS_FILE, "r") as f:
                return json.load(f)
        except Exception:
            return {"checked": [], "notes": {}}
    return {"checked": [], "notes": {}}

def save_progress(data):
    with open(PROGRESS_FILE, "w") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

if "data" not in st.session_state:
    st.session_state.data = load_progress()

# ── 天氣 API (Open-Meteo) ─────────────────────────────────

NAGOYA_LAT = 35.1815
NAGOYA_LON = 136.9066

@st.cache_data(ttl=3600)
def fetch_weather():
    url = (
        "https://api.open-meteo.com/v1/forecast"
        f"?latitude={NAGOYA_LAT}&longitude={NAGOYA_LON}"
        "&daily=weathercode,temperature_2m_max,temperature_2m_min,precipitation_probability_max"
        "&timezone=Asia%2FTokyo"
        "&start_date=2026-07-13&end_date=2026-07-21"
    )
    try:
        resp = requests.get(url, timeout=8)
        resp.raise_for_status()
        return resp.json()
    except Exception:
        return None

def wmo_to_emoji(code):
    if code == 0:              return "☀️", "晴天"
    elif code in (1, 2):       return "🌤️", "多雲時晴"
    elif code == 3:            return "☁️", "陰天"
    elif code in (45, 48):     return "🌫️", "有霧"
    elif code in (51,53,55):   return "🌦️", "毛毛雨"
    elif code in (61,63,65):   return "🌧️", "有雨"
    elif code in (80,81,82):   return "⛈️", "陣雨"
    elif code in (95,96,99):   return "⛈️", "雷雨"
    else:                      return "🌈", "不明"

def rain_advice(prob, max_temp):
    tips = []
    if prob >= 60:
        tips.append("☔ 降雨機率高，務必帶傘")
    elif prob >= 30:
        tips.append("🌂 帶把折疊傘備用")
    if max_temp >= 35:
        tips.append("🥵 高溫警報！多補水、避免長時間戶外")
    elif max_temp >= 32:
        tips.append("☀️ 炎熱，注意防曬與幼兒補水")
    if not tips:
        tips.append("✅ 天氣不錯，出門愉快！")
    return "　".join(tips)

# ── 計算進度 ──────────────────────────────────────────────

total_tasks     = sum(len(v) for v in itinerary.values())
completed_tasks = len(st.session_state.data["checked"])
pct             = int(completed_tasks / total_tasks * 100) if total_tasks else 0

# ── 標題區 ────────────────────────────────────────────────

st.title("🎒 名古屋親子遊 2026")

today       = date.today()
days_left   = (TRIP_START - today).days
trip_day    = (today - TRIP_START).days  # 旅程第幾天 (0-based)

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

# ── 導航模式選擇 ──────────────────────────────────────────

mode = st.radio("📋 顯示模式", ["每日行程", "總覽模式"], horizontal=True)
st.divider()

# ══════════════════════════════════════════════════════════
# 模式 A：每日行程（含天氣）
# ══════════════════════════════════════════════════════════

if mode == "每日行程":
    days_list    = list(itinerary.keys())
    default_idx  = max(0, min(trip_day, len(days_list) - 1)) if 0 <= trip_day <= 8 else 0
    selected_day = st.selectbox("📅 選擇天數", days_list, index=default_idx)
    day_index    = days_list.index(selected_day)

    # ── 天氣卡片 ──────────────────────────────────────────
    weather_data = fetch_weather()
    if weather_data:
        try:
            d       = weather_data["daily"]
            emoji, desc   = wmo_to_emoji(d["weathercode"][day_index])
            t_max   = d["temperature_2m_max"][day_index]
            t_min   = d["temperature_2m_min"][day_index]
            rain_p  = d["precipitation_probability_max"][day_index]
            advice  = rain_advice(rain_p, t_max)

            st.markdown(f"""
            <div class="weather-card">
                <div style="display:flex; justify-content:space-between; align-items:center;">
                    <div>
                        <div style="font-size:1rem; opacity:0.8;">名古屋天氣預報</div>
                        <div class="temp">{emoji} {t_max:.0f}° / {t_min:.0f}°C</div>
                        <div class="rain">🌧 降雨機率 {rain_p}% ｜ {desc}</div>
                    </div>
                    <div style="font-size:3rem;">{emoji}</div>
                </div>
                <div class="advice">{advice}</div>
            </div>
            """, unsafe_allow_html=True)
        except Exception:
            st.info("天氣資料暫時無法顯示")
    else:
        st.info("⚠️ 天氣預報需要網路連線，目前無法取得")

    # ── 任務清單 ──────────────────────────────────────────
    st.subheader(selected_day)
    tasks   = itinerary[selected_day]
    checked = st.session_state.data["checked"]

    for task_info in tasks:
        tid      = task_info["id"]
        is_done  = tid in checked
        label    = f"{'✅' if is_done else '⬜'} {task_info['task']}"

        with st.expander(label, expanded=not is_done):
            st.markdown(task_info.get("detail", ""))
            new_val = st.checkbox("完成此任務", value=is_done, key=f"ck_{tid}")
            if new_val and tid not in checked:
                checked.append(tid)
                save_progress(st.session_state.data)
                st.rerun()
            elif not new_val and tid in checked:
                checked.remove(tid)
                save_progress(st.session_state.data)
                st.rerun()

    # ── 每日筆記 ──────────────────────────────────────────
    st.divider()
    st.subheader("📝 今日筆記（花費 / 紀錄）")
    note_key     = f"note_{selected_day}"
    notes        = st.session_state.data.setdefault("notes", {})
    current_note = st.text_area(
        "在這裡紀錄想說的話…",
        value=notes.get(note_key, ""),
        height=100,
        key=f"note_area_{note_key}"
    )
    if current_note != notes.get(note_key, ""):
        notes[note_key] = current_note
        save_progress(st.session_state.data)

# ══════════════════════════════════════════════════════════
# 模式 B：總覽模式
# ══════════════════════════════════════════════════════════

else:
    weather_data = fetch_weather()
    checked      = st.session_state.data["checked"]

    for idx, (day_name, tasks) in enumerate(itinerary.items()):
        done_count  = sum(1 for t in tasks if t["id"] in checked)
        total_count = len(tasks)
        all_done    = done_count == total_count

        # 天氣摘要（一行）
        weather_str = ""
        if weather_data:
            try:
                d      = weather_data["daily"]
                emoji, _ = wmo_to_emoji(d["weathercode"][idx])
                t_max  = d["temperature_2m_max"][idx]
                rain_p = d["precipitation_probability_max"][idx]
                weather_str = f"　{emoji} {t_max:.0f}°C　🌧 {rain_p}%"
            except Exception:
                pass

        header = f"{'✅' if all_done else '📅'} {day_name}{weather_str}　({done_count}/{total_count})"

        with st.expander(header, expanded=False):
            for task in tasks:
                tid     = task["id"]
                is_done = tid in checked
                color   = "#27ae60" if is_done else "#aaa"
                mark    = "✅" if is_done else "⬜"
                st.markdown(
                    f'<span style="color:{color}">{mark} {task["task"]}</span>',
                    unsafe_allow_html=True
                )

    st.divider()

    # ── 重置按鈕 ──────────────────────────────────────────────
    if st.button("🗑️ 重置所有打卡紀錄", use_container_width=True):
        st.session_state.data = {"checked": [], "notes": {}}
        save_progress(st.session_state.data)
        st.rerun()
