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
      <!-- SIDEBAR FARMER -->
      <aside :class="sidebarClasses">
        <div class="agri-card p-4 mb-4 bg-white/10 backdrop-blur-lg border border-white/20">
          <div class="flex items-center gap-3" :class="{ 'flex-row-reverse': isRTL }">
            <div class="w-12 h-12 rounded-xl2 bg-gradient-to-r from-agri-green/30 to-agri-blue/30 border border-white/20 flex items-center justify-center shadow-lg flex-shrink-0">
              <span class="text-2xl text-white">👨‍🌾</span>
            </div>
            <div class="min-w-0 flex-1">
              <div class="font-semibold text-white truncate">{{ isRTL ? 'المزارع' : 'Agriculteur' }}</div>
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
         
          <!-- Dashboard -->
          <router-link class="nav-item" to="/app/farmer">
            <div class="flex items-center gap-3 p-3 rounded-xl hover:bg-white/10 transition-all duration-300" :class="{ 'flex-row-reverse': isRTL }">
              <div class="w-10 h-10 rounded-lg bg-gradient-to-r from-agri-green/30 to-agri-blue/30 border border-white/20 flex items-center justify-center flex-shrink-0">
                <span class="text-white text-xl">📊</span>
              </div>
              <div class="min-w-0 flex-1">
                <div class="text-white font-medium truncate">{{ isRTL ? 'لوحة القيادة' : 'Dashboard' }}</div>
                <div class="text-xs text-white/60 truncate">{{ isRTL ? 'نظرة عامة' : 'Vue d\'ensemble' }}</div>
              </div>
            </div>
          </router-link>




          <!-- Mes Déclarations -->
          <router-link class="nav-item" to="/app/farmer/declarations">
            <div class="flex items-center gap-3 p-3 rounded-xl hover:bg-white/10 transition-all duration-300" :class="{ 'flex-row-reverse': isRTL }">
              <div class="w-10 h-10 rounded-lg bg-emerald-500/30 border border-emerald-400/20 flex items-center justify-center flex-shrink-0">
                <span class="text-emerald-300 text-xl">♻️</span>
              </div>
              <div class="min-w-0 flex-1">
                <div class="text-white font-medium truncate">{{ isRTL ? 'تصاريحي' : 'Mes Déclarations' }}</div>
                <div class="text-xs text-white/60 truncate">{{ isRTL ? 'إدارة التصاريح' : 'Gérer mes déclarations' }}</div>
              </div>
            </div>
          </router-link>




          <!-- Profil -->
          <router-link class="nav-item" to="/app/farmer/profile">
            <div class="flex items-center gap-3 p-3 rounded-xl hover:bg-white/10 transition-all duration-300" :class="{ 'flex-row-reverse': isRTL }">
              <div class="w-10 h-10 rounded-lg bg-indigo-500/30 border border-indigo-400/20 flex items-center justify-center flex-shrink-0">
                <span class="text-indigo-300 text-xl">👤</span>
              </div>
              <div class="min-w-0 flex-1">
                <div class="text-white font-medium truncate">{{ isRTL ? 'الملف الشخصي' : 'Profil' }}</div>
                <div class="text-xs text-white/60 truncate">{{ isRTL ? 'معلوماتي' : 'Mes informations' }}</div>
              </div>
            </div>
          </router-link>
        </div>
      </aside>




      <!-- Main Content -->
      <main>
        <div class="space-y-6">
          <!-- Header -->
          <div class="mb-8">
            <div class="flex items-center justify-between mb-6 flex-wrap gap-4" :class="{ 'flex-row-reverse': isRTL }">
              <div class="flex items-center gap-4" :class="{ 'flex-row-reverse': isRTL }">
                <div class="p-3 bg-white/20 backdrop-blur-sm rounded-xl border border-white/30 flex-shrink-0">
                  <span class="text-2xl text-white">♻️</span>
                </div>
                <div>
                  <h1 class="text-3xl md:text-4xl font-bold text-white">
                    {{ isRTL ? 'تصاريحي' : 'Mes Déclarations' }}
                  </h1>
                  <p class="text-white/90 mt-2">
                    {{ isRTL ? 'متابعة حالات التصاريح' : 'Suivi des statuts' }}
                  </p>
                </div>
              </div>
             
              <div class="flex items-center gap-3" :class="{ 'flex-row-reverse': isRTL }">
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
            <h3 class="text-xl font-semibold text-white mb-2">{{ isRTL ? 'جاري تحميل التصاريح' : 'Chargement des déclarations' }}</h3>
            <p class="text-white/80">{{ isRTL ? 'يرجى الانتظار...' : 'Veuillez patienter...' }}</p>
          </div>




          <!-- Error State -->
          <div v-if="error" class="agri-card p-6 bg-gradient-to-r from-red-500/10 to-red-500/5 border border-red-500/20">
            <div class="flex items-center gap-4" :class="{ 'flex-row-reverse': isRTL }">
              <div class="p-2 bg-red-500/20 rounded-lg flex-shrink-0">
                <span class="text-red-300 text-xl">❌</span>
              </div>
              <div class="flex-1">
                <h4 class="font-medium text-red-200">{{ isRTL ? 'خطأ' : 'Erreur' }}</h4>
                <p class="text-sm text-red-200/90 mt-1">{{ error }}</p>
              </div>
              <button @click="load" class="px-4 py-2 bg-red-500/20 hover:bg-red-500/30 text-red-300 rounded-lg transition-colors">
                {{ isRTL ? 'إعادة المحاولة' : 'Réessayer' }}
              </button>
            </div>
          </div>




          <!-- Liste des déclarations -->
          <div v-if="items.length && !loading" class="grid md:grid-cols-2 gap-6">
            <div
              v-for="d in items"
              :key="d.id"
              class="agri-card p-6 hover:shadow-2xl transition-all duration-300 bg-white/10 backdrop-blur-lg border border-white/20 hover:border-white/40"
            >
              <!-- En-tête -->
              <div class="flex items-start justify-between gap-3 mb-4" :class="{ 'flex-row-reverse': isRTL }">
                <div class="flex items-center gap-3">
                  <div class="p-2 bg-gradient-to-r from-emerald-500/20 to-emerald-400/20 rounded-lg">
                    <span class="text-emerald-300 text-xl">♻️</span>
                  </div>
                  <div>
                    <div class="font-semibold text-white text-lg">{{ d.packaging_type }}</div>
                    <div class="text-xs text-white/60 mt-1">
                      {{ isRTL ? 'الكمية' : 'Qty' }}: {{ d.quantity }} • {{ isRTL ? 'التجميع' : 'Pickup' }}: {{ d.pickup_date ? formatDate(d.pickup_date) : (isRTL ? 'غير محدد' : 'N/A') }}
                    </div>
                  </div>
                </div>
                <span :class="getStatusBadgeClass(d.status)" class="px-3 py-1 rounded-full text-xs font-medium">
                  {{ getStatusLabel(d.status) }}
                </span>
              </div>




              <!-- Informations supplémentaires -->
              <div class="mt-4 space-y-2 text-sm text-white/80">
                <div class="flex items-center gap-2 p-2 bg-white/5 rounded-lg border border-white/10" :class="{ 'flex-row-reverse': isRTL }">
                  <span class="text-white/60">✅</span>
                  <span><b>{{ isRTL ? 'معتمد rinsed' : 'Certifié rincé' }}:</b> {{ d.cert_rinsed ? (isRTL ? 'نعم' : 'Oui') : (isRTL ? 'لا' : 'Non') }}</span>
                </div>
               
                <div v-if="d.location_address" class="flex items-center gap-2 p-2 bg-white/5 rounded-lg border border-white/10" :class="{ 'flex-row-reverse': isRTL }">
                  <span class="text-white/60">📍</span>
                  <span><b>{{ isRTL ? 'الموقع' : 'Lieu' }}:</b> {{ d.location_address }}</span>
                </div>
              </div>




              <!-- Pied de carte -->
              <div class="mt-4 pt-3 border-t border-white/10 flex items-center justify-between text-xs text-white/40" :class="{ 'flex-row-reverse': isRTL }">
                <span>{{ isRTL ? 'تم الإنشاء' : 'Créé' }}: {{ fmt(d.created_at) }}</span>
                <span>#{{ d.id }}</span>
              </div>
            </div>
          </div>




          <!-- Empty State -->
          <div
            v-else-if="!loading && !error && items.length === 0"
            class="agri-card p-12 text-center hover:shadow-2xl transition-all duration-300 bg-white/10 backdrop-blur-lg border border-white/20"
          >
            <div class="text-6xl mb-6 opacity-50">♻️</div>
            <h3 class="text-2xl font-bold text-white mb-3">
              {{ isRTL ? 'لا توجد تصاريح' : 'Aucune déclaration' }}
            </h3>
            <p class="text-white/80 mb-8 max-w-md mx-auto">
              {{ isRTL ? 'أضف تصريحاً من لوحة القيادة الخاصة بك.' : 'Ajoute une déclaration depuis ton dashboard.' }}
            </p>
            <router-link
              to="/app/farmer"
              class="inline-block px-6 py-3 agri-btn-export hover:scale-[1.02] transition-all duration-300"
            >
              {{ isRTL ? 'العودة إلى لوحة القيادة' : 'Retour au dashboard' }}
            </router-link>
          </div>
        </div>
      </main>
    </div>
  </div>
