<template>
  <div class="relative min-h-screen">
    <!-- Image d'arrière-plan fixe -->
    <div 
      class="fixed inset-0 bg-cover bg-center bg-no-repeat"
      style="background-image: url('https://images.unsplash.com/photo-1542601906990-b4d3fb778b09?ixlib=rb-4.0.3&auto=format&fit=crop&w=2000&q=80')"
    >
      <!-- Overlay sombre pour améliorer la lisibilité -->
      <div class="absolute inset-0 bg-black/40"></div>
    </div>
    
    <!-- Contenu par-dessus l'image -->
    <div class="relative z-10 min-h-screen flex items-center justify-center px-4 py-8">
      <div class="w-full max-w-md">
        <!-- Carte d'inscription -->
        <div class="bg-white/10 backdrop-blur-xl p-8 rounded-3xl shadow-2xl border border-white/30">
          <!-- Titre et sous-titre -->
          <div class="text-center mb-8">
            <h1 class="text-3xl font-bold text-white mb-2">
              Inscription
            </h1>
            <p class="text-white/90">
              Créer un compte AgriCycle
            </p>
          </div>

          <!-- Navigation -->
          <div class="flex justify-between items-center mb-6">
            <button @click="goBack" class="text-sm text-white/80 hover:text-white hover:underline flex items-center">
              <svg class="w-4 h-4 mr-1" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 19l-7-7m0 0l7-7m-7 7h18" />
              </svg>
              Retour
            </button>

            <router-link to="/login" class="text-sm text-white/80 hover:text-agri-green-light hover:underline">
              J'ai déjà un compte
            </router-link>
          </div>

          <!-- Formulaire d'inscription -->
          <form @submit.prevent="onRegister" class="space-y-6">
            <!-- Nom d'utilisateur -->
            <div>
              <label class="block text-white/90 text-sm font-medium mb-2">
                Nom utilisateur *
              </label>
              <input
                v-model="username"
                type="text"
                placeholder="ex: ahmed"
                :class="['w-full px-4 py-3 bg-white/10 backdrop-blur-sm border rounded-lg text-white placeholder-white/50 focus:outline-none focus:ring-2 focus:ring-agri-green-light', 
                        fieldErrors.username ? 'border-red-400' : 'border-white/20']"
              />
              <p v-if="fieldErrors.username" class="text-red-300 text-sm mt-1">
                {{ fieldErrors.username }}
              </p>
            </div>

            <!-- Téléphone -->
            <div>
              <label class="block text-white/90 text-sm font-medium mb-2">
                Téléphone *
              </label>
              <input
                v-model="phone"
                type="tel"
                placeholder="+216 XX XXX XXX"
                :class="['w-full px-4 py-3 bg-white/10 backdrop-blur-sm border rounded-lg text-white placeholder-white/50 focus:outline-none focus:ring-2 focus:ring-agri-green-light', 
                        fieldErrors.phone ? 'border-red-400' : 'border-white/20']"
              />
              <p v-if="fieldErrors.phone" class="text-red-300 text-sm mt-1">
                {{ fieldErrors.phone }}
              </p>
            </div>

            <!-- Email -->
            <div>
              <label class="block text-white/90 text-sm font-medium mb-2">
                Email *
              </label>
              <input
                v-model="email"
                type="email"
                placeholder="email@example.com"
                :class="['w-full px-4 py-3 bg-white/10 backdrop-blur-sm border rounded-lg text-white placeholder-white/50 focus:outline-none focus:ring-2 focus:ring-agri-green-light', 
                        fieldErrors.email ? 'border-red-400' : 'border-white/20']"
              />
              <p v-if="fieldErrors.email" class="text-red-300 text-sm mt-1">
                {{ fieldErrors.email }}
              </p>
            </div>

            <!-- Mot de passe -->
            <div>
              <label class="block text-white/90 text-sm font-medium mb-2">
                Mot de passe *
              </label>
              <input
                v-model="password"
                type="password"
                placeholder="••••••"
                :class="['w-full px-4 py-3 bg-white/10 backdrop-blur-sm border rounded-lg text-white placeholder-white/50 focus:outline-none focus:ring-2 focus:ring-agri-green-light', 
                        fieldErrors.password ? 'border-red-400' : 'border-white/20']"
              />
              <div v-if="fieldErrors.password" class="text-red-300 text-sm mt-1 space-y-1">
                <p v-for="(msg, index) in fieldErrors.password" :key="index">• {{ msg }}</p>
              </div>
            </div>

            <!-- Rôle -->
            <div>
              <label class="block text-white/90 text-sm font-medium mb-3">
                Choisir le profil *
              </label>
              <div class="grid grid-cols-3 gap-2">
                <button
                  type="button"
                  :class="['py-3 rounded-lg border text-sm font-medium transition-all duration-300',
                          role==='FARMER' 
                            ? 'bg-agri-green-light/20 border-agri-green-light text-white shadow-lg scale-105' 
                            : 'bg-white/10 border-white/20 text-white/90 hover:bg-white/20']"
                  @click="role='FARMER'"
                >
                  Farmer
                </button>

                <button
                  type="button"
                  :class="['py-3 rounded-lg border text-sm font-medium transition-all duration-300',
                          role==='BENEFICIARY' 
                            ? 'bg-agri-green-light/20 border-agri-green-light text-white shadow-lg scale-105' 
                            : 'bg-white/10 border-white/20 text-white/90 hover:bg-white/20']"
                  @click="role='BENEFICIARY'"
                >
                  Beneficiary
                </button>

                <button
                  type="button"
                  :class="['py-3 rounded-lg border text-sm font-medium transition-all duration-300',
                          role==='DUAL' 
                            ? 'bg-agri-green-light/20 border-agri-green-light text-white shadow-lg scale-105' 
                            : 'bg-white/10 border-white/20 text-white/90 hover:bg-white/20']"
                  @click="role='DUAL'"
                >
                  Dual
                </button>
              </div>
              <p v-if="fieldErrors.role" class="text-red-300 text-sm mt-1">
                {{ fieldErrors.role }}
              </p>
            </div>

            <!-- Ville -->
            <div>
              <label class="block text-white/90 text-sm font-medium mb-3">
                Choisir la ville *
              </label>
              <select 
                v-model="city"
                :class="['w-full px-4 py-3 bg-white/10 backdrop-blur-sm border rounded-lg text-white focus:outline-none focus:ring-2 focus:ring-agri-green-light',
                        fieldErrors.city ? 'border-red-400' : 'border-white/20']"
              >
                <option value="" disabled class="bg-gray-800">Choisir une ville</option>
                <option v-for="(cityOption, index) in cities" :key="index" :value="cityOption" class="bg-gray-800">
                  {{ cityOption }}
                </option>
              </select>
              <p v-if="fieldErrors.city" class="text-red-300 text-sm mt-1">
                {{ fieldErrors.city }}
              </p>
            </div>

            <!-- Message de succès -->
            <div v-if="ok" class="p-4 bg-green-500/20 backdrop-blur-sm border border-green-400/30 rounded-lg">
              <p class="text-green-200 text-sm">{{ ok }}</p>
            </div>

            <!-- Message d'erreur global -->
            <div v-if="error" class="p-4 bg-red-500/20 backdrop-blur-sm border border-red-400/30 rounded-lg">
              <p class="text-red-200 text-sm">{{ error }}</p>
            </div>

            <!-- Bouton d'inscription -->
            <button
              type="submit"
              :disabled="loading"
              :class="['w-full py-4 rounded-xl font-semibold text-lg transition-all duration-300',
                      loading 
                        ? 'bg-gray-400 cursor-not-allowed' 
                        : 'agri-btn-header hover:scale-[1.02]']"
            >
              {{ loading ? "Création en cours..." : "Créer le compte" }}
            </button>

            <!-- Note -->
            <p class="text-xs text-white/60 text-center">
              * Champs obligatoires
            </p>
          </form>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, reactive } from "vue";
