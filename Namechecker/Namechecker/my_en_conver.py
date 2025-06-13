import preprocess as p
import mm_transpitor_module as mm
import json
import asyncio
from aiofile import async_open

async def load_mappings():
    async with async_open('./mm_eng_mapping.json', 'r') as f:
        response_mm = await f.read()
    async with async_open('./pali_roman_mapping.json', 'r') as f:
        response_pali = await f.read()
    
    mapping_mm = json.loads(response_mm)
    mapping_pali = json.loads(response_pali)
    
    return mapping_mm, mapping_pali


async def main():
    # mapped_names = ''
    # input_text="တိုးအောင်"
    mapping_mm, mapping_pali = await load_mappings()   
    
    # word_dict=mapping_mm

    
    # # Step 1: Preprocess
    # normalized_text = p.normalize_text(input_text)
    # processed_text = p.preprocess(normalized_text)
  
    # word_list = processed_text.split(' ')
    # mapped_names = ' '.join(p.get_map(word, word_dict) for word in word_list)
    
   
    # input_code_point = ''.join(hex(ord(char)) for char in processed_text)
    # output_text= ' '.join(word.capitalize() for word in mapped_names.split())
    # #output_text = p.capitalize(mapped_names)

    # print("result str : "+ output_text)

    ###############################

    mapped_names1 = ''
    input_text="နန္ဓမာလာဘိဝံသ"  
    
    word_dict=mapping_pali
    print("result word : "+ word_dict)
    
    # Step 1: Preprocess
    normalized_text1 = p.normalize_text(input_text)
    processed_text = p.preprocess(normalized_text1)
  
    word_list = processed_text.split(' ')
    mapped_names = ' '.join(p.get_map(word, word_dict) for word in word_list)
    
   
    input_code_point = ''.join(hex(ord(char)) for char in processed_text)
    output_text1= ' '.join(word.capitalize() for word in mapped_names.split())
    #output_text = p.capitalize(mapped_names)

    print("result str : "+ output_text1)  
if __name__=="__main__":
    asyncio.run(main())


