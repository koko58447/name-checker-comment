import streamlit as st

# Page Title with Custom Style
st.markdown("""
    <h1 style='text-align: center; color: #2E7ABC;'>မြန်မာအညွှန်း</h1>
    <p style='text-align: right; font-style: italic; color: #555;'>အမျိုးသားဉာဏ်ရည်တုနည်းပညာဖွံ့ဖြိုးတိုးတက်ရေးစီမံကိန်း</p>
""", unsafe_allow_html=True)

# Content with Styling
st.markdown("""
<style>
    .content-box {
        background-color: #F9F9F9;
        padding: 20px;
        border-radius: 10px;
        box-shadow: 0 4px 8px rgba(0,0,0,0.1);
        line-height: 2.8;
        font-size: 16px;
        color: #333;
    }
    ul {
        margin-left: 20px;
    }
    li {
        margin-bottom: 12px;
        padding-bottom: 4px;
        border-bottom: 1px dashed #ccc; /* အောက်မှာအစင်းလေးဆွဲထားတာလို့ ထပ်ပြင်နိုင် */
    }

</style>

""", unsafe_allow_html=True)

# Table Header
header = [
    "စဉ်",
    "မြန်မာဗျည်း",
    "အသံထွက်သင်္ကေတ (မြန်-လိပ် ၂၀၁၉)",
    "အင်္ဂလိပ်အက္ခရာ ဖလှယ်နည်းစနစ် (MLLIP)",
    "အမည် သာဓက",
    "အင်္ဂလိပ်အက္ခရာ ဖလှယ်နည်း သာဓက"
]

# Table Data
data = [
    ["၁", "က", "/k/", "ka", "ကရား", "Ka Yarr"],
    ["၂", "ခ", "/kh/", "kha", "ခရေ", "Kha Yay"],
    ["၃", "ဂ/ဃ", "/g/", "ga", "ဂမုန်းပွင့်", "Ga Mone Pwint"],
    ["၄", "င", "/ng/", "nga", "ငပလီ", "Nga Pa Le"],
    ["၅", "စ", "/s/", "sa", "စမုန်မြစ်", "Sa Moun Myit"],
    ["၆", "ဆ", "/hs/", "hsa", "ဆလတ်ရွက်", "Hsa Lat Ywet"],
    ["၇", "ဇ / ဈ", "/z/", "za", "ဇလပ်ဝါ", "Za Lap War"],
    ["၈", "ည/ဉ", "/nj/", "nya", "ဉာဏ်မှူး/မိုးည", "Nyan Hmue/Moe Nya"],
    ["၉", "ဋ / တ", "/t/", "ta", "တမာပင်", "Ta Mar Pin"],
    ["၁၀", "ဌ / ထ", "/ht/", "hta", "ထမနဲ", "Hta Ma Nell"],
    ["၁၁", "ဍ၊ဎ / ဒ၊ဓ", "/d/", "da", "ဒလ", "Dala"],
    ["၁၂", "ဏ / န", "/n/", "na", "နယုန်လ", "Nayoun La"],
    ["၁၃", "ပ", "/p/", "pa", "ပပဝတီ", "Pa Pa Wa Te"],
    ["၁၄", "ဖ", "/hp/", "pha", "ဖရုံသီး", "Pha Youm Thee"],
    ["၁၅", "ဗ / ဘ", "/b/", "ba", "ဘစိုင်းဝဏ္ဏ", "Ba Sai Wunna"],
    ["၁၆", "မ", "/m/", "ma", "မခင်ငွေ", "Ma Khin Ngway"],
    ["၁၇", "ယ", "/j/", "ya", "ယမုန်နာ", "Ya Moun Nar"],
    ["၁၈", "ရ", "/r/", "ya/ra", "ရန်အောင်/သူရ", "Yan Aung/Thuura"],
    ["၁၉", "လ / ဠ", "/l/", "la", "လမင်းအောင်", "La Minn Aung"],
    ["၂၀", "ဝ", "/w/", "wa", "ဝဥ", "Wa Ou"],
    ["၂၁", "သ", "/th/", "tha", "သမင်", "Tha Min"],
    ["၂၂", "ဟ", "/h/", "ha", "ဟဟာဟ", "Ha Har Ha"],
    ["၂၃", "ကျ / ကြ", "/kj/", "kya", "ကျပင်းဆရာဖီး", "Kya Pinn Hsayar Phee"],
    ["၂၄", "ချ / ခြ", "/ch/", "cha", "ချရားပင်", "Cha Yarr Pin"],
    ["၂၅", "ဂျ / ဂြ", "/gj/", "gya", "ဂျလေဘီမုန့်", "Gya Lay Be Mont"],
    ["၂၆", "ငှ", "/hng/", "hnga", "ငှက်ဖျား", "Hnget Phyarr"],
    ["၂၇", "ညှ", "/hnj/", "hnya", "ကြံညှပ်", "Kyam Hnyap"],
    ["၂၈", "နှ", "/hn/", "hna", "နှမ", "Hna Ma"],
    ["၂၉", "မှ", "/hm/", "hma", "မှာတမ်းလွှာ", "Hmar Tamm Hlwar"],
    ["၃၀", "ရှ", "/sh/", "sha", "ရှောက်ရွှာမိုး/ လျှောက်လွှာ", "Shauk Shwar Moe/Shauk Hlwar"],
    ["၃၁", "လှ", "/hl/", "hla", "လှဝင်းမောင်", "Hla Winn Maung"],
    ["၃၂", "ဝှ", "/hw/", "hwa", "လျှို့ဝှက်စာ", "Hlyoh Hwet Sar"],
    ["၃၃", "သှ", "/dh/", "tha", "သတင်းစာ", "Tha Tinn Sar"]
]

