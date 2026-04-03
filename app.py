import streamlit as st
from datetime import datetime

# --- 1. 網頁基本設定與 CSS 注入 ---
st.set_page_config(page_title="名古屋親子9日遊", page_icon="✈️", layout="centered")

# 注入你原本的日系配色 CSS (針對進度條和字體微調)
st.markdown("""
    <style>
    .stProgress > div > div > div > div {
        background-color: #c94c4c;
    }
    </style>
""", unsafe_allow_html=True)

# --- 2. 行程資料庫 (Dictionary) ---
# 將資料與視圖分離，方便日後隨時修改增減
itinerary = {
    "Day 1 (7/13)": [
        {"id": "d1_1", "task": "✈️ 15:30 抵達名古屋 (NGO) - 航班 CX530"},
        {"id": "d1_2", "task": "🏨 入住 HOTEL LiVEMAX BUDGET (太閤通口)"},
        {"id": "d1_3", "task": "🍜 ESCA 地下街尋找晚餐 (推薦矢場豬排)"}
    ],
    "Day 2 (7/14)": [
        {"id": "d2_1", "task": "🏯 名古屋城 (推車友善，慢慢散步)"},
        {"id": "d2_2", "task": "🛍️ 榮町商圈 & 綠洲21 宇宙船拍夜景"},
    ],
    "Day 3 (7/15)": [
        {"id": "d3_1", "task": "🐠 名古屋港水族館 (看海豚秀/避暑)"},
        {"id": "d3_2", "task": "🚢 參觀南極觀測船富士號"},
    ],
    "Day 4 (7/16)": [
        {"id": "d4_1", "task": "🚌 08:00 車站西側集合，出發一日團"},
        {"id": "d4_2", "task": "🛖 漫步白川鄉合掌村 (記得帶輕便傘車)"},
        {"id": "d4_3", "task": "🥩 飛驒高山老街吃飛驒牛握壽司"},
    ]
    # 你可以在這裡繼續把 Day 5 到 Day 9 的行程補上...
}

# --- 3. 狀態管理 (取代原有的 LocalStorage) ---
if 'progress' not in st.session_state:
    st.session_state.progress = []

# 計算總任務與完成度
total_tasks = sum(len(tasks) for tasks in itinerary.values())
completed_tasks = len(st.session_state.progress)
progress_percent = int((completed_tasks / total_tasks) * 100) if total_tasks > 0 else 0

# --- 4. 畫面佈局：頂部資訊 ---
st.title("🎒 名古屋・白川鄉親子遊")

# 動態倒數計時 (設定為 2026/07/13)
target_date = datetime(2026, 7, 13)
days_left = (target_date - datetime.now()).days

if days_left > 0:
    st.info(f"🚀 距離出發還有 **{days_left}** 天！滿心期待！")
else:
    st.success("✨ 旅程進行中！Have Fun!")

# 進度條
st.caption(f"旅程打卡進度: {progress_percent}%")
st.progress(progress_percent)
st.divider()

# --- 5. 畫面佈局：每日行程與打卡邏輯 ---
# 使用 Tabs 讓每天的行程分開顯示，避免手機版頁面過長
tabs = st.tabs(list(itinerary.keys()))

for i, (day, tasks) in enumerate(itinerary.items()):
    with tabs[i]:
        st.subheader(day)
        
        # 生成該日的打卡 Checkbox
        for task_info in tasks:
            task_id = task_info["id"]
            task_desc = task_info["task"]
            
            # 檢查這個 ID 是否已經在完成清單中
            is_checked = task_id in st.session_state.progress
            
            # Streamlit 的 checkbox 邏輯
            changed = st.checkbox(task_desc, value=is_checked, key=f"check_{task_id}")
            
            # 如果狀態有變更，更新 session_state 並重新載入畫面以更新進度條
            if changed and task_id not in st.session_state.progress:
                st.session_state.progress.append(task_id)
                st.rerun()
            elif not changed and task_id in st.session_state.progress:
                st.session_state.progress.remove(task_id)
                st.rerun()

st.divider()

# --- 6. 功能按鈕 ---
if st.button("🗑️ 重置所有打卡紀錄"):
    st.session_state.progress = []
    st.rerun()
