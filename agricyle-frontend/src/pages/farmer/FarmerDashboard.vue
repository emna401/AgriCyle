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
          <!-- Nouveau lien vers /app/profile -->
<router-link class="nav-item" to="/app/profile">
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
      <main >
        <div class="space-y-6">
          <!-- Header -->
          <div class="mb-8">
            <div class="flex items-center justify-between mb-6 flex-wrap gap-4" :class="{ 'flex-row-reverse': isRTL }">
              <div class="flex items-center gap-4" :class="{ 'flex-row-reverse': isRTL }">
                <div class="p-3 bg-white/20 backdrop-blur-sm rounded-xl border border-white/30 flex-shrink-0">
                  <span class="text-2xl text-white">👨‍🌾</span>
                </div>
                <div>
                  <h1 class="text-3xl md:text-4xl font-bold text-white">
                    {{ isRTL ? 'لوحة قيادة المزارع' : 'Farmer Dashboard' }}
                  </h1>
                  <p class="text-white/90 mt-2">
                    {{ isRTL ? 'متابعة تصاريحك ومزرعتك' : 'Suivi de vos déclarations & ferme' }}
                  </p>
                </div>
              </div>
             
              <div class="flex items-center gap-3" :class="{ 'flex-row-reverse': isRTL }">
                <router-link
                  to="/good-practices"
                  class="px-4 py-2 border border-white/20 rounded-lg text-sm font-medium text-white/80 hover:bg-white/10 transition-all flex items-center gap-2"
                  :class="{ 'flex-row-reverse': isRTL }"
                >
                  <span>📚</span>
                  <span>{{ isRTL ? 'الممارسات الجيدة' : 'Bonnes pratiques' }}</span>
                </router-link>
               
                <button
                  @click="openNew = true"
                  class="agri-btn-export px-4 py-2 text-sm font-medium transition-all duration-300 flex items-center gap-2"
                  :class="{ 'flex-row-reverse': isRTL }"
                >
                  <span>➕</span>
                  <span>{{ isRTL ? 'تصريح جديد' : 'Nouvelle déclaration' }}</span>
                </button>
              </div>
            </div>
          </div>


          <!-- Loading State -->
          <div v-if="loading && !me" class="agri-card p-12 text-center hover:shadow-2xl transition-all duration-300 bg-white/10 backdrop-blur-lg border border-white/20">
            <div class="inline-block animate-spin text-4xl mb-4 text-white/80">⟳</div>
            <h3 class="text-xl font-semibold text-white mb-2">{{ isRTL ? 'جاري تحميل البيانات' : 'Chargement des données' }}</h3>
            <p class="text-white/80">{{ isRTL ? 'يرجى الانتظار...' : 'Veuillez patienter...' }}</p>
          </div>


          <!-- Contenu principal -->
          <div v-else class="grid lg:grid-cols-3 gap-6">
            <!-- Carte Ferme -->
            <div class="agri-card p-6 hover:shadow-2xl transition-all duration-300 bg-white/10 backdrop-blur-lg border border-white/20">
              <div class="flex items-center gap-3 mb-4" :class="{ 'flex-row-reverse': isRTL }">
                <div class="p-2 bg-gradient-to-r from-amber-500/20 to-amber-400/20 rounded-lg">
                  <span class="text-amber-300 text-xl">📍</span>
                </div>
                <div>
                  <h3 class="text-lg font-semibold text-white">{{ isRTL ? 'المزرعة' : 'Ferme' }}</h3>
                  <p class="text-sm text-white/80">{{ isRTL ? 'العنوان والموقع' : 'Adresse & localisation' }}</p>
                </div>
              </div>


              <div v-if="me?.farm_address" class="text-sm text-white/90">
                <div class="font-medium text-white">{{ me.farm_name || (isRTL ? 'مزرعتي' : 'Ma ferme') }}</div>
                <div class="text-white/80 mt-1">{{ me.farm_address }}</div>
                <div class="text-xs text-white/60 mt-2 p-2 bg-white/5 rounded-lg border border-white/10">
                  {{ isRTL ? 'خط العرض' : 'Lat' }}: {{ me.farm_lat || "-" }} | {{ isRTL ? 'خط الطول' : 'Lng' }}: {{ me.farm_lng || "-" }}
                </div>
              </div>


              <div v-else class="text-sm text-white/80">
                {{ isRTL ? 'لم يتم تسجيل أي موقع.' : 'Aucune localisation enregistrée.' }}
                <router-link to="/app/farmer/profile" class="text-agri-green-light hover:underline block mt-2">
                  {{ isRTL ? 'أضف الآن ←' : 'Ajouter maintenant →' }}
                </router-link>
              </div>
            </div>


            <!-- Carte Statistiques -->
            <div class="agri-card p-6 hover:shadow-2xl transition-all duration-300 bg-white/10 backdrop-blur-lg border border-white/20">
              <div class="flex items-center gap-3 mb-4" :class="{ 'flex-row-reverse': isRTL }">
                <div class="p-2 bg-gradient-to-r from-blue-500/20 to-blue-400/20 rounded-lg">
                  <span class="text-blue-300 text-xl">📊</span>
                </div>
                <div>
                  <h3 class="text-lg font-semibold text-white">{{ isRTL ? 'إحصائيات' : 'Statistiques' }}</h3>
                  <p class="text-sm text-white/80">{{ isRTL ? 'هذه السنة' : 'Cette année' }}</p>
                </div>
              </div>


              <div class="grid grid-cols-2 gap-3 mt-2">
                <div class="agri-card p-3 bg-white/5 backdrop-blur-sm border border-white/10">
                  <div class="text-xs text-white/60">{{ isRTL ? 'التصاريح' : 'Déclarations' }}</div>
                  <div class="text-xl font-bold text-white">{{ stats.count }}</div>
                </div>
                <div class="agri-card p-3 bg-white/5 backdrop-blur-sm border border-white/10">
                  <div class="text-xs text-white/60">{{ isRTL ? 'الكمية الإجمالية' : 'Quantité totale' }}</div>
                  <div class="text-xl font-bold text-white">{{ stats.totalQty }}</div>
                </div>
              </div>


              <div class="text-xs text-white/60 mt-3 p-2 bg-blue-900/30 border border-blue-400/20 rounded-lg">
                * {{ isRTL ? 'الكمية تعتمد على ما تعلنه (قنينات، زجاجات...)' : 'La quantité dépend de ce que tu déclares (bidons, flacons…)' }}
              </div>
            </div>


            <!-- Carte Dernier statut -->
            <div class="agri-card p-6 hover:shadow-2xl transition-all duration-300 bg-white/10 backdrop-blur-lg border border-white/20">
              <div class="flex items-center gap-3 mb-4" :class="{ 'flex-row-reverse': isRTL }">
                <div class="p-2 bg-gradient-to-r from-purple-500/20 to-purple-400/20 rounded-lg">
                  <span class="text-purple-300 text-xl">⏱️</span>
                </div>
                <div>
                  <h3 class="text-lg font-semibold text-white">{{ isRTL ? 'آخر حالة' : 'Dernier statut' }}</h3>
                  <p class="text-sm text-white/80">{{ isRTL ? 'آخر التصاريح' : 'Dernières déclarations' }}</p>
                </div>
              </div>


              <div v-if="lastThree.length" class="space-y-3">
                <div
                  v-for="d in lastThree"
                  :key="d.id"
                  class="flex items-center justify-between text-sm border-b border-white/10 pb-2 last:border-0"
                  :class="{ 'flex-row-reverse': isRTL }"
                >
                  <div>
                    <div class="font-medium text-white">{{ d.packaging_type }}</div>
                    <div class="text-xs text-white/60">
                      {{ isRTL ? 'الكمية' : 'qty' }}: {{ d.quantity }} • {{ d.pickup_date ? formatDate(d.pickup_date) : (isRTL ? 'تاريخ غير محدد' : 'date non définie') }}
                    </div>
                  </div>
                  <span :class="getStatusBadgeClass(d.status)" class="px-2 py-1 rounded-full text-xs font-medium">
                    {{ getStatusLabel(d.status) }}
                  </span>
                </div>


                <router-link
                  to="/app/farmer/declarations"
                  class="text-sm text-agri-green-light hover:underline block mt-2"
                  :class="{ 'text-right': isRTL }"
                >
                  {{ isRTL ? 'عرض الكل ←' : 'Voir tout →' }}
                </router-link>
              </div>


              <div v-else class="text-sm text-white/80">
                {{ isRTL ? 'لا توجد تصاريح.' : 'Aucune déclaration.' }}
              </div>
            </div>
          </div>
        </div>
      </main>
    </div>


    <!-- MODAL NOUVELLE DÉCLARATION - CORRIGÉ -->
    <Teleport to="body">
      <div v-if="openNew" class="fixed inset-0 z-50 overflow-y-auto bg-black/70 backdrop-blur-sm">
        <div class="flex items-center justify-center min-h-screen pt-4 px-4 pb-20 text-center">
          <div class="inline-block align-bottom bg-gray-900/95 rounded-xl text-left overflow-hidden shadow-2xl transform transition-all sm:my-8 sm:align-middle sm:max-w-lg sm:w-full border border-white/20">
            <!-- Header -->
            <div class="px-6 pt-6 pb-4 border-b border-white/20">
              <div class="flex items-start justify-between" :class="{ 'flex-row-reverse': isRTL }">
                <div>
                  <h3 class="text-xl font-semibold text-white">
                    ➕ {{ isRTL ? 'تصريح جديد' : 'Nouvelle Déclaration' }}
                  </h3>
                  <p class="text-sm text-white/60 mt-1">
                    {{ isRTL ? 'صرح عن عبواتك' : 'Déclare tes emballages' }}
                  </p>
                </div>
                <button
                  @click="openNew = false"
                  class="text-white/60 hover:text-white/80 p-1 hover:bg-white/10 rounded transition-all"
                >
                  ✕
                </button>
              </div>
            </div>


            <!-- Formulaire -->
            <form @submit.prevent="submitDeclaration" class="px-6 pb-6">
              <div class="space-y-4">
                <!-- Type d'emballage -->
                <div>
                  <label class="block text-sm font-medium text-white/80 mb-1">
                    {{ isRTL ? 'نوع العبوة' : "Type d'emballage" }}
                  </label>
                  <input
                    v-model="form.packaging_type"
                    type="text"
                    :placeholder="isRTL ? 'قنينة 5 لتر، زجاجة 1 لتر...' : 'Bidon 5L, Flacon 1L...'"
                    class="w-full px-3 py-2.5 bg-white/10 border border-white/20 rounded-lg focus:outline-none focus:ring-2 focus:ring-agri-green text-white placeholder-white/50"
                  >
                </div>


                <!-- Quantité -->
                <div>
                  <label class="block text-sm font-medium text-white/80 mb-1">
                    {{ isRTL ? 'الكمية' : 'Quantité' }}
                  </label>
                  <input
                    v-model="form.quantity"
                    type="number"
                    min="1"
                    :placeholder="isRTL ? 'مثال: 35' : 'ex: 35'"
                    class="w-full px-3 py-2.5 bg-white/10 border border-white/20 rounded-lg focus:outline-none focus:ring-2 focus:ring-agri-green text-white placeholder-white/50"
                  >
                </div>


                <!-- Certification -->
                <div class="p-3 bg-white/5 rounded-lg border border-white/10">
                  <label class="flex items-center gap-2 text-sm text-white/80" :class="{ 'flex-row-reverse': isRTL }">
                    <input type="checkbox" v-model="form.cert_rinsed" class="w-4 h-4 accent-agri-green" />
                    <span>{{ isRTL ? 'أقر بأنني قمت بشطف وثقب هذه العبوات.' : 'Je certifie avoir rincé et perforé ces emballages.' }}</span>
                  </label>
                </div>


                <!-- Date de collecte -->
                <div>
                  <label class="block text-sm font-medium text-white/80 mb-1">
                    {{ isRTL ? 'تاريخ التجميع المطلوب' : 'Date collecte souhaitée' }}
                  </label>
                  <input
                    v-model="form.pickup_date"
                    type="date"
                    class="w-full px-3 py-2.5 bg-white/10 border border-white/20 rounded-lg focus:outline-none focus:ring-2 focus:ring-agri-green text-white"
                  >
                </div>


                <!-- Messages d'erreur/succès -->
                <div v-if="err" class="p-3 bg-red-900/30 border border-red-400/20 rounded-lg">
                  <p class="text-sm text-red-300 text-center">{{ err }}</p>
                </div>
                <div v-if="ok" class="p-3 bg-green-900/30 border border-green-400/20 rounded-lg">
                  <p class="text-sm text-green-300 text-center">{{ ok }}</p>
                </div>


                <!-- Boutons -->
                <div class="flex gap-3 pt-2" :class="{ 'flex-row-reverse': isRTL }">
                  <button
                    type="button"
                    @click="openNew = false"
                    class="flex-1 px-4 py-2.5 border border-white/20 rounded-lg text-sm font-medium text-white/80 hover:bg-white/10 transition-all"
                  >
                    {{ isRTL ? 'إلغاء' : 'Annuler' }}
                  </button>
                  <button
                    type="submit"
                    :disabled="loading"
                    class="flex-1 px-4 py-2.5 agri-btn-export rounded-lg text-sm font-medium transition-all duration-300 flex items-center justify-center gap-2 disabled:opacity-50 disabled:cursor-not-allowed"
                    :class="{ 'flex-row-reverse': isRTL }"
                  >
                    <span v-if="loading" class="inline-block animate-spin">⟳</span>
                    <span v-else>📤</span>
                    <span>{{ loading ? (isRTL ? 'جاري...' : '...') : (isRTL ? 'إرسال' : 'Envoyer') }}</span>
                  </button>
                </div>
              </div>
            </form>
          </div>
        </div>
      </div>
    </Teleport>
  </div>
