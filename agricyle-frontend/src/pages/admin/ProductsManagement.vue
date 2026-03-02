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
                <span class="text-2xl text-white">📦</span>
              </div>
              <div>
                <h1 class="text-3xl md:text-4xl font-bold text-white">
                  {{ isRTL ? 'إدارة المنتجات' : 'Gestion des Produits' }}
                </h1>
                <p class="text-white/90 mt-2">
                  {{ isRTL ? 'إضافة، تعديل وحذف المنتجات' : 'Ajouter, modifier et supprimer des produits' }}
                </p>
              </div>
            </div>
            
            
          </div>
        </div>

        <!-- Carte d'ajout de produit -->
        <div class="agri-card p-6 mb-8 hover:shadow-2xl transition-all duration-300 bg-white/10 backdrop-blur-lg border border-white/20">
          <div class="flex items-center gap-3 mb-6" :class="{ 'flex-row-reverse': isRTL }">
           
            <div>
              <h3 class="font-semibold text-white text-lg">{{ isRTL ? 'إضافة منتج جديد' : 'Ajouter un produit' }}</h3>
              <p class="text-sm text-white/80 mt-1">{{ isRTL ? 'إنشاء منتج جديد' : 'Créer un nouveau produit' }}</p>
            </div>
          </div>

          <form @submit.prevent="create" class="space-y-4">
            <div class="grid md:grid-cols-4 gap-4">
              <div>
                <label class="block text-sm font-medium text-white/90 mb-2">{{ isRTL ? 'الاسم' : 'Nom' }}</label>
                <input 
                  v-model="createForm.name" 
                  type="text" 
                  :placeholder="isRTL ? 'شبكة معاد تدويرها' : 'Filet recyclé'"
                  class="agri-input-filter w-full"
                />
              </div>
              <div>
                <label class="block text-sm font-medium text-white/90 mb-2">{{ isRTL ? 'الفئة' : 'Catégorie' }}</label>
                <input 
                  v-model="createForm.category" 
                  type="text" 
                  :placeholder="isRTL ? 'شبكات' : 'Filets'"
                  class="agri-input-filter w-full"
                />
              </div>
              <div>
                <label class="block text-sm font-medium text-white/90 mb-2">{{ isRTL ? 'السعر' : 'Prix' }}</label>
                <input 
                  v-model="createForm.price" 
                  type="number" 
                  step="0.01"
                  :placeholder="isRTL ? '١٢٫٥٠' : '12.50'"
                  class="agri-input-filter w-full"
                />
              </div>
              <div>
                <label class="block text-sm font-medium text-white/90 mb-2">{{ isRTL ? 'المخزون' : 'Stock' }}</label>
                <input 
                  v-model="createForm.stock" 
                  type="number" 
                  step="1"
                  :placeholder="isRTL ? '٢٠٠' : '200'"
                  class="agri-input-filter w-full"
                />
              </div>
            </div>

            <div class="flex justify-end">
              <button 
                type="submit" 
                :disabled="saving"
                class="agri-btn-export px-8 py-3 flex items-center gap-2 disabled:opacity-50 disabled:cursor-not-allowed"
                :class="{ 'flex-row-reverse': isRTL }"
              >
                <span v-if="saving" class="inline-block animate-spin">⟳</span>
                
                <span>{{ saving ? (isRTL ? 'جاري الإنشاء...' : 'Création...') : (isRTL ? 'إنشاء' : 'Créer') }}</span>
              </button>
            </div>
          </form>

          <!-- Messages -->
          <div v-if="msg" class="mt-4 p-3 bg-agri-green/20 backdrop-blur-sm border border-agri-green/30 rounded-lg">
            <div class="flex items-center gap-2" :class="{ 'flex-row-reverse': isRTL }">
              <span class="text-agri-green-light">✅</span>
              <span class="text-white/90">{{ msg }}</span>
            </div>
          </div>
          
          <div v-if="err" class="mt-4 p-3 bg-red-500/20 backdrop-blur-sm border border-red-400/30 rounded-lg">
            <div class="flex items-center gap-2" :class="{ 'flex-row-reverse': isRTL }">
              <span class="text-red-300">❌</span>
              <span class="text-white/90">{{ err }}</span>
            </div>
          </div>
        </div>

        <!-- Loading State -->
        <div v-if="loading" class="agri-card p-12 text-center hover:shadow-2xl transition-all duration-300 bg-white/10 backdrop-blur-lg border border-white/20">
          <div class="inline-block animate-spin text-4xl mb-4 text-white/80">⟳</div>
          <h3 class="text-xl font-semibold text-white mb-2">{{ isRTL ? 'جاري تحميل المنتجات' : 'Chargement des produits' }}</h3>
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

        <!-- Liste des produits -->
        <div v-if="items.length && !loading">
          <div class="mb-4 flex items-center justify-between" :class="{ 'flex-row-reverse': isRTL }">
            <h3 class="text-lg font-semibold text-white">
              {{ items.length }} {{ isRTL ? 'منتج' : 'produit' }}{{ items.length > 1 ? (isRTL ? '' : 's') : '' }}
            </h3>
            <div class="text-sm text-white/60 bg-white/10 px-3 py-1 rounded-full border border-white/20">
              {{ isRTL ? 'ترتيب: الأحدث أولاً' : 'Tri: Plus récent d\'abord' }}
            </div>
          </div>

          <div class="space-y-4">
            <div 
              v-for="p in items" 
              :key="p.id" 
              class="agri-card p-6 hover:shadow-2xl transition-all duration-300 bg-white/10 backdrop-blur-lg border border-white/20 hover:border-white/40"
            >
              <div class="grid md:grid-cols-6 gap-4 items-end">
                <div class="md:col-span-1">
                  <label class="block text-sm font-medium text-white/90 mb-2">{{ isRTL ? 'الاسم' : 'Nom' }}</label>
                  <input 
                    v-model="p.name" 
                    type="text"
                    class="agri-input-filter w-full"
                  />
                </div>
                <div class="md:col-span-1">
                  <label class="block text-sm font-medium text-white/90 mb-2">{{ isRTL ? 'الفئة' : 'Catégorie' }}</label>
                  <input 
                    v-model="p.category" 
                    type="text"
                    class="agri-input-filter w-full"
                  />
                </div>
                <div class="md:col-span-1">
                  <label class="block text-sm font-medium text-white/90 mb-2">{{ isRTL ? 'السعر' : 'Prix' }}</label>
                  <div class="relative">
                    <input 
                      v-model="p.price" 
                      type="number" 
                      step="0.01"
                      class="agri-input-filter w-full pl-7"
                    />
                    <span class="absolute left-2 top-1/2 -translate-y-1/2 text-white/60 text-xs">TND</span>
                  </div>
                </div>
                <div class="md:col-span-1">
                  <label class="block text-sm font-medium text-white/90 mb-2">{{ isRTL ? 'المخزون' : 'Stock' }}</label>
                  <input 
                    v-model="p.stock" 
                    type="number" 
                    step="1"
                    class="agri-input-filter w-full"
                  />
                </div>

                <div class="md:col-span-2 flex gap-2" :class="{ 'flex-row-reverse': isRTL }">
                  <button 
                    class="flex-1 px-4 py-3 bg-gradient-to-r from-agri-green/20 to-agri-green/30 hover:from-agri-green/30 hover:to-agri-green/40 border border-agri-green/30 text-white rounded-lg transition-all duration-300 flex items-center justify-center gap-2"
                    :class="{ 'flex-row-reverse': isRTL }"
                    @click="update(p)"
                  >
                    <span>💾</span>
                    <span>{{ isRTL ? 'حفظ' : 'Sauver' }}</span>
                  </button>
                  <button 
                    class="flex-1 px-4 py-3 bg-gradient-to-r from-red-500/20 to-red-500/30 hover:from-red-500/30 hover:to-red-500/40 border border-red-500/30 text-white rounded-lg transition-all duration-300 flex items-center justify-center gap-2"
                    :class="{ 'flex-row-reverse': isRTL }"
                    @click="del(p)"
                  >
                    <span>🗑️</span>
                    <span>{{ isRTL ? 'حذف' : 'Supprimer' }}</span>
                  </button>
                </div>
              </div>
              
              <!-- Informations supplémentaires -->
              <div class="mt-4 pt-4 border-t border-white/20">
                <div class="grid grid-cols-1 md:grid-cols-3 gap-4">
                  <div class="p-2 bg-white/5 rounded-lg">
                    <div class="text-xs text-white/60">{{ isRTL ? 'معرف المنتج' : 'ID Produit' }}</div>
                    <div class="text-sm text-white font-mono mt-1">{{ p.id }}</div>
                  </div>
                  <div class="p-2 bg-white/5 rounded-lg">
                    <div class="text-xs text-white/60">{{ isRTL ? 'تاريخ الإنشاء' : 'Date création' }}</div>
                    <div class="text-sm text-white mt-1">{{ p.created_at ? formatDate(p.created_at) : (isRTL ? 'غير متوفر' : 'Non disponible') }}</div>
                  </div>
                  <div class="p-2 bg-white/5 rounded-lg">
                    <div class="text-xs text-white/60">{{ isRTL ? 'الحالة' : 'Statut' }}</div>
                    <div class="text-sm text-white mt-1 flex items-center gap-2">
                      <span :class="p.is_active ? 'text-green-400' : 'text-gray-400'">●</span>
                      {{ p.is_active ? (isRTL ? 'نشط' : 'Actif') : (isRTL ? 'غير نشط' : 'Inactif') }}
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>

        <!-- Empty State -->
        <div 
          v-else-if="!loading && !error && items.length === 0" 
          class="agri-card p-12 text-center hover:shadow-2xl transition-all duration-300 bg-white/10 backdrop-blur-lg border border-white/20"
        >
          <div class="text-6xl mb-6 opacity-50">📦</div>
          <h3 class="text-2xl font-bold text-white mb-3">
            {{ isRTL ? 'لا توجد منتجات' : 'Aucun produit trouvé' }}
          </h3>
          <p class="text-white/80 mb-8 max-w-md mx-auto">
            {{ isRTL ? 'قم بإنشاء أول منتج باستخدام النموذج أعلاه' : 'Créez votre premier produit avec le formulaire ci-dessus' }}
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
import { computed, onMounted, reactive, ref, onUnmounted } from "vue";
import { useAuthStore } from "../../store/auth";
import { useI18n } from "vue-i18n";
import {
  adminListProducts,
  adminCreateProduct,
  adminUpdateProduct,
  adminDeleteProduct
} from "../../api/exports";

