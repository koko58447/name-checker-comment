import streamlit as st

# Page Title with Custom Style
st.markdown("""
    <h1 style='text-align: center; color: #2E7ABC;'>ပါဠိအညွှန်း</h1>
    <p style='text-align: right; font-style: italic; color: #555;'>အမျိုးသားဉာဏ်ရည်တုနည်းပညာဖွံ့ဖြိုးတိုးတက်ရေးစီမံကိန်း</p>
""", unsafe_allow_html=True)

st.subheader("VOWELS")

# Data
data = [
    "အ a",
    "အာ ā",
    "ဣ i",
    "ဤ ī",
    "ဥ u",
    "ဦ ū",
    "ဧ e",
    "ဩ o"
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
html_table += "<tr>"
for group in data: 
   
    mm_char, en_char = group.split()
    html_table += f"<td>{mm_char} → {en_char}</td>"
    
html_table += "</tr>"

html_table += "</table>"

# Display Table
st.markdown(html_table, unsafe_allow_html=True)

st.subheader("CONSONANTS WITH VOWEL 'A'")

# Data
data = [
    ["က ka", "ခ kha", "ဂ ga", "ဃ gha", "င ṅa"],
    ["စ ca", "ဆ cha", "ဇ ja", "ဈ jha", "ဉ ña"],
    ["ဋ ṭa", "ဌ ṭha", "ဍ ḍa", "ဓ ḍha", "ဏ ṇa"],
    ["တ ta", "ထ tha", "ဒ da", "ဓ dha", "န na"],
    ["ပ pa", "ဖ pha", "ဗ ba", "ဘ bha", "မ ma"],
    
]

# Data
data1 = [
    "ယ\tya",
    "ရ\tra",
    "လ\tla",
    "ဝ\tva",
    "သ\tsa",
    "ဟ\tha",
    "ဠ\tḷa",
    "အံ\tṃ"
]

# Render HTML Table
html_table = "<table class='my-table'>\n"

for group in data:
    html_table += "<tr>"
    for item in group:
        mm_char, en_char = item.split()
        html_table += f"<td>{mm_char} → {en_char}</td>"
    html_table += "</tr><tr>"
for item1 in data1:
    mm_char, en_char = item1.split("\t")
    html_table += f"<td>{mm_char} → {en_char}</td>"

html_table += "</tr></table>"

# Display Table
st.markdown(html_table, unsafe_allow_html=True)

st.subheader("VOWELS IN COMBINATION")

# Data
data = [
    [
        "က\tka",
        "ကာ\tkā",
        "ကိ\tki",
        "ကီ\tkī",
        "ကု\tku",
        "ကူ\tkū",
        "ကေ\tke",
        "ကော\tko"
    ],
    [
        "ခ\tkha",
        "ခါ\tkhā",
        "ခိ\tkhi",
        "ခီ\tkhī",
        "ခု\tkhu",
        "ခူ\tkhū",
        "ခေ\tkhe",
        "ခေါ\tkho"
    ]
]
# Render HTML Table
html_table = "<table class='my-table'>\n"

for group in data:
    html_table += "<tr>"
    for item in group:
        mm_char, en_char = item.split("\t")
        html_table += f"<td>{mm_char} → {en_char}</td>"
    html_table += "</tr>"

html_table += "</table>"

# Display Table
st.markdown(html_table, unsafe_allow_html=True)

st.subheader("CONJUNCT-CONSONANTS")
# Data
data = [
    ["က္က\tkka", "ဉ္စ\tñca", "ဒွ\tdva", "မ္ဗ\tmba"],
    ["က္ခ\tkkha", "ဉ္ဆ\tñcha", "ဓျ\tdhya", "မ္ဘ\tmbha"],
    ["ကျ\tkya", "ဉ္ဇ\tñja", "ဓွ\tdhva", "မ္မ\tmma"],
    ["ကြိ\tkri", "ဉ္ဈ\tñjha", "န္တ\tnta", "မျ\tmya"],
    ["က္လ\tkla", "ဋ္ဋ\tṭṭa", "န္တွ\tntva", "မှ\tmha"],
    ["ကွ\tkva", "ဋ္ဌ\tṭṭha", "န္ထ\tntha", "ယျ\tyya"],
    ["ချ\tkhya", "ဍ္ဍ\tḍḍa", "န္ဒ\tnda", "ယှ\tyha"],
    ["ခွ\tkhva", "ဍ္ဎ\tḍḍh", "န္ဒြ\tndra", "လ္လ\tlla"],
    ["ဂ္ဂ\tgga", "ဏ္ဋ\tṇṭa", "န္ဓ\tndha", "လျ\tlya"],
    ["ဂ္ဂ\tggha", "ဏ္ဌ\tṇṭha", "န္န\tnna", "လှ\tlha"],
    ["ဂျ\tgya", "ဏ္ဍ\tṇḍa", "နျ\tnya", "ဝှ\tvha"],
    ["ဂြ\tgra", "ဏ္ဏ\tṇṇa", "နှ\tnha", "သ္ထ\tsta"],
    ["င်္က\tṅka", "ဏှ\tṇha", "ပ္ပ\tppa", "သ္တြ\tstra"],
    ["င်္ခ\tṅkha", "ထ္ထ\tttha", "ပ္ဖ\tppha", "သ္န\tsna"],
    ["င်္ဂ\tṅga", "တွ\ttva", "ဗ္ဗ\tbba", "သျ\tsya"],
    ["င်္ဃ\tṅgha", "တျ\ttya", "ဗ္ဘ\tbbha", "ဿ\tssa"],
    ["စ္စ\tcca", "ဒ္ဒ\tdda", "ဗျ\tbya", "ဟ္မ\thma"],
    ["စ္ဆ\tccha", "ဒ္ဓ\tddha", "ဗြ\tbra", "ဟွ\thva"],
    ["ဇ္ဇ\tjja", "ဒျ\tdya", "မ္ပ\tmpa", "ဠ\tḷha"],
    ["ဇ္ဈ\tjjha", "ဒြ\tdra", "မ္ဖ\tmpha", ""]
]


# Render HTML Table
html_table = "<table class='my-table'>\n"

for row in data:
    html_table += "<tr>"
    for item in row:
        if item.strip() == "":
            html_table += "<td></td>"  # empty cell ကိုထားပါမယ်
        else:
            mm_char, en_char = item.split("\t")
            html_table += f"<td>{mm_char} → {en_char}</td>"
    html_table += "</tr>"

html_table += "</table>"

# Display Table
st.markdown(html_table, unsafe_allow_html=True)

# Data
data = [
    "ာ-ါ-\tā",
    "ိ-\ti;",
    "ီ–\tī;",
    "ု-\tu;",
    "ူ-\tu",
    "‌ေ-\te",
    "ော-‌ေါ-\to"
]


html_table = "<table class='my-table'>\n"
html_table += "<tr>"
for group in data: 
   
    mm_char, en_char = group.split("\t")
    html_table += f"<td>{mm_char} → {en_char}</td>"
    
html_table += "</tr>"

html_table += "</table>"

# Display Table
st.markdown(html_table, unsafe_allow_html=True)

# Data (Myanmar Numbers and English Numbers)
data = [
    ["၁", "၂", "၃", "၄", "၅", "၆", "၇", "၈", "၉", "၀"],
    ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
]

# Render HTML Table
html_table = "<table class='my-table'>\n"

for row in data:
    html_table += "<tr>"
    for item in row:
       html_table += f"<td>{item}</td>"
    html_table += "</tr>"

html_table += "</table>"

# Display Table
st.markdown(html_table, unsafe_allow_html=True)

st.write("ကျမ်းကိုး- The Pali Alphabet in Myanmar and Roman Characters (ပဋ္ဌာနပါဠိ- ပဋ္ဌမတွဲ)၊ မြန်မာစာ မြန်မာမှု ပါဠိအဘိဓါန်သစ် [ဦးမြတ်ကျော် (မြန်မာစာ အဖွဲ့ဝင်)]၊ ပဒတ္ထမဉ္ဇူသာ ဟူသော ပါဠိ-မြန်မာအဘိဓါန် (ဦးဟုတ်စိန်)။")