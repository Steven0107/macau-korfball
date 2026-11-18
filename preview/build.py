# 示例預覽生成器：總會綠淺色版（顏色跟 design/style-green-spec.md，2026-10-04 Steven 揀；字體同版面跟 design/style-B-spec.md）。所有內容都係示例或者待提供，唔係真資料。
# 主菜單跟 Steven 2026-10-03 指定：本會簡介、賽事資料、裁判事務、最新消息、下載區、聯繫我們（首頁由標誌入）。
import os, shutil
PAGES = ["about","competitions","referees","news","downloads","contact"]
REFEREES = ["LENG HOU KONG","陳潁鍶","黃龍昇","吳芷澄","馮錫文","李因珊","李文锦","歐子楊","陳紜峰","許錦明","張安莉","梁梓鋒","戚耀基","吳亦豐","王明興","楊鍵深","楊艷萍","孙洪","黃思瀚","凌嘉禧"]
NAV = {
 "zh": {"index":"首頁","about":"本會簡介","competitions":"賽事資料","referees":"裁判事務","news":"最新消息","downloads":"下載區","contact":"聯繫我們"},
 "en": {"index":"Home","about":"About Us","competitions":"Competitions","referees":"Referees","news":"News","downloads":"Downloads","contact":"Contact Us"},
}
TBD = {"zh":"待公布","en":"To be announced"}
ORG = {"zh":"澳門合球總會","en":"Macau China Korfball Association"}  # Steven 2026-10-03 確認
DEMO = {"zh":"示例預覽：所有內容都係示例，未經確認，唔係真資料。","en":"Preview only: all content is example data, not confirmed."}

def cards(lang, rows, title=None):
    z = lang=="zh"; t = TBD[lang]
    h = f'<div class="card col"><b>{title}</b>' if title else ""
    if title:
        return h + "".join(f'<span>{(a if z else b)}{"：" if z else ": "}{t}</span>' for a,b in rows) + "</div>"
    return "".join(f'<div class="card col"><b>{a if z else b}</b><span>{t}</span></div>' for a,b in rows)

def sec(lang, p, inner, note=""):
    return f'<section class="wrap sec"><h2>{NAV[lang][p]}</h2>{f"<p class=note>{note}</p>" if note else ""}{inner}</section>'

def item(title, date, tag):
    return f'<div class="card"><div><b>{title}</b><span>{date}</span></div><span class="tag">{tag}</span></div>'