import { useRouter } from "vue-router";
import { register } from "../../api/exports";

const router = useRouter();

const username = ref("");
const phone = ref("");
const email = ref("");
const password = ref("");
const role = ref("FARMER");
const city = ref("");

// Liste des villes de Tunisie
const cities = [
  "Tunis", "Sfax", "Sousse", "Ariana", "Bizerte", "Gabès", "Kairouan", "Kasserine",
  "Kebili", "Mahdia", "Manouba", "Medenine", "Monastir", "Nabeul", "Tataouine", 
  "Tozeur", "Zaghouan", "Jendouba", "Beja", "Gafsa", "Siliana", "Sidi Bouzid", 
  "Ben Arous", "El Kef", "La Manouba"
];

const loading = ref(false);
const error = ref("");
const ok = ref("");
const fieldErrors = reactive({
  username: "",
  phone: "",
  email: "",
  password: "",
  role: "",
  city: ""
});

function goBack() {
  router.push("/");
}

function clearErrors() {
  error.value = "";
  ok.value = "";
  Object.keys(fieldErrors).forEach(key => {
    fieldErrors[key] = "";
  });
}

async function onRegister() {
  clearErrors();
  loading.value = true;

  // Validation frontend basique
  let hasFrontendErrors = false;
  
  if (!username.value.trim()) {
    fieldErrors.username = "Le nom d'utilisateur est requis";
    hasFrontendErrors = true;
  }
  
  if (!phone.value.trim()) {
    fieldErrors.phone = "Le téléphone est requis";
    hasFrontendErrors = true;
  }
  
  if (!email.value.trim()) {
    fieldErrors.email = "L'email est requis";
    hasFrontendErrors = true;
  } else if (!/\S+@\S+\.\S+/.test(email.value)) {
    fieldErrors.email = "Veuillez entrer un email valide";
    hasFrontendErrors = true;
  }
  
  if (!password.value) {
    fieldErrors.password = "Le mot de passe est requis";
    hasFrontendErrors = true;
  } else if (password.value.length < 6) {
    fieldErrors.password = "Mot de passe trop court (min 6 caractères)";
    hasFrontendErrors = true;
  }

  if (!city.value) {
    fieldErrors.city = "La ville est requise";
    hasFrontendErrors = true;
  }

  if (hasFrontendErrors) {
    loading.value = false;
    return;
  }

  try {
    await register({
      username: username.value.trim(),
      phone: phone.value.trim(),
      email: email.value.trim().toLowerCase(),
      password: password.value,
      role: role.value,
      city: city.value
    });

    ok.value = "✅ Compte créé avec succès ! Redirection vers la connexion...";
    
    // Vider le formulaire
    username.value = "";
    phone.value = "";
    email.value = "";
    password.value = "";
    role.value = "FARMER";
    city.value = "";
    
    // Redirection après 2 secondes
    setTimeout(() => router.push("/login"), 2000);
    
  } catch (err) {
    const backendData = err?.response?.data;
    
    if (backendData?.errors) {
      Object.keys(backendData.errors).forEach(key => {
        if (fieldErrors[key] !== undefined) {
          fieldErrors[key] = Array.isArray(backendData.errors[key]) 
            ? backendData.errors[key][0] 
            : backendData.errors[key];
        }
      });
      
      if (backendData.errors.city) {
        fieldErrors.city = Array.isArray(backendData.errors.city) 
          ? backendData.errors.city[0] 
          : backendData.errors.city;
      }
    } else {
      error.value = backendData?.detail || 
                    backendData?.message || 
                    "Erreur lors de l'inscription. Veuillez réessayer.";
    }
  } finally {
    loading.value = false;
  }
}
</script>

