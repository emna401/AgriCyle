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
    
    <div class="relative z-10">
      <!-- ==== DÉBUT DU SIDEBAR ==== -->
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

      <!-- Contenu principal - avec décalage dynamique pour le sidebar -->
      <div >
        <!-- Header -->
        <div class="mb-8">
          <div class="flex items-center justify-between mb-6">
            <div class="flex items-center gap-4">
              <div class="p-3 bg-white/20 backdrop-blur-sm rounded-xl border border-white/30">
                <span class="text-2xl text-white">♻️</span>
              </div>
              <div>
                <h1 class="text-3xl md:text-4xl font-bold text-white">Gestion des Déclarations</h1>
                <p class="text-white/90 mt-2">Valider / Collecter / Suivi</p>
              </div>
            </div>
            
            <!-- User info -->
            <div class="flex items-center gap-3">
              <div class="px-4 py-2 bg-white/10 backdrop-blur-sm rounded-full border border-white/20">
                <span class="text-sm text-white/80">Déclarations actives</span>
              </div>
            </div>
          </div>
        </div>

        <!-- Carte de filtre -->
        <div class="agri-card p-6 mb-8 hover:shadow-2xl transition-all duration-300 bg-white/10 backdrop-blur-lg border border-white/20">
          <div class="flex flex-col md:flex-row md:items-center gap-4 justify-between">
            <div class="flex items-center gap-3">
              <div class="p-2 bg-emerald-500/20 rounded-lg">
                <span class="text-emerald-300 text-xl">📊</span>
              </div>
              <div>
                <h3 class="font-semibold text-white">Filtrer par statut</h3>
                <p class="text-sm text-white/80 mt-1">Sélectionnez un statut pour affiner les résultats</p>
              </div>
            </div>
            
            <div class="flex-1 max-w-xs">
              <select v-model="filter" class="agri-input-filter w-full bg-white/10 backdrop-blur-sm border border-white/30 text-white">
                <option value="" class="bg-gray-800 text-white">Toutes les déclarations</option>
                <option value="PENDING" class="bg-gray-800 text-white">⏳ PENDING</option>
                <option value="VALIDATED" class="bg-gray-800 text-white">✅ VALIDATED</option>
                <option value="COLLECTED" class="bg-gray-800 text-white">🚚 COLLECTED</option>
                <option value="DRAFT" class="bg-gray-800 text-white">📝 DRAFT</option>
              </select>
            </div>
          </div>
          
          <!-- Stats rapides -->
          <div class="mt-6 pt-6 border-t border-white/20">
            <div class="grid grid-cols-2 md:grid-cols-4 gap-4">
              <div class="text-center p-3 bg-white/5 rounded-lg border border-white/10">
                <div class="text-2xl font-bold text-emerald-300">{{ getCountByStatus('PENDING') }}</div>
                <div class="text-xs text-white/80 mt-1">⏳ En attente</div>
              </div>
              <div class="text-center p-3 bg-white/5 rounded-lg border border-white/10">
                <div class="text-2xl font-bold text-blue-300">{{ getCountByStatus('VALIDATED') }}</div>
                <div class="text-xs text-white/80 mt-1">✅ Validées</div>
              </div>
              <div class="text-center p-3 bg-white/5 rounded-lg border border-white/10">
                <div class="text-2xl font-bold text-purple-300">{{ getCountByStatus('COLLECTED') }}</div>
                <div class="text-xs text-white/80 mt-1">🚚 Collectées</div>
              </div>
              <div class="text-center p-3 bg-white/5 rounded-lg border border-white/10">
                <div class="text-2xl font-bold text-amber-300">{{ getCountByStatus('DRAFT') }}</div>
                <div class="text-xs text-white/80 mt-1">📝 Brouillons</div>
              </div>
            </div>
          </div>
        </div>

        <!-- Loading State -->
        <div v-if="loading" class="agri-card p-8 text-center hover:shadow-2xl transition-all duration-300 bg-white/10 backdrop-blur-lg border border-white/20">
          <div class="inline-block animate-spin text-4xl mb-4">⟳</div>
          <h3 class="text-xl font-semibold text-white mb-2">Chargement des déclarations</h3>
          <p class="text-white/80">Veuillez patienter...</p>
        </div>

        <!-- Error State -->
        <div v-if="error" class="agri-card p-6 bg-gradient-to-r from-red-500/10 to-red-500/5 border border-red-500/20">
          <div class="flex items-center gap-4">
            <div class="p-2 bg-red-500/20 rounded-lg">
              <span class="text-red-300 text-xl">❌</span>
            </div>
            <div class="flex-1">
              <h4 class="font-medium text-red-200">Erreur de chargement</h4>
              <p class="text-sm text-red-200/90 mt-1">{{ error }}</p>
            </div>
            <button @click="load" class="px-4 py-2 bg-red-500/20 hover:bg-red-500/30 text-red-300 rounded-lg transition-colors">
              Réessayer
            </button>
          </div>
        </div>

        <!-- Liste des déclarations -->
        <div v-if="filtered.length && !loading">
          <div class="mb-4 flex items-center justify-between">
            <h3 class="text-lg font-semibold text-white">
              {{ filtered.length }} déclaration{{ filtered.length > 1 ? 's' : '' }}
              <span v-if="filter" class="text-white/60"> • Filtre: {{ getStatusLabel(filter) }}</span>
            </h3>
            <div class="text-sm text-white/60 bg-white/10 px-3 py-1 rounded-full border border-white/20">
              Tri: Plus récent d'abord
            </div>
          </div>

          <div class="space-y-4">
            <div 
              v-for="d in filtered" 
              :key="d.id" 
              class="agri-card p-6 hover:shadow-2xl transition-all duration-300 bg-white/10 backdrop-blur-lg border border-white/20 hover:border-white/40"
            >
              <div class="flex flex-col lg:flex-row gap-6">
                <!-- Informations principales -->
                <div class="flex-1">
                  <div class="flex items-start gap-4 mb-4">
                    <div class="p-3 rounded-xl" :class="getStatusColor(d.status)">
                      <span class="text-2xl">{{ getStatusIcon(d.status) }}</span>
                    </div>
                    
                    <div class="flex-1">
                      <div class="flex flex-wrap items-center gap-2 mb-2">
                        <span class="text-2xl font-bold text-white">#{{ d.id }}</span>
                        <span class="px-3 py-1 rounded-full text-xs font-medium" :class="getStatusBadgeClass(d.status)">
                          {{ getStatusLabel(d.status) }}
                        </span>
                      </div>
                      
                      <div class="space-y-3">
                        <div class="flex items-center gap-3">
                          <div class="flex items-center gap-2">
                            <span class="text-white/60">📦</span>
                            <span class="text-white font-medium">{{ d.packaging_type }}</span>
                          </div>
                          <div class="h-4 w-px bg-white/20"></div>
                          <div class="flex items-center gap-2">
                            <span class="text-white/60">🔢</span>
                            <span class="text-white">Quantité: {{ d.quantity }}</span>
                          </div>
                        </div>
                        
                        <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
                          <div class="p-3 bg-white/5 rounded-lg border border-white/10">
                            <div class="text-xs text-white/60 mb-1">👨‍🌾 Agriculteur</div>
                            <div class="text-white font-medium">{{ d.owner_username || d.owner?.username || d.owner || 'Non spécifié' }}</div>
                          </div>
                          
                          <div class="p-3 bg-white/5 rounded-lg border border-white/10">
                            <div class="text-xs text-white/60 mb-1">📅 Date de collecte</div>
                            <div class="text-white font-medium">{{ d.pickup_date ? formatDate(d.pickup_date) : 'Non planifiée' }}</div>
                          </div>
                        </div>
                        
                        <div class="p-3 bg-white/5 rounded-lg border border-white/10">
                          <div class="text-xs text-white/60 mb-1">📍 Adresse</div>
                          <div class="text-white">{{ d.location_address || "Adresse non spécifiée" }}</div>
                        </div>
                      </div>
                    </div>
                  </div>
                </div>
                
                <!-- Actions -->
                <div class="lg:w-64 space-y-4">
                  <div class="p-4 bg-white/5 rounded-xl border border-white/10">
                    <h4 class="text-sm font-semibold text-white mb-3">Changer le statut</h4>
                    
                    <div class="space-y-2">
                      <button
                        v-for="statusOption in statusOptions"
                        :key="statusOption.value"
                        @click="setStatus(d, statusOption.value)"
                        :class="[
                          'w-full text-left px-3 py-2 rounded-lg text-sm transition-all duration-200 flex items-center gap-2',
                          d.status === statusOption.value 
                            ? 'bg-white/20 text-white border border-white/30' 
                            : 'bg-white/5 text-white/80 hover:bg-white/10 hover:text-white border border-transparent'
                        ]"
                      >
                        <span>{{ statusOption.icon }}</span>
                        <span class="flex-1">{{ statusOption.label }}</span>
                        <span v-if="d.status === statusOption.value" class="text-xs">✓</span>
                      </button>
                    </div>
                  </div>
                  
                  <!-- Sélecteur rapide -->
                  <div>
                    <select 
                      :value="d.status" 
                      @change="setStatus(d, $event.target.value)"
                      class="w-full agri-input-filter bg-white/10 backdrop-blur-sm border border-white/30 text-white"
                    >
                      <option v-for="statusOption in statusOptions" :key="statusOption.value" :value="statusOption.value" class="bg-gray-800 text-white">
                        {{ statusOption.label }}
                      </option>
                    </select>
                    <p class="text-xs text-white/60 mt-2 text-center">Sélectionnez un nouveau statut</p>
                  </div>
                </div>
              </div>
              
              <!-- Informations supplémentaires -->
              <div class="mt-6 pt-6 border-t border-white/20">
                <div class="grid grid-cols-1 md:grid-cols-3 gap-4">
                  <div class="p-3 bg-gradient-to-r from-emerald-500/5 to-emerald-500/10 rounded-lg border border-emerald-500/20">
                    <div class="text-xs text-emerald-300 mb-1">🆔 ID Déclaration</div>
                    <div class="text-white font-mono">{{ d.id }}</div>
                  </div>
                  <div class="p-3 bg-gradient-to-r from-blue-500/5 to-blue-500/10 rounded-lg border border-blue-500/20">
                    <div class="text-xs text-blue-300 mb-1">📝 Type d'emballage</div>
                    <div class="text-white">{{ d.packaging_type || 'Non spécifié' }}</div>
                  </div>
                  <div class="p-3 bg-gradient-to-r from-purple-500/5 to-purple-500/10 rounded-lg border border-purple-500/20">
                    <div class="text-xs text-purple-300 mb-1">⏱️ Dernière mise à jour</div>
                    <div class="text-white">{{ d.updated_at ? formatDate(d.updated_at) : 'Non disponible' }}</div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>

        <!-- Empty State -->
        <div 
          v-else-if="!loading && !error" 
          class="agri-card p-12 text-center hover:shadow-2xl transition-all duration-300 bg-white/10 backdrop-blur-lg border border-white/20"
        >
          <div class="text-6xl mb-6 opacity-50">♻️</div>
          <h3 class="text-2xl font-bold text-white mb-3">Aucune déclaration trouvée</h3>
          <p class="text-white/80 mb-8 max-w-md mx-auto">
            {{ filter ? `Aucune déclaration avec le statut "${getStatusLabel(filter)}"` : 'Aucune déclaration disponible pour le moment' }}
          </p>
          <div class="flex flex-col sm:flex-row gap-3 justify-center">
            <button 
              @click="filter = ''" 
              v-if="filter"
              class="px-6 py-3 bg-white/10 hover:bg-white/20 text-white rounded-lg transition-colors border border-white/20"
            >
              Voir toutes les déclarations
            </button>
            <button 
              @click="load" 
              class="px-6 py-3 agri-btn-export hover:scale-[1.02] transition-all duration-300"
            >
              Actualiser la liste
            </button>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { computed, onMounted, ref, watch } from "vue";
