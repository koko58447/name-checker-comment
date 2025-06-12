import re
def preprocess(text):
    text = text.replace("ဿ", "သ္သ")
    text = text.replace("\u1026\u1038", "အူး")
    text = text.replace("ဥူး", "အူး")
    text = text.replace("\u1026", "အူ")
    text = text.replace("ဥူ", "အူ")
    text = text.replace("ဥုံ", "အုမ်")
    text = text.replace("ဥု", "အူ")
    text = text.replace("ဥ", "အု")
    text = text.replace("န်ုပ်", "န်နုပ်")
    text = text.replace("ဪ", "အော်")
    text = text.replace("ဩ", "အော")
    text = text.replace("ဤ", "အီ")
    text = text.replace("၏", "အိ")
    text = text.replace("ဧ", "အေ")
    text = text.replace("ဣိ", "အိ")
    text = text.replace("ဣီ", "အီ")
    text = text.replace("ဣူ", "အူ")
    text = text.replace("ဣု", "အု")
    text = text.replace("ဣ", "အိ")
    text = text.replace("၍", "ရွေ့")
    text = text.replace("၎င်း", "လည်းကောင်း")
    text = text.replace("၌", "နှိုက်")
    text = text.replace("ွှံ့", "ွှန့်")
    text = text.replace("ွံ့", "ွန့်")
    text = text.replace("ျွှံ့", "ျွှန့်")
    text = text.replace("ြွှံ့", "ြွှန့်")
    text = re.sub(r'[\u200B\u200C]', '', text)
    return text

def flatten_stack(text):
    stack_patterns = [
        re.compile(r"([\u1000-\u1020])\u1039", re.UNICODE),
        re.compile(r"([\u1000-\u1020\u1004\u103A])\u1039", re.UNICODE),
    ]

    for pattern in stack_patterns:
        while pattern.search(text):
            if pattern == stack_patterns[0]:
                text = pattern.sub(r"\1\u103A", text)
            else:
                text = pattern.sub(r"\1", text)

    return text

def convert_name(word_dict):
    all_prefixes = [
        "ဆရာတော်",
        "ဆရာမ",
        "ဆရာ",
        "သုဓမ္မာ",
        "သုဓမ္မ",
        "အဂ္ဂိ",
        "အဂ္ဂ",
        "မဟာကထာနံ",
        "မဟာ",
        "ဇောတိကဓဇ",
        "သဒ္ဓမ္မဇောတိကဓဇ",
        "မဏိဇောတဓရ",
        "သတိုး",
        "သရေ",
        "စည်သူ",
        "သီဟသူရ",
        "သူရင်း",
        "သူရဲ",
        "သူရိန်",
        "သူရိယ",
        "သူရသ္သတီ",
        "သူရဇ္ဇ",
        "သူရာ",
        "သူရ",
        "သီရိပျံချီ",
        "သီရိ",
        "ဇေယျကျော်ထင်",
        "အလင်္ကာကျော်စွာ",
        "သိပ္ပကျော်စွာ",
        "ပြည်ထောင်စု",
        "တံခွန်",
        "ဇာနည်",
        "လမ်းစဉ်ဇာနည်",
        "ပညာဗလ",
    ]

    mapped_names = ""
    return mapped_names

def get_mm_mapping(word_dict, label, index):
    if label == "အ" and index == 0:
        return "a"
    elif label in word_dict:
        return word_dict[label]
    else:
        return transcriptor.transcript(label)

def get_intermediate_map(merged_label, word_dict, index):
    if merged_label == "အူး" and index == 0:
        return "u"
    elif merged_label == "မောင်" and index == 0:
        return "mg"
    elif merged_label == "အ" and index == 0:
        return "a"
    elif merged_label in word_dict and word_dict[merged_label] != "":
        return word_dict[merged_label].capitalize()
    else:
        flattened_text = flatten_stack(merged_label)
        final_syllable_list = syllable_split(flattened_text)
        return ''.join(get_mm_mapping(word_dict, syllable, i) for i, syllable in enumerate(final_syllable_list))

def get_prefix_spilitted_map(text, word_dict):
    if text in word_dict and word_dict[text] != "":
        return word_dict[text].capitalize()
    elif text in word_dict and word_dict[text] == "":
        flattened_text = flatten_stack(text)
        syllable_list = syllable_split(flattened_text)
        return ''.join(get_mm_mapping(word_dict, syllable, i) for i, syllable in enumerate(syllable_list))
    else:
        syllable_list = syllable_split(text)
        merge_list = merge_consecutive(syllable_list, word_dict)
        return ' '.join(get_intermediate_map(item, word_dict, i) for i, item in enumerate(merge_list))

def get_map(text, word_dict):
    mapped_word = ""
    prefix_splitted_string = []

    remaining = text

    index = 0
    while index < len(text):
        splitted_text = split_prefix_name(remaining, all_prefixes)
        prefix_splitted_string.append(splitted_text)
        remaining = remaining[len(splitted_text):]
        index += len(splitted_text)

    mapped_word = " ".join(get_prefix_splitted_map(entry, word_dict) for entry in prefix_splitted_string)

    return mapped_word

def capitalize(string):
    return string if not string else string[0].upper() + string[1:]