</template>


<script setup>
import { computed, onMounted, reactive, ref } from "vue";
import { useAuthStore } from "../../store/auth";
import { useI18n } from "vue-i18n";
import { createDeclaration, getMe, getMyDeclarations } from "../../api/exports";


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


const me = ref(null);
const declarations = ref([]);
const stats = reactive({ count: 0, totalQty: 0 });


const openNew = ref(false);
const loading = ref(false);
const err = ref("");
const ok = ref("");


const form = reactive({
  packaging_type: "",
  quantity: 1,
  cert_rinsed: false,
  pickup_date: ""
});


const lastThree = computed(() => declarations.value.slice(0, 3));


// Fonctions utilitaires
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


function computeStats() {
  stats.count = declarations.value.length;
  stats.totalQty = declarations.value.reduce((s, d) => s + Number(d.quantity || 0), 0);
}


async function load() {
  const meRes = await getMe();
  me.value = meRes.data;
  auth.user = me.value;


  const dRes = await getMyDeclarations();
  declarations.value = (dRes.data || []).slice().sort((a, b) => (b.id || 0) - (a.id || 0));
  computeStats();
}


async function submitDeclaration() {
  err.value = "";
  ok.value = "";


  if (!form.packaging_type) {
    err.value = isRTL.value ? "نوع العبوة مطلوب." : "Type emballage obligatoire.";
    return;
  }
  if (Number(form.quantity) <= 0) {
    err.value = isRTL.value ? "كمية غير صالحة." : "Quantité invalide.";
    return;
  }


  loading.value = true;
  try {
    await createDeclaration({
      packaging_type: form.packaging_type,
      quantity: Number(form.quantity),
      cert_rinsed: !!form.cert_rinsed,
      pickup_date: form.pickup_date || null
    });


    ok.value = isRTL.value ? "تم إرسال التصريح ✅" : "Déclaration envoyée ✅";
   
    // Fermer le modal après un court délai pour voir le message de succès
    setTimeout(() => {
      openNew.value = false;
      // Réinitialiser le formulaire
      form.packaging_type = "";
      form.quantity = 1;
      form.cert_rinsed = false;
      form.pickup_date = "";
      ok.value = "";
    }, 1500);


    await load();
  } catch (e) {
    console.error(e);
    err.value = isRTL.value ? "خطأ في إنشاء التصريح." : "Erreur création déclaration.";
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


/* Input style */
input, select, textarea {
  background: rgba(255, 255, 255, 0.1);
  backdrop-filter: blur(10px);
  border: 1px solid rgba(255, 255, 255, 0.2);
  border-radius: 10px;
  padding: 10px 16px;
  color: white;
  font-size: 14px;
  transition: all 0.3s ease;
  outline: none;
}


input:focus, select:focus, textarea:focus {
  border-color: rgba(255, 255, 255, 0.5);
  box-shadow: 0 0 0 3px rgba(255, 255, 255, 0.1);
}


input::placeholder, textarea::placeholder {
  color: rgba(255, 255, 255, 0.5);
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


/* Style pour bouton désactivé */
button:disabled {
  cursor: not-allowed;
  pointer-events: none;
  opacity: 0.5;
}
</style>