const auth = useAuthStore();
const { locale } = useI18n();

// Gestion de la langue
const lang = ref('fr');
const showLangDropdown = ref(false);
const langSelector = ref(null);

// Computed pour la direction RTL/LTR
const isRTL = computed(() => lang.value === 'ar');
const direction = computed(() => isRTL.value ? 'rtl' : 'ltr');
const langFlag = computed(() => lang.value === 'fr' ? '🇫🇷' : '🇹🇳');
const langLabel = computed(() => lang.value === 'fr' ? 'FR' : 'AR');

// Sidebar classes computed - position changes based on language
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

// Content classes computed - margins change based on language
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

// Fonctions de langue
function changeLanguage(newLang) {
  lang.value = newLang;
  locale.value = newLang;
  localStorage.setItem('lang', newLang);
  showLangDropdown.value = false;
  
  document.documentElement.dir = newLang === 'ar' ? 'rtl' : 'ltr';
  document.documentElement.lang = newLang;
}

function toggleLangDropdown() {
  showLangDropdown.value = !showLangDropdown.value;
}

function handleClickOutside(event) {
  if (langSelector.value && !langSelector.value.contains(event.target)) {
    showLangDropdown.value = false;
  }
}

// Données produits
const items = ref([]);
const loading = ref(false);
const saving = ref(false);
const error = ref("");
const msg = ref("");
const err = ref("");

