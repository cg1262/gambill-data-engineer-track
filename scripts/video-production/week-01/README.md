# Week 1 video production

This renderer turns [the Week 1 script](../../lessons/phase-1/week-01-environment-and-git.md) into a 1920×1080 lesson with generic synthetic narration, eight visual sections, staged terminal examples, a Git-state diagram, and English captions.

The [finished video and caption files](../../../videos/week-01-make-your-setup-reproducible/) are separate from the course website. Nothing has been added to the site's pages or video configuration.

## Rebuild

Use Python 3.12, Pillow, numpy, `sherpa-onnx==1.12.40`, and an FFmpeg build with H.264, AAC, and libass support. The renderer currently uses DejaVu fonts from `/usr/share/fonts/truetype/dejavu`.

Download and safely unpack the [LJSpeech-medium model archive](https://github.com/k2-fsa/sherpa-onnx/releases/download/tts-models/vits-piper-en_US-ljspeech-medium.tar.bz2). Preserve TLS verification. The model card identifies its LJ Speech training dataset as public domain. The engine and model must be available on the machine used for regeneration; they are not vendored into this repository.

From the repository root, with those Python dependencies active:

```bash
python scripts/video-production/week-01/render.py \
  --model-dir /path/to/vits-piper-en_US-ljspeech-medium
```

Use `--prepare-only` to generate narration, frames, and timing files before encoding. Use `--render-only` to encode from an already prepared working directory. The default working directory is `/tmp/gambill-week01-production/render`; `--work` and `--output` accept alternative paths. Prepared speech is cached by spoken text so visual changes do not require regenerating narration. The renderer is specific to this lesson's eight-paragraph script and storyboard.

## Production details

- Narration follows the spoken Script section. Inline commands receive speech-friendly pronunciation; captions preserve the written command spelling.
- The voice is a generic US English synthetic voice, with no cloning of Chris's voice or likeness.
- Terminal graphics use illustrative locations and a placeholder clone URL. The displayed Python, requests, and `environment OK` results were verified in an isolated local fresh clone.
- The pull-request sequence is a workflow diagram. No GitHub pull request or review is implied by the demonstration's local Git operations.
- Captions are burned into the MP4 for immediate playback. The separate `.srt` supports reuse when editing or uploading.
- `storyboard.json` stores narration text, timing, and the prepared-frame paths. `production-notes.json` records source/model hashes and the verified demo result. Temporary frame paths are recreated by preparation rather than shipped as permanent dependencies.
