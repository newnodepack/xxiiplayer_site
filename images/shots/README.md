# 스크린샷

이 폴더의 파일은 `tools/sync_shots.py` 가 앱 마케팅 폴더에서 가져와 웹용으로 줄인 것입니다.
**직접 넣지 말고 스크립트를 쓰십시오** — 원본(1080px, 2.5MB)을 그대로 두면 페이지가 무거워집니다.

```bash
python tools/sync_shots.py "D:\My Files\xxiiplayer\marketing\screenshots_2.37"
python tools/build_pages.py
```

원본 폴더를 생략하면 `sync_shots.py` 의 `SOURCE`(현재 `screenshots_2.36`)를 씁니다.

## 매칭

| 파일 | 쓰이는 곳 |
| --- | --- |
| `02_now_playing.png` | 히어로 — 앞쪽 (기울여 겹침) |
| `04b_playlist_detail.png` | 히어로 — 뒤쪽 |
| `01_songs.png` · `04a_playlists.png` | 기능 ① 라이브러리 |
| `03_equalizer.png` | 기능 ② 소리 |
| `05_edit_aac.png` · `06_multi_select.png` | 기능 ③ 공간 음향 AAC 변환 |
| `13_android_auto_playlist.png` · `14_android_auto_now_playing.png` | 기능 ④ 차 안에서 (가로형) |
| `08_videos.png` · `09_video_player.png` | 기능 ⑤ 내 영상 |
| `10_studio.png` | 기능 ⑥ 레코딩 스튜디오 (대표, 크게) |
| `11_community.png` · `12_community_post.png` | 기능 ⑦ 커뮤니티 |

`07_*` 는 원본에 없고, `_preview.png` 는 사용하지 않습니다.

## 바꾸려면

- **다른 화면으로 교체** — `tools/content.py` 의 `SHOTS`(키 → 파일명)와 각 기능의 `"shots"` 목록,
  히어로는 `HERO_SHOTS` 를 고친 뒤 `build_pages.py` 재실행.
- **해상도 조정** — `tools/sync_shots.py` 의 `WANTED`(파일 → 최대 가로폭). 렌더 폭의 2배가 기준입니다.
- 가로형 캡처는 기능에 `"wide": True` 를 주면 폭 넓은 단에 위아래로 쌓입니다.

페이지는 이미지의 실제 픽셀 크기를 읽어 `width`/`height` 를 넣으므로 로딩 중 레이아웃이 흔들리지
않습니다. 파일이 없으면 같은 비율의 조용한 자리 표시가 대신 나옵니다.
