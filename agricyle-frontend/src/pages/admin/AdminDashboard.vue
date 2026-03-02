<template>
  <div class="relative min-h-screen" :dir="lang">
    <!-- Image d'arrière-plan fixe -->
    <div 
      class="fixed inset-0 bg-cover bg-center bg-no-repeat"
      style="background-image: url('https://images.unsplash.com/photo-1542601906990-b4d3fb778b09?ixlib=rb-4.0.3&auto=format&fit=crop&w=2000&q=80')"
    >
      <!-- Overlay sombre pour améliorer la lisibilité -->
      <div class="absolute inset-0 bg-black/40"></div>
    </div>
    
    <!-- Contenu par-dessus l'image -->
    <div class="relative z-10">
      <aside :class="sidebarClasses">
        <div class="agri-card p-4 mb-4 bg-white/10 backdrop-blur-lg border border-white/20">
          <div class="flex items-center gap-3">
            <div class="w-12 h-12 rounded-xl2 bg-gradient-to-r from-agri-green/30 to-agri-blue/30 border border-white/20 flex items-center justify-center shadow-lg">
              <span class="text-2xl text-white">🛡️</span>
            </div>
            <div>
              <div class="font-semibold text-white">Administration</div>
              <div v-if="auth.user" class="text-xs text-white/80 mt-1">
                {{ auth.user.username }} • {{ auth.user.role }}
              </div>
            </div>
          </div>
        </div>

        <div class="agri-card p-4 space-y-2 bg-white/10 backdrop-blur-lg border border-white/20">
          <div class="text-xs font-semibold text-white/60 px-2 mb-2">MENU PRINCIPAL</div>
          
          <router-link class="nav-item" to="/app/admin">
            <div class="flex items-center gap-3 p-3 rounded-xl hover:bg-white/10 transition-all duration-300">
              <div class="w-10 h-10 rounded-lg bg-gradient-to-r from-agri-green/30 to-agri-blue/30 border border-white/20 flex items-center justify-center">
                <span class="text-white text-xl">📊</span>
              </div>
              <div>
                <div class="text-white font-medium">Tableau de Bord</div>
                <div class="text-xs text-white/60">Vue d'ensemble</div>
              </div>
            </div>
          </router-link>

          <router-link class="nav-item" to="/app/admin/declarations">
            <div class="flex items-center gap-3 p-3 rounded-xl hover:bg-white/10 transition-all duration-300">
              <div class="w-10 h-10 rounded-lg bg-emerald-500/30 border border-emerald-400/20 flex items-center justify-center">
                <span class="text-emerald-300 text-xl">♻️</span>
              </div>
              <div class="text-white font-medium">Déclarations</div>
            </div>
          </router-link>

          <router-link class="nav-item" to="/app/admin/products">
            <div class="flex items-center gap-3 p-3 rounded-xl hover:bg-white/10 transition-all duration-300">
              <div class="w-10 h-10 rounded-lg bg-sky-500/30 border border-sky-400/20 flex items-center justify-center">
                <span class="text-sky-300 text-xl">📦</span>
              </div>
              <div class="text-white font-medium">Produits</div>
            </div>
          </router-link>

          <router-link class="nav-item" to="/app/admin/orders">
            <div class="flex items-center gap-3 p-3 rounded-xl hover:bg-white/10 transition-all duration-300">
              <div class="w-10 h-10 rounded-lg bg-amber-500/30 border border-amber-400/20 flex items-center justify-center">
                <span class="text-amber-300 text-xl">🧾</span>
              </div>
              <div class="text-white font-medium">Commandes</div>
            </div>
          </router-link>

          <router-link class="nav-item" to="/app/admin/users">
            <div class="flex items-center gap-3 p-3 rounded-xl hover:bg-white/10 transition-all duration-300">
              <div class="w-10 h-10 rounded-lg bg-indigo-500/30 border border-indigo-400/20 flex items-center justify-center">
                <span class="text-indigo-300 text-xl">👥</span>
              </div>
              <div class="text-white font-medium">Utilisateurs</div>
            </div>
          </router-link>
        </div>
      </aside>
      <!-- ==== FIN DU SIDEBAR ==== -->

      <!-- Main Content - Marges dynamiques selon la langue -->
      <main >
        <!-- Header -->
        <div class="mb-10">
          <div class="flex items-center justify-between mb-6">
            <div class="flex items-center gap-4">
              <div class="p-3 bg-white/20 backdrop-blur-sm rounded-xl border border-white/30">
                <span class="text-2xl text-white">📊</span>
              </div>
              <div>
                <h1 class="text-3xl md:text-4xl font-bold text-white">Tableau de Bord Admin</h1>
                <p class="text-white/90 mt-2">Supervision AgriCycle - Cartographie, statistiques et exports</p>
              </div>
            </div>
            
            <!-- User info -->
            <div class="flex items-center gap-3">
              <div class="px-4 py-2 bg-white/10 backdrop-blur-sm rounded-full border border-white/20">
                <span class="text-sm text-white/80">Connecté: {{ auth.user?.username }} ({{ auth.user?.role }})</span>
              </div>
            </div>
          </div>
        </div>

        <!-- Stats Cards - Première ligne -->
        <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-6 mb-8">
          <!-- Agriculteurs -->
          <div class="agri-card p-6 hover:shadow-2xl transition-all duration-300 bg-white/10 backdrop-blur-lg border border-white/20">
            <div class="flex items-center gap-4 mb-4">
              <div class="p-3 bg-gradient-to-r from-green-500/20 to-green-400/20 rounded-xl">
                <span class="text-green-300 text-2xl">👨‍🌾</span>
              </div>
              <div class="flex-1">
                <div class="text-sm font-medium text-white/80">Agriculteurs</div>
                <div class="text-3xl font-bold text-white">{{ stats.farmers || 0 }}</div>
              </div>
            </div>
            <div class="text-xs text-white/60 mb-2">Comptes FARMER actifs</div>
            <div v-if="stats.total_farmers_dual" class="text-xs text-green-300 font-medium bg-green-500/10 px-2 py-1 rounded">
              + {{ stats.dual_users || 0 }} DUAL = {{ stats.total_farmers_dual }} agriculteurs totaux
            </div>
          </div>

          <!-- Bénéficiaires -->
          <div class="agri-card p-6 hover:shadow-2xl transition-all duration-300 bg-white/10 backdrop-blur-lg border border-white/20">
            <div class="flex items-center gap-4 mb-4">
              <div class="p-3 bg-gradient-to-r from-blue-500/20 to-blue-400/20 rounded-xl">
                <span class="text-blue-300 text-2xl">👥</span>
              </div>
              <div class="flex-1">
                <div class="text-sm font-medium text-white/80">Bénéficiaires</div>
                <div class="text-3xl font-bold text-white">{{ stats.beneficiaries || 0 }}</div>
              </div>
            </div>
            <div class="text-xs text-white/60 mb-2">Comptes BENEFICIARY actifs</div>
            <div v-if="stats.total_beneficiaries_dual" class="text-xs text-blue-300 font-medium bg-blue-500/10 px-2 py-1 rounded">
              + {{ stats.dual_users || 0 }} DUAL = {{ stats.total_beneficiaries_dual }} bénéficiaires totaux
            </div>
          </div>

          <!-- Dual -->
          <div class="agri-card p-6 hover:shadow-2xl transition-all duration-300 bg-white/10 backdrop-blur-lg border border-white/20">
            <div class="flex items-center gap-4 mb-4">
              <div class="p-3 bg-gradient-to-r from-orange-500/20 to-orange-400/20 rounded-xl">
                <span class="text-orange-300 text-2xl">👥👨‍🌾</span>
              </div>
              <div class="flex-1">
                <div class="text-sm font-medium text-white/80">Utilisateurs DUAL</div>
                <div class="text-3xl font-bold text-white">{{ stats.dual_users || 0 }}</div>
              </div>
            </div>
            <div class="text-xs text-white/60">Agriculteurs & Bénéficiaires</div>
          </div>

          <!-- Total Utilisateurs -->
          <div class="agri-card p-6 hover:shadow-2xl transition-all duration-300 bg-white/10 backdrop-blur-lg border border-white/20">
            <div class="flex items-center gap-4 mb-4">
              <div class="p-3 bg-gradient-to-r from-purple-500/20 to-purple-400/20 rounded-xl">
                <span class="text-purple-300 text-2xl">👤</span>
              </div>
              <div class="flex-1">
                <div class="text-sm font-medium text-white/80">Total Utilisateurs</div>
                <div class="text-3xl font-bold text-white">{{ stats.total_users || 0 }}</div>
              </div>
            </div>
            <div class="text-xs text-white/60">Tous comptes actifs</div>
          </div>
        </div>

        <!-- Deuxième ligne de stats -->
        <div class="grid grid-cols-1 sm:grid-cols-3 gap-6 mb-10">
          <!-- Déclarations -->
          <div class="agri-card p-6 hover:shadow-2xl transition-all duration-300 bg-white/10 backdrop-blur-lg border border-white/20">
            <div class="flex items-center gap-4 mb-4">
              <div class="p-3 bg-gradient-to-r from-emerald-500/20 to-emerald-400/20 rounded-xl">
                <span class="text-emerald-300 text-2xl">♻️</span>
              </div>
              <div class="flex-1">
                <div class="text-sm font-medium text-white/80">Déclarations</div>
                <div class="text-3xl font-bold text-white">{{ stats.declarations || 0 }}</div>
              </div>
            </div>
            <div class="text-xs text-white/60">Total des déclarations reçues</div>
          </div>

          <!-- Commandes -->
          <div class="agri-card p-6 hover:shadow-2xl transition-all duration-300 bg-white/10 backdrop-blur-lg border border-white/20">
            <div class="flex items-center gap-4 mb-4">
              <div class="p-3 bg-gradient-to-r from-sky-500/20 to-sky-400/20 rounded-xl">
                <span class="text-sky-300 text-2xl">🧾</span>
              </div>
              <div class="flex-1">
                <div class="text-sm font-medium text-white/80">Commandes</div>
                <div class="text-3xl font-bold text-white">{{ stats.orders || 0 }}</div>
              </div>
            </div>
            <div class="text-xs text-white/60">Hors paniers abandonnés</div>
          </div>

          <!-- Revenu total -->
          <div class="agri-card p-6 hover:shadow-2xl transition-all duration-300 bg-white/10 backdrop-blur-lg border border-white/20">
            <div class="flex items-center gap-4 mb-4">
              <div class="p-3 bg-gradient-to-r from-amber-500/20 to-amber-400/20 rounded-xl">
                <span class="text-amber-300 text-2xl">💰</span>
              </div>
              <div class="flex-1">
                <div class="text-sm font-medium text-white/80">Revenu total</div>
                <div class="text-3xl font-bold text-white">{{ formatCurrency(stats.revenue) }}</div>
              </div>
            </div>
            <div class="text-xs text-white/60">Depuis le lancement</div>
          </div>
        </div>

        <!-- Map & Exports -->
        <div class="grid lg:grid-cols-2 gap-8">
          <!-- Carte des utilisateurs -->
          <div class="agri-card overflow-hidden hover:shadow-2xl transition-all duration-300">
            <div class="px-6 py-5 border-b border-white/20 bg-gradient-to-r from-agri-green/10 to-agri-blue/10">
              <div class="flex items-center justify-between">
                <div class="flex items-center gap-4">
                  <div class="p-2 bg-white/20 border border-white/30 rounded-lg">
                    <span class="text-white text-xl">🗺️</span>
                  </div>
                  <div>
                    <h3 class="text-lg font-semibold text-white">Carte des utilisateurs</h3>
                    <p class="text-sm text-white/80">Localisation en Tunisie</p>
                  </div>
                </div>
                
                <div class="flex items-center gap-3">
                  <div class="flex items-center gap-2">
                    <div class="w-3 h-3 bg-green-400 rounded-full"></div>
                    <span class="text-xs text-white/80">Agriculteur</span>
                  </div>
                  <div class="flex items-center gap-2">
                    <div class="w-3 h-3 bg-blue-400 rounded-full"></div>
                    <span class="text-xs text-white/80">Bénéficiaire</span>
                  </div>
                  <div class="flex items-center gap-2">
                    <div class="w-3 h-3 bg-orange-400 rounded-full"></div>
                    <span class="text-xs text-white/80">Dual</span>
                  </div>
                </div>
              </div>
            </div>
            
            <div class="p-4">
              <div ref="mapRef" class="w-full h-[400px] rounded-lg overflow-hidden border border-white/20 shadow-inner"></div>
              
              <div class="mt-4 px-3 py-2 bg-white/10 rounded-lg backdrop-blur-sm">
                <div class="flex items-center justify-between">
                  <div class="text-sm text-white/80">
                    <span v-if="loading">🔄 Chargement de la carte...</span>
                    <span v-else>📍 Cliquez sur un marqueur pour les détails</span>
                  </div>
                  <div class="text-xs text-white/60 bg-white/10 px-2 py-1 rounded border border-white/20">
                    {{ usersMap.length }} utilisateurs
                  </div>
                </div>
              </div>
            </div>
          </div>

          <!-- Exports -->
          <div class="space-y-6">
            <!-- Exports Statistiques -->
            <div class="agri-card p-6 hover:shadow-2xl transition-all duration-300 bg-white/10 backdrop-blur-lg border border-white/20">
              <div class="flex items-start justify-between mb-4">
                <div>
                  <div class="flex items-center gap-3 mb-2">
                    <div class="p-2 bg-blue-500/20 rounded-lg">
                      <span class="text-blue-300 text-xl">📊</span>
                    </div>
                    <h4 class="font-semibold text-white text-lg">Rapports Statistiques</h4>
                  </div>
                  <p class="text-sm text-white/80">Analyse complète de la plateforme</p>
                </div>
                <span class="px-3 py-1 bg-blue-500/20 text-blue-300 text-xs font-medium rounded-full">Détaillé</span>
              </div>
              
              <div class="space-y-3 mb-6">
                <div class="flex items-center gap-3 text-sm text-white/90 bg-white/10 p-3 rounded-lg">
                  <div class="w-6 h-6 bg-green-500/20 rounded flex items-center justify-center">
                    <span class="text-green-400 text-xs">✓</span>
                  </div>
                  <span>Statistiques par statut et région</span>
                </div>
                <div class="flex items-center gap-3 text-sm text-white/90 bg-white/10 p-3 rounded-lg">
                  <div class="w-6 h-6 bg-green-500/20 rounded flex items-center justify-center">
                    <span class="text-green-400 text-xs">✓</span>
                  </div>
                  <span>Top produits et tendances mensuelles</span>
                </div>
                <div class="flex items-center gap-3 text-sm text-white/90 bg-white/10 p-3 rounded-lg">
                  <div class="w-6 h-6 bg-green-500/20 rounded flex items-center justify-center">
                    <span class="text-green-400 text-xs">✓</span>
                  </div>
                  <span>Analyse détaillée des performances</span>
                </div>
              </div>
              
              <div class="flex gap-3">
                <button
                  @click="downloadStatsXlsx"
                  :disabled="dlStats"
                  :class="['flex-1 px-4 py-3 rounded-lg text-sm font-medium transition-all duration-300 flex items-center justify-center gap-3',
                          dlStats ? 'bg-white/10 text-white/40 cursor-not-allowed' : 'agri-btn-export hover:scale-[1.02]']"
                >
                  <span v-if="dlStats" class="inline-block animate-spin">⟳</span>
                  <span v-else>📊</span>
                  <span>{{ dlStats ? 'Génération...' : 'Excel (.xlsx)' }}</span>
                </button>
                
                <button
                  @click="downloadStatsPdf"
                  :disabled="dlStats"
                  :class="['flex-1 px-4 py-3 rounded-lg text-sm font-medium transition-all duration-300 flex items-center justify-center gap-3',
                          dlStats ? 'bg-white/10 text-white/40 cursor-not-allowed' : 'agri-btn-export-pdf hover:scale-[1.02]']"
                >
                  <span v-if="dlStats" class="inline-block animate-spin">⟳</span>
                  <span v-else>📄</span>
                  <span>{{ dlStats ? 'Génération...' : 'PDF' }}</span>
                </button>
              </div>
            </div>
          </div>
        </div>

        <!-- Message d'erreur -->
        <div v-if="error" class="mt-8">
          <div class="agri-card p-6 bg-gradient-to-r from-red-500/10 to-red-500/5 border border-red-500/20">
            <div class="flex items-center gap-4">
              <div class="p-2 bg-red-500/20 rounded-lg">
                <span class="text-red-300 text-xl">❌</span>
              </div>
              <div class="flex-1">
                <h4 class="font-medium text-red-200">Erreur</h4>
                <p class="text-sm text-red-200/90 mt-1">{{ error }}</p>
              </div>
              <button @click="error = ''" class="text-red-300 hover:text-red-200">
                <span class="text-xl">×</span>
              </button>
            </div>
          </div>
        </div>
      </main>
    </div>
  </div>
