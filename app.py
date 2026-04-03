import streamlit as st
from datetime import datetime

# --- 1. 網頁基本設定 ---
st.set_page_config(page_title="名古屋親子9日遊", page_icon="✈️", layout="centered")

# --- 2. 注入日系美化 CSS ---
st.markdown("""
    <style>
    /* 匯入日系字體 */
    @import url('https://fonts.googleapis.com/css2?family=Noto+Serif+TC:wght@400;700&family=Zen+Maru+Gothic:wght@500;700&display=swap');

    /* 隱藏 Streamlit 預設的頂部選單和底部浮水印 */
    #MainMenu {visibility: hidden;}
    header {visibility: hidden;}
    footer {visibility: hidden;}

    /* 替換整個 App 的背景：加入和紙白與圓點點陣圖 */
    .stApp {
        background-color: #f0ebe5;
        background-image: radial-gradient(#dcdcdc 1px, transparent 1px);
        background-size: 20px 20px;
        font-family: 'Zen Maru Gothic', sans-serif !important;
    }

    /* 讓所有標題變成明體，增加高級感 */
    h1, h2, h3, h4, h5, h6 {
        font-family: 'Noto Serif TC', serif !important;
        color: #3e3a39 !important;
        font-weight: 700 !important;
        letter-spacing: 1px;
    }

    /* 美化進度條：改成日本紅 */
    .stProgress > div > div > div > div {
        background-color: #c94c4c !important;
    }

    /* 美化 Tabs 分頁按鈕 */
    .stTabs [data-baseweb="tab-list"] {
        gap: 8px;
        overflow-x: auto; /* 手機版可左右滑動 */
    }
    .stTabs [data-baseweb="tab"] {
        height: 50px;
        white-space: pre-wrap;
        background-color: #ffffff;
        border-radius: 8px 8px 0px 0px;
        box-shadow: 0px 2px 5px rgba(0,0,0,0.05);
        color: #8e9eab;
        padding: 0 16px;
    }
    .stTabs [aria-selected="true"] {
        background-color: #fdfbf7;
        border-top: 3px solid #c94c4c;
        color: #c94c4c !important;
        font-weight: bold;
    }

    /* 美化 Checkbox 勾選框文字 */
    .stCheckbox label {
        color: #3e3a39 !important;
        font-size: 16px !important;
        padding-top: 5px;
        padding-bottom: 5px;
    }
    </style>
""", unsafe_allow_html=True)

