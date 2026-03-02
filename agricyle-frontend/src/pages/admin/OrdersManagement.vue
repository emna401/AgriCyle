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
          <div class="flex items-center gap-3" :class="{ 'flex-row-reverse': isRTL }">
            <div class="w-12 h-12 rounded-xl2 bg-gradient-to-r from-agri-green/30 to-agri-blue/30 border border-white/20 flex items-center justify-center shadow-lg flex-shrink-0">
              <span class="text-2xl text-white">🛡️</span>
            </div>
            <div class="min-w-0 flex-1">
              <div class="font-semibold text-white truncate">{{ isRTL ? 'الإدارة' : 'Administration' }}</div>
              <div v-if="auth.user" class="text-xs text-white/80 mt-1 truncate">
                {{ auth.user.username }} • {{ auth.user.role }}
              </div>
            </div>
          </div>
        </div>

        <div class="agri-card p-4 space-y-2 bg-white/10 backdrop-blur-lg border border-white/20 flex-1 overflow-y-auto">
          <div class="text-xs font-semibold text-white/60 px-2 mb-2">
            {{ isRTL ? 'القائمة الرئيسية' : 'MENU PRINCIPAL' }}
          </div>
          
          <router-link class="nav-item" to="/app/admin">
            <div class="flex items-center gap-3 p-3 rounded-xl hover:bg-white/10 transition-all duration-300" :class="{ 'flex-row-reverse': isRTL }">
              <div class="w-10 h-10 rounded-lg bg-gradient-to-r from-agri-green/30 to-agri-blue/30 border border-white/20 flex items-center justify-center flex-shrink-0">
                <span class="text-white text-xl">📊</span>
              </div>
              <div class="min-w-0 flex-1">
                <div class="text-white font-medium truncate">{{ isRTL ? 'لوحة القيادة' : 'Tableau de Bord' }}</div>
                <div class="text-xs text-white/60 truncate">{{ isRTL ? 'نظرة عامة' : 'Vue d\'ensemble' }}</div>
              </div>
            </div>
          </router-link>

          <router-link class="nav-item" to="/app/admin/declarations">
            <div class="flex items-center gap-3 p-3 rounded-xl hover:bg-white/10 transition-all duration-300" :class="{ 'flex-row-reverse': isRTL }">
              <div class="w-10 h-10 rounded-lg bg-emerald-500/30 border border-emerald-400/20 flex items-center justify-center flex-shrink-0">
                <span class="text-emerald-300 text-xl">♻️</span>
              </div>
              <div class="text-white font-medium truncate">{{ isRTL ? 'التصاريح' : 'Déclarations' }}</div>
            </div>
          </router-link>

          <router-link class="nav-item" to="/app/admin/products">
            <div class="flex items-center gap-3 p-3 rounded-xl hover:bg-white/10 transition-all duration-300" :class="{ 'flex-row-reverse': isRTL }">
              <div class="w-10 h-10 rounded-lg bg-sky-500/30 border border-sky-400/20 flex items-center justify-center flex-shrink-0">
                <span class="text-sky-300 text-xl">📦</span>
              </div>
              <div class="text-white font-medium truncate">{{ isRTL ? 'المنتجات' : 'Produits' }}</div>
            </div>
          </router-link>

          <router-link class="nav-item" to="/app/admin/orders">
            <div class="flex items-center gap-3 p-3 rounded-xl hover:bg-white/10 transition-all duration-300" :class="{ 'flex-row-reverse': isRTL }">
              <div class="w-10 h-10 rounded-lg bg-amber-500/30 border border-amber-400/20 flex items-center justify-center flex-shrink-0">
                <span class="text-amber-300 text-xl">🧾</span>
              </div>
              <div class="text-white font-medium truncate">{{ isRTL ? 'الطلبات' : 'Commandes' }}</div>
            </div>
          </router-link>

          <router-link class="nav-item" to="/app/admin/users">
            <div class="flex items-center gap-3 p-3 rounded-xl hover:bg-white/10 transition-all duration-300" :class="{ 'flex-row-reverse': isRTL }">
              <div class="w-10 h-10 rounded-lg bg-indigo-500/30 border border-indigo-400/20 flex items-center justify-center flex-shrink-0">
                <span class="text-indigo-300 text-xl">👥</span>
              </div>
              <div class="text-white font-medium truncate">{{ isRTL ? 'المستخدمين' : 'Utilisateurs' }}</div>
            </div>
          </router-link>
        </div>
      </aside>
      <!-- ==== FIN DU SIDEBAR ==== -->

      <!-- Contenu principal - avec décalage dynamique pour le sidebar -->
      <div >
        <!-- Header -->
        <div class="mb-8">
          <div class="flex items-center justify-between mb-6 flex-wrap gap-4" :class="{ 'flex-row-reverse': isRTL }">
            <div class="flex items-center gap-4" :class="{ 'flex-row-reverse': isRTL }">
              <div class="p-3 bg-white/20 backdrop-blur-sm rounded-xl border border-white/30 flex-shrink-0">
                <span class="text-2xl text-white">🧾</span>
              </div>
              <div>
                <h1 class="text-3xl md:text-4xl font-bold text-white">
                  {{ isRTL ? 'إدارة الطلبات' : 'Gestion des Commandes' }}
                </h1>
                <p class="text-white/90 mt-2">
                  {{ isRTL ? 'عرض وتحديث حالة الطلبات' : 'Visualiser et mettre à jour le statut des commandes' }}
                </p>
              </div>
            </div>
            
            <!-- User info avec boutons d'export et langue désactivée -->
            <div class="flex items-center gap-3" :class="{ 'flex-row-reverse': isRTL }">
              <!-- Boutons d'export -->
              <button 
                @click="exportXlsx"
                :disabled="dl"
                class="agri-btn-export px-4 py-2 text-sm flex items-center gap-2 disabled:opacity-50 disabled:cursor-not-allowed"
                :class="{ 'flex-row-reverse': isRTL }"
              >
                <span v-if="dl" class="inline-block animate-spin">⟳</span>
                <span v-else>📊</span>
                <span>{{ dl ? (isRTL ? 'جاري...' : 'Export...') : (isRTL ? 'إكسل' : 'Excel') }}</span>
              </button>
              
              <button 
                @click="exportPdf"
                :disabled="dl"
                class="agri-btn-export-pdf px-4 py-2 text-sm flex items-center gap-2 disabled:opacity-50 disabled:cursor-not-allowed"
                :class="{ 'flex-row-reverse': isRTL }"
              >
                <span v-if="dl" class="inline-block animate-spin">⟳</span>
                <span v-else>📄</span>
                <span>{{ dl ? (isRTL ? 'جاري...' : 'Export...') : (isRTL ? 'PDF' : 'PDF') }}</span>
              </button>
              
             
              
              <div class="px-4 py-2 bg-white/10 backdrop-blur-sm rounded-full border border-white/20">
                <span class="text-sm text-white/80">
                  {{ isRTL ? 'متصل:' : 'Connecté:' }} {{ auth.user?.username }} ({{ auth.user?.role }})
                </span>
              </div>
            </div>
          </div>
        </div>

        <!-- Loading State -->
        <div v-if="loading" class="agri-card p-12 text-center hover:shadow-2xl transition-all duration-300 bg-white/10 backdrop-blur-lg border border-white/20">
          <div class="inline-block animate-spin text-4xl mb-4 text-white/80">⟳</div>
          <h3 class="text-xl font-semibold text-white mb-2">{{ isRTL ? 'جاري تحميل الطلبات' : 'Chargement des commandes' }}</h3>
          <p class="text-white/80">{{ isRTL ? 'يرجى الانتظار...' : 'Veuillez patienter...' }}</p>
        </div>

        <!-- Error State -->
        <div v-if="error" class="agri-card p-6 bg-gradient-to-r from-red-500/10 to-red-500/5 border border-red-500/20">
          <div class="flex items-center gap-4" :class="{ 'flex-row-reverse': isRTL }">
            <div class="p-2 bg-red-500/20 rounded-lg flex-shrink-0">
              <span class="text-red-300 text-xl">❌</span>
            </div>
            <div class="flex-1">
              <h4 class="font-medium text-red-200">{{ isRTL ? 'خطأ في التحميل' : 'Erreur de chargement' }}</h4>
              <p class="text-sm text-red-200/90 mt-1">{{ error }}</p>
            </div>
            <button @click="load" class="px-4 py-2 bg-red-500/20 hover:bg-red-500/30 text-red-300 rounded-lg transition-colors">
              {{ isRTL ? 'إعادة المحاولة' : 'Réessayer' }}
            </button>
          </div>
        </div>

        <!-- Statistiques rapides -->
        <div v-if="orders.length && !loading" class="grid grid-cols-2 md:grid-cols-5 gap-4 mb-6">
          <div class="agri-card p-3 text-center bg-white/5 backdrop-blur-sm border border-white/10">
            <div class="text-2xl font-bold text-amber-300">{{ getStatusCount('CART') }}</div>
            <div class="text-xs text-white/80 mt-1">🛒 CART</div>
          </div>
          <div class="agri-card p-3 text-center bg-white/5 backdrop-blur-sm border border-white/10">
            <div class="text-2xl font-bold text-blue-300">{{ getStatusCount('CONFIRMED') }}</div>
            <div class="text-xs text-white/80 mt-1">✅ CONFIRMED</div>
          </div>
          <div class="agri-card p-3 text-center bg-white/5 backdrop-blur-sm border border-white/10">
            <div class="text-2xl font-bold text-purple-300">{{ getStatusCount('PREPARING') }}</div>
            <div class="text-xs text-white/80 mt-1">⚙️ PREPARING</div>
          </div>
          <div class="agri-card p-3 text-center bg-white/5 backdrop-blur-sm border border-white/10">
            <div class="text-2xl font-bold text-green-300">{{ getStatusCount('SHIPPED') }}</div>
            <div class="text-xs text-white/80 mt-1">🚚 SHIPPED</div>
          </div>
          <div class="agri-card p-3 text-center bg-white/5 backdrop-blur-sm border border-white/10">
            <div class="text-2xl font-bold text-red-300">{{ getStatusCount('CANCELLED') }}</div>
            <div class="text-xs text-white/80 mt-1">❌ CANCELLED</div>
          </div>
        </div>

        <!-- Liste des commandes -->
        <div v-if="orders.length && !loading">
          <div class="mb-4 flex items-center justify-between" :class="{ 'flex-row-reverse': isRTL }">
            <h3 class="text-lg font-semibold text-white">
              {{ orders.length }} {{ isRTL ? 'طلب' : 'commande' }}{{ orders.length > 1 ? (isRTL ? '' : 's') : '' }}
            </h3>
            <div class="text-sm text-white/60 bg-white/10 px-3 py-1 rounded-full border border-white/20">
              {{ isRTL ? 'ترتيب: الأحدث أولاً' : 'Tri: Plus récent d\'abord' }}
            </div>
          </div>

          <div class="space-y-4">
            <div 
              v-for="o in orders" 
              :key="o.id" 
              class="agri-card p-6 hover:shadow-2xl transition-all duration-300 bg-white/10 backdrop-blur-lg border border-white/20 hover:border-white/40"
            >
              <div class="flex flex-col lg:flex-row gap-4">
                <!-- Informations commande -->
                <div class="flex-1">
                  <div class="flex items-start gap-4 mb-4">
                    <div class="p-3 rounded-xl" :class="getStatusColor(o.status)">
                      <span class="text-2xl">{{ getStatusIcon(o.status) }}</span>
                    </div>
                    
                    <div class="flex-1">
                      <div class="flex flex-wrap items-center gap-2 mb-2">
                        <span class="text-2xl font-bold text-white">#{{ o.id }}</span>
                        <span class="px-3 py-1 rounded-full text-xs font-medium" :class="getStatusBadgeClass(o.status)">
                          {{ o.status }}
                        </span>
                      </div>
                      
                      <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
                        <div class="p-3 bg-white/5 rounded-lg border border-white/10">
                          <div class="text-xs text-white/60 mb-1">{{ isRTL ? 'المشتري' : 'Acheteur' }}</div>
                          <div class="text-white font-medium">{{ o.buyer_username || o.buyer?.username || o.buyer || 'Non spécifié' }}</div>
                        </div>
                        
                        <div class="p-3 bg-white/5 rounded-lg border border-white/10">
                          <div class="text-xs text-white/60 mb-1">{{ isRTL ? 'تاريخ الطلب' : 'Date commande' }}</div>
                          <div class="text-white font-medium">{{ fmt(o.created_at) }}</div>
                        </div>
                      </div>
                    </div>
                  </div>

                  <!-- Articles commandés -->
                  <div v-if="o.items?.length" class="mt-4">
                    <h4 class="text-sm font-semibold text-white mb-2">{{ isRTL ? 'المنتجات' : 'Articles' }}</h4>
                    <div class="space-y-2">
                      <div 
                        v-for="it in o.items" 
                        :key="it.id" 
                        class="flex items-center justify-between p-3 bg-white/5 rounded-lg border border-white/10"
                        :class="{ 'flex-row-reverse': isRTL }"
                      >
                        <div class="flex items-center gap-3" :class="{ 'flex-row-reverse': isRTL }">
                          <span class="text-white/60 text-lg">📦</span>
                          <span class="text-white font-medium">{{ it.product_name || it.product?.name || "Produit" }}</span>
                          <span class="text-white/60">×{{ it.qty }}</span>
                        </div>
                        <span class="text-white font-semibold">{{ money(Number(it.unit_price) * Number(it.qty)) }}</span>
                      </div>
                    </div>
                  </div>
                </div>
                
                <!-- Actions -->
                <div class="lg:w-64 space-y-4">
                  <div class="p-4 bg-white/5 rounded-xl border border-white/10">
                    <h4 class="text-sm font-semibold text-white mb-3">{{ isRTL ? 'حالة الطلب' : 'Statut commande' }}</h4>
                    
                    <select 
                      :value="o.status" 
                      @change="setStatus(o, $event.target.value)"
                      class="agri-input-filter w-full bg-white/10 backdrop-blur-sm border border-white/30 text-white mb-3"
                    >
                      <option value="CART" class="bg-gray-800 text-white">🛒 CART</option>
                      <option value="CONFIRMED" class="bg-gray-800 text-white">✅ CONFIRMED</option>
                      <option value="PREPARING" class="bg-gray-800 text-white">⚙️ PREPARING</option>
                      <option value="SHIPPED" class="bg-gray-800 text-white">🚚 SHIPPED</option>
                      <option value="CANCELLED" class="bg-gray-800 text-white">❌ CANCELLED</option>
                    </select>
                    
                    <div class="mt-2 text-center">
                      <span class="text-xs text-white/60">
                        {{ isRTL ? 'مجموع الطلب' : 'Total commande' }}: 
                        <span class="text-amber-300 font-bold ml-1">{{ money(o.total_amount) }}</span>
                      </span>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>

        <!-- Empty State -->
        <div 
          v-else-if="!loading && !error && orders.length === 0" 
          class="agri-card p-12 text-center hover:shadow-2xl transition-all duration-300 bg-white/10 backdrop-blur-lg border border-white/20"
        >
          <div class="text-6xl mb-6 opacity-50">🧾</div>
          <h3 class="text-2xl font-bold text-white mb-3">
            {{ isRTL ? 'لا توجد طلبات' : 'Aucune commande trouvée' }}
          </h3>
          <p class="text-white/80 mb-8 max-w-md mx-auto">
            {{ isRTL ? 'Aucune commande disponible pour le moment' : 'Aucune commande disponible pour le moment' }}
          </p>
          <button 
            @click="load" 
            class="px-6 py-3 agri-btn-export hover:scale-[1.02] transition-all duration-300"
          >
            {{ isRTL ? 'تحديث القائمة' : 'Actualiser la liste' }}
          </button>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { computed, onMounted, ref } from "vue";
