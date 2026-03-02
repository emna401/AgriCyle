<template>
  <div class="space-y-6">
    <!-- Header -->
    <div class="flex flex-col md:flex-row md:items-center justify-between gap-4">
      <div>
        <h1 class="text-2xl md:text-3xl font-bold text-gray-900">📚 Gestion des Bonnes Pratiques</h1>

      </div>
    </div>

    <!-- Stats -->
    <div class="grid grid-cols-1 sm:grid-cols-4 gap-4">
      <div class="bg-white rounded-xl shadow p-4">
        <div class="text-sm text-gray-600">Total</div>
        <div class="text-2xl font-bold text-gray-900">{{ items.length }}</div>
      </div>
      <div class="bg-white rounded-xl shadow p-4">
        <div class="text-sm text-gray-600">Avec vidéo</div>
        <div class="text-2xl font-bold text-agri-green">{{ items.filter(i => i.video_url).length }}</div>
      </div>
      <div class="bg-white rounded-xl shadow p-4">
        <div class="text-sm text-gray-600">Avec image</div>
        <div class="text-2xl font-bold text-blue-600">{{ items.filter(i => i.image).length }}</div>
      </div>
      <div class="bg-white rounded-xl shadow p-4">
        <div class="text-sm text-gray-600">Mis à jour</div>
        <div class="text-2xl font-bold text-yellow-600">{{ formatDate(new Date()) }}</div>
      </div>
    </div>

    <!-- Formulaire de création -->
    <div class="bg-white rounded-xl shadow overflow-hidden">
      <div class="px-6 py-4 border-b border-gray-200 bg-gradient-to-r from-agri-green/5 to-blue-50">
        <div class="flex items-center gap-3">
          <div class="p-2 bg-agri-green/10 rounded-lg">
            <span class="text-agri-green text-xl">➕</span>
          </div>
          <div>
            <h3 class="text-lg font-semibold text-gray-900">Ajouter une nouvelle bonne pratique</h3>
            <p class="text-sm text-gray-600">Remplissez le formulaire ci-dessous</p>
          </div>
        </div>
      </div>
      
      <form @submit.prevent="create" class="p-6">
        <div class="grid md:grid-cols-2 gap-6">
          <!-- Titres -->
          <div class="space-y-4">
            <div>
              <label class="block text-sm font-medium text-gray-700 mb-2">
                <span class="flex items-center gap-2">
                  🇫🇷 Titre Français *
                  <span class="text-xs bg-gray-100 text-gray-600 px-2 py-0.5 rounded">Obligatoire</span>
                </span>
              </label>
              <input
                v-model="createForm.title_fr"
                type="text"
                required
                placeholder="Ex: Irrigation efficace"
                class="w-full px-4 py-3 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-agri-green focus:border-transparent transition"
              >
            </div>
            
            <div>
              <label class="block text-sm font-medium text-gray-700 mb-2">
                <span class="flex items-center gap-2">
                  🇹🇳 Titre Arabe *
                  <span class="text-xs bg-gray-100 text-gray-600 px-2 py-0.5 rounded">Obligatoire</span>
                </span>
              </label>
              <input
                v-model="createForm.title_ar"
                type="text"
                required
                placeholder="مثال: الري الفعال"
                dir="rtl"
                class="w-full px-4 py-3 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-agri-green focus:border-transparent transition text-right"
              >
            </div>
          </div>
          
          <!-- Contenus -->
          <div class="md:col-span-2 grid md:grid-cols-2 gap-6">
            <div>
              <label class="block text-sm font-medium text-gray-700 mb-2">
                <span class="flex items-center gap-2">
                  🇫🇷 Description Française *
                  <span class="text-xs bg-gray-100 text-gray-600 px-2 py-0.5 rounded">Obligatoire</span>
                </span>
              </label>
              <textarea
                v-model="createForm.body_fr"
                rows="5"
                required
                placeholder="Décrivez la bonne pratique en français..."
                class="w-full px-4 py-3 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-agri-green focus:border-transparent transition resize-none"
              ></textarea>
              <p class="text-xs text-gray-500 mt-1">{{ createForm.body_fr.length }} caractères</p>
            </div>
            
            <div>
              <label class="block text-sm font-medium text-gray-700 mb-2">
                <span class="flex items-center gap-2">
                  🇹🇳 Description Arabe *
                  <span class="text-xs bg-gray-100 text-gray-600 px-2 py-0.5 rounded">Obligatoire</span>
                </span>
              </label>
              <textarea
                v-model="createForm.body_ar"
                rows="5"
                required
                placeholder="وصف الممارسة الجيدة باللغة العربية..."
                dir="rtl"
                class="w-full px-4 py-3 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-agri-green focus:border-transparent transition resize-none text-right"
              ></textarea>
              <p class="text-xs text-gray-500 mt-1 text-right">{{ createForm.body_ar.length }} حرف</p>
            </div>
          </div>
          
          <!-- Médias -->
          <div class="space-y-4">
            <div>
              <label class="block text-sm font-medium text-gray-700 mb-2">
                <span class="flex items-center gap-2">
                  🎬 URL Vidéo
                  <span class="text-xs bg-blue-100 text-blue-600 px-2 py-0.5 rounded">Optionnel</span>
                </span>
              </label>
              <input
                v-model="createForm.video_url"
                type="url"
                placeholder="https://youtube.com/..."
                class="w-full px-4 py-3 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-agri-green focus:border-transparent transition"
              >
              <p class="text-xs text-gray-500 mt-1">YouTube, Vimeo, ou autre lien vidéo</p>
            </div>
          </div>
          
          <!-- Image -->
          <div class="space-y-4">
            <div>
              <label class="block text-sm font-medium text-gray-700 mb-2">
                <span class="flex items-center gap-2">
                  🖼️ Image
                  <span class="text-xs bg-blue-100 text-blue-600 px-2 py-0.5 rounded">Optionnel</span>
                </span>
              </label>
              <div class="flex items-center gap-4">
                <div class="flex-1">
                  <input
                    type="file"
                    @change="onCreateFile"
                    accept="image/*"
                    class="w-full px-4 py-3 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-agri-green focus:border-transparent transition file:mr-4 file:py-2 file:px-4 file:rounded file:border-0 file:text-sm file:font-semibold file:bg-agri-green/10 file:text-agri-green hover:file:bg-agri-green/20"
                  >
                </div>
                <div v-if="createForm.imageFile" class="flex-shrink-0">
                  <div class="w-16 h-16 bg-gray-100 rounded-lg overflow-hidden">
                    <img 
                      :src="getImagePreview(createForm.imageFile)" 
                      alt="Preview" 
                      class="w-full h-full object-cover"
                    >
                  </div>
                </div>
              </div>
              <p class="text-xs text-gray-500 mt-1">JPG, PNG, GIF • Max 5MB</p>
            </div>
          </div>
        </div>
        
        <!-- Actions -->
        <div class="flex items-center justify-between mt-8 pt-6 border-t border-gray-200">
          <div class="space-y-1">
            <p class="text-sm text-gray-600">Prêt à publier ?</p>
            <p class="text-xs text-gray-500">Cette bonne pratique sera visible par tous les utilisateurs</p>
          </div>
          <button
            type="submit"
            :disabled="saving"
            class="px-6 py-3 bg-agri-green text-white font-medium rounded-lg hover:bg-agri-green-dark focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-agri-green disabled:opacity-50 disabled:cursor-not-allowed transition flex items-center gap-2"
          >
            <span v-if="saving" class="inline-block animate-spin">⟳</span>
            <span>{{ saving ? 'Création en cours...' : '➕ Créer la bonne pratique' }}</span>
          </button>
        </div>
        
        <!-- Messages -->
        <div v-if="msg" class="mt-4 p-4 bg-green-50 border border-green-200 rounded-lg">
          <div class="flex items-center gap-3">
            <span class="text-green-600">✅</span>
            <p class="text-sm text-green-700">{{ msg }}</p>
          </div>
        </div>
        
        <div v-if="err" class="mt-4 p-4 bg-red-50 border border-red-200 rounded-lg">
          <div class="flex items-center gap-3">
            <span class="text-red-600">❌</span>
            <p class="text-sm text-red-700">{{ err }}</p>
          </div>
        </div>
      </form>
    </div>

    <!-- Liste des bonnes pratiques -->
    <div class="bg-white rounded-xl shadow overflow-hidden">
      <div class="px-6 py-4 border-b border-gray-200 bg-gradient-to-r from-gray-50 to-gray-100">
        <div class="flex items-center justify-between">
          <div class="flex items-center gap-3">
            <div class="p-2 bg-gray-100 rounded-lg">
              <span class="text-gray-700 text-xl">📋</span>
            </div>
            <div>
              <h3 class="text-lg font-semibold text-gray-900">Liste des bonnes pratiques</h3>
              <p class="text-sm text-gray-600">{{ items.length }} élément(s) au total</p>
            </div>
          </div>
          
          <button
            @click="load"
            :disabled="loading"
            class="px-4 py-2 bg-white border border-gray-300 rounded-lg hover:bg-gray-50 text-sm font-medium transition-colors disabled:opacity-50 disabled:cursor-not-allowed flex items-center gap-2"
          >
            <span v-if="loading" class="inline-block animate-spin">⟳</span>
            <span>{{ loading ? 'Chargement...' : '🔄 Actualiser' }}</span>
          </button>
        </div>
      </div>
      
      <!-- Loading State -->
      <div v-if="loading" class="p-12 text-center">
        <div class="inline-block animate-spin rounded-full h-12 w-12 border-b-2 border-agri-green"></div>
        <p class="mt-4 text-gray-600">Chargement des bonnes pratiques...</p>
      </div>
      
      <!-- Error State -->
      <div v-else-if="error" class="p-8 text-center">
        <div class="inline-flex items-center justify-center w-16 h-16 bg-red-100 rounded-full mb-4">
          <span class="text-red-600 text-2xl">❌</span>
        </div>
        <p class="text-gray-700 font-medium">{{ error }}</p>
        <p class="text-sm text-gray-500 mt-1">Impossible de charger les données</p>
        <button
          @click="load"
          class="mt-4 px-4 py-2 bg-agri-green text-white rounded-lg hover:bg-agri-green-dark text-sm font-medium"
        >
          Réessayer
        </button>
      </div>
      
      <!-- Empty State -->
      <div v-else-if="items.length === 0" class="p-12 text-center">
        <div class="inline-flex items-center justify-center w-20 h-20 bg-gray-100 rounded-full mb-4">
          <span class="text-gray-400 text-3xl">📚</span>
        </div>
        <h4 class="text-lg font-medium text-gray-900">Aucune bonne pratique</h4>
        <p class="text-gray-600 mt-1">Commencez par en créer une en utilisant le formulaire ci-dessus</p>
      </div>
      
      <!-- List Items -->
      <div v-else class="divide-y divide-gray-200">
        <div
          v-for="gp in items"
          :key="gp.id"
          class="p-6 hover:bg-gray-50 transition-colors"
        >
          <div class="flex flex-col lg:flex-row lg:items-start gap-6">
            <!-- Image Preview -->
            <div class="lg:w-48 flex-shrink-0">
              <div class="aspect-video bg-gray-100 rounded-lg overflow-hidden">
                <div v-if="gp.image || gp._newImageFile" class="w-full h-full">
                  <img 
                    :src="gp._newImageFile ? getImagePreview(gp._newImageFile) : gp.image" 
                    :alt="gp.title_fr"
                    class="w-full h-full object-cover"
                  >
                </div>
                <div v-else class="w-full h-full flex items-center justify-center bg-gray-200">
                  <span class="text-gray-400 text-4xl">🖼️</span>
                </div>
              </div>
              
              <!-- Video Indicator -->
              <div v-if="gp.video_url" class="mt-2 flex items-center gap-2">
                <span class="text-red-500">▶️</span>
                <span class="text-xs text-gray-600 truncate">Vidéo disponible</span>
              </div>
              
              <!-- File Upload -->
              <div class="mt-3">
                <label class="block text-xs font-medium text-gray-700 mb-1">
                  Remplacer l'image
                </label>
                <input
                  type="file"
                  @change="(e)=>onEditFile(gp, e)"
                  accept="image/*"
                  class="w-full text-xs px-3 py-2 border border-gray-300 rounded focus:outline-none focus:ring-1 focus:ring-agri-green"
                >
              </div>
            </div>
            
            <!-- Content -->
            <div class="flex-1 space-y-4">
              <!-- Header -->
              <div class="flex flex-col sm:flex-row sm:items-start sm:justify-between gap-3">
                <div>
                  <div class="flex items-center gap-2">
                    <span class="px-2 py-1 bg-gray-100 text-gray-700 text-xs font-medium rounded">#{{ gp.id }}</span>
                    <span class="text-sm text-gray-500">{{ formatDate(gp.created_at) }}</span>
                  </div>
                  <h4 class="text-lg font-semibold text-gray-900 mt-1">{{ gp.title_fr }}</h4>
                  <h5 class="text-md font-medium text-gray-700 mt-1 text-right" dir="rtl">{{ gp.title_ar }}</h5>
                </div>
                
                <!-- Actions -->
                <div class="flex gap-2">
                  <button
                    @click="save(gp)"
                    class="px-4 py-2 bg-agri-green text-white text-sm font-medium rounded-lg hover:bg-agri-green-dark transition-colors flex items-center gap-2"
                  >
                    <span>💾</span>
                    <span>Sauvegarder</span>
                  </button>
                  <button
                    @click="del(gp)"
                    class="px-4 py-2 bg-red-100 text-red-700 text-sm font-medium rounded-lg hover:bg-red-200 transition-colors flex items-center gap-2"
                  >
                    <span>🗑️</span>
                    <span>Supprimer</span>
                  </button>
                </div>
              </div>
              
              <!-- Video URL -->
              <div v-if="gp.video_url" class="p-3 bg-blue-50 rounded-lg">
                <label class="block text-sm font-medium text-blue-700 mb-1">🎬 URL Vidéo</label>
                <input
                  v-model="gp.video_url"
                  type="url"
                  placeholder="https://..."
                  class="w-full px-3 py-2 border border-blue-200 rounded focus:outline-none focus:ring-1 focus:ring-blue-500 bg-white"
                >
                <a 
                  :href="gp.video_url" 
                  target="_blank" 
                  class="inline-block mt-1 text-xs text-blue-600 hover:text-blue-800 hover:underline"
                >
                  🔗 Ouvrir le lien
                </a>
              </div>
              
              <!-- Content Fields -->
              <div class="grid md:grid-cols-2 gap-4">
                <div>
                  <label class="block text-sm font-medium text-gray-700 mb-2">
                    <span class="flex items-center gap-2">
                      🇫🇷 Contenu Français
                    </span>
                  </label>
                  <textarea
                    v-model="gp.body_fr"
                    rows="6"
                    class="w-full px-3 py-2 border border-gray-300 rounded focus:outline-none focus:ring-1 focus:ring-agri-green resize-none"
                  ></textarea>
                  <p class="text-xs text-gray-500 mt-1">{{ gp.body_fr?.length || 0 }} caractères</p>
                </div>
                
                <div>
                  <label class="block text-sm font-medium text-gray-700 mb-2">
                    <span class="flex items-center gap-2">
                      🇹🇳 المحتوى العربي
                    </span>
                  </label>
                  <textarea
                    v-model="gp.body_ar"
                    rows="6"
                    dir="rtl"
                    class="w-full px-3 py-2 border border-gray-300 rounded focus:outline-none focus:ring-1 focus:ring-agri-green resize-none text-right"
                  ></textarea>
                  <p class="text-xs text-gray-500 mt-1 text-right">{{ gp.body_ar?.length || 0 }} حرف</p>
                </div>
              </div>
              
              <!-- Stats -->
              <div class="flex items-center gap-4 text-sm text-gray-500 pt-3 border-t border-gray-200">
                <div class="flex items-center gap-1">
                  <span>📅</span>
                  <span>Créé le {{ formatDate(gp.created_at) }}</span>
                </div>
                <div class="flex items-center gap-1">
                  <span>🖼️</span>
                  <span>{{ gp.image ? 'Avec image' : 'Pas d\'image' }}</span>
                </div>
                <div v-if="gp.video_url" class="flex items-center gap-1">
                  <span>🎬</span>
                  <span>Avec vidéo</span>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { onMounted, reactive, ref } from "vue";