</template>

<script setup>
import { onMounted, ref, computed, watch } from "vue";
import { useAuthStore } from "../../store/auth";
import { useI18n } from "vue-i18n";
import L from "leaflet";
import "leaflet/dist/leaflet.css";

import {
  adminGetFarmersMap,
  adminStats,
  adminExportStatsXlsx,
  adminExportStatsPdf,
  adminExportOrdersXlsx,
  adminExportOrdersPdf
} from "../../api/exports";

const auth = useAuthStore();
const { locale } = useI18n();

// Language state - synced with i18n
const lang = computed({
  get: () => locale.value,
  set: (value) => {
    locale.value = value;
    localStorage.setItem('lang', value);
    
    // Apply RTL/LTR to document
    if (value === 'ar') {
      document.documentElement.dir = 'rtl';
      document.documentElement.lang = 'ar';
    } else {
      document.documentElement.dir = 'ltr';
      document.documentElement.lang = 'fr';
    }
  }
});

// CORRECTION CLÉ: Classes du sidebar simplifiées et sans .flat()
const sidebarClasses = computed(() => {
  const baseClasses = [
    'fixed',
    'top-0',
    'h-full',
    'w-72',
    'flex',
    'flex-col',
    'p-4',
    'bg-black/40',
    'backdrop-blur-xl',
    'transition-all',
    'duration-500',
    'ease-in-out',
    'z-40' // Assure que le sidebar est au-dessus du contenu
  ];
  
  if (lang.value === 'ar') {
    return [...baseClasses, 'lg:flex', 'right-0', 'border-l', 'border-white/20'];
  } else {
    return [...baseClasses, 'hidden', 'lg:flex', 'left-0', 'border-r', 'border-white/20'];
  }
});

