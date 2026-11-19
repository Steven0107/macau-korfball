// GUI Foundry Command Palette, adapted to filter the existing bilingual roster.
const search = document.querySelector(".roster-search");
const input = search.querySelector("input");
const count = search.querySelector("output");
const names = Array.from(document.querySelectorAll("#roster li"));
const chinese = document.documentElement.lang.startsWith("zh");

function filterRoster() {
  const query = input.value.trim().normalize("NFKC").toLowerCase();
  let visible = 0;
  for (const name of names) {
    name.hidden = !name.textContent.normalize("NFKC").toLowerCase().includes(query);
    if (!name.hidden) visible++;
  }
  count.textContent = chinese ? `顯示 ${visible} / ${names.length} 位裁判` : `${visible} of ${names.length} referees`;
}
input.addEventListener("input", filterRoster);
search.hidden = false;
filterRoster();