import Card from "../../components/ui/Card.vue";
import Input from "../../components/ui/Input.vue";
import Button from "../../components/ui/Button.vue";
import {
  adminListGoodPractices,
  adminCreateGoodPractice,
  adminUpdateGoodPractice,
  adminDeleteGoodPractice
} from "../../api/exports";

const items = ref([]);
const loading = ref(false);
const saving = ref(false);
const error = ref("");

const msg = ref("");
const err = ref("");

const createForm = reactive({
  title_fr: "",
  title_ar: "",
  body_fr: "",
  body_ar: "",
  video_url: "",
  imageFile: null
});

function onCreateFile(e) {
  createForm.imageFile = e.target.files?.[0] || null;
}

function getImagePreview(file) {
  return file ? URL.createObjectURL(file) : null;
}

function onEditFile(gp, e) {
  gp._newImageFile = e.target.files?.[0] || null;
}

function formatDate(dateString) {
  if (!dateString) return 'N/A';
  try {
    const date = new Date(dateString);
    return date.toLocaleDateString('fr-FR', {
      day: '2-digit',
      month: 'short',
      year: 'numeric'
    });
  } catch {
    return dateString;
  }
}

async function load() {
  loading.value = true; 
  error.value = "";
  try {
    const res = await adminListGoodPractices();
    items.value = (res.data || []).slice().sort((a, b) => (b.id || 0) - (a.id || 0));
  } catch (e) {
    error.value = "Impossible de charger les données.";
    console.error("Erreur chargement:", e);
  } finally {
    loading.value = false;
  }
}

