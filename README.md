# XXII player — 사이트

GitHub Pages 정적 사이트. 디자인은 **Nocturne** 시스템(다크 그라운드 `#161826`, 브랜드 레드 `#E10600`
액센트를 선과 광채로만 사용)을 따릅니다.

## 구조

```
index.html          한국어 (기본)     ← 생성물
en/ fr/ es/ ar/     나머지 4개 언어    ← 생성물  (ar 은 RTL)
privacy-policy.html      개인정보 처리방침 (ko+en)   ← 직접 편집
account-deletion.html    계정 및 데이터 삭제 (ko+en) ← 직접 편집
privacy_ilbonvpn.html    다른 앱(ilbonvpn) 문서      ← 무관
css/nocturne.css    디자인 토큰 + 공통 컴포넌트
css/landing.css     랜딩 전용 컴포넌트
images/shots/       앱 스크린샷 (README 참조)
tools/content.py    모든 문구 — 5개 언어
tools/build_pages.py 페이지 생성기
sitemap.xml robots.txt site.webmanifest  ← sitemap 은 생성물
```

## 랜딩 페이지 수정하기

`index.html` 과 `en/ fr/ es/ ar/index.html` 은 **생성물입니다.** 직접 고치면 다음 빌드에서 덮어쓰입니다.
문구는 `tools/content.py`, 구조·마크업은 `tools/build_pages.py` 에서 고친 뒤 다시 생성하십시오.

```bash
python tools/build_pages.py
```

언어를 추가하려면 `tools/content.py` 의 `LANG_ORDER` · `LANG_PATHS` · `LANGS` 에 항목을 더하면
hreflang, 사이트맵, 언어 전환 링크가 자동으로 따라옵니다.

## 스크린샷

`images/shots/` 에 파일을 넣으면 5개 언어 페이지에 모두 반영됩니다. 파일명과 쓰임새는
`images/shots/README.md` 를 보십시오. 없는 동안에는 조용한 자리 표시가 대신 나옵니다.

## 로컬에서 보기

```bash
python -m http.server 4173
```