# CSS Styling for Table
st.markdown("""
<style>
.my-table {
    width: 100%;
    border-collapse: collapse;
    font-family: sans-serif;
    box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    margin-bottom: 30px;
}
.my-table thead th {
    background-color: #2E7ABC;
    color: white;
    padding: 12px;
    text-align: left;
}
.my-table tbody tr:nth-child(even) {
    background-color: #f2f2f2;
}
.my-table tbody tr:hover {
    background-color: #e9f5fb;
}
.my-table td {
    padding: 10px;
    border-bottom: 1px solid #ddd;
}
</style>
""", unsafe_allow_html=True)

# Render HTML Table
html_table = "<table class='my-table'>\n"

# Add Header
html_table += "<thead><tr>"
for col in header:
    html_table += f"<th>{col}</th>"
html_table += "</tr></thead>"

# Add Body
html_table += "<tbody>"
for row in data:
    html_table += "<tr>"
    for cell in row:
        html_table += f"<td>{cell}</td>"
    html_table += "</tr>"
html_table += "</tbody></table>"

# Display Table
st.markdown(html_table, unsafe_allow_html=True)

# Content List
content_list = [
    "အသံတူဗျည်းတစ်လုံးစီယူသည့် စနစ်အရ မြန်မာဗျည်းသံ ၃၃ သံ ရှိပါသည်။",
    "\"ကျ၊ ချ၊ ဂျ၊ ငှ၊ ညှ၊ နှ၊ မှ၊ ရှ၊ လှ၊ ဝှ၊ သှ\" တို့သည် သီးခြားဗျည်းသံများဖြစ်သည့်အတွက် သီးခြား ဗျည်းများအဖြစ် သတ်မှတ်ပါသည်။",
    "\"သှ\" မှာ သံပြင်း သ သံကို ညွှန်းခြင်းဖြစ်ပြီး သ အက္ခရာအောက်က အကောက်ကလေး ထည့်ရေးသားခြင်း ဖြစ်ပါသည်။ သှ ကိုလည်း tha ဟု စာလုံးပေါင်းပါသည်။",
]