const createForm = reactive({ 
  name: "", 
  category: "", 
  price: 0, 
  stock: 0 
});

// Formatage de date
function formatDate(dateString) {
  const date = new Date(dateString);
  return date.toLocaleDateString(lang.value === 'ar' ? 'ar-TN' : 'fr-FR', {
    day: '2-digit',
    month: '2-digit',
    year: 'numeric',
    hour: '2-digit',
    minute: '2-digit'
  });
}

// Chargement des produits
async function load() {
  loading.value = true;
  error.value = "";
  try {
    const res = await adminListProducts();
    items.value = (res.data || []).slice().sort((a, b) => (b.id || 0) - (a.id || 0));
  } catch (e) {
    error.value = lang.value === 'ar' 
      ? "غير قادر على تحميل المنتجات." 
      : "Impossible de charger les produits.";
    console.error("Erreur de chargement:", e);
  } finally {
    loading.value = false;
  }
}

// Création de produit
async function create() {
  msg.value = ""; 
  err.value = "";
  
  if (!createForm.name) { 
    err.value = lang.value === 'ar' ? "الاسم مطلوب" : "Nom obligatoire"; 
    return; 
  }
  
  saving.value = true;
  try {
    await adminCreateProduct({
      name: createForm.name,
      category: createForm.category || null,
      price: Number(createForm.price || 0),
      stock: Number(createForm.stock || 0)
    });
    
    msg.value = lang.value === 'ar' ? "تم إنشاء المنتج ✅" : "Produit créé ✅";
    createForm.name = ""; 
    createForm.category = ""; 
    createForm.price = 0; 
    createForm.stock = 0;
    await load();
  } catch (e) {
    err.value = lang.value === 'ar' 
      ? "خطأ في إنشاء المنتج." 
      : "Erreur création produit.";
    console.error("Erreur création:", e);
  } finally {
    saving.value = false;
  }
}

