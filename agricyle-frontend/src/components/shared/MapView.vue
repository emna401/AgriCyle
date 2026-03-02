<template>
  <div class="agri-card p-3">
    <div class="flex items-center justify-between mb-2">
      <div>
        <div class="font-semibold text-agri-text">🗺️ Carte</div>
        <div class="text-xs text-gray-500">
          {{ readOnly ? "Lecture seule" : "Clique pour placer le marqueur" }}
        </div>
      </div>

      <button
        v-if="!readOnly && lat && lng"
        class="agri-btn-outline text-sm"
        @click="clearMarker"
      >
        Effacer
      </button>
    </div>

    <div ref="mapRef" class="w-full h-[320px] rounded-xl2 overflow-hidden"></div>

    <div class="mt-2 text-xs text-gray-600">
      📍 Lat: <b>{{ lat || "-" }}</b> | Lng: <b>{{ lng || "-" }}</b>
    </div>
  </div>
</template>

<script setup>
import { onMounted, ref, watch } from "vue";
import L from "leaflet";
import "leaflet/dist/leaflet.css";

const props = defineProps({
  lat: { type: [Number, String], default: null },
  lng: { type: [Number, String], default: null },
  readOnly: { type: Boolean, default: false }
});

const emit = defineEmits(["update:latlng"]);

const mapRef = ref(null);
let map = null;
let marker = null;

function setMarker(lat, lng) {
  const pos = [lat, lng];

  if (!marker) {
    marker = L.marker(pos).addTo(map);
  } else {
    marker.setLatLng(pos);
  }

  map.setView(pos, 13);
}

function clearMarker() {
  if (marker) {
    map.removeLayer(marker);
    marker = null;
  }
  emit("update:latlng", { lat: null, lng: null });
}

onMounted(() => {
  // Default position Tunisia center
  const defaultLat = 34.0;
  const defaultLng = 9.0;

  map = L.map(mapRef.value).setView([defaultLat, defaultLng], 6);

  L.tileLayer("https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png", {
    attribution: "&copy; OpenStreetMap contributors"
  }).addTo(map);

  // initial marker if exists
  if (props.lat && props.lng) {
    setMarker(Number(props.lat), Number(props.lng));
  }

  if (!props.readOnly) {
    map.on("click", (e) => {
      const newLat = Number(e.latlng.lat.toFixed(6));
      const newLng = Number(e.latlng.lng.toFixed(6));

      setMarker(newLat, newLng);
      emit("update:latlng", { lat: newLat, lng: newLng });
    });
  }
});

watch(
  () => [props.lat, props.lng],
  ([newLat, newLng]) => {
    if (!map) return;
    if (newLat && newLng) setMarker(Number(newLat), Number(newLng));
  }
);
</script>
