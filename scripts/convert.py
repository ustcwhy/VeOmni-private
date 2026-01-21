import json
import os
import ast

src_path = "/data1/kmz/QAdata/train.jsonl"
tgt_path = "/data1/hyw/QAdata/train.veomni.json"
with open(src_path, "r") as f:
    context = f.readlines()

tgt_data = []
id = 0
for line in context:
    item = ast.literal_eval(line.strip())
    tgt_data.append({
        "id": id,
        "image": item["image_bin"],
        "image_bin": item["image_bin"],
        "image_resolution": item["image_resolution"],
        "conversations": [
            {
                "from": "human",
                "value": f"<image>\n{item['instruction']}"
            },
            {
                "from": "gpt",
                "value": item["answer"],
            }
        ],
        "scene": item["scene"],
        "recep": item["recep"],
    })
    # print(item["image_resolution"][0])
    # break
    

with open(tgt_path, 'w') as f:
    json.dump(tgt_data, f, indent=4)