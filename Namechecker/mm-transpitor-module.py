import re

singleton = {
            "က": "k",
            "ခ": "kh",
            "ဂ": "g",
            "ဃ": "g",
            "င": "ng",
            "စ": "s",
            "ဆ": "hs",
            "ဇ": "z",
            "ဈ": "z",
            "ဉ": "ny",
            "ည": "ny",
            "ဋ": "t",
            "ဌ": "ht",
            "ဍ": "d",
            "ဎ": "d",
            "ဏ": "n",
            "တ": "t",
            "ထ": "ht",
            "ဒ": "d",
            "ဓ": "d",
            "န": "n",
            "ပ": "p",
            "ဖ": "ph",
            "ဗ": "b",
            "ဘ": "b",
            "မ": "m",
            "ယ": "y",
            "ရ": "y",
            "လ": "l",
            "ဝ": "w",
            "သ": "th",
            "ဟ": "h",
            "ဠ": "l",
            "အ": ""
        }
vowelForm = {
            "ာ": "ar",
            "ါ": "ar",
            "ိ": "ei",
            "ီ": "e",
            "ု": "u",
            "ူ": "uu",
            "ေ": "ay",
            "ံ": "am",
            "ဲ": "ell",
            "ှ": "h"
        }
specialCharsForm = {
            "၁": "1",
            "၂": "2",
            "၃": "3",
            "၄": "4",
            "၅": "5",
            "၆": "6",
            "၇": "7",
            "၈": "8",
            "၉": "9",
            "၀": "0",
            "၊": ",",
            "။": "."
        }