import { useAuthStore } from "../../store/auth";
import { useI18n } from "vue-i18n";
import { adminListDeclarations, adminUpdateDeclarationStatus } from "../../api/exports";

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

// Sidebar classes computed - position changes based on language
const sidebarClasses = computed(() => {
  return [
    'fixed',
    'top-0',
    'h-full',
    'w-72',
    'flex-col',
    'p-4',
    'bg-black/40',
    'backdrop-blur-xl',
    'border-white/20',
    'transition-all',
    'duration-500',
    'ease-in-out',
    lang.value === 'ar' 
      ? ['lg:flex', 'right-0', 'border-l'] 
      : ['hidden', 'lg:flex', 'left-0', 'border-r']
  ].flat();
});

// Content classes computed - margins change based on language
const contentClasses = computed(() => {
  return [
    'transition-all',
    'duration-500',
    'ease-in-out',
    lang.value === 'ar' 
      ? ['lg:mr-72', 'pt-20', 'px-4', 'md:px-6', 'lg:px-8', 'pb-10'] 
      : ['lg:ml-72', 'pt-20', 'px-4', 'md:px-6', 'lg:px-8', 'pb-10']
  ].flat();
});

const items = ref([]);
const loading = ref(false);
const error = ref("");
const filter = ref("");

const statusOptions = [
  { value: "PENDING", label: "⏳ En attente", icon: "⏳" },
  { value: "VALIDATED", label: "✅ Validée", icon: "✅" },
  { value: "COLLECTED", label: "🚚 Collectée", icon: "🚚" },
  { value: "DRAFT", label: "📝 Brouillon", icon: "📝" }
];