# Styled HTML for List with Edit Icon
styled_html = """
<style>
.list-container {
    background-color: #F8F9FA;
    padding: 20px;
    border-radius: 10px;
    box-shadow: 0 4px 6px rgba(0,0,0,0.05);
    font-family: 'Myanmar3', sans-serif;
    color: #333;
}
.list-container ul {
    padding-left: 20px;
    list-style-type: none; /* default bullet ဖျက်ပါမယ် */
}
.list-container li {
    position: relative;
    padding-left: 30px;
    margin-bottom: 12px;
    line-height: 1.6;
}
.list-container li::before {
    content: '✍️'; /* edit icon */
    position: absolute;
    left: 0;
    top: 0;
    color: #2E7ABC; /* icon color */
    font-size: 18px;
}
</style>

<div class="list-container">
    <ul>
"""

# Add list items dynamically
for text in content_list:
    styled_html += f"<li>{text}</li>"

# Close the div and ul
styled_html += "</ul></div>"

# Display in Streamlit
st.markdown(styled_html, unsafe_allow_html=True)


# Table Header
header = [
    "စဉ်",
    "မြန်မာဗျည်းတွဲ",
    "အသံထွက်သင်္ကေတ (မြန်-လိပ် ၂၀၁၉)",
    "အင်္ဂလိပ်အက္ခရာ ဖလှယ်နည်းစနစ် (MLLIP)",
    "အမည် သာဓက",
    "အင်္ဂလိပ်အက္ခရာ ဖလှယ်နည်း သာဓက"
]

# Table Data
data = [
    ["၁", "ျ", "/j/", "y", "ယပင့်", "Ya Pint"],
    ["၂", "ြ", "/j/", "r/y", "ဗြာဟ္မီအက္ခရာ/ယယစ်", "Branme Etkharar/Ya Yit"],
    ["၃", "ွ", "/w/", "w", "ဝဆွဲ", "Wa Hswell"]
]

# CSS Styling for Table
st.markdown("""
""", unsafe_allow_html=True)

# Render HTML Table
html_table = "<table class='my-table'>\n"

# Add Header
html_table += "<thead><tr>"
for col in header:
    html_table += f"<th>{col}</th>"
html_table += "</tr></thead>"

# Add Body
html_table += "<tbody>"
for row in data:
    html_table += "<tr>"
    for cell in row:
        html_table += f"<td>{cell}</td>"
    html_table += "</tr>"
html_table += "</tbody></table>"

# Display Table
st.markdown(html_table, unsafe_allow_html=True)

# Content List
content_list = [
    "အသံထွက်စနစ်အရ ယပင့် (ျ)၊ ရရစ် (ြ)၊ ဝဆွဲ (ွ) တို့ကို ဗျည်းတွဲအဖြစ် သတ်မှတ်ပါသည်။",
    "ဟထိုး (ှ) တစ်သားတည်းဖြစ်နေသည့် \"ငှ၊ ညှ၊ နှ၊ မှ၊ ရှ၊ လှ၊ ဝှ\" တို့သည် သီးခြားဗျည်းများဖြစ်၍ ဟထိုး (ှ)ကို ဗျည်းတွဲအဖြစ် မသတ်မှတ်ပါ။"
]

# Styled HTML for List with Edit Icon
styled_html = """

<div class="list-container">
    <ul>
"""

# Add list items dynamically
for text in content_list:
    styled_html += f"<li>{text}</li>"

# Close the div and ul
styled_html += "</ul></div>"

# Display in Streamlit
st.markdown(styled_html, unsafe_allow_html=True)

# Table Header
header = [
    "စဉ်",
    "မြန်မာသရ",
    "အသံထွက်သင်္ကေတ (မြန်-လိပ် ၂၀၁၉)",
    "အင်္ဂလိပ်အက္ခရာ ဖလှယ်နည်းစနစ် (MLLIP)",
    "အမည် သာဓက",
    "အင်္ဂလိပ်အက္ခရာ ဖလှယ်နည်း သာဓက"
]


