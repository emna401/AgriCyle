import { createI18n } from "vue-i18n";
import fr from "./fr.json";
import ar from "./ar.json";

const saved = localStorage.getItem("lang") || "fr";

const i18n = createI18n({
  legacy: true,            // IMPORTANT pour utiliser $t dans template
  globalInjection: true,   // injecte $t partout
  locale: saved,
  fallbackLocale: "fr",
  messages: { fr, ar },
});

export default i18n;