// CORRECTION CLÉ: Classes du contenu simplifiées
const contentClasses = computed(() => {
  const baseClasses = [
    'transition-all',
    'duration-500',
    'ease-in-out',
    'pt-20',
    'px-4',
    'md:px-6',
    'lg:px-8',
    'pb-10'
  ];
  
  if (lang.value === 'ar') {
    return [...baseClasses, 'lg:mr-72'];
  } else {
    return [...baseClasses, 'lg:ml-72'];
  }
});

const mapRef = ref(null);
let map = null;
let markers = [];

const usersMap = ref([]);
const stats = ref({ 
  farmers: 0, 
  beneficiaries: 0,
  dual_users: 0,
  total_users: 0,
  declarations: 0, 
  orders: 0, 
  revenue: 0,
  products: 0,
  total_farmers_dual: 0,
  total_beneficiaries_dual: 0,
  users_points: []
});

const loading = ref(false);
const dlStats = ref(false);
const dlOrders = ref(false);
const error = ref("");

function formatCurrency(amount) {
  const num = Number(amount || 0);
  return new Intl.NumberFormat(lang.value === 'ar' ? 'ar-TN' : 'fr-TN', {
    style: 'currency',
    currency: 'TND',
    minimumFractionDigits: 2
  }).format(num);
}