const filtered = computed(() => {
  if (!filter.value) return items.value;
  return items.value.filter((x) => x.status === filter.value);
});

function getCountByStatus(status) {
  return items.value.filter(item => item.status === status).length;
}

function getStatusLabel(status) {
  const option = statusOptions.find(opt => opt.value === status);
  return option ? option.label.split(' ').slice(1).join(' ') : status;
}

function getStatusIcon(status) {
  const option = statusOptions.find(opt => opt.value === status);
  return option ? option.icon : '📄';
}

function getStatusColor(status) {
  switch(status) {
    case 'PENDING': return 'bg-amber-500/20 border border-amber-400/20';
    case 'VALIDATED': return 'bg-emerald-500/20 border border-emerald-400/20';
    case 'COLLECTED': return 'bg-purple-500/20 border border-purple-400/20';
    case 'DRAFT': return 'bg-gray-500/20 border border-gray-400/20';
    default: return 'bg-gray-500/20 border border-gray-400/20';
  }
}

function getStatusBadgeClass(status) {
  switch(status) {
    case 'PENDING': return 'bg-amber-500/30 text-amber-300 border border-amber-400/30';
    case 'VALIDATED': return 'bg-emerald-500/30 text-emerald-300 border border-emerald-400/30';
    case 'COLLECTED': return 'bg-purple-500/30 text-purple-300 border border-purple-400/30';
    case 'DRAFT': return 'bg-gray-500/30 text-gray-300 border border-gray-400/30';
    default: return 'bg-gray-500/30 text-gray-300 border border-gray-400/30';
  }
}