import { useAuthStore } from "../../store/auth";
import { useI18n } from "vue-i18n";
import {
  adminListOrders,
  adminExportOrdersXlsx,
  adminExportOrdersPdf,
  adminSetOrderStatus
} from "../../api/exports";

const auth = useAuthStore();
const { locale } = useI18n();

// Gestion de la langue - désactivée
const lang = ref('fr');
const isRTL = computed(() => lang.value === 'ar');
const langFlag = computed(() => lang.value === 'fr' ? '🇫🇷' : '🇹🇳');
const langLabel = computed(() => lang.value === 'fr' ? 'FR' : 'AR');

// Sidebar classes
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
    'border-white/20',
    'transition-all',
    'duration-500',
    'ease-in-out',
    'z-40',
    'hidden',
    'lg:flex'
  ];
  
  if (lang.value === 'ar') {
    return [...baseClasses, 'right-0', 'border-l'];
  } else {
    return [...baseClasses, 'left-0', 'border-r'];
  }
});

// Content classes
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

// Données
const orders = ref([]);
const loading = ref(false);
const error = ref("");
const dl = ref(false);

// Fonctions utilitaires
function money(v) {
  const n = Number(v || 0);
  return new Intl.NumberFormat(lang.value === 'ar' ? 'ar-TN' : 'fr-TN', {
    style: 'currency',
    currency: 'TND',
    minimumFractionDigits: 2
  }).format(n);
}