async function refreshAll() {
  await loadStats();
  await loadMapData();
}

function initMap() {
  if (!mapRef.value) return;
  
  map = L.map(mapRef.value).setView([34.0, 9.0], 6);
  
  L.tileLayer("https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png", {
    attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a>',
    maxZoom: 19
  }).addTo(map);
  
  L.control.zoom({ position: 'topright' }).addTo(map);
}

function clearMarkers() {
  markers.forEach(marker => marker.remove());
  markers = [];
}

function renderMarkers() {
  clearMarkers();
  
  usersMap.value.forEach(user => {
    if (!user.farm_lat || !user.farm_lng) return;
    
    const lat = Number(user.farm_lat);
    const lng = Number(user.farm_lng);
    
    let iconColor = '#9ca3af';
    let roleText = 'Utilisateur';
    
    if (user.role === 'FARMER') {
      iconColor = '#10b981';
      roleText = 'Agriculteur';
    } else if (user.role === 'BENEFICIARY') {
      iconColor = '#3b82f6';
      roleText = 'Bénéficiaire';
    } else if (user.role === 'DUAL') {
      iconColor = '#f97316';
      roleText = 'Agriculteur & Bénéficiaire (DUAL)';
    }
    
    const customIcon = L.divIcon({
      html: `
        <div style="
          width: 24px;
          height: 24px;
          background-color: ${iconColor};
          border-radius: 50%;
          border: 3px solid white;
          box-shadow: 0 2px 6px rgba(0,0,0,0.3);
          display: flex;
          align-items: center;
          justify-content: center;
          transition: transform 0.2s;
        ">
          <div style="
            width: 8px;
            height: 8px;
            background-color: white;
            border-radius: 50%;
          "></div>
        </div>
      `,
      className: 'custom-marker',
      iconSize: [24, 24],
      iconAnchor: [12, 12]
    });
    
    const marker = L.marker([lat, lng], { icon: customIcon })
      .addTo(map)
      .bindPopup(`
        <div style="min-width: 280px; max-width: 320px; padding: 12px; background: rgba(255, 255, 255, 0.95); border-radius: 12px; box-shadow: 0 10px 25px rgba(0,0,0,0.1);">
          <div style="display: flex; align-items: center; gap: 12px; margin-bottom: 12px; padding-bottom: 12px; border-bottom: 1px solid #e5e7eb;">
            <div style="width: 40px; height: 40px; background-color: ${iconColor}; border-radius: 50%; display: flex; align-items: center; justify-content: center; color: white; font-weight: bold; font-size: 16px;">
              ${user.username.charAt(0).toUpperCase()}
            </div>
            <div>
              <strong style="font-size: 16px; color: #1f2937;">${user.username}</strong><br>
              <small style="color: #6b7280;"><strong>Rôle:</strong> ${roleText}</small>
            </div>
          </div>
          <div style="color: #4b5563; font-size: 13px; line-height: 1.5;">
            <strong>Statut:</strong> ${user.status || 'ACTIVE'}<br>
            ${user.farm_name ? `<strong>Ferme:</strong> ${user.farm_name}<br>` : ''}
            ${user.governorate ? `<strong>Gouvernorat:</strong> ${user.governorate}<br>` : ''}
            ${user.delegation ? `<strong>Délégation:</strong> ${user.delegation}<br>` : ''}
            ${user.farm_address ? `<strong>Adresse:</strong> ${user.farm_address}<br>` : ''}
            ${user.email ? `<strong>Email:</strong> ${user.email}<br>` : ''}
            ${user.phone ? `<strong>Téléphone:</strong> ${user.phone}` : ''}
          </div>
        </div>
      `);
    
    markers.push(marker);
  });
  
  if (markers.length > 0) {
    const group = new L.featureGroup(markers);
    map.fitBounds(group.getBounds().pad(0.1));
  }
}

