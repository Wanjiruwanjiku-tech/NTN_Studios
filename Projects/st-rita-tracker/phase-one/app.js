// Helpers
const $ = sel => document.querySelector(sel);
const dateEl = $("#date");
const fields = {
  affirmation: $("#affirmation"),
  priority: $("#priority"),
  health: $("#actions-health"),
  voice: $("#actions-voice"),
  growth: $("#actions-growth"),
  adjustment: $("#adjustment"),
  nourish: $("#nourish"),
  challenge: $("#challenge"),
  release: $("#release"),
  weekNote: $("#weekNote")
};

function todayISO() {
  // Lock to local day (avoids timezone surprises in Nairobi)
  const d = new Date();
  return new Date(d.getFullYear(), d.getMonth(), d.getDate()).toISOString().slice(0,10);
}

function getEnergy() {
  return document.querySelector('input[name="energy"]:checked')?.value || "medium";
}
function setEnergy(v) {
  const el = document.querySelector(`input[name="energy"][value="${v}"]`);
  if (el) el.checked = true;
}

function loadAll() {
  try { return JSON.parse(localStorage.getItem("ds_entries") || "{}"); }
  catch { return {}; }
}
function saveAll(map) {
  localStorage.setItem("ds_entries", JSON.stringify(map));
}

function formToEntry() {
  return {
    date: dateEl.value,
    affirmation: fields.affirmation.value.trim(),
    priority: fields.priority.value.trim(),
    actions: {
      health: fields.health.value.trim(),
      voice: fields.voice.value.trim(),
      growth: fields.growth.value.trim()
    },
    energy: getEnergy(),
    adjustment: fields.adjustment.value.trim(),
    nourish: fields.nourish.value.trim(),
    challenge: fields.challenge.value.trim(),
    release: fields.release.value.trim(),
    weekNote: fields.weekNote.value.trim()
  };
}

function entryToForm(e = {}) {
  fields.affirmation.value = e.affirmation || "";
  fields.priority.value = e.priority || "";
  fields.health.value = e.actions?.health || "";
  fields.voice.value = e.actions?.voice || "";
  fields.growth.value = e.actions?.growth || "";
  setEnergy(e.energy || "medium");
  fields.adjustment.value = e.adjustment || "";
  fields.nourish.value = e.nourish || "";
  fields.challenge.value = e.challenge || "";
  fields.release.value = e.release || "";
  fields.weekNote.value = e.weekNote || "";
}

function loadByDate(date) {
  const map = loadAll();
  entryToForm(map[date] || {});
}

// Buttons
$("#saveBtn").addEventListener("click", () => {
  const entry = formToEntry();
  const map = loadAll();
  map[entry.date] = entry;
  saveAll(map);
  alert("Saved ✅");
});

$("#printBtn").addEventListener("click", () => window.print());

$("#exportBtn").addEventListener("click", () => {
  const data = JSON.stringify(loadAll(), null, 2);
  const blob = new Blob([data], { type: "application/json" });
  const a = document.createElement("a");
  a.href = URL.createObjectURL(blob);
  a.download = "daily-system-entries.json";
  a.click();
});

$("#importFile").addEventListener("change", e => {
  const file = e.target.files[0];
  if (!file) return;
  const reader = new FileReader();
  reader.onload = () => {
    try {
      const json = JSON.parse(reader.result);
      if (typeof json === "object") {
        saveAll(json);
        loadByDate(dateEl.value);
        alert("Imported ✅");
      }
    } catch {
      alert("Invalid JSON");
    }
  };
  reader.readAsText(file);
});

// Init
if (!dateEl.value) dateEl.value = todayISO();
dateEl.addEventListener("change", e => loadByDate(e.target.value));
loadByDate(dateEl.value);

// Optional: tiny autosave on input (deliberate practice: comment this in/out)
// document.addEventListener("input", () => $("#saveBtn").click());
