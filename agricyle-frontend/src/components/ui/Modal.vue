<template>
  <div v-if="open" class="fixed inset-0 z-50 flex items-center justify-center">
    <!-- overlay -->
    <div
      class="absolute inset-0 bg-black/30"
      @click="$emit('close')"
    ></div>

    <!-- content -->
    <div class="relative w-full max-w-lg mx-4 agri-card p-5 shadow-soft">
      <div class="flex items-start justify-between gap-4 mb-3">
        <div>
          <h2 class="text-lg font-semibold text-agri-text">{{ title }}</h2>
          <p v-if="subtitle" class="text-sm text-gray-600">{{ subtitle }}</p>
        </div>

        <button
          class="px-2 py-1 rounded-xl2 hover:bg-agri-beige transition"
          @click="$emit('close')"
        >
          ✖
        </button>
      </div>

      <div>
        <slot />
      </div>
    </div>
  </div>
</template>

<script setup>
defineProps({
  open: { type: Boolean, default: false },
  title: { type: String, default: "" },
  subtitle: { type: String, default: "" }
});

defineEmits(["close"]);
</script>
