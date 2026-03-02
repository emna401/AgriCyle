<template>
  <div class="grid md:grid-cols-2 gap-4 items-stretch">
    <Card title="🌍 Langue / Language" subtitle="Choisis la langue de l'application">
      <div class="space-y-3">
        <Button class="w-full" @click="setLang('fr')">Français 🇫🇷</Button>
        <Button class="w-full" variant="outline" @click="setLang('ar')">العربية 🇹🇳</Button>
      </div>

      <div class="mt-4 text-sm text-gray-600">
        Tu peux changer la langue plus tard dans la barre du haut.
      </div>
    </Card>

    <div class="agri-card p-6 flex flex-col justify-between bg-gradient-to-br from-agri-beige to-white">
      <div>
        <h2 class="text-2xl font-bold text-agri-text">AgriCycle 🌿</h2>
        <p class="text-gray-600 mt-2">
          Collecte des emballages agricoles → recyclage → produits utiles.
        </p>
      </div>

      <div class="mt-6 text-sm text-gray-600">
        Couleurs apaisantes • Navigation simple • Mobile-friendly
      </div>
    </div>
  </div>
</template>

<script setup>
import Card from "../../components/ui/Card.vue";
import Button from "../../components/ui/Button.vue";
import { useI18n } from "vue-i18n";
import { useRouter } from "vue-router";

const { locale } = useI18n();
const router = useRouter();

function setLang(v) {
  locale.value = v;
  localStorage.setItem("lang", v);
  document.documentElement.dir = v === "ar" ? "rtl" : "ltr";
  router.push("/");
}
</script>
