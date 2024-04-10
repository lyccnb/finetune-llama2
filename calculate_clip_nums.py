# 统计 fho_lta_test_unannnotated fho_lta_train fho_lta_val 分别有多少个 clips
filename_train="/data2/liuyicheng/datasets/Ego4d/v2/annotations/fho_lta_train.json"
filename_val="/data2/liuyicheng/datasets/Ego4d/v2/annotations/fho_lta_val.json"
filename_test="/data2/liuyicheng/datasets/Ego4d/v2/annotations/fho_lta_test_unannotated.json"
import json
for filename, split in zip([filename_train, filename_val, filename_test], ["train", "val", "test"]):
    with open(filename, "r") as f:
        data = json.load(f)
    clip_uids = [clip['clip_uid'] for clip in data['clips']]
    unique_clip_count = len(set(clip_uids))
    print(split ,":", unique_clip_count)