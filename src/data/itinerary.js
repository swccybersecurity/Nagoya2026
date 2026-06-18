const B = import.meta.env.BASE_URL + 'images/'

export const TRIP = {
  title: '名古屋親子遊 2026',
  subtitle: '三大人．兩小孩的夏日冒險',
  start: new Date('2026-07-13'),
  end:   new Date('2026-07-21'),
  flightOut: 'CX530',
  flightRtn: 'CX531',
}

export const HOTEL = {
  name:    '名古屋王子大飯店天空塔',
  nameEn:  'Nagoya Prince Hotel Sky Tower',
  station: '笹島ライブ駅（あおなみ線）直通',
  floor:   '全室 32 樓以上・140m 高・城市景觀',
  tip:     '入住時可購買 LEGOLAND + SEA LIFE 套票（Day 5 用），省去網路搶票',
  phone:   '+81-52-565-1110',
  map:     'https://www.google.com/maps/search/?api=1&query=Nagoya+Prince+Hotel+Sky+Tower',
}

export const TIPS = [
  {
    icon: '☀️',
    variant: 'kaki',
    title: '7 月防暑必備',
    body: '名古屋是日本數一數二的高溫城市，均溫 34–36°C、體感近 40°C。隨身攜帶手持電風扇、冷卻毛巾、SPF50 防曬與帽子。安排水族館、樂高等室內景點在 11:00–15:00 正午時段。',
  },
  {
    icon: '🚇',
    variant: 'yamabuki',
    title: '交通卡 manaca',
    body: '抵達名古屋站後立即購買 manaca 卡（¥500 押金），可在地鐵、名鐵、巴士通用。週末假日地鐵一日乘車券 ¥760（平日 ¥870），多個景點當天可考慮購買。',
  },
  {
    icon: '🧒',
    variant: 'fuji',
    title: '5歲＋3歲行程節奏',
    body: '每天安排一個主景點即可，不要貪多。下午 14:00 後安排低強度活動或回飯店休息。犬山城天守樓梯很陡，3 歲建議大人背上樓；樂高有部分戶外設施，記得補防曬。',
  },
  {
    icon: '🍱',
    variant: 'yamabuki',
    title: '名古屋飲食文化',
    body: '必嚐：味噌豬排（矢場とん）、小倉吐司早餐（Komeda 咖啡）、手羽先炸雞翅（風来坊）、吉田麵。百貨公司地下街育嬰室完善，是帶小孩吃飯的好選擇。',
  },
  {
    icon: '🎫',
    variant: 'kaki',
    title: '票券攻略',
    body: 'LEGOLAND 建議從飯店購買套票或提前網路購票，現場票較貴。磁浮鐵道館需事先至官網預約入館時間（免費但有名額限制），現場常一位難求。',
  },
  {
    icon: '🆘',
    variant: 'fuji',
    title: '緊急資訊',
    body: '駐大阪台灣辦事處（管轄名古屋）：+81-6-6443-8481。飯店 24 小時多語言線上醫生服務。旅遊保險建議出發前確認醫療理賠額度。',
  },
]

export const CHECKLIST = [
  { id: 'c1',  cat: '證件',  text: '護照（確認有效期限 6 個月以上）' },
  { id: 'c2',  cat: '證件',  text: '小孩護照' },
  { id: 'c3',  cat: '證件',  text: '旅遊平安保險' },
  { id: 'c4',  cat: '票券',  text: '訂妥 CX530 / CX531 機票' },
  { id: 'c5',  cat: '票券',  text: '訂妥名古屋王子大飯店' },
  { id: 'c6',  cat: '票券',  text: '磁浮鐵道館預約（官網免費預約）' },
  { id: 'c7',  cat: '票券',  text: '白川鄉一日遊巴士或常滑行程確認' },
  { id: 'c8',  cat: '通訊',  text: '日本網卡（機場取or出發前到手）' },
  { id: 'c9',  cat: '通訊',  text: 'Google Maps 離線地圖（名古屋、犬山、白川鄉）下載' },
  { id: 'c10', cat: '小孩',  text: '折疊輕便推車（景點收折備用）' },
  { id: 'c11', cat: '小孩',  text: '小孩常備藥（退燒藥、腸胃藥、防蚊液）' },
  { id: 'c12', cat: '小孩',  text: '防曬乳（SPF50+）× 全家份' },
  { id: 'c13', cat: '小孩',  text: '手持電風扇' },
  { id: 'c14', cat: '小孩',  text: '兒童水壺（保冷）' },
  { id: 'c15', cat: '行李',  text: '信用卡（VISA/Master，JCB 更好用）' },
  { id: 'c16', cat: '行李',  text: '日幣現金（建議帶 ¥50,000 備用）' },
  { id: 'c17', cat: '行李',  text: 'manaca 卡購買清單（抵達後第一件事）' },
]