function formatDate(dateString) {
  const date = new Date(dateString);
  return date.toLocaleDateString('fr-FR', {
    day: '2-digit',
    month: '2-digit',
    year: 'numeric',
    hour: '2-digit',
    minute: '2-digit'
  });
}

async function load() {
  loading.value = true;
  error.value = "";
  try {
    const res = await adminListDeclarations();
    items.value = (res.data || []).slice().sort((a, b) => (b.id || 0) - (a.id || 0));
  } catch (e) {
    error.value = "Impossible de charger les déclarations. Veuillez réessayer.";
    console.error("Erreur de chargement:", e);
  } finally {
    loading.value = false;
  }
}

async function setStatus(d, status) {
  try {
    await adminUpdateDeclarationStatus(d.id, { status });
    d.status = status;
    
    // Feedback visuel
    const declarationCard = document.querySelector(`[data-declaration-id="${d.id}"]`);
    if (declarationCard) {
      declarationCard.classList.add('status-updated');
      setTimeout(() => {
        declarationCard.classList.remove('status-updated');
      }, 1000);
    }
  } catch (e) {
    alert("Erreur lors de la mise à jour du statut. Veuillez réessayer.");
    console.error("Erreur de mise à jour:", e);
  }
}

onMounted(() => {
  // Initialize language from localStorage
  const savedLang = localStorage.getItem('lang') || 'fr';
  lang.value = savedLang;
  
  // Apply initial direction
  if (savedLang === 'ar') {
    document.documentElement.dir = 'rtl';
    document.documentElement.lang = 'ar';
  }
  
  load();
});
</script>

