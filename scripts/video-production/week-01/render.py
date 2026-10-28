#!/usr/bin/env python3
"""Render the Week 1 script as a narrated, captioned 1080p lesson.

Dependencies: Pillow, numpy, sherpa-onnx==1.12.40, ffmpeg with libass.
Pass --model-dir pointing at the unpacked en_US-ljspeech-medium model.
All speech is generic synthesis; no speaker cloning is used.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import math
from pathlib import Path
import re
import subprocess
import textwrap
import wave

import numpy as np
from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parents[3]
SCRIPT = ROOT / "scripts/lessons/phase-1/week-01-environment-and-git.md"
DEFAULT_OUT = ROOT / "videos/week-01-make-your-setup-reproducible"
W, H = 1920, 1080
BG = "#0D1521"
PANEL = "#152233"
LINE = "#2B3D52"
INK = "#F3F6FA"
MUTED = "#A8B8C9"
ORANGE = "#E8842A"
BLUE = "#6FA3D2"
GREEN = "#8CD6B0"
RED = "#F69B94"
FONT_ROOT = Path("/usr/share/fonts/truetype/dejavu")


def font(size, bold=False, mono=False):
    name = "DejaVuSansMono" if mono else "DejaVuSans"
    if bold:
        name += "-Bold"
    return ImageFont.truetype(str(FONT_ROOT / (name + ".ttf")), size)


def text(draw, xy, value, size=30, color=INK, bold=False, mono=False):
    draw.text(xy, value, font=font(size, bold, mono), fill=color)


def wrapped(draw, xy, value, width, size=30, color=INK, bold=False, spacing=12):
    lines, line = [], ""
    for word in value.split():
        candidate = (line + " " + word).strip()
        if draw.textlength(candidate, font=font(size, bold)) > width and line:
            lines.append(line)
            line = word
        else:
            line = candidate
    if line:
        lines.append(line)
    for index, line in enumerate(lines):
        text(draw, (xy[0], xy[1] + index * (size + spacing)), line, size, color, bold)
    return xy[1] + len(lines) * (size + spacing)


def box(draw, bounds, color=PANEL, outline=LINE, radius=22):
    draw.rounded_rectangle(bounds, radius=radius, fill=color, outline=outline, width=2)


def terminal(draw, bounds, lines, label="TERMINAL", size=31, highlight=None):
    x, y, right, bottom = bounds
    box(draw, bounds, "#101B29")
    draw.line((x, y + 62, right, y + 62), fill=LINE, width=2)
    for i, color in enumerate(("#F08079", "#EBC16B", "#7FC6A2")):
        draw.ellipse((x + 26 + i * 26, y + 24, x + 40 + i * 26, y + 38), fill=color)
    text(draw, (x + 130, y + 19), label, 21, MUTED, mono=True)
    for i, item in enumerate(lines):
        value, color = item if isinstance(item, tuple) else (item, INK)
        yy = y + 91 + i * (size + 18)
        if highlight == i:
            draw.rounded_rectangle((x + 17, yy - 5, right - 17, yy + size + 10), 8, fill="#293226")
        text(draw, (x + 33, yy), value, size, color, mono=True)


TITLES = [
    ("Make your setup reproducible", "A working script is only the beginning."),
    ("Start in the right directory", "Check your location before changing your code."),
    ("Isolate the interpreter", "Create it. Activate it. Pin the dependencies."),
    ("Choose what enters history", "Ignore local environments, credentials, and raw data."),
    ("Know the Git states", "Working tree → stage → local history → remote"),
    ("Keep the change reviewable", "A small baseline, three meaningful commits, then review."),
    ("Prove it with a fresh clone", "Rebuild from the README and requirements alone."),
    ("Bring evidence to the review", "A clean setup and a history you can explain."),
]
CHAPTERS = ["THE PROBLEM", "LOCATION", "ENVIRONMENT", "IGNORE RULES", "GIT STATES", "REVIEW", "FRESH CLONE", "YOUR EVIDENCE"]


def base(scene):
    image = Image.new("RGB", (W, H), BG)
    draw = ImageDraw.Draw(image)
    draw.rectangle((0, 0, 13, H), fill=ORANGE)
    text(draw, (80, 44), "GAMBILL DATA", 26, ORANGE, True)
    text(draw, (80, 85), "DATA ENGINEER TRACK / LAUNCH", 19, MUTED)
    text(draw, (1550, 49), "WEEK 01  ·  M00", 22, BLUE, True)
    title, subtitle = TITLES[scene]
    text(draw, (80, 150), title, 58, INK, True)
    text(draw, (83, 232), subtitle, 29, MUTED)
    draw.line((80, 305, 1840, 305), fill=LINE, width=2)
    draw.rectangle((14, 918, W, H), fill="#080F19")
    # A reserved caption band keeps subtitles clear of the lesson graphics.
    text(draw, (80, 884), "SYNTHETIC NARRATION  /  ORIGINAL WEEK 1 LESSON SCRIPT", 17, MUTED)
    for i in range(8):
        xx = 80 + i * 222
        draw.rounded_rectangle((xx, 1048, xx + 205, 1055), 3, fill=ORANGE if i <= scene else LINE)
        text(draw, (xx, 1062), CHAPTERS[i], 12, MUTED)
    return image, draw


def scene_image(scene, sentence):
    image, d = base(scene)
    if scene == 0:
        box(d, (80, 365, 875, 722))
        box(d, (1045, 365, 1840, 722))
        text(d, (120, 402), "YOUR MACHINE", 24, BLUE, True)
        text(d, (1085, 402), "FRESH CLONE", 24, BLUE, True)
        text(d, (120, 479), "It works.", 64, GREEN, True)
        text(d, (1085, 479), "Import error.", 60, RED, True)
        text(d, (120, 592), "$ python check_env.py", 29, MUTED, mono=True)
        text(d, (1085, 592), "ModuleNotFoundError", 30, RED, mono=True)
        text(d, (925, 492), "→", 72, ORANGE)
        wrapped(d, (120, 774), "The goal: a teammate can rebuild the environment from your instructions.", 1650, 32)
    elif scene == 1:
        terminal(d, (80, 355, 1180, 824), [
            ("$ pwd", ORANGE), "/home/you/course-repo", "",
            ("$ git status", ORANGE), "On branch main", "nothing to commit, working tree clean"
        ], size=30, label="ILLUSTRATIVE PROJECT LOCATION")
        text(d, (1260, 390), "CHECK FIRST", 26, BLUE, True)
        wrapped(d, (1260, 463), "Where am I?", 500, 42, bold=True)
        wrapped(d, (1260, 561), "What does Git see?", 500, 38, bold=True)
        wrapped(d, (1260, 673), "Relative paths begin in your current directory.", 480, 29, MUTED)
    elif scene == 2:
        commands = [
            "$ python -m venv .venv", "$ source .venv/bin/activate",
            "$ python -m pip install requests", "$ python -m pip freeze > requirements.txt"
        ]
        visible = 1 if sentence < 2 else 2 if sentence < 4 else 4
        terminal(d, (80, 365, 1390, 735), [(c, ORANGE) for c in commands[:visible]], size=30)
        box(d, (1440, 365, 1840, 735))
        text(d, (1470, 405), "ONE PROJECT", 23, BLUE, True)
        text(d, (1470, 468), ".venv/", 39, GREEN, mono=True)
        wrapped(d, (1470, 548), "A separate interpreter and dependency set.", 335, 27, MUTED)
        text(d, (95, 784), "PowerShell: .venv\\Scripts\\Activate.ps1", 28, MUTED, mono=True)
    elif scene == 3:
        terminal(d, (80, 365, 1050, 805), [
            (".venv/", GREEN), (".env", GREEN), ("data/raw/", GREEN), ("data/processed/", GREEN), "__pycache__/"
        ], label=".gitignore", size=33)
        text(d, (1135, 397), "KEEP LOCAL", 27, BLUE, True)
        wrapped(d, (1135, 466), "Environment folders\nCredentials\nRaw data".replace("\n", " · "), 630, 40, INK, True)
        box(d, (1135, 661, 1840, 805), "#302424", "#643D38")
        wrapped(d, (1163, 687), "Ignore rules do not remove files already committed.", 645, 30, RED)
    elif scene == 4:
        labels = ["WORKING TREE", "STAGE", "LOCAL HISTORY", "REMOTE"]
        details = ["Files you edit", "Selected snapshot", "Recorded commits", "Shared commits"]
        active = min(max(sentence - 1, 0), 3)
        for i, (label, detail) in enumerate(zip(labels, details)):
            x = 80 + i * 455
            box(d, (x, 410, x + 395, 638), "#20332D" if i == active else PANEL, GREEN if i == active else LINE)
            text(d, (x + 24, 440), f"0{i+1}", 24, ORANGE, True)
            text(d, (x + 24, 493), label, 26, INK, True)
            text(d, (x + 24, 555), detail, 24, MUTED)
            if i < 3:
                text(d, (x + 406, 480), "→", 43, ORANGE)
        for x, command in [(100, "edit"), (555, "git add"), (1010, "git commit"), (1465, "git push")]:
            text(d, (x, 684), command, 29, ORANGE, mono=True)
        text(d, (100, 790), "Inspect:  git diff     |     git diff --staged", 30, BLUE, mono=True)
    elif scene == 5:
        box(d, (80, 367, 1090, 818))
        text(d, (120, 400), "feature/env-setup", 34, BLUE, mono=True)
        commits = ["Add the environment check", "Document setup and run", "Explain the decisions"]
        for i, item in enumerate(commits):
            y = 490 + i * 93
            d.ellipse((130, y, 158, y + 28), fill=ORANGE)
            if i < 2:
                d.line((144, y + 28, 144, y + 93), fill=LINE, width=4)
            text(d, (190, y - 2), item, 32)
        text(d, (1180, 390), "REVIEW THE DIFF", 26, BLUE, True)
        wrapped(d, (1180, 462), "Baseline → branch → meaningful commits → pull request → review → merge", 610, 36, INK, True)
        wrapped(d, (1180, 713), "A workflow diagram; no GitHub pull request is implied by this demo.", 610, 23, MUTED)
    elif scene == 6:
        commands = [
            "$ git clone <your-repo-url> fresh-check", "$ cd fresh-check",
            "$ python -m venv .venv", "$ source .venv/bin/activate",
            "$ python -m pip install -r requirements.txt", "$ python src/check_env.py"
        ]
        terminal(d, (80, 350, 1840, 855), [(c, ORANGE) for c in commands] + [
            ("Python: 3.12.14    requests: 2.32.5", MUTED), ("environment OK", GREEN)
        ], size=29, label="COMMAND GUIDE / VERIFIED CHECK OUTPUT FROM A LOCAL FRESH CLONE")
    else:
        items = ["Fresh clone rebuilds successfully", "Pinned dependencies import", "Environment and secrets stay local", "Each commit explains a change"]
        for i, item in enumerate(items):
            yy = 382 + i * 102
            box(d, (80, yy, 1280, yy + 80))
            text(d, (109, yy + 15), "✓", 36, GREEN, True)
            text(d, (175, yy + 19), item, 31)
        box(d, (1340, 382, 1840, 768), "#292A24", "#62523A")
        text(d, (1375, 416), "YOUR NEXT STEP", 24, ORANGE, True)
        wrapped(d, (1375, 487), "Build it. Rebuild it. Explain it.", 420, 40, INK, True)
        wrapped(d, (1375, 672), "Week 1 · Module M00", 420, 25, MUTED)
    return image


PRONUNCIATIONS = {
    "pwd": "P W D", "python -m venv .venv": "python, dash m, v e n v, dot v e n v",
    "source .venv/bin/activate": "source, dot v e n v, slash bin slash activate",
    ".venv/Scripts": "dot v e n v, slash scripts", "python -m pip": "python dash m pip",
    "requirements.txt": "requirements dot t x t", ".gitignore": "dot git ignore",
    "git diff --staged": "git diff, dash dash staged",
}


def speakable(value):
    value = re.sub(r"`([^`]+)`", lambda m: PRONUNCIATIONS.get(m[1], m[1]), value)
    value = value.replace("README", "read me").replace("PR", "pull request")
    return value


def stamp(seconds, ass=False):
    multiplier = 100 if ass else 1000
    value = round(seconds * multiplier)
    hours, value = divmod(value, 3600 * multiplier)
    minutes, value = divmod(value, 60 * multiplier)
    sec, fraction = divmod(value, multiplier)
    return f"{hours}:{minutes:02}:{sec:02}.{fraction:02}" if ass else f"{hours:02}:{minutes:02}:{sec:02},{fraction:03}"


def caption_chunks(value):
    value = value.replace("`", "")
    chunks, current = [], ""
    for word in value.split():
        candidate = (current + " " + word).strip()
        if len(candidate) > 94 and current:
            chunks.append(current)
            current = word
        else:
            current = candidate
    if current:
        chunks.append(current)
    return chunks


def prepare(args):
    import sherpa_onnx
    output, work = args.output, args.work
    output.mkdir(parents=True, exist_ok=True)
    work.mkdir(parents=True, exist_ok=True)
    (work / "speech").mkdir(exist_ok=True)
    (work / "frames").mkdir(exist_ok=True)
    model = args.model_dir
    config = sherpa_onnx.OfflineTtsConfig(model=sherpa_onnx.OfflineTtsModelConfig(
        vits=sherpa_onnx.OfflineTtsVitsModelConfig(model=str(model / "en_US-ljspeech-medium.onnx"),
        tokens=str(model / "tokens.txt"), data_dir=str(model / "espeak-ng-data")), num_threads=2), silence_scale=0.4)
    tts = sherpa_onnx.OfflineTts(config)
    sample_rate = tts.sample_rate
    body = SCRIPT.read_text().split("## Script\n", 1)[1].split("\n## Screen example", 1)[0].strip()
    paragraphs = body.split("\n\n")
    assert len(paragraphs) == 8
    audio_parts, segments, cues = [], [], []
    cursor = 0.0
    for scene, paragraph in enumerate(paragraphs):
        sentences = re.split(r"(?<=[.!?])\s+(?=[A-Z])", paragraph)
        print(f"Narrating section {scene+1}/8: {CHAPTERS[scene]}", flush=True)
        for index, sentence in enumerate(sentences):
            spoken = speakable(sentence)
            cache = work / "speech" / (hashlib.sha256(spoken.encode()).hexdigest()[:20] + ".npy")
            if cache.exists():
                samples = np.load(cache)
            else:
                generated = tts.generate(spoken, speed=0.98)
                assert generated.sample_rate == sample_rate and len(generated.samples) > 0
                samples = np.asarray(generated.samples, dtype=np.float32)
                audible = np.flatnonzero(np.abs(samples) > 0.004)
                assert len(audible)
                samples = samples[max(0, audible[0] - int(.08*sample_rate)):min(len(samples), audible[-1] + int(.17*sample_rate))]
                np.save(cache, samples)
            gap = .65 if index == 0 else .13
            audio_parts.append(np.zeros(round(gap * sample_rate), dtype=np.float32))
            audio_parts.append(samples)
            start = cursor + gap
            end = start + len(samples) / sample_rate
            frame = work / "frames" / f"scene-{scene:02}-{index:02}.png"
            scene_image(scene, index).save(frame)
            segments.append({"scene": scene, "sentence": index, "frame": str(frame), "start": cursor,
                             "speech_start": start, "end": end, "duration": end-cursor,
                             "caption": sentence.replace("`", ""), "spoken": spoken})
            chunks = caption_chunks(sentence)
            weights = [len(c) for c in chunks]
            cue_start = start
            for chunk, weight in zip(chunks, weights):
                cue_end = cue_start + (end-start) * weight / sum(weights)
                cues.append({"start": cue_start, "end": cue_end, "text": chunk})
                cue_start = cue_end
            cursor = end
    audio_parts.append(np.zeros(round(3.2 * sample_rate), dtype=np.float32))
    samples = np.concatenate(audio_parts)
    assert np.isfinite(samples).all()
    peak = float(np.max(np.abs(samples)))
    if peak > .94:
        samples *= .94 / peak
    with wave.open(str(work / "narration.wav"), "wb") as wav:
        wav.setnchannels(1)
        wav.setsampwidth(2)
        wav.setframerate(sample_rate)
        wav.writeframes((np.clip(samples, -1, 1)*32767).astype("<i2").tobytes())
    total = len(samples) / sample_rate
    segments[-1]["duration"] += 3.2
    segments[-1]["end"] += 3.2
    (output / "storyboard.json").write_text(json.dumps({"source_script":str(SCRIPT.relative_to(ROOT)),
        "voice":"generic en_US-ljspeech-medium; no voice cloning", "speech_engine":sherpa_onnx.__version__,
        "sample_rate":sample_rate, "duration_seconds":total, "sections":CHAPTERS, "segments":segments,
        "captions":cues}, indent=2))
    srt, ass_lines = [], []
    for i, cue in enumerate(cues, 1):
        lines = textwrap.wrap(cue["text"], width=57, break_long_words=False)
        assert len(lines) <= 2, lines
        srt.append(f"{i}\n{stamp(cue['start'])} --> {stamp(cue['end'])}\n" + "\n".join(lines) + "\n")
        escaped = r"\N".join(lines).replace("{", "(").replace("}", ")")
        ass_lines.append(f"Dialogue: 0,{stamp(cue['start'],True)},{stamp(cue['end'],True)},Default,,0,0,0,,{escaped}")
    (output / "week-01-captions.srt").write_text("\n".join(srt))
    header = """[Script Info]