async function loadStats() {
  try {
    const response = await adminStats();
    
    if (response.data) {
      stats.value = {
        ...response.data,
        avg_order_value: response.data.orders > 0 ? 
          (response.data.revenue || 0) / response.data.orders : 0,
        activity_rate: response.data.total_users > 0 ? 
          ((response.data.active_users || 0) / response.data.total_users * 100) : 0
      };
      
      if (response.data.users_points && response.data.users_points.length > 0) {
        usersMap.value = response.data.users_points;
        renderMarkers();
      }
    }
  } catch (error) {
    console.error("Erreur chargement stats:", error);
    error.value = "Impossible de charger les statistiques";
  }
}

async function loadMapData() {
  loading.value = true;
  try {
    const response = await adminGetFarmersMap();
    usersMap.value = response.data || [];
    renderMarkers();
  } catch (err) {
    console.error('Erreur chargement carte:', err);
    error.value = "Impossible de charger la carte des utilisateurs";
  } finally {
    loading.value = false;
  }
}

async function downloadStatsXlsx() {
  dlStats.value = true;
  error.value = "";
  try {
    const response = await adminExportStatsXlsx();
    downloadBlob(response.data, `stats_agricycle_${new Date().toISOString().split('T')[0]}.xlsx`);
  } catch (err) {
    console.error('Erreur export stats Excel:', err);
    error.value = "Erreur lors de l'export Excel des statistiques";
  } finally {
    dlStats.value = false;
  }
}