function fmt(d) {
  if (!d) return "-";
  const date = new Date(d);
  return date.toLocaleDateString(lang.value === 'ar' ? 'ar-TN' : 'fr-FR', {
    day: '2-digit',
    month: '2-digit',
    year: 'numeric',
    hour: '2-digit',
    minute: '2-digit'
  });
}

function getStatusCount(status) {
  return orders.value.filter(o => o.status === status).length;
}

function getStatusIcon(status) {
  const icons = {
    'CART': '🛒',
    'CONFIRMED': '✅',
    'PREPARING': '⚙️',
    'SHIPPED': '🚚',
    'CANCELLED': '❌'
  };
  return icons[status] || '📄';
}

function getStatusColor(status) {
  const colors = {
    'CART': 'bg-amber-500/20 border border-amber-400/20',
    'CONFIRMED': 'bg-blue-500/20 border border-blue-400/20',
    'PREPARING': 'bg-purple-500/20 border border-purple-400/20',
    'SHIPPED': 'bg-emerald-500/20 border border-emerald-400/20',
    'CANCELLED': 'bg-red-500/20 border border-red-400/20'
  };
  return colors[status] || 'bg-gray-500/20 border border-gray-400/20';
}

function getStatusBadgeClass(status) {
  const classes = {
    'CART': 'bg-amber-500/30 text-amber-300 border border-amber-400/30',
    'CONFIRMED': 'bg-blue-500/30 text-blue-300 border border-blue-400/30',
    'PREPARING': 'bg-purple-500/30 text-purple-300 border border-purple-400/30',
    'SHIPPED': 'bg-emerald-500/30 text-emerald-300 border border-emerald-400/30',
    'CANCELLED': 'bg-red-500/30 text-red-300 border border-red-400/30'
  };
  return classes[status] || 'bg-gray-500/30 text-gray-300 border border-gray-400/30';
}