<style scoped>
/* Styles spécifiques pour cette page */
.agri-input-filter {
  background: rgba(255, 255, 255, 0.1);
  backdrop-filter: blur(10px);
  border: 1px solid rgba(255, 255, 255, 0.3);
  border-radius: 10px;
  padding: 10px 16px;
  color: white;
  font-size: 14px;
  transition: all 0.3s ease;
  outline: none;
}

.agri-input-filter:focus {
  border-color: rgba(255, 255, 255, 0.5);
  box-shadow: 0 0 0 3px rgba(255, 255, 255, 0.1);
}

.agri-input-filter option {
  background: #1f2937;
  color: white;
  padding: 8px;
}

/* Animation pour la mise à jour du statut */
.status-updated {
  animation: statusUpdate 1s ease;
}

@keyframes statusUpdate {
  0% { background: rgba(72, 187, 120, 0.1); }
  50% { background: rgba(72, 187, 120, 0.2); }
  100% { background: rgba(255, 255, 255, 0.1); }
}

/* Bouton d'export */
.agri-btn-export {
  background: linear-gradient(135deg, #48bb78 0%, #2f855a 100%);
  color: white;
  font-weight: 600;
  box-shadow: 0 4px 15px rgba(72, 187, 120, 0.3);
  border: none;
  border-radius: 10px;
  padding: 12px 24px;
  transition: all 0.3s ease;
}

.agri-btn-export:hover:not(:disabled) {
  box-shadow: 0 8px 25px rgba(72, 187, 120, 0.4);
  transform: translateY(-2px);
}

/* Glassmorphism Card */
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

/* Navigation sidebar */
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

/* Animation d'entrée */
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

.agri-card {
  animation: fadeInUp 0.6s ease-out forwards;
  opacity: 0;
}

.agri-card:nth-child(1) { animation-delay: 0.1s; }
.agri-card:nth-child(2) { animation-delay: 0.2s; }
.agri-card:nth-child(3) { animation-delay: 0.3s; }
.agri-card:nth-child(4) { animation-delay: 0.4s; }
.agri-card:nth-child(5) { animation-delay: 0.5s; }

/* Responsive */
@media (max-width: 1024px) {
  aside {
    display: none !important;
  }
  
  .lg\:ml-72, .lg\:mr-72 {
    margin-left: 0 !important;
    margin-right: 0 !important;
  }
}

@media (max-width: 768px) {
  .pt-20 {
    padding-top: 5rem;
  }
  
  .text-3xl, .text-4xl {
    font-size: 1.75rem;
  }
  
  .agri-card {
    padding: 1.25rem;
  }
  
  .grid-cols-2, .grid-cols-3, .grid-cols-4 {
    grid-template-columns: 1fr;
  }
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

/* Effet de texte avec ombre */
.text-white {
  text-shadow: 0 1px 2px rgba(0, 0, 0, 0.3);
}

.font-bold {
  text-shadow: 0 2px 4px rgba(0, 0, 0, 0.4);
}

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

/* Smooth transitions for language switch */
.agri-sidebar {
  will-change: transform, opacity;
}
</style>