<style scoped>
/* Assurer que l'image couvre toute la page */
.fixed {
  position: fixed;
}

.inset-0 {
  top: 0;
  right: 0;
  bottom: 0;
  left: 0;
}

/* Centrage vertical et horizontal */
.min-h-screen {
  min-height: 100vh;
}

.flex.items-center.justify-center {
  display: flex;
  align-items: center;
  justify-content: center;
}

/* Couleur verte claire */
.text-agri-green-light {
  color: #68d391;
}

/* Styles pour les boutons */
.agri-btn-header {
  background: linear-gradient(135deg, #48bb78 0%, #2f855a 100%);
  color: white;
  border-radius: 12px;
  transition: all 0.3s ease;
  border: none;
  cursor: pointer;
  font-weight: 600;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  box-shadow: 0 10px 25px rgba(72, 187, 120, 0.3);
}

.agri-btn-header:hover:not(:disabled) {
  transform: translateY(-3px);
  box-shadow: 0 15px 35px rgba(72, 187, 120, 0.4);
  background: linear-gradient(135deg, #5cc489 0%, #3a9a6b 100%);
}

/* Effet de texte avec ombre */
.text-white {
  text-shadow: 0 1px 2px rgba(0, 0, 0, 0.3);
}

/* Placeholder blanc */
::placeholder {
  color: rgba(255, 255, 255, 0.5);
}

/* Style pour les options du select */
select option {
  background-color: #1f2937;
  color: white;
}

select option:checked {
  background-color: #48bb78;
  color: white;
}

/* Focus styles */
input:focus, select:focus {
  outline: none;
  box-shadow: 0 0 0 3px rgba(104, 211, 145, 0.3);
}

/* Style pour les boutons de rôle */
.border-agri-green-light {
  border-color: #68d391;
}

.bg-agri-green-light\/20 {
  background-color: rgba(104, 211, 145, 0.2);
}

/* Responsive */
@media (max-width: 640px) {
  .max-w-md {
    max-width: 100%;
  }
  
  .p-8 {
    padding: 1.5rem;
  }
  
  .grid-cols-3 {
    grid-template-columns: repeat(3, minmax(0, 1fr));
  }
  
  .text-3xl {
    font-size: 1.75rem;
  }
  
  .space-y-6 > * + * {
    margin-top: 1rem;
  }
}
</style>