// Mise à jour de produit
async function update(p) {
  try {
    await adminUpdateProduct(p.id, {
      name: p.name,
      category: p.category || null,
      price: Number(p.price || 0),
      stock: Number(p.stock || 0),
      is_active: p.is_active !== false
    });
    
    // Feedback visuel
    alert(lang.value === 'ar' ? "تم حفظ المنتج ✅" : "Produit sauvegardé ✅");
  } catch (e) {
    alert(lang.value === 'ar' 
      ? "خطأ في تحديث المنتج." 
      : "Erreur update produit.");
    console.error("Erreur mise à jour:", e);
  }
}

// Suppression de produit
async function del(p) {
  if (!confirm(lang.value === 'ar' 
    ? "هل أنت متأكد من حذف هذا المنتج؟" 
    : "Supprimer ce produit ?")) return;
    
  try {
    await adminDeleteProduct(p.id);
    await load();
  } catch (e) {
    alert(lang.value === 'ar' 
      ? "خطأ في حذف المنتج." 
      : "Erreur suppression produit.");
    console.error("Erreur suppression:", e);
  }
}

onMounted(() => {
  const savedLang = localStorage.getItem('lang') || 'fr';
  lang.value = savedLang;
  locale.value = savedLang;
  
  document.documentElement.dir = savedLang === 'ar' ? 'rtl' : 'ltr';
  document.documentElement.lang = savedLang;
  
  document.addEventListener('click', handleClickOutside);
  load();
});

onUnmounted(() => {
  document.removeEventListener('click', handleClickOutside);
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

.agri-input-filter::placeholder {
  color: rgba(255, 255, 255, 0.5);
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

[dir="rtl"] .pl-7 {
  padding-left: 0;
  padding-right: 1.75rem;
}

[dir="rtl"] .left-2 {
  left: auto;
  right: 0.5rem;
}

[dir="rtl"] .ml-auto {
  margin-left: 0;
  margin-right: auto;
}

/* Responsive */
@media (max-width: 1024px) {
  .lg\:ml-72, .lg\:mr-72 {
    margin-left: 0 !important;
    margin-right: 0 !important;
  }
  
  .grid-cols-2, .grid-cols-3, .grid-cols-4 {
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

/* Style pour les inputs de prix */
[dir="rtl"] .agri-input-filter.pl-7 {
  padding-left: 0.75rem;
  padding-right: 1.75rem;
}
</style>