async function downloadStatsPdf() {
  dlStats.value = true;
  error.value = "";
  try {
    const response = await adminExportStatsPdf();
    downloadBlob(response.data, `stats_agricycle_${new Date().toISOString().split('T')[0]}.pdf`);
  } catch (err) {
    console.error('Erreur export stats PDF:', err);
    error.value = "Erreur lors de l'export PDF des statistiques";
  } finally {
    dlStats.value = false;
  }
}

async function downloadOrdersXlsx() {
  dlOrders.value = true;
  error.value = "";
  try {
    const response = await adminExportOrdersXlsx();
    downloadBlob(response.data, `commandes_agricycle_${new Date().toISOString().split('T')[0]}.xlsx`);
  } catch (err) {
    console.error('Erreur export commandes Excel:', err);
    error.value = "Erreur lors de l'export Excel des commandes";
  } finally {
    dlOrders.value = false;
  }
}

async function downloadOrdersPdf() {
  dlOrders.value = true;
  error.value = "";
  try {
    const response = await adminExportOrdersPdf();
    downloadBlob(response.data, `commandes_agricycle_${new Date().toISOString().split('T')[0]}.pdf`);
  } catch (err) {
    console.error('Erreur export commandes PDF:', err);
    error.value = "Erreur lors de l'export PDF des commandes";
  } finally {
    dlOrders.value = false;
  }
}

