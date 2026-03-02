<template>
  <div class="agri-card p-4">
    <div v-if="title" class="mb-3">
      <h3 class="agri-title">{{ title }}</h3>
      <p v-if="subtitle" class="agri-subtitle">{{ subtitle }}</p>
    </div>

    <slot />
  </div>
</template>

<script setup>
defineProps({
  title: { type: String, default: "" },
  subtitle: { type: String, default: "" }
});
</script>