asat_extended_form = {
    "\u103e\u1031\u102c\u1000\u103a": "auk",  # ငှောက်
    "\u103e\u1031\u102c\u1002\u103a": "auk",  # ကောဂ်
    "\u103e\u1031\u102c\u1004\u103a\u1038": "oung",  # ကောင်း
    "\u103e\u1031\u102c\u1004\u1037\u103a": "ount",  # ကောင့်
    "\u103e\u1031\u102c\u1004\u103a": "aung",  # ကောင်
    "\u103e\u1031\u102c\u1005\u103a": "auk",  # ကောစ်
    "\u103e\u1031\u102c\u1007\u103a": "auk",  # ကောဇ်
    "\u103e\u1031\u102c\u1009\u103a\u1038": "oung",  # ကောဉ်း
    "\u103e\u1031\u102c\u1009\u1037\u103a": "ount",  # ကောဉ့်
    "\u103e\u1031\u102c\u1009\u103a": "aung",  # ကောဉ်
    "\u103e\u1031\u102c\u100a\u103a\u1038": "oung",  # ကောည်း
    "\u103e\u1031\u102c\u100a\u1037\u103a": "ount",  # ကောည့်
    "\u103e\u1031\u102c\u100a\u103a": "aung",  # ကောည်
    "\u103e\u1031\u102c\u100b\u103a": "auk",  # ကောဋ်
    "\u103e\u1031\u102c\u100d\u103a": "auk",  # ကောဍ်
    "\u103e\u1031\u102c\u100f\u103a\u1038": "oung",  # ကောဏ်း
    "\u103e\u1031\u102c\u100f\u1037\u103a": "ount", # ကောဏ့်
    "\u103e\u1031\u102c\u100f\u103a": "aung", # ကောဏ်
    "\u103e\u1031\u102c\u1010\u103a": "auk", # ကောတ်
    "\u103e\u1031\u102c\u1012\u103a": "auk", # ကောဒ်
    "\u103e\u1031\u102c\u1014\u103a\u1038": "oung", # ကောန်း
    "\u103e\u1031\u102c\u1014\u1037\u103a": "ount", # ကောန့်
    "\u103e\u1031\u102c\u1014\u103a": "aung", # ကောန်
    "\u103e\u1031\u102c\u1015\u103a": "auk", # ကောပ်
    "\u103e\u1031\u102c\u1017\u103a": "auk", # ကောဗ်
    "\u103e\u1031\u102c\u1019\u103a\u1038": "oumg", # ကောမ်း
    "\u103e\u1031\u102c\u1019\u1037\u103a": "oumt", # ကောမ့်
    "\u103e\u1031\u102c\u1019\u103a": "aumg", # ကောမ်
    "\u103e\u1031\u102c\u101a\u1037\u103a": "auk", # ကောယ့်
    "\u103e\u1031\u102c\u101a\u103a": "auk", # ကောယ်
    "\u103e\u1031\u102c\u101b\u103a": "au", # ကောရ်
    "\u103e\u1031\u102c\u101c\u103a": "aung", # ကောလ်
    "\u103e\u1031\u102c\u101d\u103a": "auk", # ကောဝ်
    "\u103e\u1031\u102c\u101e\u103a": "auk", # ကောသ်
    "\u103e\u1031\u102c\u101f\u103a": "aun", # ကောဟ်
    "\u1031\u102c\u1000\u103a": "auk", # ကောက်
    "\u1031\u102c\u1002\u103a": "auk", # ကောဂ်
    "\u1031\u102c\u1004\u103a\u1038": "oung", # ကောင်း
    "\u1031\u102c\u1004\u1037\u103a": "ount", # ကောင့်
    "\u1031\u102c\u1004\u103a": "aung", # ကောင်
    "\u1031\u102c\u1005\u103a": "auk", # ကောစ်
    "\u1031\u102c\u1007\u103a": "auk", # ကောဇ်
    "\u1031\u102c\u1009\u103a\u1038": "oung", # ကောဉ်း
    "\u1031\u102c\u1009\u1037\u103a": "ount", # ကောဉ့်
    "\u1031\u102c\u1009\u103a": "aung", # ကောဉ်
    "\u1031\u102c\u100a\u103a\u1038": "oung", # ကောည်း
    "\u1031\u102c\u100a\u1037\u103a": "ount", # ကောည့်
    "\u1031\u102c\u100a\u103a": "aung", # ကောည်
    "\u1031\u102c\u100b\u103a": "auk", # ကောဋ်
    "\u1031\u102c\u100d\u103a": "auk", # ကောဍ်
    "\u1031\u102c\u100f\u103a\u1038": "oung", # ကောဏ်း
    "\u1031\u102c\u100f\u1037\u103a": "ount", # ကောဏ့်
    "\u1031\u102c\u100f\u103a": "aung", # ကောဏ်
    "\u1031\u102c\u1010\u103a": "auk", # ကောတ်
    "\u1031\u102c\u1012\u103a": "auk", # ကောဒ်
    "\u1031\u102c\u1014\u103a\u1038": "oung", # ကောန်း
    "\u1031\u102c\u1014\u1037\u103a": "ount", # ကောန့်
    "\u1031\u102c\u1014\u103a": "aung", # ကောန်
    "\u1031\u102c\u1015\u103a": "auk", # ကောပ်
    "\u1031\u102c\u1017\u103a": "auk", # ကောဗ်
    "\u1031\u102c\u1019\u103a\u1038": "oumg", # ကောမ်း
    "\u1031\u102c\u1019\u1037\u103a": "oumt", # ကောမ့်
    "\u1031\u102c\u1019\u103a": "aumg", # ကောမ်
    "\u1031\u102c\u101a\u1037\u103a": "auk", # ကောယ့်
    "\u1031\u102c\u101a\u103a": "auk", # ကောယ်
    "\u1031\u102c\u101b\u103a": "au", # ကောရ်
    "\u1031\u102c\u101c\u103a": "aung", # ကောလ်
    "\u1031\u102c\u101d\u103a": "auk", # ကောဝ်
    "\u1031\u102c\u101e\u103a": "auk", # ကောသ်
    "\u1031\u102c\u101f\u103a": "aun", # ကောဟ်
     "\u103e\u1031\u102b\u1000\u103a": "auk", # ငှေါက်
    "\u103e\u1031\u102b\u1002\u103a": "auk", # ခေါဂ်
    "\u103e\u1031\u102b\u1004\u103a\u1038": "oung", # ကေါင်း
    "\u103e\u1031\u102b\u1004\u1037\u103a": "ount", # ကေါင့်
    "\u103e\u1031\u102b\u1004\u103a": "aung", # ကေါင်
    "\u103e\u1031\u102b\u1005\u103a": "auk", # ကေါစ်
    "\u103e\u1031\u102b\u1007\u103a": "auk", # ကေါဇ်
    "\u103e\u1031\u102b\u1009\u103a\u1038": "oung", # ကေါဉ်း
    "\u103e\u1031\u102b\u1009\u1037\u103a": "ount", # ကေါဉ့်
    "\u103e\u1031\u102b\u1009\u103a": "aung", # ကေါဉ်
    "\u103e\u1031\u102b\u100a\u103a\u1038": "oung", # ကေါည်း
    "\u103e\u1031\u102b\u100a\u1037\u103a": "ount", # ကေါည့်
    "\u103e\u1031\u102b\u100a\u103a": "aung", # ကေါည်
    "\u103e\u1031\u102b\u100b\u103a": "auk", # ကေါဋ်
    "\u103e\u1031\u102b\u100d\u103a": "auk", # ကေါဍ်
    "\u103e\u1031\u102b\u100f\u103a\u1038": "oung", # ကေါဏ်း
    "\u103e\u1031\u102b\u100f\u1037\u103a": "ount", # ကေါဏ့်
    "\u103e\u1031\u102b\u100f\u103a": "aung", # ကေါဏ်
    "\u103e\u1031\u102b\u1010\u103a": "auk", # ကေါတ်
    "\u103e\u1031\u102b\u1012\u103a": "auk", # ကေါဒ်
    "\u103e\u1031\u102b\u1014\u103a\u1038": "oung", # ကေါန်း
    "\u103e\u1031\u102b\u1014\u1037\u103a": "ount", # ကေါန့်
    "\u103e\u1031\u102b\u1014\u103a": "aung", # ကေါန်
    "\u103e\u1031\u102b\u1015\u103a": "auk", # ကေါပ်
    "\u103e\u1031\u102b\u1017\u103a": "auk", # ကေါဗ်
    "\u103e\u1031\u102b\u1019\u103a\u1038": "oumg", # ကေါမ်း
    "\u103e\u1031\u102b\u1019\u1037\u103a": "oumt", # ကေါမ့်
    "\u103e\u1031\u102b\u1019\u103a": "aumg", # ကေါမ်
    "\u103e\u1031\u102b\u101a\u1037\u103a": "auk", # ကေါယ့်
    "\u103e\u1031\u102b\u101a\u103a": "auk", # ကေါယ်
    "\u103e\u1031\u102b\u101b\u103a": "auk", # ကေါရ်
    "\u103e\u1031\u102b\u101c\u103a": "aung", # ကေါလ်
    "\u103e\u1031\u102b\u101d\u103a": "auk", # ကေါဝ်
    "\u103e\u1031\u102b\u101e\u103a": "auk", # ကေါသ်
    "\u103e\u1031\u102b\u101f\u103a": "aun", # ကေါဟ်
    "\u1031\u102b\u1000\u103a": "auk", # ခေါက်
    "\u1031\u102b\u1002\u103a": "auk", # ခေါဂ်
    "\u1031\u102b\u1004\u103a\u1038": "oung", # ကေါင်း
    "\u1031\u102b\u1004\u1037\u103a": "ount", # ကေါင့်
    "\u1031\u102b\u1004\u103a": "aung", # ကေါင်
    "\u1031\u102b\u1005\u103a": "auk", # ကေါစ်
    "\u1031\u102b\u1007\u103a": "auk", # ကေါဇ်
    "\u1031\u102b\u1009\u103a\u1038": "oung", # ကေါဉ်း
    "\u1031\u102b\u1009\u1037\u103a": "ount", # ကေါဉ့်
    "\u1031\u102b\u1009\u103a": "aung", # ကေါဉ်
    "\u1031\u102b\u100a\u103a\u1038": "oung", # ကေါည်း
    "\u1031\u102b\u100a\u1037\u103a": "ount", # ကေါည့်
    "\u1031\u102b\u100a\u103a": "aung", # ကေါည်
    "\u1031\u102b\u100b\u103a": "auk", # ကေါဋ်
    "\u1031\u102b\u100d\u103a": "auk", # ကေါဍ်
    "\u1031\u102b\u100f\u103a\u1038": "oung", # ကေါဏ်း
    "\u1031\u102b\u100f\u1037\u103a": "ount", # ကေါဏ့်
    "\u1031\u102b\u100f\u103a": "aung", # ကေါဏ်
    "\u1031\u102b\u1010\u103a": "auk", # ကေါတ်
    "\u1031\u102b\u1012\u103a": "auk", # ကေါဒ်
    "\u1031\u102b\u1014\u103a\u1038": "oung", # ကေါန်း
    "\u1031\u102b\u1014\u1037\u103a": "ount", # ကေါန့်
    "\u1031\u102b\u1014\u103a": "aung", # ကေါန်
    "\u1031\u102b\u1015\u103a": "auk", # ကေါပ်
    "\u1031\u102b\u1017\u103a": "auk", # ကေါဗ်
    "\u1031\u102b\u1019\u103a\u1038": "oumg", # ကေါမ်း
    "\u1031\u102b\u1019\u1037\u103a": "oumt", # ကေါမ့်
    "\u1031\u102b\u1019\u103a": "aumg", # ကေါမ်
    "\u1031\u102b\u101a\u1037\u103a": "auk", # ကေါယ့်
    "\u1031\u102b\u101a\u103a": "auk", # ကေါယ်
    "\u1031\u102b\u101b\u103a": "auk", # ကေါရ်
    "\u1031\u102b\u101c\u103a": "aung", # ကေါလ်
    "\u1031\u102b\u101d\u103a": "auk", # ကေါဝ်
    "\u1031\u102b\u101e\u103a": "auk", # ကေါသ်
    "\u1031\u102b\u101f\u103a": "aun", # ကေါဟ်
    "\u1031\u101e\u103a": "it", 
    "\u103e\u1031\u1010\u103a": "it",
    "\u1031\u1010\u103a": "it", 
    "\u1031\u100a\u1037\u103a": "ei", 
    "\u1031\u100a\u103a": "i",
    "က်ျာ": "atyar", 
    "ှိုက်": "aik",
    "ှိုဂ်": "aik",
    "ှိုင်း": "ine",
    "ှိုင့်": "aint",
    "ှိုင်": "aing",
    "ှိုစ်": "aik",
    "ှိုဇ်": "aik",
    "ှိုဉ်း": "ainn",
    "ှိုဉ့်": "ainnt",
    "ှိုဉ်": "aiin",
    "ှိုည်း": "aine",
    "ှိုည့်": "aint",
    "ှိုည်": "aing",
    "ှိုဋ်": "aik",
    "ှိုဍ်": "aik",
    "ှိုဏ်း": "aine",
    "ှိုဏ့်": "aint",
    "ှိုဏ်": "aing",
    "ှိုတ်": "aik",
    "ှိုဒ်": "aik",
    "ှိုန်း": "aine",
    "ှိုန့်": "aint",
    "ှိုန်": "aing",
    "ှိုပ်": "aik",
    "ှိုဗ်": "aik",
    "ှိုမ်း": "aime",
    "ှိုမ့်": "aimt",
    "ှိုမ်": "aimg",
    "ှိုယ့်": "oh",
    "ှိုယ်": "o",
    "ှိုရ်": "o",
    "ှိုလ်": "o",
    "ှိုဝ်": "o",
    "ှိုသ်": "aik",
    "ှိုဟ်": "ain",
    "ိုက်": "aik",
    "ိုဂ်": "aik",
    "ိုင်း": "ine",
    "ိုင့်": "aint",
    "ိုင်": "aing",
    "ိုစ်": "aik",
    "ိုဇ်": "aik",
    "ိုဉ်း": "ainn",
    "ိုဉ့်": "ainnt",
    "ိုဉ်": "aiing",
    "ိုည်း": "aine",
    "ိုည့်": "aint",
    "ိုည်": "aing",
    "ိုဋ်": "aik",
    "ိုဍ်": "aik",
    "ိုဏ်း": "aine",
    "ိုဏ့်": "aint",
    "ိုဏ်": "aing",
    "ိုတ်": "aik",
    "ိုဒ်": "aik",
    "ိုန်း": "aine",
    "ိုန့်": "aint",
    "ိုန်": "aing",
    "ိုပ်": "aik",
    "ိုဗ်": "aik",
    "ိုမ်း": "aime",
    "ိုမ့်": "aimt",
    "ိုမ်": "aimg",
    "ိုယ့်": "oh",
    "ိုယ်": "o",
    "ိုရ်": "o",
    "ိုလ်": "o",
    "ိုဝ့်": "oh",
    "ိုဝ်": "o",
    "ိုသ်": "aik",
    "ိုဟ်": "o",
    "ှာက်": "et",
    "ှာဂ်": "et",
    "ှာင်း": "inn",
    "ှာင့်": "int",
    "ှာင်": "in",
    "ှာစ်": "it",
    "ှာဇ်": "it",
    "ှာဉ်း": "inn",
    "ှာဉ့်": "innt",
    "ှာဉ်": "in",
    "ှာည်း": "ee",
    "ှာည့်": "ei",
    "ှာည်": "i",
    "ှာဋ်": "at",
    "ှာဍ်": "at",
    "ှာဏ်း": "ann",
    "ှာဏ့်": "ant",
    "ှာဏ်": "an",
    "ှာတ်": "at",
    "ှာဒ်": "at",
    "ှာန်း": "ann",
    "ှာန့်": "ant",
    "ှာန်": "an",
    "ှာပ်": "ap",
    "ှာဗ်": "ap",
    "ှာမ်း": "amm",
    "ှာမ့်": "amt",
    "ှာမ်": "am",
    "ှာယ့်": "ellt",
    "ှာယ်": "el",
    "ှာရ်": "an",
    "ှာလ်": "an",
    "ှာဝ်": "ap",
    "ှာသ်": "at",
    "ှာဟ်": "an",
    "ာက်": "et",
    "ာဂ်": "et",
    "ာင်း": "inn",
    "ာင့်": "int",
    "ာင်": "in",
    "ာစ်": "it",
    "ာဇ်": "it",
    "ာဉ်း": "inn",
    "ာဉ့်": "innt",
    "ာဉ်": "in",
    "ာည်း": "ee",
    "ာည့်": "ei",
    "ာည်": "i",
    "ာဋ်": "at",
    "ာဍ်": "at",
    "ာဏ်း": "ann",
    "ာဏ့်": "ant",
    "ာဏ်": "an",
    "ာတ်": "at",
    "ာဒ်": "at",
    "ာန်း": "ann",
    "ာန့်": "ant",
    "ာန်": "an",
    "ာပ်": "ap",
    "ာဗ်": "ap",
    "ာမ်း": "amm",
    "ာမ့်": "amt",
    "ာမ်": "am",
    "ာယ့်": "ellt",
    "ာယ်": "el",
    "ာရ်": "an",
    "ာလ်": "an",
    "ာဝ်": "ap",
    "ာသ်": "at",
    "ာဟ်": "an",
    "ါက်": "et",
    "ါဂ်": "et",
    "ါင်း": "inn",
    "ါင့်": "int",
    "ါင်": "in",
    "ါစ်": "it",
    "ါဇ်": "it",
    "ါဉ်း": "inn",
    "ါဉ့်": "innt",
    "ါဉ်": "iin",
    "ါည်း": "ee",
    "ါည့်": "ei",
    "ါည်": "i",
    "ါဋ်": "at",
    "ါဍ်": "at",
    "ါဏ်း": "ann",
    "ါဏ့်": "ant",
    "ါဏ်": "an",
    "ါတ်": "at",
    "ါဒ်": "at",
    "ါန်း": "ann",
    "ါန့်": "ant",
    "ါန်": "an",
    "ါပ်": "ap",
    "ါဗ်": "ap",
    "ါမ်း": "amm",
    "ါမ့်": "amt",
    "ါမ်": "am",
    "ါယ့်": "ellt",
    "ါယ်": "el",
    "ါရ်": "an",
    "ါလ်": "an",
    "ါဝ်": "ap",
    "ါသ်": "at",
    "ါဟ်": "an",
    "ှိက်": "eik",
    "ှိဂ်": "eik",
    "ှိင်း": "einn",
    "ှိင့်": "eint",
    "ှိင်": "ein",
    "ှိစ်": "eik",
    "ှိဇ်": "eik",
    "ှိဉ်း": "einn",
    "ှိဉ့်": "einnt",
    "ှိဉ်": "eiin",
    "ှိည်း": "einn",
    "ှိည့်": "eint",
    "ှိည်": "ein",
    "ှိဋ်": "eik",
    "ှိဍ်": "eik",
    "ှိဏ်း": "einn",
    "ှိဏ့်": "eint",
    "ှိဏ်": "ein",
    "ှိတ်": "eik",
    "ှိဒ်": "eik",
    "ှိန်း": "einn",
    "ှိန့်": "eint",
    "ှိန်": "ein",
    "ှိပ်": "eik",
    "ှိဗ်": "eik",
    "ှိမ်း": "eimm",
    "ှိမ့်": "eimt",
    "ှိမ်": "eim",
    "ှိယ့်": "eik",
    "ှိယ်": "eik",
    "ှိရ်": "eik",
    "ှိလ်": "ein",
    "ှိဝ်": "eik",
    "ှိသ်": "eik",
    "ှိဟ်": "ein",
    "ိက်": "eik",
    "ိဂ်": "eik",
    "ိင်း": "einn",
    "ိင့်": "eint",
    "ိင်": "ein",
    "ိစ်": "eik",
    "ိဇ်": "eik",
    "ိဉ်း": "einn",
    "ိဉ့်": "einnt",
    "ိဉ်": "eiin",
    "ိည်း": "einn",
    "ိည့်": "eint",
    "ိည်": "ein",
    "ိဋ်": "eik",
    "ိဍ်": "eik",
    "ိဏ်း": "einn",
    "ိဏ့်": "eint",
    "ိဏ်": "ein",
    "ိတ်": "eik",
    "ိဒ်": "eik",
    "ိန်း": "einn",
    "ိန့်": "eint",
    "ိန်": "ein",
    "ိပ်": "ake",
    "ိဗ်": "ake",
    "ိမ်း": "eimm",
    "ိမ့်": "eimt",
    "ိမ်": "eim",
    "ိယ့်": "eik",
    "ိယ်": "eik",
    "ိရ်": "eik",
    "ိလ်": "ein",
    "ိဝ်": "eik",
    "ိသ်": "eik",
    "ိဟ်": "ein",
    "ိံ": "ein",
    "ှုက်": "oak",
    "ှုဂ်": "oak",
    "ှုင်း": "one",
    "ှုင့်": "ont",
    "ှုင်": "oun",
    "ှုစ်": "oat",
    "ှုဇ်": "oat",
    "ှုဉ်း": "one",
    "ှုဉ့်": "ont",
    "ှုဉ်": "oun",
    "ှုည်း": "one",
    "ှုည့်": "ont",
    "ှုည်": "oun",
    "ှုဋ်": "oat",
    "ှုဍ်": "oat",
    "ှုဏ်း": "one",
    "ှုဏ့်": "ont",
    "ှုဏ်": "oun",
    "ှုတ်": "oak",
    "ှုဒ်": "oak",
    "ှုန်း": "one",
    "ှုန့်": "ont",
    "ှုန်": "oun",
    "ှုပ်": "oke",
    "ှုဗ်": "oke",
    "ှုမ်း": "ome",
    "ှုမ့်": "omt",
    "ှုမ်": "oum",
    "ှုယ့်": "omt",
    "ှုယ်": "oun",
    "ှုရ်": "oun",
    "ှုလ်": "oun",
    "ှုဝ်": "oat",
    "ှုသ်": "oat",
    "ှုဟ်": "oan",
    "ုက်": "oak",
    "ုဂ်": "oak",
    "ုင်း": "one",
    "ုင့်": "ont",
    "ုင်": "oun",
    "ုစ်": "oat",
    "ုဇ်": "oat",
    "ုဉ်း": "one",
    "ုဉ့်": "ont",
    "ုဉ်": "oun",
    "ုည်း": "one",
    "ုည့်": "ont",
    "ုည်": "oun",
    "ုဋ်": "oat",
    "ုဍ်": "oat",
    "ုဏ်း": "one",
    "ုဏ့်": "ont",
    "ုဏ်": "oun",
    "ုတ်": "oak",
    "ုဒ်": "oak",
    "ုန်း": "one",
    "ုန့်": "ont",
    "ုန်": "oun",
    "ုပ်": "oke",
    "ုဗ်": "oke",
    "ုမ်း": "ome",
    "ုမ့်": "omt",
    "ုမ်": "oum",
    "ုယ့်": "omt",
    "ုယ်": "oun",
    "ုရ်": "oun",
    "ုလ်": "oun",
    "ုဝ်": "oat",
    "ုသ်": "oat",
    "ုဟ်": "oan",
    "ှက်": "et",
    "ှဂ်": "et",
    "ှင်း": "inn",
    "ှင့်": "int",
    "ှင်": "in",
    "ှစ်": "it",
    "ှဇ်": "it",
    "ှဉ်း": "inn",
    "ှဉ့်": "innt",
    "ှဉ်": "iin",
    "ှည်း": "ee",
    "ှည့်": "ei",
    "ှည်": "i",
    "ှဋ်": "at",
    "ှဍ်": "at",
    "ှဏ်း": "ann",
    "ှဏ့်": "ant",
    "ှဏ်": "an",
    "ှတ်": "at",
    "ှဒ်": "at",
    "ှန်း": "ann",
    "ှန့်": "ant",
    "ှန်": "an",
    "ှပ်": "ap",
    "ှဗ်": "ap",
    "ှမ်း": "amm",
    "ှမ့်": "amt",
    "ှမ်": "am",
    "ှယ့်": "ellt",
    "ှယ်": "el",
    "ှရ်": "el",
    "ှလ်": "an",
    "ှဝ်": "ap",
    "ှသ်": "at",
    "ှဟ်": "an",
    
    "က်": "et",
    "ဂ်": "et",
    "င်း": "inn",
    "င့်": "int",
    "င်": "in",
    "စ်": "it",
    "ဇ်": "it",
    "ဉ်း": "inn",
    "ဉ့်": "int",
    "ဉ်": "in",
    "ည်း": "ee",
    "ည့်": "ei",
    "ည်": "i",
    "ဋ်": "at",
    "ဍ်": "at",
    "ဏ်း": "ann",
    "ဏ့်": "ant",
    "ဏ်": "an",
    "တ်": "at",
    "ဒ်": "at",
    "န်း": "ann",
    "န့်": "ant",
    "န်": "an",
    "ပ်": "ap",
    "ဗ်": "ap",
    "မ်း": "amm",
    "မ့်": "amt",
    "မ်": "am",
    "ယ့်": "ellt",
    "ယ်": "el",
    "ရ်": "el",
    "လ်": "an",
    "ဝ်": "ap",
    "သ်": "at",
    "ဟ်": "an",
    "\u1031ရ်": "ay",
    "ွှိူက်": "waik",
    "ွှိုဂ်": "waik",
    "ွှိုင်း": "wine",
    "ွှိုင့်": "waint",
    "ွှိုင်": "waing",
    "ွှိုစ်": "waik",
    "ွှိုဇ်": "waik",
    "ွှိုဉ်း": "wainn",
    "ွှိုဉ့်": "wainnt",
    "ွှိုဉ်": "waiing",
    "ွှိုည်း": "waine",
    "ွှိုည့်": "waint",
    "ွှိုည်": "waing",
    "ွှိုဋ်": "waik",
    "ွှိုဍ်": "waik",
    "ွှိုဏ်း": "waine",
    "ွှိုဏ့်": "waint",
    "ွှိုဏ်": "waing",
    "ွှိူတ်": "waik",
    "ွှိုဒ်": "waik",
    "ွှိုန်း": "waine",
    "ွှိုန့်": "waint",
    "ွှိုန်": "waing",
    "ွှိုပ်": "waik",
    "ွှိုဗ်": "waik",
    "ွှိုမ်း": "waime",
    "ွှိုမ့်": "waimt",
    "ွှိုမ်": "waimg",
    "ွှိုယ့်": "woh",
    "ွှိုယ်": "wo",
    "ွှိုရ်": "wo",
    "ွှိုလ်": "wo",
    "ွှိုဝ်": "wo",
    "ွှိုသ်": "waik",
    "ွှိုဟ်": "wain",
    "ွိုက်": "waik",
    "ွိုဂ်": "waik",
    "ွိုင်း": "wine",
    "ွိုင့်": "waint",
    "ွိုင်": "waing",
    "ွိုစ်": "waik",
    "ွိုဇ်": "waik",
    "ွိုဉ်း": "wainn",
    "ွိုဉ့်": "wainnt",
    "ွိုဉ်": "waiin",
    "ွိုည်း": "waine",
    "ွိုည့်": "waint",
    "ွိုည်": "waing",
    "ွိုဋ်": "waik",
    "ွိုဍ်": "waik",
    "ွိုဏ်း": "waine",
    "ွိုဏ့်": "waint",
    "ွိုဏ်": "waing",
    "ွိုတ်": "waik",
    "ွိုဒ်": "waik",
    "ွိုန်း": "waine",
    "ွိုန့်": "waint",
    "ွိုန်": "waing",
    "ွိုပ်": "waik",
    "ွိုဗ်": "waik",
    "ွိုမ်း": "waime",
    "ွိုမ့်": "waimt",
    "ွိုမ်": "waimg",
    "ွိုယ့်": "woh",
    "ွိုယ်": "wo",
    "ွိုရ်": "wo",
    "ွိုလ်": "wo",
    "ွိုဝ်": "wo",
    "ွိုသ်": "waik",
    "ွိုဟ်": "wain",
    "ွှိက်": "weik",
    "ွှိဂ်": "weik",
    "ွှိင်း": "weinn",
    "ွှိင့်": "weint",
    "ွှိင်": "wein",
    "ွှိစ်": "weik",
    "ွှိဇ်": "weik",
    "ွှိဉ်း": "weinn",
    "ွှိဉ့်": "weinnt",
    "ွှိဉ်": "weiin",
    "ွှိည်း": "weinn",
    "ွှိည့်": "weint",
    "ွှိည်": "wein",
    "ွှိဋ်": "weik",
    "ွှိဍ်": "weik",
    "ွှိဏ်း": "weinn",
    "ွှိဏ့်": "weint",
    "ွှိဏ်": "wein",
    "ွှိတ်": "weik",
    "ွှိဒ်": "weik",
    "ွှိန်း": "weinn",
    "ွှိန့်": "weint",
    "ွှိန်": "wein",
    "ွှိပ်": "wake",
    "ွှိဗ်": "wake",
    "ွှိမ်း": "weimm",
    "ွှိမ့်": "weimt",
    "ွှိမ်": "weim",
    "ွှိယ့်": "weik",
    "ွှိယ်": "weik",
    "ွှိရ်": "weik",
    "ွှိလ်": "wein",
    "ွှိဝ်": "weik",
    "ွှိသ်": "weik",
    "ွှိဟ်": "wein",
    "ွိက်": "weik",
    "ွိဂ်": "weik",
    "ွိင်း": "weinn",
    "ွိင့်": "weint",
    "ွိင်": "wein",
    "ွိစ်": "weik",
    "ွိဇ်": "weik",
    "ွိဉ်း": "weinn",
    "ွိဉ့်": "weinnt",
    "ွိဉ်": "weiin",
    "ွိည်း": "weinn",
    "ွိည့်": "weint",
    "ွိည်": "wein",
    "ွိဋ်": "weik",
    "ွိဍ်": "weik",
    "ွိဏ်း": "weinn",
    "ွိဏ့်": "weint",
    "ွိဏ်": "wein",
    "ွိတ်": "weik",
    "ွိဒ်": "weik",
    "ွိန်း": "weinn",
    "ွိန့်": "weint",
    "ွိန်": "wein",
    "ွိပ်": "wake",
    "ွိဗ်": "wake",
    "ွိမ်း": "weimm",
    "ွိမ့်": "weimt",
    "ွိမ်": "weim",
    "ွိယ့်": "weik",
    "ွိယ်": "weik",
    "ွိရ်": "weik",
    "ွိလ်": "wein",
    "ွိဝ်": "weik",
    "ွိသ်": "weik",
    "ွိဟ်": "wein",
    "ွှက်": "wet",
    "ွှဂ်": "wet",
    "ွှင်း": "winn",
    "ွှင့်": "wint",
    "ွှင်": "win",
    "ွှစ်": "wit",
    "ွှဇ်": "wit",
    "ွှဉ်း": "winn",
    "ွှဉ့်": "winnt",
    "ွှဉ်": "wiin",
    "ွှည်း": "wee",
    "ွှည့်": "wei",
    "ွှည်": "wi",
    "ွှဋ်": "ut",
    "ွှဍ်": "ut",
    "ွှဏ်း": "unn",
    "ွှဏ့်": "unt",
    "ွှဏ်": "un",
    "ွှတ်": "ut",
    "ွှဒ်": "ut",
    "ွှန်း": "unn",
    "ွှန့်": "unt",
    "ွှန်": "un",
    "ွှပ်": "up",
    "ွှဗ်": "up",
    "ွှမ်း": "wamm",
    "ွှမ့်": "wamt",
    "ွှမ်": "wam",
    "ွှယ့်": "wellt",
    "ွှယ်": "wel",
    "ွှရ်": "wel",
    "ွှလ်": "wan",
    "ွှဝ်": "wap",
    "ွှသ်": "wat",
    "ွှဟ်": "wan",
    "ွက်": "wet",
    "ွဂ်": "wet",
    "ွင်း": "winn",
    "ွင့်": "wint",
    "ွင်": "win",
    "ွစ်": "wit",
    "ွဇ်": "wit",
    "ွဉ်း": "winn",
    "ွဉ့်": "winnt",
    "ွဉ်": "wiin",
    "ွည်း": "wee",
    "ွည့်": "wei",
    "ွည်": "wi",
    "ွဋ်": "ut",
    "ွဍ်": "ut",
    "ွဏ်း": "unn",
    "ွဏ့်": "unt",
    "ွဏ်": "un",
    "ွတ်": "ut",
    "ွဒ်": "ut",
    "ွန်း": "unn",
    "ွန့်": "unt",
    "ွန်": "un",
    "ွပ်": "oup",
    "ွဗ်": "oup",
    "ွမ်း": "wamm",
    "ွမ့်": "wamt",
    "ွမ်": "wam",
    "ွယ့်": "wellt",
    "ွယ်": "wel",
    "ွရ်": "wel",
    "ွလ်": "wan",
    "ွဝ်": "wap",
    "ွသ်": "wat",
    "ွဟ်": "wan",
}