function downloadBlob(blob, filename) {
  const url = window.URL.createObjectURL(blob);
  const link = document.createElement('a');
  link.href = url;
  link.download = filename;
  document.body.appendChild(link);
  link.click();
  document.body.removeChild(link);
  window.URL.revokeObjectURL(url);
}

onMounted(async () => {
  // Initialize language from localStorage
  const savedLang = localStorage.getItem('lang') || 'fr';
  lang.value = savedLang;
  
  // Apply initial direction
  if (savedLang === 'ar') {
    document.documentElement.dir = 'rtl';
    document.documentElement.lang = 'ar';
  }
  
  initMap();
  await loadStats();
  
  if (usersMap.value.length === 0) {
    await loadMapData();
  }
});

// CORRECTION IMPORTANTE: Watcher pour forcer la mise à jour du DOM après changement de langue
watch(lang, (newLang, oldLang) => {
  // Force reflow pour déclencher les transitions CSS
  setTimeout(() => {
    document.body.classList.add('force-reflow');
    setTimeout(() => {
      document.body.classList.remove('force-reflow');
    }, 50);
  }, 10);
});
</script>

<style scoped>
/* Styles généraux */
.min-h-screen {
  min-height: 100vh;
}

.fixed {
  position: fixed;
}

.inset-0 {
  top: 0;
  right: 0;
  bottom: 0;
  left: 0;
}


.agri-card {
  background: rgba(255, 255, 255, 0.1);
  backdrop-filter: blur(10px);
  border: 1px solid rgba(255, 255, 255, 0.2);
  border-radius: 16px;
  transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
}

.agri-card:hover {
  transform: translateY(-8px);
  box-shadow: 0 20px 40px rgba(0, 0, 0, 0.3);
  background: rgba(255, 255, 255, 0.15);
  border-color: rgba(255, 255, 255, 0.3);
}

