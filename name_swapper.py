import os
import re

# --- CONFIGURATION ---
# Reads the 40 SRT files in `subtitles/` and writes updated copies to
# `subtitles_updated/` (leaving the original SRT files untouched).
INPUT_DIR = "subtitles"
OUTPUT_DIR = "subtitles_updated"

# The Master Lore Dictionary used during localization (Pinyin -> Localized English).
# Swap or edit any key/value pairs below to mass-update names across all 40 episodes.
LORE_MAPPING = {
    # --- JIANGHAI TEAM ---
    "Li Fei": "Leo",
    "Xiao Fei": "Leo",
    "Mai Jun": "Mark",
    "Ding Wei": "Teddy",
    "David": "Teddy",
    "Wang Xiaohua": "Monica",
    "Zhao Xiaosong": "Shawn",
    "Mi Li": "Mini",
    "Milly": "Mini",
    "Mi Fan": "Mickey",
    "Coach Gao": "Coach Tony",
    "Gao Dashu": "Tony",
    "Song Yuan": "Chuck",
    "Mao Dayu": "Matthew",

    # --- CHENGNAN TEAM ---
    "Chen Hao": "Jacky",
    "Ken": "Jacky",
    "Zhou Yanyan": "Zoe",
    "Hu Xiaoyong": "Hugo",
    "Coach Xiao": "Coach Sarah",
    "Xiao Shengnan": "Sarah",
    "Ma Kai": "Marco",

    # --- SAINT QIAO TEAM ---
    "Maike": "Michael",
    "Geu Deung": "Gordon",
    "Gu Deng": "Gordon",
    "Linna": "Linda",
    "Lin Na": "Linda",
    "Coach Wu": "Coach William",
    "Wu Qiang": "William",
}

# Compile a regex pattern sorted by longest key first with word boundaries (\b)
# This prevents partial overlaps and avoids replacing letters inside other words.
sorted_keys = sorted(LORE_MAPPING.keys(), key=len, reverse=True)
pattern = re.compile(
    r"\b(" + "|".join(map(re.escape, sorted_keys)) + r")\b",
    re.IGNORECASE,
)


def replace_names(match):
    """Callback function to grab the correct replacement with exact casing"""
    old_name = match.group(0)
    # Find the matching key in our dictionary (ignoring case)
    for key, value in LORE_MAPPING.items():
        if key.lower() == old_name.lower():
            return value
    return old_name


def process_srt(file_path, output_path, filename):
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read().replace("\r\n", "\n")

    # Split the SRT into individual blocks (separated by double newlines)
    blocks = content.strip().split("\n\n")
    new_blocks = []

    for block in blocks:
        lines = block.split("\n")
        # A valid SRT block needs at least 3 lines: Index, Timecode, Text
        if len(lines) >= 3:
            block_idx = lines[0]
            timecode = lines[1]
            text = "\n".join(lines[2:])

            # Check if any old names exist in the text
            if pattern.search(text):
                new_text = pattern.sub(replace_names, text)

                # Log the change to the terminal
                print(f"[{filename} | Block {block_idx}]")
                print(f"  [-] Old: {text.replace(chr(10), ' ')}")
                print(f"  [+] New: {new_text.replace(chr(10), ' ')}\n")

                # Reconstruct the block with the new text
                new_blocks.append(f"{block_idx}\n{timecode}\n{new_text}")
            else:
                new_blocks.append(block)
        else:
            new_blocks.append(block)

    # Write the patched blocks to the new file
    with open(output_path, "w", encoding="utf-8") as f:
        f.write("\n\n".join(new_blocks) + "\n")


def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    print(">>> Firing up the Auto-Patcher...\n")

    processed_count = 0

    for filename in sorted(os.listdir(INPUT_DIR)):
        if not filename.lower().endswith(".srt"):
            continue

        source_path = os.path.join(INPUT_DIR, filename)
        target_path = os.path.join(OUTPUT_DIR, filename)

        process_srt(source_path, target_path, filename)
        processed_count += 1

    print(f">>> Swept {processed_count} files. Patched files saved in '{OUTPUT_DIR}'.")


if __name__ == "__main__":
    main()