vowel_extended_form = {
    "ှဲ": "el",  # အ
    "ို့": "oh",  # အို့
    "ှို့": "oh",  # အှို့
    "ိုး": "oe",
    "ှိုး": "oe",  #
    "\u1031\u102c\u103a": "aw",  # ကော်
    "\u103e\u1031\u102c\u103a": "aw",  # ကှော်
    "\u1031\u102b\u103a": "aw",  # ခေါ်
    "\u103e\u1031\u102b\u103a": "aw",  # ခှေါ်
    "\u1031\u102c\u1037": "awt",  # ကော့
    "\u103e\u1031\u102c\u1037": "awt",  # ကှော့
    "\u1031\u102b\u1037": "awt",  # ခေါ့
    "\u103e\u1031\u102b\u1037": "awt"  # ခှေါ့
    "ာ့": "a",
    "ှာ့": "a",
    "ါ့": "a",
    "ှါ့": "a",
    "ဲ့": "elt",
    "ှဲ့": "elt",
    "ှာ": "ar",
    "ှါ": "ar",
    "ား": "arr",
    "ှား": "arr",
    "ါး": "arr",
    "ှါး": "arr",
    "ံ့": "amt",
    "ှံ": "am",
    "ှံ့": "amt",
    "ုံး": "ome",
    "ှုံး": "ome",
    "ုံ့": "omt",
    "ှုံ့": "omt",
    "ုံ": "oum",
    "ှုံ": "oum",
    "ှု": "u",
    "ှူ": "uu",
    "\u103e\u1031": "ay", # အှေ
    "\u1031\u1037": "ae", # အေ့
    "\u103e\u1031\u1037": "ae", # အှေ့
    "\u1031\u1038": "aye", # အေး
    "\u103e\u1031\u1038": "aye", # အှေး
    "\u1031\u102c": "aww", # မော
    "\u103e\u1031\u102c": "aww", # မှော
    "\u1031\u102b": "aww", # ခေါ
    "\u103e\u1031\u102b": "aww", # ခှေါ
    "ီး": "ee",
    "ှီး": "ee",
    "ှီ": "e",
    "ှိ": "ei",
    "ူး": "oo",
    "ှူး": "ue",
    "\u102d\u102f": "o", # အို
    "\u103e\u102d\u102f": "o",
}