def body(lang, p):
    z = lang=="zh"
    if p=="index":
        links = "".join(f'<a href="{key}.html">{NAV[lang][key]}<span aria-hidden="true">↗</span></a>' for key in ("about","referees","downloads"))
        return f'''<section class="feature"><div class="feature-copy"><h1>{ORG[lang]}</h1>
<p>{ORG["en"] if z else ORG["zh"]}</p><a class="btn" href="competitions.html">{NAV[lang]["competitions"]} →</a></div>
<img src="../assets/court.webp" alt="" width="1000" height="720"></section>
<div class="wrap shortcuts">{links}</div>
<section class="wrap sec"><h2>{NAV[lang]["news"]}</h2>
{item("示例比賽" if z else "Example match","日期待定" if z else "Date TBC","賽事" if z else "Match")}
{item("示例裁判課程" if z else "Example referee course","日期待定" if z else "Date TBC","裁判" if z else "Referees")}
{item("示例教練課程" if z else "Example coach course","日期待定" if z else "Date TBC","教練" if z else "Coaches")}
{item("示例活動" if z else "Example event","日期待定" if z else "Date TBC","活動" if z else "Event")}
<a class="more" href="news.html">{"睇全部消息 ›" if z else "All news ›"}</a></section>'''
    if p=="about":
        return sec(lang,p,cards(lang,[("簡介","Introduction"),("成立年份","Founded"),("宗旨","Mission"),("理事會","Board")]))
    if p=="competitions":
        h = ["日期","時間","地點","對賽","組別","賽果"] if z else ["Date","Time","Venue","Match","Division","Result"]
        ex = ["示例","—","示例場地","A隊 對 B隊","示例組","—"] if z else ["Example","—","Example venue","Team A vs Team B","Example","—"]
        tbl = '<h3>'+("比賽時間表及賽果" if z else "Fixtures & results")+'</h3><div class="tbl"><table><tr>' + "".join(f"<th>{x}</th>" for x in h) + "</tr>" + ("<tr>"+"".join(f"<td>{x}</td>" for x in ex)+"</tr>")*3 + '</table></div>'
        more = '<h3>'+("其他" if z else "More")+'</h3>' + cards(lang,[("賽事章程","Competition rules"),("參賽隊伍","Teams"),("往屆成績","Past results")])
        return sec(lang,p,tbl+more)
    if p=="referees":
        return sec(lang,p,
          '<h3>'+("裁判證書課程" if z else "Referee certification courses")+'</h3>'
          + cards(lang,[("日期","Dates"),("資格要求","Requirements"),("費用","Fee"),("報名方法","How to apply")],"示例裁判課程" if z else "Example referee course")
          + '<h3>'+("教練證書課程" if z else "Coach certification courses")+'</h3>'  # Steven 2026-10-03：教練課程要保留，暫放裁判事務
          + cards(lang,[("日期","Dates"),("資格要求","Requirements"),("費用","Fee"),("報名方法","How to apply")],"示例教練課程" if z else "Example coach course")
          + '<h3>'+("裁判名單" if z else "Referee roster")+'</h3>'
          + '<div class="card col"><b>'+("IKF 一級" if z else "IKF Level 1")+'</b>'
          + '<ul style="padding-inline-start:1.5em">'
          + ''.join(f'<li>{name}</li>' for name in REFEREES)
          + '</ul></div>')
    if p=="news":
        photos = '<p class="note">'+("活動照片將於公布後上載。" if z else "Activity photos will appear here when available.")+'</p>'
        return sec(lang,p,
          item("示例比賽消息" if z else "Example match news","日期待定" if z else "Date TBC","賽事" if z else "Match")
          + item("示例活動" if z else "Example event","日期待定" if z else "Date TBC","活動" if z else "Event")
          + '<h3>'+("活動相片" if z else "Photo gallery")+'</h3>' + photos,
          "有小朋友嘅相片要先確認同意先上載；所有相片上載前會刪走位置等 EXIF 資料。" if z else "Photos of minors are only published with consent; location and device data are removed before upload.")
    if p=="downloads":
        rows = [("示例報名表格","Example entry form","PDF"),("示例賽事章程","Example competition rules","PDF"),("示例裁判課程簡章","Example referee course brochure","PDF")]
        return sec(lang,p,"".join(item(a if z else b, TBD[lang], c) for a,b,c in rows))
    if p=="contact":
        return sec(lang,p,cards(lang,[("電郵","Email"),("電話","Phone"),("地址","Address"),("社交媒體","Social media"),("對外聯絡人","Contact person")]),
          "歡迎各地總會聯絡我哋，商討友誼賽、交流同合作。（示例文字）" if z else "We welcome associations worldwide to contact us about friendlies, exchanges and cooperation. (Example text)")