ScriptType: v4.00+
PlayResX: 1920
PlayResY: 1080
WrapStyle: 2

[V4+ Styles]
Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding
Style: Default,DejaVu Sans,31,&H00F8FAFC,&H000000FF,&H00080F19,&H00080F19,0,0,0,0,100,100,0,0,1,1,0,2,130,130,72,1

[Events]
Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text
"""
    (work / "captions.ass").write_text(header+"\n".join(ass_lines)+"\n")
    concat = []
    for segment in segments:
        concat += [f"file '{segment['frame']}'", f"duration {segment['duration']:.6f}"]
    concat.append(f"file '{segments[-1]['frame']}'")
    (work / "frames.ffconcat").write_text("\n".join(concat)+"\n")
    # Keep a clean standalone poster and an inspectable chapter contact sheet.
    scene_image(0, 0).save(output / "week-01-poster.png")
    contact = Image.new("RGB", (1920, 1080), BG)
    for scene in range(8):
        image = scene_image(scene, 6).resize((480,270),Image.Resampling.LANCZOS)
        contact.paste(image,((scene % 4)*480,(scene // 4)*270))
    contact.crop((0,0,1920,540)).save(work / "contact-sheet.png")
    print(f"Prepared {len(segments)} narration segments, {len(cues)} caption cues, {total:.1f}s", flush=True)


def render(args):
    metadata = json.loads((args.output / "storyboard.json").read_text())
    video = args.output / "week-01-make-your-setup-reproducible.mp4"
    command = ["ffmpeg","-y","-hide_banner","-loglevel","warning","-f","concat","-safe","0",
        "-i",str(args.work/"frames.ffconcat"),"-i",str(args.work/"narration.wav"),
        "-map","0:v:0","-map","1:a:0","-vf",f"fps=24,subtitles={args.work/'captions.ass'}",
        "-af","loudnorm=I=-16:TP=-1.5:LRA=11","-c:v","libx264","-preset","medium","-crf","20",
        "-pix_fmt","yuv420p","-threads","2","-filter_threads","2","-c:a","aac","-b:a","160k",
        "-ar","48000","-ac","2","-t",str(metadata['duration_seconds']),"-movflags","+faststart",
        "-metadata","title=Week 1: Make your setup reproducible",
        "-metadata","comment=Generic synthetic narration; based on the Gambill Data Engineer Track Week 1 script.",str(video)]
    subprocess.run(command,check=True)
    print(f"Rendered {video}",flush=True)


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--model-dir",type=Path,required=True)
    parser.add_argument("--output",type=Path,default=DEFAULT_OUT)
    parser.add_argument("--work",type=Path,default=Path('/tmp/gambill-week01-production/render'))
    parser.add_argument("--prepare-only",action="store_true")
    parser.add_argument("--render-only",action="store_true")
    args=parser.parse_args()
    if not args.render_only:
        prepare(args)
    if not args.prepare_only:
        render(args)


if __name__ == "__main__":
    main()