cluster_form = {"ျ": "y", "ြ": "y", "ွ": "w"}
modify_form = {"ခ": "ch", "ရ": "sh", "သ": "sh"}

def transcript(text: str) -> str:
    output = []
    i = 0

    while i < len(text):
        char = text[i]
        next_char = text[i + 1] if i + 1 < len(text) else ""
        after_next = text[i + 2] if i + 2 < len(text) else ""
        third_next = text[i + 3] if i + 3 < len(text) else ""
        all_but_s = text[1:] if len(text) > 1 else ""
        all_but_sc = text[2:] if len(text) > 2 else ""
        all_but_scc = text[3:] if len(text) > 3 else ""

        # Your processing logic would go here
        # For now, we'll just append the current character
        output.append(char)
        i += 1

    if (char in singleton and 
        next in clusterForm and 
        afterNext in clusterForm and 
        allButSCC in asatExtendedForm):
        if thirdNext == 'ှ':
            if ('ျ' in next or 'ြ' in next) and char in modifyForm:
                if 'ွ' in afterNext:
                    output.append(vowelForm[thirdNext] + 
                                modifyForm[char] + 
                                asatExtendedForm[allButSC])
                else:
                    output.append(vowelForm[thirdNext] + 
                                modifyForm[char] + 
                                clusterForm[afterNext] + 
                                asatExtendedForm[allButSCC])
            else:
        if 'ွ' in afterNext:
            output.append(
                vowel_form[thirdNext] +
                singleton[char] +
                cluster_form[next] +
                asat_extended_form[allButSC]
            )
        else:
            output.append(
                vowel_form[thirdNext] +
                singleton[char] +
                cluster_form[next] +
                cluster_form[afterNext] +
                asat_extended_form[allButSCC]
            )
    else:
        if ('ျ' in next or 'ြ' in next) and char in modify_form:
            if 'ွ' in after_next:
                output.append(modify_form[char] + asat_extended_form[all_but_sc])
            else:
                output.append(singleton[char] + 
                            cluster_form[next] + 
                            cluster_form[after_next] + 
                            asat_extended_form[all_but_scc])
        else:
            if 'ွ' in after_next:
                output.append(singleton[char] + 
                            cluster_form[next] + 
                            asat_extended_form[all_but_sc])
            else:
                output.append(singleton[char] + 
                            cluster_form[next] + 
                            cluster_form[after_next] + 
                            asat_extended_form[all_but_scc])
        i += 3 + len(all_but_scc)
        # debug_print('rule 4.2: Singleton + Cluster + Cluster + AsatExtendedForm')

    elif (char in singleton and 
        next in clusterForm and 
        allButSC in asatExtendedForm):
        if afterNext == 'ှ':
            if 'ွ' in next:
                if 'ရ' in char:
                    output.append(f'sh{asatExtendedForm[allButS]}')
                else:
                    output.append(vowelForm[afterNext] + 
                                singleton[char] + 
                                asatExtendedForm[allButS])
            elif ('ျ' in next or 'ြ' in next) and char in modifyForm:
                output.append(f'{vowelForm[afterNext]}{modifyForm[char]}{asatExtendedForm[allButSC]}')
            else:
                output.append(vowelForm[afterNext] + 
                            singleton[char] + 
                            clusterForm[next] + 
                            asatExtendedForm[allButSC])
            i += 3 + len(allButSC)
        else:
            if 'ွ' in next:
                output.append(singleton[char] + asatExtendedForm[allButS])
            elif ('ျ' in next or 'ြ' in next) and char in modifyForm:
                output.append(f'{modifyForm[char]}{asatExtendedForm[allButSC]}')
            else:
                output.append(singleton[char] + 
                            clusterForm[next] + 
                            asatExtendedForm[allButSC])
            i += 2 + len(allButSC)
        # print('rule 4.1: Singleton + Cluster + AsatExtendedForm')

    # Rule 4.0: Singleton + AsatExtendedForm
    elif (char in singleton and 
        allButS in asatExtendedForm):
        if next == 'ှ':
            if 'ရ' in char:
                output.append(f'sh{asatExtendedForm[allButS]}')
            else:
                output.append(vowelForm[next] + 
                            singleton[char] + 
                            asatExtendedForm[allButS])
            i += 2 + len(allButS)
        else:
            output.append(f"{singleton[char]}{asatExtendedForm[allButS]}")
            i += 1 + len(allButS)
        # print('rule 4.0: Singleton + AsatExtendedForm')
    if (char in singleton and 
        next in clusterForm and 
        after_next in clusterForm and 
        all_but_scc in vowelExtendedForm):
        if third_next == 'ှ':
            if ('ျ' in next or 'ြ' in next) and char in modifyForm:
                output.append(
                    f"{vowelForm[third_next]}{modifyForm[char]}{clusterForm[after_next]}{vowelExtendedForm[all_but_scc]}")
            else:
                output.append(
                    f"{vowelForm[third_next]}{singleton[char]}{clusterForm[next]}{clusterForm[after_next]}{vowelExtendedForm[all_but_scc]}")
            i += 3 + len(all_but_scc)
        else:
            if ('ျ' in next or 'ြ' in next) and char in modifyForm:
                output.append(modifyForm[char] + 
                            clusterForm[after_next] + 
                            vowelExtendedForm[all_but_scc])
            else:
                output.append(singleton[char] + 
                            clusterForm[next] + 
                            clusterForm[after_next] + 
                            vowelExtendedForm[all_but_scc])
            i += 3 + len(all_but_scc)
        # debugPrint('rule 3.1: Singleton + Cluster + Cluster + Extended')

    # Rule 3.0: Singleton + Cluster + Cluster + Vowel
    elif (char in singleton and 
        next in clusterForm and 
        after_next in clusterForm):
        if third_next in vowelForm:
            if third_next == 'ှ':
                if ('ျ' in next or 'ြ' in next) and char in modifyForm:
                    output.append(
                        f"{vowelForm[third_next]}{modifyForm[char]}{clusterForm[after_next]}a")
                else:
                    output.append(
                        f"{vowelForm[third_next]}{singleton[char]}{clusterForm[next]}{clusterForm[after_next]}a")
            else:
                if ('ျ' in next or 'ြ' in next) and char in modifyForm:
                    output.append(modifyForm[char] + 
                                clusterForm[after_next] + 
                                vowelForm[third_next])
                else:
                    output.append(singleton[char] + 
                                clusterForm[next] + 
                                clusterForm[after_next] + 
                                vowelForm[third_next])
            i += 4
        else:
            if ('ျ' in next or 'ြ' in next) and char in modifyForm:
                output.append(f"{modifyForm[char]}{clusterForm[after_next]}a")
            else:
                output.append(
                    f"{singleton[char]}{clusterForm[next]}{clusterForm[after_next]}a")
            i += 3
        # debugPrint('rule 3.0: Singleton + Cluster + Cluster + Vowel')
    elif (char in singleton and 
        next in clusterForm and 
        allButSC in vowelExtendedForm):
        if afterNext == 'ှ':
            if (('ျ' in next or 'ြ' in next) and 
                char in modifyForm):
                output.append(vowelForm[afterNext] + 
                            modifyForm[char] + 
                            vowelExtendedForm[allButSC])
            else:
                if 'ရ' in char:
                    output.append(f'sh{clusterForm[next]}{vowelExtendedForm[allButSC]}')
                else:
                    output.append(vowelForm[afterNext] + 
                                singleton[char] + 
                                clusterForm[next] + 
                                vowelExtendedForm[allButSC])
            i += 2 + len(allButSC)
        else:
            if (('ျ' in next or 'ြ' in next) and 
                char in modifyForm):
                output.append(modifyForm[char] + vowelExtendedForm[allButSC])
            else:
                output.append(singleton[char] + 
                            clusterForm[next] + 
                            vowelExtendedForm[allButSC])
            i += 2 + len(allButSC)
        # debugPrint('rule 2.1: Singleton + Cluster + Vowel Extended')

    # Rule 2.0: Singleton + Cluster + Vowel
    elif (char in singleton and next in clusterForm):
        if afterNext in vowelForm:
            if afterNext == 'ှ':
                if (('ျ' in next or 'ြ' in next) and 
                    char in modifyForm):
                    output.append(f'{vowelForm[afterNext]}{modifyForm[char]}a')
                else:
                    if 'ရ' in char:
                        output.append(f'sh{clusterForm[next]}a')
                    else:
                        output.append(f'{vowelForm[afterNext]}{singleton[char]}{clusterForm[next]}a')
            else:
                if (('ျ' in next or 'ြ' in next) and 
                    char in modifyForm):
                    output.append(modifyForm[char] + vowelForm[afterNext])
                else:
                    output.append(singleton[char] + 
                                clusterForm[next] + 
                                vowelForm[afterNext])
            i += 3
        else:
            if (('ျ' in next or 'ြ' in next) and 
                char in modifyForm):
                output.append(f'{modifyForm[char]}a')
            else:
                output.append(f'{singleton[char]}{clusterForm[next]}a')
            i += 2
        # debugPrint('rule 2.0: Singleton + Cluster + Vowel')
    return ''.join(output)