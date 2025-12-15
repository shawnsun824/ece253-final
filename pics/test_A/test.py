import os
import re

test_A_dir = "/home/has038/teams/project-team-7/pics/test_A"

# 先预览要删哪些：True = 只打印不删除；False = 真删
dry_run = False

# 匹配：文件名是纯数字（无前导0），扩展名是常见图片格式
pattern = re.compile(r"^[1-9]\d*\.(jpg|jpeg|png|bmp|tif|tiff|webp)$", re.IGNORECASE)

to_delete = []
for fn in os.listdir(test_A_dir):
    if pattern.match(fn):
        to_delete.append(fn)

to_delete = sorted(to_delete, key=lambda x: int(os.path.splitext(x)[0]))

print(f"[INFO] Found {len(to_delete)} files to delete in {test_A_dir}:")
print(to_delete[:20], "..." if len(to_delete) > 20 else "")

if not dry_run:
    deleted = 0
    for fn in to_delete:
        path = os.path.join(test_A_dir, fn)
        os.remove(path)
        deleted += 1
    print(f"[DONE] Deleted {deleted} files.")
else:
    print("[DRY RUN] No files deleted. Set dry_run=False to actually delete.")
