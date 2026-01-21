import json
import os
import ast

# src_paths = [
#     "/data1/kmz/QAdata/train.jsonl",
#     "/data1/kmz/QAdatav2/train_single_v2.jsonl",
# ]
# tgt_path = "/data1/hyw/QAdata/train.veomni.single_img.merged_v1_v2.json"

# src_paths = [
#     "/data1/kmz/QAdatav2/train_pairs_v2.jsonl",
# ]
# tgt_path = "/data1/hyw/QAdata/train.veomni.pairs.v2.json"

src_paths = [
    "/data1/kmz/QAdata/train.jsonl",
    "/data1/kmz/QAdatav2/train_single_v2.jsonl",
    "/data1/kmz/QAdatav2/train_pairs_v2.jsonl",
]
tgt_path = "/data1/hyw/QAdata/train.veomni.all.merged_v1_v2.json" # 119391

context = []
for path in src_paths:
    with open(path, "r") as f:
        context.extend(f.readlines())

tgt_data = []
id = 0
for line in context:
    item = ast.literal_eval(line.strip())
    if type(item["image_bin"]) is list:
        assert len(item["image_bin"]) == 1 or len(item["image_bin"]) == 2
    elif type(item["image_bin"]) is str:
        item["image_bin"] = [item["image_bin"]]
    else:
        print(f"not supported type {type(item['image_bin'])}")
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
        # "scene": item["scene"],
        # "recep": item["recep"],
    })
    # print(item["image_resolution"][0])
    # break
    
print(f"total samples: {len(tgt_data)}")
with open(tgt_path, 'w') as f:
    json.dump(tgt_data, f, indent=4)