def page(lang, p):
    other = "en" if lang=="zh" else "zh"
    nav = "".join(f'<a href="{q}.html" class="{('cta ' if q=='contact' else '')+('on' if q==p else '')}">{NAV[lang][q]}</a>' for q in PAGES)
    return f'''<!doctype html><html lang="{"zh-Hant" if lang=="zh" else "en"}" class="{lang}"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1"><title>{NAV[lang][p]} | {ORG[lang]}</title>
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Noto+Sans+TC:wght@400;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="../assets/style.css"></head><body>
<div class="demo">{DEMO[lang]}</div>
<header><div class="wrap bar"><a class="brand" href="index.html" aria-label="{NAV[lang]["index"]}"><img src="../assets/logo.jpg" alt="{ORG[lang]}"><span><b>{ORG["zh"]}</b><small>{ORG["en"]}</small></span></a>
<input type="checkbox" id="menu" class="menu-toggle"><label for="menu" class="menu-btn" aria-label="Menu"><span></span>{"選單" if lang=="zh" else "Menu"}</label>
<nav>{nav}</nav><a class="lang" href="../{other}/{p}.html">{"EN" if lang=="zh" else "中文"}</a></div></header>
<main>{body(lang,p)}</main>
<footer><div class="wrap"><b>© {ORG[lang]}</b><a href="contact.html">{NAV[lang]["contact"]} ↗</a></div></footer></body></html>'''

