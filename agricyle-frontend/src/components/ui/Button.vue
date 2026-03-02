<template>
  <button
    :type="type"
    :disabled="disabled"
    :class="classes"
  >
    <slot />
  </button>
</template>

<script setup>
import { computed } from "vue";

const props = defineProps({
  type: { type: String, default: "button" },
  variant: { type: String, default: "primary" }, // primary | outline | danger
  size: { type: String, default: "md" }, // sm | md
  disabled: { type: Boolean, default: false }
});

const classes = computed(() => {
  const base =
    "rounded-xl2 font-medium transition px-4 py-2 inline-flex items-center justify-center gap-2";

  const sizes = {
    sm: "text-sm px-3 py-1.5",
    md: "text-sm px-4 py-2"
  };

  const variants = {
    primary: "bg-agri-green text-white hover:bg-agri-green-dark",
    outline: "bg-white border border-black/10 hover:bg-agri-beige text-agri-text",
    danger: "bg-red-500 text-white hover:bg-red-600"
  };

  const disabled = props.disabled ? "opacity-60 cursor-not-allowed" : "";

  return `${base} ${sizes[props.size]} ${variants[props.variant]} ${disabled}`;
});
</script>
