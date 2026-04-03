import streamlit as st
from datetime import datetime

# --- 1. 乾淨的原生設定 (捨棄容易破圖的 CSS) ---
st.set_page_config(page_title="名古屋親子遊", page_icon="🎒", layout="centered")

# --- 2. 豐富化的行程資料庫 (加入細節與地圖連結) ---
itinerary = {
    "Day 1 (7/13) - 抵達與安頓": [
        {"id": "d1_1", "task": "✈️ 15:30 抵達名古屋 NGO", "detail": "航班 CX530。領行李、過海關、裝網卡。"},
        {"id": "d1_2", "task": "🚆 搭名鐵前往名古屋車站", "detail": "尋找「名鐵線」指標，搭乘 μ-SKY 或特急列車往名古屋。"},
        {"id": "d1_3", "task": "🏨 入住 HOTEL LiVEMAX BUDGET", "detail": "位於太閤通口。記得確認嬰兒推車是否方便進出電梯。\n[📍 點我開 Google Map 導航](https://maps.app.goo.gl/YourMapLinkHere)"},
        {"id": "d1_4", "task": "🍜 ESCA 地下街晚餐", "detail": "就在車站旁邊。推薦名店：矢場味噌豬排、鳥開親子丼、吉田麵。"}
    ],
    "Day 2 (7/14) - 經典市區": [
        {"id": "d2_1", "task": "🎒 備妥推車、尿布、水壺出門", "detail": "今天預計會走比較多路，請確認推車狀態。"},
        {"id": "d2_2", "task": "🏯 名古屋城散步", "detail": "搭乘地鐵名城線至「市役所站」。園區平坦好推推車，可慢慢散步拍照。"},
        {"id": "d2_3", "task": "🛍️ 榮町商圈吃午餐 / 逛街", "detail": "百貨公司多，尋找有舒適冷氣和育嬰室的百貨吃午餐。"},
        {"id": "d2_4", "task": "🌃 綠洲21 (Oasis 21) 夜景", "detail": "宇宙船造型建築，晚上點燈很美，小孩可在底層廣場活動。"}
    ],
    "Day 3 (7/15) - 港區放電": [
        {"id": "d3_1", "task": "🎒 攜帶防曬與小孩替換衣物", "detail": "今天在水族館可能會有玩水或流汗的狀況。"},
        {"id": "d3_2", "task": "🐠 名古屋港水族館", "detail": "搭乘地鐵名港線至「名古屋港站」。\n必看亮點：海豚秀、小白鯨、企鵝。室內避暑首選！"},
        {"id": "d3_3", "task": "🚢 參觀南極觀測船富士號", "detail": "就在水族館旁邊，視小孩體力決定是否登船參觀。"},
        {"id": "d3_4", "task": "🍽️ 港區周邊吃晚餐", "detail": "可在水族館周邊商場解決晚餐，避開市區下班人潮。"}
    ],
    "Day 4 (7/16) - 童話合掌村": [
        {"id": "d4_1", "task": "🚌 08:00 太閤通口集合出發", "detail": "參加一日團。⚠️ 務必攜帶：輕便好收折的傘車、小孩安撫零食/玩具。"},
        {"id": "d4_2", "task": "🥩 飛驒高山老街散步", "detail": "中午抵達高山。必吃：飛驒牛握壽司、五平餅。"},
        {"id": "d4_3", "task": "🛖 漫步白川鄉合掌村", "detail": "世界遺產打卡！若要上觀景台需轉搭接駁車，推車需收折。"},
        {"id": "d4_4", "task": "🚌 傍晚返回飯店解散", "detail": "預計 18:00-19:00 回到名古屋車站，直接在周邊吃晚餐。"}
    ],
    "Day 5 (7/17) - 樂高日": [
        {"id": "d5_1", "task": "🎒 準備防曬、水與滿滿體力", "detail": "前往樂高樂園。搭乘青波線至「金城埠頭站」。"},
        {"id": "d5_2", "task": "🧱 名古屋樂高樂園", "detail": "專為 2-12 歲設計，設施非常溫和。建議先下載官方 App 查看設施等待時間。"},
        {"id": "d5_3", "task": "🚄 磁浮鐵道館 (彈性)", "detail": "在樂高樂園旁邊。如果小孩提早離開樂高還有體力，可以進去看超大新幹線。"}
    ],
    "Day 6 (7/18) - 麵包超人": [
        {"id": "d6_1", "task": "🍞 名古屋麵包超人兒童博物館", "detail": "搭乘直達巴士前往長島度假村。學齡前幼童的天堂，絕對會失心瘋！"},
        {"id": "d6_2", "task": "🛍️ 三井 Outlet 爵士之夢長島", "detail": "大人血拚時間！日本最大級 Outlet，爸媽可輪流顧小孩去逛。"},
        {"id": "d6_3", "task": "🚌 搭乘巴士返回市區", "detail": "留意末班車時間。"}
    ],
    "Day 7 (7/19) - 悠閒散步": [
        {"id": "d7_1", "task": "⛩️ 大須觀音參拜", "detail": "搭乘地鐵鶴舞線至「大須觀音站」。"},
        {"id": "d7_2", "task": "🍡 大須商店街逛街", "detail": "有巨大雨棚，推嬰兒車逛街很舒服。買藥妝、吃大須小吃（如炸雞、糰子）。"},
        {"id": "d7_3", "task": "🌳 久屋大通公園", "detail": "下午若想讓小孩在草地上跑跳放電，可以來這裡散步喝咖啡。"}
    ],
    "Day 8 (7/20) - 網美與採買": [
        {"id": "d8_1", "task": "📸 則武森林 (Noritake Garden)", "detail": "極美的紅磚建築群與陶瓷博物館，適合拍全家福。"},
        {"id": "d8_2", "task": "📚 AEON Mall 則武新町店", "detail": "緊鄰則武森林。室內育嬰設施完善，必拍絕美「蔦屋書店」大書牆。"},
        {"id": "d8_3", "task": "🎁 車站周邊最後採買", "detail": "回飯店前，在高島屋或名鐵百貨補齊伴手禮（小倉吐司餅乾、青柳外郎糕）。"}
    ],
    "Day 9 (7/21) - 準備回家": [
        {"id": "d9_1", "task": "☕ 體驗名古屋特色早餐", "detail": "找間飯店附近的咖啡廳（如 Komeda），體驗「點飲料送早餐 (小倉吐司)」文化。"},
        {"id": "d9_2", "task": "🧳 飯店退房與行李確認", "detail": "10:00 前退房。清點行李件數。"},
        {"id": "d9_3", "task": "🚆 搭名鐵前往機場", "detail": "建議中午左右就出發前往中部國際機場，機場內也有很多好逛的。"},
        {"id": "d9_4", "task": "✈️ 16:40 航班 CX531", "detail": "準備登機，平安回家！"}
    ]
}