function downloadBlob(blob, filename) {
  const url = window.URL.createObjectURL(blob);
  const a = document.createElement("a");
  a.href = url;
  a.download = filename;
  document.body.appendChild(a);
  a.click();
  document.body.removeChild(a);
  window.URL.revokeObjectURL(url);
}

// Chargement des commandes
async function load() {
  loading.value = true; 
  error.value = "";
  try {
    const res = await adminListOrders();
    orders.value = (res.data || []).slice().sort((a, b) => (b.id || 0) - (a.id || 0));
  } catch (e) {
    error.value = lang.value === 'ar' 
      ? "غير قادر على تحميل الطلبات." 
      : "Impossible de charger les commandes.";
    console.error("Erreur de chargement:", e);
  } finally {
    loading.value = false;
  }
}

// Mise à jour du statut
async function setStatus(o, status) {
  try {
    await adminSetOrderStatus(o.id, { status });
    o.status = status;
  } catch (e) {
    alert(lang.value === 'ar' 
      ? "خطأ في تحديث الحالة" 
      : "Erreur update status");
    console.error("Erreur mise à jour statut:", e);
  }
}

// Export Excel
async function exportXlsx() {
  dl.value = true;
  try {
    const res = await adminExportOrdersXlsx();
    downloadBlob(res.data, `commandes_agricycle_${new Date().toISOString().split('T')[0]}.xlsx`);
  } catch (e) {
    alert(lang.value === 'ar' 
      ? "فشل تصدير إكسل" 
      : "Export excel échoué");
  } finally {
    dl.value = false;
  }
}

