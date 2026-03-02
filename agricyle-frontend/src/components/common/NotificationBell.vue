<template>
  <button class="relative p-2 rounded-xl2 hover:bg-agri-beige transition">
    🔔
    <span
      v-if="count > 0"
      class="absolute -top-1 -right-1 bg-agri-green text-white text-[10px] px-2 py-[2px] rounded-full"
    >
      {{ count }}
    </span>
  </button>
</template>

<script setup>
import { ref } from "vue";

// plus tard tu peux brancher sur API notifications
const count = ref(0);
</script>