# --- 3. 狀態管理 ---
if 'progress' not in st.session_state:
    st.session_state.progress = []

total_tasks = sum(len(tasks) for tasks in itinerary.values())
completed_tasks = len(st.session_state.progress)
progress_percent = int((completed_tasks / total_tasks) * 100) if total_tasks > 0 else 0

# --- 4. 畫面佈局：頂部資訊 ---
st.title("🎒 名古屋親子遊導覽")

target_date = datetime(2026, 7, 13)
days_left = (target_date - datetime.now()).days

col1, col2 = st.columns([2, 1])
with col1:
    if days_left > 0:
        st.info(f"🚀 距離出發還有 **{days_left}** 天")
    elif days_left >= -8:
        st.success("✨ 旅程進行中！")
    else:
        st.warning("🏠 旅程已圓滿結束")
with col2:
    st.metric(label="完成度", value=f"{progress_percent}%")

st.progress(progress_percent)
st.divider()

# --- 5. 畫面佈局：下拉式選單與每日行程 ---
days_list = list(itinerary.keys())
# 手機版最友善的 Dropdown 導航
selected_day = st.selectbox("📅 選擇行程天數：", days_list)

st.subheader(selected_day)
tasks = itinerary[selected_day]

# 顯示該日的任務
for task_info in tasks:
    task_id = task_info["id"]
    task_desc = task_info["task"]
    task_detail = task_info.get("detail", "")
    
    is_checked = task_id in st.session_state.progress
    
    # 每個任務使用 Expander 包裝，畫面乾淨又能看細節
    with st.expander(f"{'✅ ' if is_checked else '⬜ '}{task_desc}", expanded=not is_checked):
        # 顯示詳細資訊（支援 Markdown, 可以放連結）
        st.markdown(task_detail)
        
        # 打卡按鈕
        changed = st.checkbox("完成此任務", value=is_checked, key=f"check_{task_id}")
        
        if changed and task_id not in st.session_state.progress:
            st.session_state.progress.append(task_id)
            st.rerun()
        elif not changed and task_id in st.session_state.progress:
            st.session_state.progress.remove(task_id)
            st.rerun()

st.divider()

# --- 6. 每日專屬筆記區 ---
st.subheader("📝 今日筆記 (花費/紀錄)")
note_key = f"note_{selected_day}"
if note_key not in st.session_state:
    st.session_state[note_key] = ""

# 使用 text_area 讓你可以隨手打字紀錄
current_note = st.text_area("在這裡紀錄想說的話...", value=st.session_state[note_key], height=100)
if current_note != st.session_state[note_key]:
    st.session_state[note_key] = current_note

st.divider()

# --- 7. 重置按鈕 ---
if st.button("🗑️ 重置所有打卡紀錄", use_container_width=True):
    st.session_state.progress = []
    st.rerun()
