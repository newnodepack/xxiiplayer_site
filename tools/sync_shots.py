# -*- coding: utf-8 -*-
"""
앱 마케팅 스크린샷을 사이트용으로 가져옵니다.

    python tools/sync_shots.py [원본폴더]

기본 원본은 아래 SOURCE 입니다. 새 버전을 찍으면 폴더만 바꿔서 다시 실행하십시오.
원본(1080px)을 그대로 쓰면 페이지가 무거워지므로, 화면에 그려지는 크기의 2배로 줄이고
PNG 를 최적화해서 images/shots/ 에 씁니다. 파일명은 원본 그대로 유지합니다.
"""
import io
import os
import sys

from PIL import Image

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SOURCE = r"D:\My Files\xxiiplayer\marketing\screenshots_2.36"
DEST = os.path.join(ROOT, "images", "shots")

# 사이트에서 쓰는 파일만 가져옵니다 (_preview.png 등은 제외).
# 값은 내보낼 최대 가로폭 — 화면 렌더 폭의 약 2배.
WANTED = {
    # 값은 내보낼 최대 가로폭 — 화면 렌더 폭의 약 2배.
    "02_now_playing.png": 560,            # 히어로
    "04b_playlist_detail.png": 560,       # 히어로
    "03_equalizer.png": 720,              # 기능 단독
    "10_studio.png": 760,                 # 기능 단독(대표)
    "13_android_auto_playlist.png": 900,  # 차량 화면(가로)
    "14_android_auto_now_playing.png": 900,
    "01_songs.png": 400,                  # 기능 2장 묶음
    "04a_playlists.png": 400,
    "05_edit_aac.png": 400,
    "06_multi_select.png": 400,
    "08_videos.png": 400,
    "09_video_player.png": 400,
    "11_community.png": 400,
    "12_community_post.png": 400,
}


def main(source=None):
    src = source or SOURCE
    if not os.path.isdir(src):
        sys.exit("원본 폴더를 찾을 수 없습니다: %s" % src)
    if not os.path.isdir(DEST):
        os.makedirs(DEST)

    total_in = total_out = 0
    missing = []
    for name, max_w in sorted(WANTED.items()):
        s = os.path.join(src, name)
        if not os.path.isfile(s):
            missing.append(name)
            continue
        d = os.path.join(DEST, name)
        im = Image.open(s).convert("RGB")
        w, h = im.size
        if w > max_w:
            im = im.resize((max_w, round(h * max_w / w)), Image.LANCZOS)

        # 원본이 이미 팔레트 PNG 인 경우가 많아, 24비트로 다시 저장하면 오히려 커집니다.
        # 트루컬러와 256색 팔레트를 모두 만들어 작은 쪽을 씁니다.
        cand = []
        for label, img in (("rgb", im),
                           ("pal", im.quantize(colors=256, method=Image.MEDIANCUT, dither=Image.FLOYDSTEINBERG))):
            buf = io.BytesIO()
            img.save(buf, "PNG", optimize=True)
            cand.append((buf.tell(), label, buf.getvalue()))
        size, label, data = min(cand)
        with open(d, "wb") as fh:
            fh.write(data)

        a, b = os.path.getsize(s), os.path.getsize(d)
        total_in += a
        total_out += b
        print("  %-32s %4dx%-5d → %4dx%-5d  %6.1f → %5.1f KB"
              % (name, w, h, im.size[0], im.size[1], a / 1024, b / 1024), "[%s]" % label)

    print("\n  합계 %.1f MB → %.1f MB" % (total_in / 1048576, total_out / 1048576))
    if missing:
        print("  원본에 없음: %s" % ", ".join(missing))
    print("\n이어서 `python tools/build_pages.py` 를 실행하십시오.")


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else None)