</template>




<script setup>
import { onMounted, ref, computed } from "vue";
import { useAuthStore } from "../../store/auth";
import { useI18n } from "vue-i18n";
import { getMyDeclarations } from "../../api/exports";




const auth = useAuthStore();
const { locale } = useI18n();




// Gestion de la langue
const lang = ref('fr');
const isRTL = computed(() => lang.value === 'ar');




// Classes du sidebar
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




// Classes du conteneur principal
const contentContainerClasses = computed(() => {
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




const items = ref([]);
const loading = ref(false);
const error = ref("");




// Fonctions utilitaires
function fmt(d) {
  if (!d) return "-";
  try {
    return new Date(d).toLocaleDateString(lang.value === 'ar' ? 'ar-TN' : 'fr-FR', {
      day: '2-digit',
      month: '2-digit',
      year: 'numeric',
      hour: '2-digit',
      minute: '2-digit'
    });
  } catch {
    return String(d).replace("T", " ").slice(0, 16);
  }
}




function formatDate(dateString) {
  if (!dateString) return '';
  try {
    return new Date(dateString).toLocaleDateString(lang.value === 'ar' ? 'ar-TN' : 'fr-FR', {
      day: '2-digit',
      month: '2-digit',
      year: 'numeric'
    });
  } catch {
    return dateString;
  }
}




function getStatusLabel(status) {
  const labels = {
    'PENDING': isRTL.value ? 'قيد الانتظار' : 'En attente',
    'CONFIRMED': isRTL.value ? 'مؤكد' : 'Confirmé',
    'COLLECTED': isRTL.value ? 'تم التجميع' : 'Collecté',
    'CANCELLED': isRTL.value ? 'ملغي' : 'Annulé'
  };
  return labels[status] || status;
}




function getStatusBadgeClass(status) {
  const classes = {
    'PENDING': 'bg-yellow-500/20 text-yellow-200 border border-yellow-400/20',
    'CONFIRMED': 'bg-green-500/20 text-green-200 border border-green-400/20',
    'COLLECTED': 'bg-blue-500/20 text-blue-200 border border-blue-400/20',
    'CANCELLED': 'bg-red-500/20 text-red-200 border border-red-400/20'
  };
  return classes[status] || 'bg-gray-500/20 text-gray-200 border border-gray-400/20';
}




async function load() {
  loading.value = true;
  error.value = "";
  try {
    const res = await getMyDeclarations();
    items.value = (res.data || []).slice().sort((a, b) => (b.id || 0) - (a.id || 0));
  } catch (e) {
    console.error(e);
    error.value = isRTL.value ? "غير قادر على تحميل تصاريحك." : "Impossible de charger tes déclarations.";
  } finally {
    loading.value = false;
  }
}




onMounted(() => {
  const savedLang = localStorage.getItem('lang') || 'fr';
  lang.value = savedLang;
  locale.value = savedLang;
 
  if (savedLang === 'ar') {
    document.documentElement.dir = 'rtl';
    document.documentElement.lang = 'ar';
  } else {
    document.documentElement.dir = 'ltr';
    document.documentElement.lang = 'fr';
  }
 
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
  transform: translateY(-4px);
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




[dir="rtl"] .nav-item:hover {
  transform: translateX(-4px);
}




.router-link-active {
  background: linear-gradient(135deg, rgba(46, 204, 113, 0.3) 0%, rgba(52, 152, 219, 0.3) 100%);
  border: 1px solid rgba(255, 255, 255, 0.3);
  box-shadow: 0 4px 15px rgba(46, 204, 113, 0.2);
}




/* Boutons */
.agri-btn-export {
  background: linear-gradient(135deg, #48bb78 0%, #2f855a 100%);
  color: white;
  font-weight: 600;
  box-shadow: 0 4px 15px rgba(72, 187, 120, 0.3);
  border: none;
  border-radius: 10px;
  transition: all 0.3s ease;
}




.agri-btn-export:hover:not(:disabled) {
  box-shadow: 0 8px 25px rgba(72, 187, 120, 0.4);
  transform: translateY(-2px);
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
 
  .grid-cols-2 {
    grid-template-columns: 1fr;
  }
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




/* RTL Support */
[dir="rtl"] .flex {
  flex-direction: row-reverse;
}




[dir="rtl"] .gap-3, [dir="rtl"] .gap-4 {
  gap: 1rem;
}




[dir="rtl"] .ml-4 {
  margin-left: 0 !important;
  margin-right: 1rem !important;
}




[dir="rtl"] .mr-4 {
  margin-right: 0 !important;
  margin-left: 1rem !important;
}




[dir="rtl"] .text-left {
  text-align: right !important;
}




[dir="rtl"] .text-right {
  text-align: left !important;
}




/* Scrollbar personnalisée */
::-webkit-scrollbar {
  width: 8px;
  height: 8px;
}




::-webkit-scrollbar-track {
  background: rgba(255, 255, 255, 0.1);
  border-radius: 4px;
}




::-webkit-scrollbar-thumb {
  background: rgba(255, 255, 255, 0.3);
  border-radius: 4px;
}




::-webkit-scrollbar-thumb:hover {
  background: rgba(255, 255, 255, 0.4);
}




/* Badges */
.badge-pending {
  background: rgba(245, 158, 11, 0.2);
  color: #fcd34d;
  border: 1px solid rgba(245, 158, 11, 0.3);
}




.badge-confirmed {
  background: rgba(16, 185, 129, 0.2);
  color: #a7f3d0;
  border: 1px solid rgba(16, 185, 129, 0.3);
}




.badge-collected {
  background: rgba(59, 130, 246, 0.2);
  color: #bfdbfe;
  border: 1px solid rgba(59, 130, 246, 0.3);
}




.badge-cancelled {
  background: rgba(239, 68, 68, 0.2);
  color: #fecaca;
  border: 1px solid rgba(239, 68, 68, 0.3);
}
</style>