// Export PDF
async function exportPdf() {
  dl.value = true;
  try {
    const res = await adminExportOrdersPdf();
    downloadBlob(res.data, `commandes_agricycle_${new Date().toISOString().split('T')[0]}.pdf`);
  } catch (e) {
    alert(lang.value === 'ar' 
      ? "فشل تصدير PDF" 
      : "Export pdf échoué");
  } finally {
    dl.value = false;
  }
}

onMounted(() => {
  const savedLang = localStorage.getItem('lang') || 'fr';
  lang.value = savedLang;
  locale.value = savedLang;
  
  document.documentElement.dir = savedLang === 'ar' ? 'rtl' : 'ltr';
  document.documentElement.lang = savedLang;
  
  load();
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

/* Input style */
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
}

/* Boutons d'export */
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

.agri-btn-export-pdf {
  background: linear-gradient(135deg, #f56565 0%, #c53030 100%);
  color: white;
  font-weight: 600;
  box-shadow: 0 4px 15px rgba(245, 101, 101, 0.3);
  border: none;
  border-radius: 10px;
  padding: 12px 24px;
  transition: all 0.3s ease;
}

.agri-btn-export-pdf:hover:not(:disabled) {
  box-shadow: 0 8px 25px rgba(245, 101, 101, 0.4);
  transform: translateY(-2px);
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

[dir="rtl"] .nav-item:hover {
  transform: translateX(-4px);
}

.router-link-active {
  background: linear-gradient(135deg, rgba(46, 204, 113, 0.3) 0%, rgba(52, 152, 219, 0.3) 100%);
  border: 1px solid rgba(255, 255, 255, 0.3);
  box-shadow: 0 4px 15px rgba(46, 204, 113, 0.2);
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

/* RTL Support */
[dir="rtl"] .flex {
  flex-direction: row-reverse;
}

[dir="rtl"] .gap-3, [dir="rtl"] .gap-4 {
  gap: 1rem;
}

[dir="rtl"] .ml-1 {
  margin-left: 0;
  margin-right: 0.25rem;
}

/* Responsive */
@media (max-width: 1024px) {
  .lg\:ml-72, .lg\:mr-72 {
    margin-left: 0 !important;
    margin-right: 0 !important;
  }
  
  .grid-cols-2, .grid-cols-3, .grid-cols-4, .grid-cols-5 {
    grid-template-columns: 1fr;
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
}

/* Style pour bouton désactivé */
button:disabled {
  cursor: not-allowed;
  pointer-events: none;
}
</style>