export const BUDGET_DAYS = [
  { day: 1, label: 'Day 1・移動日',       amount: 3500  },
  { day: 2, label: 'Day 2・名古屋城',     amount: 4200  },
  { day: 3, label: 'Day 3・水族館',       amount: 7200  },
  { day: 4, label: 'Day 4・白川鄉/常滑',  amount: 5500  },
  { day: 5, label: 'Day 5・LEGOLAND',     amount: 25000 },
  { day: 6, label: 'Day 6・麵包超人',     amount: 12000 },
  { day: 7, label: 'Day 7・大須商圈',     amount: 4000  },
  { day: 8, label: 'Day 8・犬山城',       amount: 6500  },
  { day: 9, label: 'Day 9・返程日',       amount: 3000  },
]

export const days = [
  // ────── Day 1 ──────
  {
    id: 1, num: '01', date: '7/13（一）',
    title: '抵達！名古屋初見',
    badgeClass: 'badge-day-1',
    tag: { text: '移動日', cls: 'bg-yamabuki-100 text-yamabuki-700 border-yamabuki-300' },
    budget: { label: '當日預估花費', amount: '3,500', note: '含機場交通、晚餐' },
    cover: B + 'airport.jpg',
    timeline: [
      { time: '15:30', html: '✈️ 抵達中部國際機場（NGO）— 航班 CX530<br><span class="text-ivory-600 text-sm">領行李 → 過海關 → 裝網卡</span>' },
      { time: '16:00', html: '🚆 名鐵 μSKY 特急前往名古屋站<br><span class="text-ivory-600 text-sm">大人 ¥1,250 / 兒童 ¥630，約 28 分鐘</span>' },
      { time: '17:00', html: '🏨 飯店 Check-in<br><span class="text-ivory-600 text-sm">名古屋王子大飯店，笹島ライブ駅直通</span>' },
      { time: '18:30', html: '🍜 ESCA 地下街晚餐<br><span class="text-ivory-600 text-sm">矢場味噌豬排 / 鳥開親子丼 / 吉田麵，步行 5 分鐘</span>' },
    ],
    highlights: [
      { variant: 'yamabuki', title: '🚆 機場交通',
        body: '名鐵 μSKY 特急 28 分鐘直達名古屋站。入關後在機場購買 manaca 交通卡（¥500 押金），方便後續市區移動。' },
      { variant: 'default',  title: '🏨 入住小提醒',
        body: '詢問 LEGOLAND + SEA LIFE 套票（Day 5 用）。全室 32 樓以上，入夜後可俯瞰名古屋金鯱夜景。' },
    ],
  },

  // ────── Day 2 ──────
  {
    id: 2, num: '02', date: '7/14（二）',
    title: '名古屋城 → 榮町商圈',
    badgeClass: 'badge-day-2',
    tag: { text: '市區探索', cls: 'bg-kaki-50 text-kaki-600 border-kaki-300' },
    budget: { label: '當日預估花費', amount: '4,200', note: '含票價、午晚餐' },
    cover: B + 'nagoya_castle.png',
    timeline: [
      { time: '09:30', html: '🏯 名古屋城散步<br><span class="text-ivory-600 text-sm">地鐵名城線「市役所站」，大人 ¥500 / 國中以下免費</span>' },
      { time: '12:00', html: '🚇 地鐵前往榮町（約 20 分）' },
      { time: '12:30', html: '🍽️ 榮町商圈午餐<br><span class="text-ivory-600 text-sm">百貨公司育嬰室完善，冷氣強</span>' },
      { time: '14:00', html: '🛍️ 逛街自由時間' },
      { time: '18:30', html: '🌃 綠洲 21 夜景<br><span class="text-ivory-600 text-sm">宇宙船造型點燈，廣場讓小孩奔跑</span>' },
    ],
    highlights: [
      { variant: 'yamabuki', title: '🏯 名古屋城現況',
        body: '主天守閣正進行木造復元工事（整修中），目前開放本丸御殿與周邊腹地。腹地寬廣，7 月建議 9:00 開門即入場，11:00 前離開。' },
      { variant: 'green',    title: '🌃 綠洲 21 推薦',
        body: '免費入場，晚上點燈後非常漂亮。廣場草坪適合小孩跑跳，週邊有多間餐廳可選。' },
    ],
  },

  // ────── Day 3 ──────
  {
    id: 3, num: '03', date: '7/15（三）',
    title: '名古屋港水族館',
    badgeClass: 'badge-day-3',
    tag: { text: '親子必去', cls: 'bg-sky-50 text-sky-700 border-sky-200' },
    budget: { label: '當日預估花費', amount: '7,200', note: '水族館＋富士號＋餐費' },
    cover: B + 'aquarium.jpg',
    timeline: [
      { time: '10:00', html: '🐠 名古屋港水族館<br><span class="text-ivory-600 text-sm">地鐵名港線「名古屋港站」，大人 ¥2,030 / 5歲 ¥500 / 3歲免費</span>' },
      { time: '12:00', html: '🍱 水族館內商場午餐' },
      { time: '14:00', html: '🚢 南極觀測船富士號<br><span class="text-ivory-600 text-sm">大人 ¥300 / 幼兒免費，就在水族館旁</span>' },
      { time: '17:00', html: '🍽️ Jetty 港區商場晚餐<br><span class="text-ivory-600 text-sm">避開市區下班人潮</span>' },
    ],
    highlights: [
      { variant: 'sky',      title: '🐬 必看：海豚秀',
        body: '入場後立即確認海豚秀時間。白鯨館、企鵝館也是重點，5 歲女生大概捨不得走。全館室內冷氣，7 月正午最適合泡在這裡。' },
      { variant: 'yamabuki', title: '💴 票價精算（3大2小）',
        list: ['大人 ¥2,030 × 3 = ¥6,090', '5 歲 ¥500 × 1 = ¥500', '3 歲免費', '南極觀測船 ¥300 × 3 = ¥900'] },
    ],
  },

  // ────── Day 4 (DUAL PLAN) ──────
  {
    id: 4, num: '04', date: '7/16（四）',
    title: '選擇今天的冒險',
    badgeClass: 'badge-day-4',
    tag: { text: '二選一', cls: 'bg-fuji-100 text-fuji-700 border-fuji-300' },
    cover: B + 'shirakawa.jpg',
    isDualPlan: true,
    plans: [
      {
        id: 'shirakawa',
        label: '🏔️ 白川鄉',
        sublabel: '世界遺產路線',
        coverImg: B + 'shirakawa.jpg',
        budget: { label: '當日預估花費', amount: '6,500', note: '含巴士、午餐、合掌村' },
        timeline: [
          { time: '08:00', html: '🚌 太閤通口搭遊覽車出發<br><span class="text-ivory-600 text-sm">攜帶：輕便折疊車、零食玩具備用</span>' },
          { time: '10:30', html: '🛖 抵達白川鄉合掌村<br><span class="text-ivory-600 text-sm">自由漫步合掌屋群落，荻町城跡展望台俯瞰全景</span>' },
          { time: '13:00', html: '🍡 午餐＆村內參觀<br><span class="text-ivory-600 text-sm">五平餅、岩魚定食、合掌建築體驗</span>' },
          { time: '15:30', html: '🚌 上車返回名古屋' },
          { time: '18:00', html: '🍜 回名古屋周邊晚餐' },
        ],
        highlights: [
          { variant: 'fuji',    title: '🌿 白川鄉小提醒',
            body: '觀景台接駁車需收折推車。夏季人潮較少比冬季清幽，合掌屋保有綠意，適合帶小孩慢慢走。' },
          { variant: 'default', title: '⏱️ 行程說明',
            body: '本版本省略飛驒高山老街，車程縮短約 2–3 小時，全程約 8 小時，對小孩更友善。' },
        ],
      },
      {
        id: 'tokoname',
        label: '🏺 常滑',
        sublabel: '輕鬆備案路線',
        coverImg: B + 'osustreet.jpg',
        budget: { label: '當日預估花費', amount: '3,800', note: '含交通、午餐、陶藝體驗' },
        timeline: [
          { time: '09:30', html: '🚆 名古屋站搭名鐵前往常滑站<br><span class="text-ivory-600 text-sm">約 40 分鐘，兒童票 ¥290</span>' },
          { time: '10:30', html: '🏺 やきもの散歩道<br><span class="text-ivory-600 text-sm">招財貓大道、古窯跡、陶磁器煙囪</span>' },
          { time: '12:00', html: '🍜 老街午餐' },
          { time: '13:30', html: '🎨 INAX ライブミュージアム（彈性）<br><span class="text-ivory-600 text-sm">互動陶藝展，可動手體驗</span>' },
          { time: '15:00', html: '🚆 返回名古屋，下午自由活動' },
          { time: '17:00', html: '🏨 提早回飯店讓小孩補眠' },
        ],
        highlights: [
          { variant: 'green',   title: '😊 為什麼選常滑？',
            body: '白川鄉路線車程長、小孩體力吃緊時的完美備案。招財貓街道小孩很愛，沿途有遮蔭，步行輕鬆。' },
          { variant: 'yamabuki', title: '✈️ 小彩蛋',
            body: '常滑市就在 NGO 機場旁邊（10 分鐘），若 Day 9 有剩餘時間也可順路再逛一次。' },
        ],
      },
    ],
  },

  // ────── Day 5 ──────
  {
    id: 5, num: '05', date: '7/17（五）',
    title: '樂高王國征服日',
    badgeClass: 'badge-day-5',
    tag: { text: '小孩爆炸', cls: 'bg-orange-50 text-orange-600 border-orange-300' },
    budget: { label: '當日預估花費', amount: '25,000', note: '含 4 張門票（門票建議飯店購）' },
    cover: B + 'legolnad.jpg',
    timeline: [
      { time: '09:30', html: '🧱 出發前往 LEGOLAND Japan<br><span class="text-ivory-600 text-sm">あおなみ線「金城埠頭站」，飯店 1 站直達</span>' },
      { time: '10:00', html: '🎢 LEGOLAND Japan 全日玩耍<br><span class="text-ivory-600 text-sm">大人 ¥6,200～ / 兒童 ¥4,700～（暑假期間）<br>先下載官方 App 查等候時間</span>' },
      { time: '15:00', html: '🚄 磁浮鐵道館（彈性）<br><span class="text-ivory-600 text-sm">大人 ¥1,000 / 幼兒免費 ⚠️ 需事先網路預約！</span>' },
      { time: '18:00', html: '🍽️ 飯店商場或周邊晚餐' },
    ],
    highlights: [
      { variant: 'yamabuki', title: '🎫 票務攻略',
        body: '建議在飯店 Check-in 時購買 LEGOLAND + SEA LIFE 套票，省去網路搶票。票價依季節浮動，暑假為高峰期。' },
      { variant: 'kaki',     title: '🚄 磁浮鐵道館注意',
        body: '人氣高，現場常額滿，務必提前至官網預約入館時段（免費）。3 歲男生看到巨大新幹線應該不想離開。' },
    ],
  },

  // ────── Day 6 ──────
  {
    id: 6, num: '06', date: '7/18（六）',
    title: '麵包超人 × 三井 Outlet',
    badgeClass: 'badge-day-6',
    tag: { text: '長島度假村', cls: 'bg-pink-50 text-pink-600 border-pink-300' },
    budget: { label: '當日預估花費', amount: '12,000', note: '博物館票＋購物＋交通＋餐費' },
    cover: B + 'anpanman.jpg',
    timeline: [
      { time: '09:00', html: '🚌 名鐵バスセンター搭高速巴士<br><span class="text-ivory-600 text-sm">前往長島度假村，約 40 分鐘</span>' },
      { time: '10:00', html: '🍞 麵包超人兒童博物館<br><span class="text-ivory-600 text-sm">大人 / 兒童（1 歲以上）均 ¥2,500，全室內冷氣</span>' },
      { time: '13:00', html: '🍜 長島商場午餐' },
      { time: '14:00', html: '🛍️ 三井 Outlet 爵士之夢長島<br><span class="text-ivory-600 text-sm">日本最大 Outlet，240+ 品牌</span>' },
      { time: '17:00', html: '🚌 巴士返回名古屋' },
    ],
    highlights: [
      { variant: 'pink',     title: '🍞 博物館攻略',
        body: '建議 10:00 開館即入場，人潮集中於 11:00 後。館內有角色互動表演與合照時間，5 歲以下最喜歡。' },
      { variant: 'yamabuki', title: '🛍️ Outlet 採購',
        body: '戶外品牌（Columbia、The North Face）選擇多。名牌可看 Annex 區。記得輪流顧小孩讓另一半逛。' },
    ],
  },

  // ────── Day 7 ──────
  {
    id: 7, num: '07', date: '7/19（日）',
    title: '大須商圈悠閒散步',
    badgeClass: 'badge-day-7',
    tag: { text: '輕鬆日', cls: 'bg-emerald-50 text-emerald-700 border-emerald-200' },
    budget: { label: '當日預估花費', amount: '4,000', note: '含餐費、零食、藥妝' },
    cover: B + 'osustreet.jpg',
    timeline: [
      { time: '10:00', html: '⛩️ 大須觀音參拜<br><span class="text-ivory-600 text-sm">地鐵鶴舞線「大須觀音站」</span>' },
      { time: '10:30', html: '🍡 大須商店街漫遊<br><span class="text-ivory-600 text-sm">700m 全覆蓋雨棚，炸雞、糰子、藥妝掃貨</span>' },
      { time: '13:00', html: '🍜 商店街內午餐' },
      { time: '15:00', html: '🌳 久屋大通公園<br><span class="text-ivory-600 text-sm">兒童遊樂區＋草坪，傍晚涼快後放電</span>' },
      { time: '17:30', html: '🏨 返回飯店休息' },
    ],
    highlights: [
      { variant: 'green',    title: '☔ 大須商店街優點',
        body: '700 公尺全覆蓋雨棚，7 月下午陣雨不怕。有多間藥妝、100 均、古著店，有趣不貴，推車也順暢。' },
      { variant: 'yamabuki', title: '🌳 久屋大通公園',
        body: '2020 年整修後煥然一新，有兒童遊樂區與草坪。傍晚涼快後讓小孩盡情放電，大人坐著喝咖啡。' },
    ],
  },

  // ────── Day 8 ──────
  {
    id: 8, num: '08', date: '7/20（一）',
    title: '犬山城下町日帰り',
    badgeClass: 'badge-day-8',
    tag: { text: '國寶天守閣', cls: 'bg-yamabuki-100 text-yamabuki-700 border-yamabuki-300' },
    budget: { label: '當日預估花費', amount: '6,500', note: '含交通、票價、午餐、伴手禮' },
    cover: B + 'dogmount.jpg',
    timeline: [
      { time: '09:00', html: '🚆 名古屋站搭名鐵犬山線<br><span class="text-ivory-600 text-sm">約 30 分鐘抵達犬山站</span>' },
      { time: '09:30', html: '🏯 犬山城<br><span class="text-ivory-600 text-sm">大人 ¥1,000 / 兒童 ¥200 ⚠️ 天守樓梯陡，3 歲需大人背</span>' },
      { time: '11:30', html: '🍡 犬山老街散步<br><span class="text-ivory-600 text-sm">山椒煎餅、草莓大福、五平餅</span>' },
      { time: '13:00', html: '🍜 老街午餐' },
      { time: '14:30', html: '🚆 名鐵返回名古屋（約 30 分）' },
      { time: '16:00', html: '🎁 JR 名古屋高島屋 B1 掃伴手禮<br><span class="text-ivory-600 text-sm">外郎餅・ゆかり蝦煎餅・なごやん</span>' },
    ],
    highlights: [
      { variant: 'yamabuki', title: '🏯 犬山城注意事項',
        body: '日本現存最古老天守閣（國寶）。樓梯非常陡，5 歲需牽手，3 歲強烈建議用背帶背上樓；推車請寄放城下。' },
      { variant: 'default',  title: '🎁 伴手禮清單',
        list: ['JR 名古屋高島屋 B1：種類最齊全（推薦）', 'KITTE 名古屋：文青選品', '機場 NGO 出境層：最後備用（選擇較少）'] },
    ],
  },

  // ────── Day 9 ──────
  {
    id: 9, num: '09', date: '7/21（二）',
    title: 'Komeda 早餐 → 返程',
    badgeClass: 'badge-day-9',
    tag: { text: '返程日', cls: 'bg-slate-100 text-slate-600 border-slate-300' },
    budget: { label: '當日預估花費', amount: '3,000', note: '含早餐、機場交通' },
    cover: B + 'komeda.jpg',
    timeline: [
      { time: '08:00', html: '☕ Komeda 咖啡早餐<br><span class="text-ivory-600 text-sm">點飲料送小倉厚片吐司（Morning Service），名古屋必體驗！</span>' },
      { time: '10:00', html: '🧳 飯店退房<br><span class="text-ivory-600 text-sm">清點行李件數，10:00 前退房</span>' },
      { time: '10:30', html: '🚆 搭あおなみ線 + 名鐵 μSKY 前往機場<br><span class="text-ivory-600 text-sm">建議 13:30 前抵達 NGO</span>' },
      { time: '16:40', html: '✈️ 航班 CX531 返台<br><span class="text-ivory-600 text-sm">再見名古屋，下次再來！</span>' },
    ],
    highlights: [
      { variant: 'yamabuki', title: '☕ Komeda 文化',
        body: '早上點任何飲料，免費附贈小倉厚片吐司（Morning Service）。這是名古屋獨有的早餐文化，務必體驗一次。' },
      { variant: 'default',  title: '⏰ 回程時間軸',
        list: ['10:00 退房', '10:30 搭あおなみ線', '11:00 名古屋站換名鐵 μSKY', '11:30 抵達 NGO 機場', '13:30 最晚入關'] },
    ],
  },
]