# Table Data
data = [
    ["၁", "အ", "/a/", "a", "အချစ်", "Achit"],
    ["၂", "အာ", "/a/", "ar", "အာကာမျိုး", "Ar Kar Myoe"],
    ["၃", "အ", "/a./", "ah", "မောင်အ", "Mg Ah"],
    ["၄", "အား", "/a:/", "arr", "ဦးဖိုးကျား", "U Phoe Kyarr"],
    ["၅", "အီ / ဤ / အည်", "/i/", "e/i", "ရီရီမြင့်/စည်သူဝင်း", "Ye Ye Myint/Sithuu Winn"],
    ["၆", "အိ / ဣ / ၏ / အည့်", "/i./", "ei", "အိအိချွန်/ ဖူးပြည့်ခိုင်/ အိနန္ဒာကျော့", "Ei Ei Chun/ Phoo Pyei Khaing/ Ei Nandar Kyawt"],
    ["၇", "အီး / အည်း", "/i:/", "ee", "နတ်သမီး", "Nat Tha Mee"],
    ["၈", "အူ / ဦ", "/u/", "uu", "သူဇာ/မူမူခိုင်", "Thuuzar/ Muu Muu Khaing"],
    ["၉", "အု / ဥ", "/u./", "ou/u", "ရွှေဥ/ယုယု", "Shway Ou/Yu Yu"],
    ["၁၀", "အူး / ဦး", "/u:/", "oo/U/ue", "ဦးမြဦး/ ဖူးဖူး/ မှူးမှူး", "U Mya Oo/ Phoo Phoo/ Hmue Hmue"],
    ["၁၁", "အေ / ဧ", "/ei/", "ay", "ဖေမြင့်", "Phay Myint"],
    ["၁၂", "အေ့", "/ei./", "ae", "ချမ်းမြေ့မောင်ချို", "Chamm Myae Maung Cho"],
    ["၁၃", "အေး", "/ei:/", "aye", "ဒေါ်အေးအေးမြင့်", "Daw Aye Aye Myint"],
    ["၁၄", "အယ်", "/e/", "el", "မိုးမြင့်ကြယ်", "Moe Myint Kyel"],
    ["၁၅", "အဲ့ / အယ့်", "/e./", "elt", "လဲ့လဲ့ဝင်း", "Lelt Lelt Winn"],
    ["၁၆", "အဲ", "/e:/", "ell", "စောခူဆဲ", "Saww Khuu Hsell"],
    ["၁၇", "အော် / ‌ဪ", "/o/", "aw", "ဦးပေါ်ဦး/ ကျော်ကျော်", "U Paw Oo/ Kyaw Kyaw"],
    ["၁၈", "အော့", "/o./", "awt", "ပန်းတမော့/အိကျော့", "Pann Ta Mawt/ Ei Kyawt"],
    ["၁၉", "အော / ဩ", "/o:/", "aww", "စောတောနော်", "Saww Taww Naw"],
    ["၂၀", "အို", "/ou/", "o", "ကိုပြည်", "Ko Pyi"],
    ["၂၁", "အို့", "/ou./", "oh", "မို့မို့ဇော်ဝင်း", "Moh Moh Zaw Winn"],
    ["၂၂", "အိုး", "/ou:/", "oe", "မောင်သာနိုး/ ပြအိုး", "Mg Thar Noe/ Pya Oe"],
    ["၂၃", "အက်", "/e'/", "et", "ခင်ခက်ခက်ခိုင်", "Khin Khet Khet Khaing"],
    ["၂၄", "အောက်", "/au'/", "auk", "မောင်ပေါက်စီ", "Mg Pauk Se"],
    ["၂၅", "အိုက်", "/ai'/", "aik", "ဦးတိုက်စံ", "U Taik Sam"],
    ["၂၆", "အင် / အဉ်", "/in/", "in", "ထူးအိမ်သင်", "Htoo Eim Thin"],
    ["၂၇", "အင့် / အဉ့်", "/in./", "int", "မြင့်သူ", "Myint Thuu"],
    ["၂၈", "အင်း / အဉ်း", "/in:/", "inn", "ခင်ဇော်ဝင်း", "Khin Zaw Winn"],
    ["၂၉", "အောင်", "/aun/", "aung/ -g", "မောင်မောင်မောင်အောင်", "Mg Maung Maung Aung"],
    ["၃၀", "အောင့်", "/aun./", "ount", "မြို့ထောင့်စေတီ", "Myoh Htount Say Te"],
    ["၃၁", "အောင်း", "/aun:/", "oung", "အောင်မောင်း", "Aung Moung"],
    ["၃၂", "အိုင်", "/ain/", "aing", "ဇော်ပိုင်", "Zaw Paing"],
    ["၃၃", "အိုင့်", "/ain./", "aint", "တစ်လုံးချိုင့်", "Tit Lome Chaint"],
    ["၃၄", "အိုင်း", "/ain:/", "ai/ine", "စိုင်းစိုင်း/ ရှိုင်းဝေအောင်", "Sai Sai/Shine Way Aung"],
    ["၃၅", "အစ်", "/I'/", "it", "ကစ်ကစ်", "Kit Kit"],
    ["၃၆", "အတ် / အပ်", "/a'/", "at/ap/-ao", "မြတ်ကျော်/ဇလပ်ဖြူ/ စဝ်ခွန်မိန်း", "Myat Kyaw/ Za Lap Phyuu/ Sao Khun Meinn"],
    ["၃၇", "အိတ် / အိပ်", "/ei'/", "eik/ake", "သိဒ္ဓိစိုး/ဆိပ်ခွန်", "Theikdei Soe/Hsake Khun"],
    ["၃၈", "အုတ် / အုပ်", "/ou'/", "oak/oke", "ဦးဗုဒ်/အုပ်စိုးခန့်", "U Boak/Oke Soe Khant"],
    ["၃၉", "အန် / အမ်/ အံ", "/an/", "an/am", "ရန်နိုင်/ဦးယံ", "Yan Naing/U Yam"],
    ["၄၀", "အန့် / အမ့်/အံ့", "/an./", "ant/amt", "ခန့်စည်သူ/အံ့မျိုးထွဋ်", "Khant Sithuu/Amt Myoe Htut"],
    ["၄၁", "အန်း / အမ်း", "/an:/", "ann/amm", "အောင်ဆန်း/စမ်းစမ်း", "Aung Hsann/Samm Samm"],
    ["၄၂", "အိန် / အိမ်", "/ein/", "ein/ eim", "စိန်စိန်/ ထူးအိမ်သင်", "Sein Sein/ Htoo Eim Thin"],
    ["၄၃", "အိန့် / အိမ့်", "/ein./", "eint/eimt", "အိမ့်နေခြည်/ မောင်စိမ့်", "Eimt Nay Chi/ Mg Seimt"],
    ["၄၄", "အိန်း / အိမ်း", "/ein:/", "einn/eimm", "သိန်းသန်းစိုး/ စိမ်းစိမ်းဦး", "Theinn Thann Soe/ Seimm Seimm Oo"],
    ["၄၅", "အုန် / အုမ် / အုံ", "/oun/", "ohn/ohm/ oun/oum", "ပြည်စုန်မင်း/ ဥမ္မာခင်/ ခုံတော်", "Pyi Soun Minn/Ohmmar Khin/Khoum Taw"],
    ["၄၆", "အုန့် / အုမ့် / အုံ့", "/oun./", "ont/omt", "ပုံ့ပုံ့", "Pomt Pomt"],
    ["၄၇", "အုန်း / အုမ်း / အုံး", "/oun:/", "own/owm/one/ome", "ဦးအုန်းမောင်/မောင်ဖုန်းနိုင်", "U Own Maung/Mg Phone Naing"],
    ["၄၈", "အွတ်/အွပ်", "/u'/", "ut", "ဇော်ဝင်းထွဋ်", "Zaw Winn Htut"],
    ["၄၉", "အွန်", "/un/", "un/um/on", "ခွန်အောင်နိုင်/မွန်", "Khun Aung Naing/ Mon"],
    ["၅၀", "အွန့်", "/un./", "unt/umt", "မျိုးညွန့်", "Myoe Nyunt"],
    ["၅၁", "အွန်း", "/un:/", "unn/umm", "ခွန်းဆင့်နေခြည်", "Khunn Hsint Nay Chi"]
]