async function create() {
  msg.value = ""; 
  err.value = "";
  
  // Validation
  if (!createForm.title_fr.trim() || !createForm.title_ar.trim() || 
      !createForm.body_fr.trim() || !createForm.body_ar.trim()) {
    err.value = "Tous les champs obligatoires doivent être remplis";
    return;
  }
  
  saving.value = true;
  try {
    const fd = new FormData();
    fd.append("title_fr", createForm.title_fr.trim());
    fd.append("title_ar", createForm.title_ar.trim());
    fd.append("body_fr", createForm.body_fr.trim());
    fd.append("body_ar", createForm.body_ar.trim());
    if (createForm.video_url.trim()) fd.append("video_url", createForm.video_url.trim());
    if (createForm.imageFile) fd.append("image", createForm.imageFile);

    await adminCreateGoodPractice(fd);
    msg.value = "✅ Bonne pratique créée avec succès";

    // Reset form
    createForm.title_fr = "";
    createForm.title_ar = "";
    createForm.body_fr = "";
    createForm.body_ar = "";
    createForm.video_url = "";
    createForm.imageFile = null;

    await load();
  } catch (e) {
    err.value = "❌ Erreur lors de la création: " + (e.response?.data?.detail || e.message);
    console.error("Erreur création:", e);
  } finally {
    saving.value = false;
  }
}

