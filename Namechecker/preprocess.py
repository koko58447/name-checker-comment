import re
import unicodedata
import mm_transpitor_module as mm

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


def get_mm_mapping(word_dict, label, index):
    if label == "အ" and index == 0:
        return "a"
    elif label in word_dict:
        return word_dict[label]
    else:
        return mm.transcript(label)

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
    print(text)
    mapped_word = ""
    prefix_splitted_string = []

    remaining = text

    index = 0
    while index < len(text):
        splitted_text = split_prefix_name(remaining, all_prefixes)
        print(splitted_text)
        prefix_splitted_string.append(splitted_text)
        remaining = remaining[len(splitted_text):]
        index += len(splitted_text)

    mapped_word = " ".join(get_prefix_spilitted_map(entry, word_dict) for entry in prefix_splitted_string)

    return mapped_word

def capitalize(string):
    return string if not string else string[0].upper() + string[1:]

##################

def get_raw_unicode(text):
    """Return the raw Unicode representation of the input text."""
    return ''.join(f'\\u{ord(c):04X}' for c in text)

def normalize_text(text):
    """Normalize the input text using NFC (Normalization Form C)."""
    return unicodedata.normalize('NFC', text)

def split_prefix_name(text, prefixes):
    """Split the input text into prefix and name if the text starts with any of the given prefixes."""
    
    for prefix in prefixes:
        if text.startswith(prefix):
            return prefix
    return text

def get_syllable(label, burmese_consonant, others):
    """
    Split the input label into syllables based on Burmese consonants and other characters.
    
    Args:
        label (str): The input label to split into syllables.
        burmese_consonant (str): A string of Burmese consonants.
        others (str): A string of other characters.
    
    Returns:
        list: A list of syllables.
    """
    # Regular expression pattern to match Burmese consonants and other characters
    pattern = re.compile(r'(?<![္])([' + burmese_consonant + r'])(?![်္ ့])|([' + others + r'])', re.UNICODE)
    
    # Replace matches with a space-separated string
    reg_label = re.sub(pattern, lambda match: f" {match.group(1) or ''}{match.group(2) or ''}", label).strip()
    
    # Regular expression pattern to match Burmese consonants followed by Latin characters
    pattern2 = re.compile(r'([က-ၴ])([a-zA-Z0-9])', re.UNICODE)
    
    # Replace matches with a space-separated string
    reg_label = re.sub(pattern2, lambda match: f"{match.group(1)} {match.group(2)}", reg_label)
    
    # Regular expression pattern to match consecutive digits or Myanmar digits
    pattern3 = re.compile(r'([0-9၀-၉])\s+([0-9၀-၉])\s*', re.UNICODE)
    
    # Replace matches with a concatenated string
    reg_label = re.sub(pattern3, lambda match: f"{match.group(1)}{match.group(2)}", reg_label)
    
    # Regular expression pattern to match digits or Myanmar digits followed by a plus sign
    pattern4 = re.compile(r'([0-9၀-၉])\s+(\+)', re.UNICODE)
    
    # Replace matches with a concatenated string
    reg_label = re.sub(pattern4, lambda match: f"{match.group(1)}{match.group(2)}", reg_label).strip()
    
    # Split the resulting string into syllables
    return reg_label.split()

def syllable_split(label):
    """
    Split the input label into syllables.
    
    Args:
        label (str): The input label to split into syllables.
    
    Returns:
        list: A list of syllables.
    """
    burmese_consonant = 'ကခဂဃငစဆဇဈညဉဋဌဍဎဏတထဒဓနပဖဗဘမယရလဝသဟဠအ'
    others = r'ဣဤဥဦဧဩဪဿ၌၍၏၀-၉၊။!-/:-@[-`{-~\s.,'
    
    # Split the label into words and then split each word into syllables
    return [syllable for word in label.split() for syllable in get_syllable(word, burmese_consonant, others)]

def merge_consecutive(lst, mapping):
    """
    Merge consecutive elements in the input list based on the given mapping.
    
    Args:
        lst (list): The input list to merge consecutive elements.
        mapping (dict): A dictionary mapping consecutive elements to their merged values.
    
    Returns:
        list: The merged list.
    """
    new_list = []
    max_length = max(len(key) for key in mapping.keys())
    
    i = 0
    while i < len(lst):
        match_found = False
        
        # Check for the longest possible match (max_length -> 2)
        for length in range(max_length, 1, -1):
            if i + length <= len(lst):
                substring = ''.join(lst[i:i + length])
                if substring in mapping:
                    # new_list.append(mapping[substring])  # Replace with mapped value
                    new_list.append(substring)  # Replace with mapped key
                    i += length
                    match_found = True
                    break
        
        if not match_found:
            new_list.append(lst[i])
            i += 1
    
    return new_list

# Example usage:
label = "မြန်မာစာ"
burmese_consonant = 'ကခဂဃငစဆဇဈညဉဋဌဍဎဏတထဒဓနပဖဗဘမယရလဝသဟဠအ'
others = r'ဣဤဥဦဧဩဪဿ၌၍၏၀-၉၊။!-/:-@[-`{-~\s.,'

# print(get_syllable(label, burmese_consonant, others))
# print(syllable_split(label))
