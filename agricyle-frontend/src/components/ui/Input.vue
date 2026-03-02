<template>
  <div class="space-y-1">
    <label v-if="label" class="text-sm font-medium text-gray-700">
      {{ label }}
    </label>

    <input
      :type="type"
      :value="modelValue"
      @input="$emit('update:modelValue', $event.target.value)"
      :placeholder="placeholder"
      :class="[
        'agri-input',
        error ? 'border-red-400 focus:ring-red-200' : ''
      ]"
    />

    <p v-if="error" class="text-xs text-red-600">
      {{ error }}
    </p>
  </div>
</template>

<script setup>
defineProps({
  modelValue: { type: [String, Number], default: "" },
  label: { type: String, default: "" },
  placeholder: { type: String, default: "" },
  type: { type: String, default: "text" },
  error: { type: String, default: "" }
});

defineEmits(["update:modelValue"]);
</script>