/* Boutons d'export */
.agri-btn-export {
  background: linear-gradient(135deg, #48bb78 0%, #2f855a 100%);
  color: white;
  font-weight: 600;
  box-shadow: 0 4px 15px rgba(72, 187, 120, 0.3);
  border: none;
}

.agri-btn-export:hover:not(:disabled) {
  box-shadow: 0 8px 25px rgba(72, 187, 120, 0.4);
  transform: translateY(-2px);
}

.agri-btn-export-pdf {
  background: linear-gradient(135deg, #f56565 0%, #c53030 100%);
  color: white;
  font-weight: 600;
  box-shadow: 0 4px 15px rgba(245, 101, 101, 0.3);
  border: none;
}

.agri-btn-export-pdf:hover:not(:disabled) {
  box-shadow: 0 8px 25px rgba(245, 101, 101, 0.4);
  transform: translateY(-2px);
}

/* Navigation items dans sidebar */
.nav-item {
  display: block;
  border-radius: 12px;
  transition: all 0.3s ease;
  text-decoration: none;
}

.nav-item:hover {
  background: rgba(255, 255, 255, 0.15);
  transform: translateX(4px);
  box-shadow: 0 4px 15px rgba(0, 0, 0, 0.1);
}

.router-link-active {
  background: linear-gradient(135deg, rgba(46, 204, 113, 0.3) 0%, rgba(52, 152, 219, 0.3) 100%);
  border: 1px solid rgba(255, 255, 255, 0.3);
  box-shadow: 0 4px 15px rgba(46, 204, 113, 0.2);
}

.router-link-active:hover {
  background: linear-gradient(135deg, rgba(46, 204, 113, 0.4) 0%, rgba(52, 152, 219, 0.4) 100%);
}

/* Effet de texte avec ombre */
.text-white {
  text-shadow: 0 1px 2px rgba(0, 0, 0, 0.3);
}

.font-bold {
  text-shadow: 0 2px 4px rgba(0, 0, 0, 0.4);
}

/* Animation spin */
.animate-spin {
  animation: spin 1s linear infinite;
}

@keyframes spin {
  from { transform: rotate(0deg); }
  to { transform: rotate(360deg); }
}

/* Rounded corners */
.rounded-xl2 {
  border-radius: 14px;
}

/* Responsive - CORRECTION: Suppression des règles qui écrasent les marges */
@media (max-width: 1024px) {
  /* Suppression de la règle aside { display: none !important; } */
  /* Suppression des règles .lg\:ml-72, .lg\:mr-72 qui écrasent les marges */
  
  .grid-cols-2, .grid-cols-3, .grid-cols-4 {
    grid-template-columns: 1fr;
  }
  
  .text-3xl, .text-4xl {
    font-size: 1.75rem;
  }
  
  .agri-card {
    padding: 1.25rem;
  }
}

@media (max-width: 768px) {
  .pt-20 {
    padding-top: 5rem;
  }
  
  .text-2xl {
    font-size: 1.5rem;
  }
  
  .p-6 {
    padding: 1rem;
  }
}

/* Animation d'entrée pour les cartes */
@keyframes fadeInUp {
  from {
    opacity: 0;
    transform: translateY(20px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

.grid > div {
  animation: fadeInUp 0.6s ease-out forwards;
  opacity: 0;
}

.grid > div:nth-child(1) { animation-delay: 0.1s; }
.grid > div:nth-child(2) { animation-delay: 0.2s; }
.grid > div:nth-child(3) { animation-delay: 0.3s; }
.grid > div:nth-child(4) { animation-delay: 0.4s; }
.grid > div:nth-child(5) { animation-delay: 0.5s; }
.grid > div:nth-child(6) { animation-delay: 0.6s; }
.grid > div:nth-child(7) { animation-delay: 0.7s; }

/* RTL Support - Inversion des éléments */
[dir="rtl"] .nav-item:hover {
  transform: translateX(-4px);
}

[dir="rtl"] .flex {
  flex-direction: row-reverse;
}

[dir="rtl"] .gap-3, [dir="rtl"] .gap-4 {
  gap: 1rem;
}

[dir="rtl"] select {
  direction: rtl;
  text-align: center;
}

[dir="rtl"] .text-left {
  text-align: right !important;
}

[dir="rtl"] .text-right {
  text-align: left !important;
}

[dir="rtl"] .ml-4 {
  margin-left: 0 !important;
  margin-right: 1rem !important;
}

[dir="rtl"] .mr-4 {
  margin-right: 0 !important;
  margin-left: 1rem !important;
}

/* Force reflow pour les transitions */
.force-reflow {
  opacity: 0.999;
}
</style>