async function save(gp) {
  try {
    const fd = new FormData();
    fd.append("title_fr", gp.title_fr.trim());
    fd.append("title_ar", gp.title_ar.trim());
    fd.append("body_fr", gp.body_fr.trim());
    fd.append("body_ar", gp.body_ar.trim());
    fd.append("video_url", gp.video_url?.trim() || "");
    if (gp._newImageFile) fd.append("image", gp._newImageFile);

    await adminUpdateGoodPractice(gp.id, fd);
    alert("✅ Changements sauvegardés avec succès");
    gp._newImageFile = null;
    await load();
  } catch (e) {
    alert("❌ Erreur lors de la sauvegarde: " + (e.response?.data?.detail || e.message));
    console.error("Erreur sauvegarde:", e);
  }
}

async function del(gp) {
  if (!confirm(`Êtes-vous sûr de vouloir supprimer "${gp.title_fr}" ?\nCette action est irréversible.`)) return;
  try {
    await adminDeleteGoodPractice(gp.id);
    await load();
  } catch (e) {
    alert("❌ Erreur lors de la suppression: " + (e.response?.data?.detail || e.message));
    console.error("Erreur suppression:", e);
  }
}

onMounted(load);
</script>

<style scoped>
/* Custom scrollbar */
textarea::-webkit-scrollbar {
  width: 6px;
}

textarea::-webkit-scrollbar-track {
  background: #f1f1f1;
  border-radius: 3px;
}

textarea::-webkit-scrollbar-thumb {
  background: #c1c1c1;
  border-radius: 3px;
}

textarea::-webkit-scrollbar-thumb:hover {
  background: #a1a1a1;
}

/* Smooth transitions */
.transition {
  transition: all 0.2s ease-in-out;
}

/* Focus styles */
input:focus, textarea:focus, select:focus {
  outline: none;
  box-shadow: 0 0 0 3px rgba(34, 197, 94, 0.1);
}

/* Animation for loading spinner */
@keyframes spin {
  to { transform: rotate(360deg); }
}

.animate-spin {
  animation: spin 1s linear infinite;
}
</style>