# Render HTML Table
html_table = "<table class='my-table'>\n"

# Add Header
html_table += "<thead><tr>"
for col in header:
    html_table += f"<th>{col}</th>"
html_table += "</tr></thead>"

# Add Body
html_table += "<tbody>"
for row in data:
    html_table += "<tr>"
    for cell in row:
        html_table += f"<td>{cell}</td>"
    html_table += "</tr>"
html_table += "</tbody></table>"

# Display Table
st.markdown(html_table, unsafe_allow_html=True)

# Content List
content_list = [
    "အသံတူသရတစ်လုံးစီယူသည့် စနစ်အရ မြန်မာသရသံ ၅၁ သံ ရှိပါသည်။",
    "အသံထွက်စနစ်အရ အတ်နှင့် အွတ်၊ အန် နှင့် အွန် တို့သည် သီးခြားသရသံများ ဖြစ်ပါသည်။",
    "င-သတ်၊ ဉ-သတ် တို့ကို in ဟု စာလုံးပေါင်းပါသည်။",
    "တ-သတ် ကို t၊ ပ-သတ်ကို p / ke၊ န-သတ်ကို n၊ မ-သတ်နှင့် သေးသေးတင်ကို m တို့ဖြင့် စာလုံးပေါင်းပါသည်။",
    "အမျိုးသားနာမည် အစ စကားလုံး ဦး ကို U၊ မောင် ကို Mg ဟု စာလုံးပေါင်းပါသည်။",
    "ရ၊ ြ တို့ကို r ဟု သတ်မှတ်ထားသော်လည်း ယ သံ ထွက်သည့် ရ၊ ြ တို့ကို y ဖြင့် စာလုံးပေါင်းပါသည်။",
    "အများသိ မြို့အမည် ၅၃၀ ကို မူလစာလုံးပေါင်းအတိုင်း ဖော်ပြထားပါသည်။",
    "နာမည်တွင် ပါဠိစကားလုံးပါဝင်ပါက ပါဠိစကားလုံးများကို တစ်ဆက်တည်း စာလုံးပေါင်းပါသည်။",
    "ပါဠိစစ်စစ် စာလုံးပေါင်းကို အသုံးပြုလိုပါက ပါဠိ-ရိုမန်ကဏ္ဍတွင် ရှာဖွေရန်ဖြစ်ပါသည်။",
    "ကျမ်းကိုး- မြန်မာသဒ္ဒါ (မြန်မာစာအဖွဲ့)၊ နှုတ်ပြောမြန်မာသဒ္ဒါ (မောင်ခင်မင်- ဓနုဖြူ)၊ မြန်မာ-အင်္ဂလိပ်အဘိဓာန် (၂၀၁၉)၊ The Pali Alphabet in Myanmar and Roman Characters (ပဋ္ဌာနပါဠိ- ပဋ္ဌမတွဲ)၊ Let's Write English Sentences (စိုးသစ်)။"
]


# Styled HTML for List with Edit Icon
styled_html = """
<div class="list-container">
    <ul>
"""

# Add list items dynamically
for text in content_list:
    styled_html += f"<li>{text}</li>"

# Close the div and ul
styled_html += "</ul></div>"

# Display in Streamlit
st.markdown(styled_html, unsafe_allow_html=True)