CSS = '''*{box-sizing:border-box;margin:0;padding:0}
/* 總會綠淺色版（Steven 2026-10-04 揀方案二，跟 design/style-green-spec.md）。綠底一律白字（--on-accent）。--navy 而家係深綠 #0A4314。 */
:root{--bg:#F5F8F5;--surface:#FFFFFF;--hero:#EAF3EA;--hero-2:#E1EDE2;--navy:#0A4314;--line:#D8E3DA;--photo:#CFDDD2;--accent:#0B6A12;--accent-text:#0B6A12;--on-accent:#FFFFFF;--text:#18261C;--text-2:#4B5B50;--sample:#FFD54A}
body{background:var(--bg);color:var(--text);font-family:"Noto Sans TC","Noto Sans CJK TC",sans-serif;font-weight:400;font-size:16px;line-height:1.6}
a{color:inherit;text-decoration:none}
.wrap{max-width:1040px;margin:0 auto;padding:0 20px}
.demo{background:var(--sample);color:#222;text-align:center;font-size:13px;font-weight:700;padding:6px}
header{background:var(--surface);border-bottom:3px solid var(--accent);position:sticky;top:0;z-index:5;box-shadow:0 1px 4px rgba(10,67,20,.08)}
.bar{display:flex;align-items:center;gap:16px;min-height:64px;flex-wrap:wrap}
/* 官方標誌（Steven 2026-10-03 提供，design/logo/official/）+ 中英文字名 */
.brand{display:flex;align-items:center;gap:10px;min-height:44px;line-height:1.2;color:var(--navy)}
.brand img{height:48px;width:auto;border-radius:6px;display:block}
.brand span{display:flex;flex-direction:column}
.brand b{font-size:17px;font-weight:700}.brand small{font-size:11px;color:var(--text-2)}
nav{display:flex;gap:20px;flex:1;font-size:15px;align-items:center}
nav a{color:var(--text-2);padding:10px 0;white-space:nowrap;border-bottom:2px solid transparent}
nav a.on,nav a:hover{color:var(--accent-text);border-bottom-color:var(--accent)}
nav a.cta{color:var(--accent-text);border:1.5px solid var(--accent-text);border-radius:6px;padding:7px 14px;line-height:1.3;font-weight:700}
nav a.cta:hover,nav a.cta.on{background:var(--accent);border-color:var(--accent);color:var(--on-accent)}
.lang{background:var(--navy);color:#fff;font-weight:700;padding:0 14px;min-height:44px;display:flex;align-items:center;border-radius:22px;font-size:13px;margin-left:auto}
.menu-toggle{display:none}.menu-btn{display:none}
.hero{background:repeating-linear-gradient(-55deg,var(--hero) 0 22px,var(--hero-2) 22px 44px);padding:72px 0;border-bottom:1px solid var(--line)}
.hero h1{font-size:56px;font-weight:700;line-height:1.15;color:var(--text)}
.en .hero h1{text-transform:uppercase}
.hero h1 em{color:var(--accent-text);font-style:normal}
.lead{font-size:20px;font-weight:700;margin-top:10px}.sub{color:var(--text-2);margin:6px 0 24px}
.btn{display:inline-block;background:var(--accent);color:var(--on-accent);font-weight:700;padding:12px 22px;border-radius:6px}
.en .btn{text-transform:uppercase}
.sec{padding:40px 20px}
.sec h2{color:var(--accent-text);font-size:26px;margin-bottom:16px}
.en .sec h2{text-transform:uppercase;letter-spacing:1px}
.sec h3{font-size:18px;margin:24px 0 12px}
.card{background:var(--surface);border:1px solid var(--line);border-left:4px solid var(--accent);border-radius:6px;padding:16px;margin-bottom:12px;display:flex;justify-content:space-between;align-items:center;gap:12px}
.card.col{flex-direction:column;align-items:flex-start;gap:4px}
.card b{font-size:16px}.card span{display:block;color:var(--text-2);font-size:14px}
.card span.tag{background:var(--navy);color:#fff;font-size:12px;font-weight:700;padding:3px 10px;border-radius:10px}
.more{display:inline-block;color:var(--accent-text);font-weight:700;padding:10px 0}
.note{color:var(--text-2);margin-bottom:16px}
.photos{display:grid;grid-template-columns:repeat(3,1fr);gap:8px}
.photos div{background:var(--photo);border-radius:4px;aspect-ratio:4/3}
.tbl{overflow-x:auto}table{width:100%;border-collapse:collapse;min-width:560px;background:var(--surface)}
th{background:var(--navy);color:#fff;text-align:left;padding:10px}td{padding:10px;border-top:1px solid var(--line)}
footer{background:var(--navy);color:#C9DCCB;padding:24px 0;font-size:13px;margin-top:24px}
@media(max-width:760px){
 .menu-btn{display:flex;align-items:center;gap:8px;min-height:44px;padding:0 14px;border:1px solid var(--line);border-radius:22px;font-size:14px;cursor:pointer;margin-left:auto}
 .menu-btn span,.menu-btn span::before,.menu-btn span::after{display:block;width:16px;height:2px;background:var(--text);position:relative}
 .menu-btn span::before,.menu-btn span::after{content:"";position:absolute}.menu-btn span::before{top:-5px}.menu-btn span::after{top:5px}
 .lang{margin-left:0}
 .bar{gap:10px}.brand{gap:8px}.brand img{height:38px}.brand b{font-size:15px}.brand small{display:none}
 nav{display:none;order:3;flex:0 0 100%;flex-direction:column;gap:0;padding-bottom:8px}
 nav a{padding:12px 4px;border-bottom:1px solid var(--line);font-size:16px}
 nav a.on{border-bottom-color:var(--accent)}
 nav a.cta{border:0;border-bottom:1px solid var(--line);border-radius:0;padding:12px 4px;background:none}
 .menu-toggle:checked~nav{display:flex}
 .hero{padding:48px 0}.hero h1{font-size:32px}.sec h2{font-size:22px}
 .photos{grid-template-columns:repeat(2,1fr)}
}
@media(max-width:379px){.brand span{display:none}}
'''
shutil.rmtree("site",ignore_errors=True)
os.makedirs("site/assets",exist_ok=True)
shutil.copy("court.webp","site/assets/court.webp")
open("site/assets/style.css","w").write(CSS + open("theme.css").read())
shutil.copy("../design/logo/official/mcka-logo-official.jpg","site/assets/logo.jpg")
for lang in ("zh","en"):
    os.makedirs(f"site/{lang}",exist_ok=True)
    for p in ["index"]+PAGES:
        open(f"site/{lang}/{p}.html","w").write(page(lang,p))
open("site/index.html","w").write('<!doctype html><meta charset="utf-8"><meta http-equiv="refresh" content="0; url=zh/index.html"><a href="zh/index.html">中文</a> | <a href="en/index.html">English</a>')
print("built")
