# 合球總會設計師錯誤紀錄（反饋迴路）

跟 `/home/box/wiki/Quality/feedback-loop.md`（2026-10-05 起）。每行：`YYYY-MM-DD | 代碼 | 一句描述 | 已改？ | 防再發`

## 每次設計交付嘅核對標準
1. 色碼寫喺規格檔，對比度用公式計過，正文／細字達 WCAG AA（≥4.5），圖形／大字達 3。
2. 預覽圖用本機 Chrome 截圖，路徑一定 `file://`；交群組前自己 Read 過圖，冇裁切、冇走位。
3. 跟已有決定（`decisions-log.md`、現行 `style-green-spec.md`）；改色／改 logo 前先問 Steven 或等 Manager 分派。
4. 唔捏造總會資料、聯絡、日期；官方 logo 向量重製未批之前唔叫管家換上網站。
5. 用 `Quality/glossary/korfball.md` 標準詞（必讀 §1A、§1C、§2），交貨前對 §4「網站／設計」清單：色碼同規格檔、對比度數字、截圖寬度（1280／390／360）、資料來源、decisions-log。
6. 新檔寫入 `README.md`，決定寫入 `decisions-log.md`，commit 同 push。

| 日期 | 代碼 | 描述 | 已改？ | 防再發 |
|---|---|---|---|---|
| 2026-10-03 | PROC | 官方 logo 向量預覽第一次截圖裁咗底行英文，交群組前有重截，但應喺第一次截完就用 Read 核對 | 已改（同輪重截再交） | 截圖後必 Read，確認完整 |
| 2026-10-03 | MEM | 淺色版初推橙字 #C25700，細字喺淺底對比唔夠，之後先改建議 #AD4C00 | 已改（規格同管家跟進） | 改色必計晒所有淺底對比先交 |
| 2026-10-06 | FMT | 術語表生效後自查：舊 logo v1／v2 說明檔用咗禁用詞「籃框」（應為「合球籃（korf）」） | 已改（README 同 preview.html 文字） | 交設計說明前對照 `Quality/glossary/korfball.md` §1A、§2；舊 PNG 預覽圖只作存檔 |
