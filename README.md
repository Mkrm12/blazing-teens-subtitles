# Blazing Teens (2006) — English Subtitles

Complete English subtitles (`.srt`) for all 40 episodes of the 2006 Chinese live-action series ***Blazing Teens*** (**火力少年王** / *Huǒlì Shàoniánwáng*, Season 1), alongside the custom 4-pillar AI extraction pipeline built to localize them.

### Download Subtitles

* **Complete Season 1 Pack (All 40 Episodes):** [**Download `BlazingTeens_2006_SRTs.zip`**](./subtitles/BlazingTeens_2006_SRTs.zip) *(also on [GitHub Releases](../../releases/tag/v1.0.0))*
* **Individual Episodes:** Browse the [**`subtitles/`**](./subtitles/) folder (`S01E01.srt` – `S01E40.srt`)

The pack contains **40 separate SubRip (`.srt`) files — one per episode** — each reviewed by hand across 4 quality-control passes rather than published as raw machine translation.

### Watching with Subtitles

* **Over Official YouTube:** All 40 raw Chinese episodes are hosted on the official [**火力少年王 Blazing Teens** YouTube channel (`@blazingteens2484`)](https://www.youtube.com/watch?v=Xh0Yl-H1Y2Y). Install a free subtitle overlay extension such as [Substital](https://substital.com/) or [asbplayer](https://github.com/killergerbah/asbplayer), open any episode, and drag the matching `.srt` file onto the video.
* **Local Video Playback:** Drop any raw `.mp4` episode and `.srt` file into VLC/MPV, or use the included millisecond-accurate browser player ([`player.html`](./player.html)).

---

### The Origin Story

This started as a pure passion project. Growing up across Asia, *Blazing Teens* (2006) aired dubbed on networks like Cartoon Network and Pogo and sparked a massive Auldey yo-yo craze. Two decades later, all of the old English and Hindi broadcast dubs have become lost media — only raw Mandarin episodes with hardcoded Chinese text burned directly into the video frames survived.

Standard AI transcription tools (like raw Whisper) fail completely on 2000s Chinese sports dramas. They hallucinate during loud action scenes, stutter when characters shout, and ignore burned-in on-screen text like location signs and named yo-yo techniques. I needed a pipeline that could literally "watch" each frame the way a human would before handing structured context to an LLM for translation.

### How the Pipeline Works (The 4 Pillars)

Rather than transcribing audio in isolation, the pipeline builds a chronologically clamped multimodal context dump for each episode:

1. **Audio (`Whisper`):** Extracts raw Mandarin dialogue and runs a custom NLP deduplicator to strip out "Whisper stutters" during loud yo-yo battles.
2. **Speaker Diarization (`PyAnnote`):** Maps speaker turns across multi-character scenes so dialogue attribution stays consistent.
3. **Dual-Box OCR Master Clock (`EasyOCR` + `PaddleOCR`):** Sweeps video frames to read hardcoded Chinese subtitles, location cards, and technique titles — acting as the master timing anchor so subtitle cues stay synced and readable.
4. **Vision Context (`Florence-2`):** Generates concise visual scene descriptions so the translation stage understands what is physically happening on screen.

Output dumps are split into two parts per episode to avoid LLM context-window degradation, checked mathematically for timestamp overlaps with [`stitcher.py`](./stitcher.py), and reviewed across 4 manual QC passes using [`player.html`](./player.html).

### Translation & Localization

During development, several models were benchmarked across 200+ block multimodal batches (including Mistral and Qwen). A dual-model workflow proved strongest: **DeepSeek** handled dense structural translation and slang consistency, while **Gemini** refined natural English phrasing.

Across the final manual QC passes, character names, teams (*Jianghai*, *Chengnan*, *Saint Qiao*), competitive `1A`/`2A`/`4A` yo-yo trick names, and official **Auldey** yo-yo models (*Fire Warrior*, *Fire Warrior S*, *Fire Silver Electricity*, *Blazing Dragon Ball*, *Phantom Light Wheel*, *Speed Demon*, *Storm War Eagle*, *Shock Wave*, *Vortex*, *Super Light Speed*, *Nuclear Fission*, *Ghost Face*) were standardized across all 40 episodes. To view the Pinyin-to-English character mapping or batch-swap names across all 40 `.srt` files at once, see [`name_swapper.py`](./name_swapper.py).

### Character Names

The subtitles use the English names familiar from the international broadcast. For viewers who know the original Mandarin names, the main mappings are:

| Team | Original Name (Pinyin) | Name in Subtitles |
| :--- | :--- | :--- |
| Jianghai | Li Fei (李非) — lead, played by Zhang Yifan (张逸凡) | Leo |
| Jianghai | Mai Jun (麦军) | Mark |
| Jianghai | Mi Li (米莉) | Mini |
| Jianghai | Mi Fan | Mickey |
| Jianghai | Mao Dayu | Matthew |
| Jianghai | Wang Xiaohua | Monica |
| Jianghai | Zhao Xiaosong | Shawn |
| Jianghai | Song Yuan | Chuck |
| Jianghai | Ding Wei | Teddy |
| Jianghai | Coach Gao Dashu (高大树) | Coach Tony |
| Chengnan | Chen Hao (陈浩) | Jacky |
| Chengnan | Ma Kai (马凯) | Marco |
| Chengnan | Zhou Yanyan | Zoe |
| Chengnan | Hu Xiaoyong | Hugo |
| Chengnan | Coach Xiao Shengnan | Coach Sarah |
| Saint Qiao | Maike / Mike (迈克) | Michael |
| Saint Qiao | Gu Deng | Gordon |
| Saint Qiao | Lin Na | Linda |
| Saint Qiao | Coach Wu Qiang | Coach William |

<details>
<summary><strong>Episode Subtitle File Index (Episodes 01–40)</strong></summary>

<br>

| Episode | File | Episode | File |
| :--- | :--- | :--- | :--- |
| Episode 01 | [`BlazingTeens_2006_S01E01.srt`](./subtitles/BlazingTeens_2006_S01E01.srt) | Episode 21 | [`BlazingTeens_2006_S01E21.srt`](./subtitles/BlazingTeens_2006_S01E21.srt) |
| Episode 02 | [`BlazingTeens_2006_S01E02.srt`](./subtitles/BlazingTeens_2006_S01E02.srt) | Episode 22 | [`BlazingTeens_2006_S01E22.srt`](./subtitles/BlazingTeens_2006_S01E22.srt) |
| Episode 03 | [`BlazingTeens_2006_S01E03.srt`](./subtitles/BlazingTeens_2006_S01E03.srt) | Episode 23 | [`BlazingTeens_2006_S01E23.srt`](./subtitles/BlazingTeens_2006_S01E23.srt) |
| Episode 04 | [`BlazingTeens_2006_S01E04.srt`](./subtitles/BlazingTeens_2006_S01E04.srt) | Episode 24 | [`BlazingTeens_2006_S01E24.srt`](./subtitles/BlazingTeens_2006_S01E24.srt) |
| Episode 05 | [`BlazingTeens_2006_S01E05.srt`](./subtitles/BlazingTeens_2006_S01E05.srt) | Episode 25 | [`BlazingTeens_2006_S01E25.srt`](./subtitles/BlazingTeens_2006_S01E25.srt) |
| Episode 06 | [`BlazingTeens_2006_S01E06.srt`](./subtitles/BlazingTeens_2006_S01E06.srt) | Episode 26 | [`BlazingTeens_2006_S01E26.srt`](./subtitles/BlazingTeens_2006_S01E26.srt) |
| Episode 07 | [`BlazingTeens_2006_S01E07.srt`](./subtitles/BlazingTeens_2006_S01E07.srt) | Episode 27 | [`BlazingTeens_2006_S01E27.srt`](./subtitles/BlazingTeens_2006_S01E27.srt) |
| Episode 08 | [`BlazingTeens_2006_S01E08.srt`](./subtitles/BlazingTeens_2006_S01E08.srt) | Episode 28 | [`BlazingTeens_2006_S01E28.srt`](./subtitles/BlazingTeens_2006_S01E28.srt) |
| Episode 09 | [`BlazingTeens_2006_S01E09.srt`](./subtitles/BlazingTeens_2006_S01E09.srt) | Episode 29 | [`BlazingTeens_2006_S01E29.srt`](./subtitles/BlazingTeens_2006_S01E29.srt) |
| Episode 10 | [`BlazingTeens_2006_S01E10.srt`](./subtitles/BlazingTeens_2006_S01E10.srt) | Episode 30 | [`BlazingTeens_2006_S01E30.srt`](./subtitles/BlazingTeens_2006_S01E30.srt) |
| Episode 11 | [`BlazingTeens_2006_S01E11.srt`](./subtitles/BlazingTeens_2006_S01E11.srt) | Episode 31 | [`BlazingTeens_2006_S01E31.srt`](./subtitles/BlazingTeens_2006_S01E31.srt) |
| Episode 12 | [`BlazingTeens_2006_S01E12.srt`](./subtitles/BlazingTeens_2006_S01E12.srt) | Episode 32 | [`BlazingTeens_2006_S01E32.srt`](./subtitles/BlazingTeens_2006_S01E32.srt) |
| Episode 13 | [`BlazingTeens_2006_S01E13.srt`](./subtitles/BlazingTeens_2006_S01E13.srt) | Episode 33 | [`BlazingTeens_2006_S01E33.srt`](./subtitles/BlazingTeens_2006_S01E33.srt) |
| Episode 14 | [`BlazingTeens_2006_S01E14.srt`](./subtitles/BlazingTeens_2006_S01E14.srt) | Episode 34 | [`BlazingTeens_2006_S01E34.srt`](./subtitles/BlazingTeens_2006_S01E34.srt) |
| Episode 15 | [`BlazingTeens_2006_S01E15.srt`](./subtitles/BlazingTeens_2006_S01E15.srt) | Episode 35 | [`BlazingTeens_2006_S01E35.srt`](./subtitles/BlazingTeens_2006_S01E35.srt) |
| Episode 16 | [`BlazingTeens_2006_S01E16.srt`](./subtitles/BlazingTeens_2006_S01E16.srt) | Episode 36 | [`BlazingTeens_2006_S01E36.srt`](./subtitles/BlazingTeens_2006_S01E36.srt) |
| Episode 17 | [`BlazingTeens_2006_S01E17.srt`](./subtitles/BlazingTeens_2006_S01E17.srt) | Episode 37 | [`BlazingTeens_2006_S01E37.srt`](./subtitles/BlazingTeens_2006_S01E37.srt) |
| Episode 18 | [`BlazingTeens_2006_S01E18.srt`](./subtitles/BlazingTeens_2006_S01E18.srt) | Episode 38 | [`BlazingTeens_2006_S01E38.srt`](./subtitles/BlazingTeens_2006_S01E38.srt) |
| Episode 19 | [`BlazingTeens_2006_S01E19.srt`](./subtitles/BlazingTeens_2006_S01E19.srt) | Episode 39 | [`BlazingTeens_2006_S01E39.srt`](./subtitles/BlazingTeens_2006_S01E39.srt) |
| Episode 20 | [`BlazingTeens_2006_S01E20.srt`](./subtitles/BlazingTeens_2006_S01E20.srt) | Episode 40 | [`BlazingTeens_2006_S01E40.srt`](./subtitles/BlazingTeens_2006_S01E40.srt) |

</details>

### FAQ

**Which series is this for?**
The original 2006 Chinese live-action *Blazing Teens* (火力少年王, Season 1, 40 episodes) following Li Fei / Leo and the Jianghai yo-yo team. It is not for the later animated *Blazing Teens* spin-offs.

**Are all 40 episodes included?**
Yes. Episodes 1–40 are each provided as a separate `.srt` file (`BlazingTeens_2006_S01E01.srt` – `S01E40.srt`), and all 40 are also bundled in a single `.zip`.

**Are these raw machine translations?**
No. The pipeline produced the first draft, then every episode went through 4 manual QC passes for timing, translation accuracy, character names, and yo-yo terminology.

**Which video do they sync to?**
They are timed against the 40-episode Mandarin broadcast — the same episodes uploaded on the official 火力少年王 Blazing Teens YouTube channel (`@blazingteens2484`).

**Is this the same pack that's on other subtitle sites?**
Yes. The same Season 1 English pack (one `.zip`, 307 KB) was uploaded by the author to subtitle databases such as Podnapisi on 22 August 2026. This repository is the primary, maintained source.

---

### License & Rights Confirmation

© 2026 Mukarram Nazir. See [`LICENSE`](./LICENSE) for full terms:

* **All 40 English Subtitle Files (`S01E01.srt` – `S01E40.srt` & `.zip` archive):** Original English translations and timing created independently from scratch by Mukarram Nazir and published under [**CC BY 4.0**](https://creativecommons.org/licenses/by/4.0/).
* **Official Rights-Holder Permission:** **Alpha Group Co., Ltd. (广东奥飞娱乐股份有限公司)**, its subsidiaries, and authorized channel operators are additionally granted a perpetual, worldwide, royalty-free license to review, modify, and publish all 40 English subtitle tracks across official YouTube channels and platforms free of charge and without restriction.
* **Pipeline Code & Tooling:** Licensed under the **MIT License**.

*Disclaimer: Blazing Teens (火力少年王) and its underlying episodes and characters are the intellectual property of Alpha Group Co., Ltd. / Auldey. This is a non-commercial fan preservation project.*
