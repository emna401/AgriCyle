<template>
  <select v-model="lang" class="agri-input text-sm w-24">
    <option value="fr">FR</option>
    <option value="ar">AR</option>
  </select>
</template>

<script setup>
import { computed } from "vue";
import { useI18n } from "vue-i18n";

const { locale } = useI18n();

const lang = computed({
  get: () => locale.value,
  set: (v) => {
    locale.value = v;
    localStorage.setItem("lang", v);

    // RTL support
    if (v === "ar") document.documentElement.dir = "rtl";
    else document.documentElement.dir = "ltr";
  }
});
</script>