# --- 3. 完整的 9天8夜行程資料庫 ---
itinerary = {
    "Day 1 (7/13)": [
        {"id": "d1_1", "task": "✈️ 15:30 抵達名古屋 NGO (航班 CX530)"},
        {"id": "d1_2", "task": "🚆 搭名鐵前往名古屋車站"},
        {"id": "d1_3", "task": "🏨 入住 HOTEL LiVEMAX BUDGET (太閤通口)"},
        {"id": "d1_4", "task": "🍜 ESCA 地下街吃晚餐 (推薦矢場豬排)"}
    ],
    "Day 2 (7/14)": [
        {"id": "d2_1", "task": "🎒 備妥推車、尿布、水壺出門"},
        {"id": "d2_2", "task": "🏯 名古屋城散步 (園區平坦好推推車)"},
        {"id": "d2_3", "task": "🛍️ 榮町商圈吃午餐 / 逛街"},
        {"id": "d2_4", "task": "🌃 綠洲21 (Oasis 21) 看宇宙船夜景"}
    ],
    "Day 3 (7/15)": [
        {"id": "d3_1", "task": "🎒 小孩放電日：帶好防曬與替換衣物"},
        {"id": "d3_2", "task": "🐠 名古屋港水族館 (看海豚秀/吹冷氣避暑)"},
        {"id": "d3_3", "task": "🚢 參觀南極觀測船富士號 (視小孩體力)"},
        {"id": "d3_4", "task": "🍽️ 港區周邊吃晚餐再回市區"}
    ],
    "Day 4 (7/16)": [
        {"id": "d4_1", "task": "🚌 08:00 名古屋車站太閤通口集合 (帶輕便傘車)"},
        {"id": "d4_2", "task": "🥩 飛驒高山老街散步吃飛驒牛握壽司"},
        {"id": "d4_3", "task": "🛖 漫步白川鄉合掌村 (世界遺產打卡)"},
        {"id": "d4_4", "task": "🚌 傍晚隨遊覽車回到飯店周邊解散"}
    ],
    "Day 5 (7/17)": [
        {"id": "d5_1", "task": "🎒 準備好防曬、水與滿滿體力"},
        {"id": "d5_2", "task": "🧱 名古屋樂高樂園 (全日放電，設施溫和)"},
        {"id": "d5_3", "task": "🚄 磁浮鐵道館 (看超大新幹線，視體力順遊)"}
    ],
    "Day 6 (7/18)": [
        {"id": "d6_1", "task": "🍞 名古屋麵包超人兒童博物館 (長島溫泉樂園旁)"},
        {"id": "d6_2", "task": "🛍️ 三井 Outlet 爵士之夢長島 (大人血拚輪替)"},
        {"id": "d6_3", "task": "🚌 搭乘直達巴士返回名古屋市區"}
    ],
    "Day 7 (7/19)": [
        {"id": "d7_1", "task": "⛩️ 大須觀音參拜"},
        {"id": "d7_2", "task": "🍡 大須商店街吃小吃、買藥妝 (有雨棚好逛)"},
        {"id": "d7_3", "task": "🌳 久屋大通公園散步讓小孩跑跳"}
    ],
    "Day 8 (7/20)": [
        {"id": "d8_1", "task": "📸 則武森林 (Noritake Garden) 拍紅磚建築全家福"},
        {"id": "d8_2", "task": "📚 逛旁邊的 AEON Mall 則武新町店 (超美蔦屋書店)"},
        {"id": "d8_3", "task": "🎁 名古屋車站周邊百貨最後伴手禮採買"}
    ],
    "Day 9 (7/21)": [
        {"id": "d9_1", "task": "☕ 咖啡廳體驗名古屋特色「點飲料送早餐 (小倉吐司)」"},
        {"id": "d9_2", "task": "🧳 飯店退房，確認行李件數"},
        {"id": "d9_3", "task": "🚆 搭乘名鐵前往中部國際機場"},
        {"id": "d9_4", "task": "✈️ 16:40 搭乘航班 CX531 準備回家"}
    ]
}

# --- 4. 狀態管理 (取代 LocalStorage) ---
if 'progress' not in st.session_state:
    st.session_state.progress = []

# 計算總任務與完成度
total_tasks = sum(len(tasks) for tasks in itinerary.values())
completed_tasks = len(st.session_state.progress)
progress_percent = int((completed_tasks / total_tasks) * 100) if total_tasks > 0 else 0

# --- 5. 畫面佈局：頂部資訊 ---
st.title("🎒 名古屋・白川鄉親子遊")

# 動態倒數計時 (設定為 2026/07/13)
target_date = datetime(2026, 7, 13)
days_left = (target_date - datetime.now()).days

if days_left > 0:
    st.info(f"🚀 距離出發還有 **{days_left}** 天！滿心期待！")
elif days_left >= -8:  # 旅程為 9天8夜，所以到 -8 天為止都算進行中
    st.success("✨ 旅程進行中！Have Fun!")
else:
    st.warning("🏠 旅程已圓滿結束，歡迎回家！")

# 進度條
st.caption(f"旅程打卡進度: {progress_percent}%")
st.progress(progress_percent)
st.divider()

# --- 6. 畫面佈局：每日行程與打卡邏輯 ---
# 取得所有天數的名稱
days_list = list(itinerary.keys())

# 使用 Tabs 建立分頁，讓 9 天的行程分開顯示
tabs = st.tabs(days_list)

# 將每天的任務填入對應的 Tab 裡
for i, day in enumerate(days_list):
    with tabs[i]:
        st.subheader(day)
        
        tasks = itinerary[day]
        for task_info in tasks:
            task_id = task_info["id"]
            task_desc = task_info["task"]
            
            # 檢查是否已完成
            is_checked = task_id in st.session_state.progress
            
            # 產生 Checkbox
            changed = st.checkbox(task_desc, value=is_checked, key=f"check_{task_id}")
            
            # 狀態更新邏輯
            if changed and task_id not in st.session_state.progress:
                st.session_state.progress.append(task_id)
                st.rerun()
            elif not changed and task_id in st.session_state.progress:
                st.session_state.progress.remove(task_id)
                st.rerun()

st.divider()

# --- 7. 功能按鈕 ---
# 使用 columns 讓按鈕置中或排版好看
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    if st.button("🗑️ 重置所有打卡紀錄", use_container_width=True):
        st.session_state.progress = []
        st.rerun()
