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
        <!-- Carte de connexion -->
        <div class="bg-white/10 backdrop-blur-xl p-8 rounded-3xl shadow-2xl border border-white/30">
          <!-- Titre et sous-titre -->
          <div class="text-center mb-8">
            <h1 class="text-3xl font-bold text-white mb-2">
              Connexion
            </h1>
            <p class="text-white/90">
              Accès sécurisé à votre espace AgriCycle
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
            <router-link to="/register" class="text-sm text-white/80 hover:text-agri-green-light hover:underline">
              Créer un compte
            </router-link>
          </div>

          <!-- Formulaire de connexion -->
          <form @submit.prevent="onLogin" class="space-y-6">
            <!-- Identifiant (email ou téléphone) -->
            <div>
              <label class="block text-white/90 text-sm font-medium mb-2">
                Email ou Téléphone *
              </label>
              <input
                v-model="identifier"
                type="text"
                placeholder="email@example.com ou +216 XX XXX XXX"
                :class="['w-full px-4 py-3 bg-white/10 backdrop-blur-sm border rounded-lg text-white placeholder-white/50 focus:outline-none focus:ring-2 focus:ring-agri-green-light', 
                        error ? 'border-red-400' : 'border-white/20']"
              />
            </div>

            <!-- Mot de passe -->
            <div>
              <div class="flex justify-between items-center mb-2">
                <label class="block text-white/90 text-sm font-medium">
                  Mot de passe *
                </label>
                <router-link to="/forgot-password" class="text-xs text-white/80 hover:text-agri-green-light hover:underline">
                  Mot de passe oublié ?
                </router-link>
              </div>
              <input
                v-model="password"
                type="password"
                placeholder="••••••••"
                :class="['w-full px-4 py-3 bg-white/10 backdrop-blur-sm border rounded-lg text-white placeholder-white/50 focus:outline-none focus:ring-2 focus:ring-agri-green-light', 
                        error ? 'border-red-400' : 'border-white/20']"
              />
            </div>

            <!-- Message d'erreur -->
            <div v-if="error" class="p-4 bg-red-500/20 backdrop-blur-sm border border-red-400/30 rounded-lg">
              <p class="text-red-200 text-sm text-center">{{ error }}</p>
            </div>

            <!-- Bouton de connexion -->
            <button
              type="submit"
              :disabled="loading"
              :class="['w-full py-4 rounded-xl font-semibold text-lg transition-all duration-300',
                      loading 
                        ? 'bg-gray-400 cursor-not-allowed' 
                        : 'agri-btn-header hover:scale-[1.02]']"
            >
              {{ loading ? "Connexion..." : "Se connecter" }}
            </button>

            <!-- Séparateur -->
            <div class="relative flex items-center justify-center">
              <div class="flex-grow border-t border-white/20"></div>
              <span class="mx-4 text-white/60 text-sm">Ou</span>
              <div class="flex-grow border-t border-white/20"></div>
            </div>

            <!-- Options supplémentaires -->
            <div class="text-center">
              <p class="text-white/70 text-sm mb-4">
                Nouveau sur AgriCycle ?
              </p>
              <router-link 
                to="/register" 
                class="inline-block w-full py-3 rounded-lg border-2 border-white text-white font-medium hover:bg-white hover:text-agri-green-dark transition-all duration-300"
              >
                Créer un nouveau compte
              </router-link>
            </div>
          </form>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from "vue";
import { useRouter } from "vue-router";
import { useAuthStore } from "../../store/auth";
import { login } from "../../api/exports";

const router = useRouter();
const auth = useAuthStore();

const identifier = ref("");  // identifier peut être email ou téléphone
const password = ref("");
const error = ref("");
const loading = ref(false);

function goBack() {
  router.push("/");
}

async function onLogin() {
  error.value = "";
  loading.value = true;
  
  // Frontend validation
  if (!identifier.value || !password.value) {
    error.value = "Veuillez remplir tous les champs";
    loading.value = false;
    return;
  }

  try {
    // Connexion avec identifier qui peut être email ou téléphone
    const res = await login({ identifier: identifier.value, password: password.value });
    auth.setTokens(res.data);
    await auth.fetchMe();

    const role = auth.user.role;
    if (role === "FARMER") return router.push("/app/farmer");
    if (role === "BENEFICIARY") return router.push("/app/beneficiary");
    if (role === "DUAL") return router.push("/app/dual");
    if (role === "ADMIN" || role === "SUPERADMIN") return router.push("/app/admin");

    router.push("/app/profile");
  } catch (e) {
    console.log("LOGIN ERROR:", e?.response?.status, e?.response?.data);
    error.value = e?.response?.data?.detail || e?.response?.data?.message || "Erreur de connexion";
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

.text-agri-green-dark {
  color: #2f855a;
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

/* Focus styles */
input:focus {
  outline: none;
  box-shadow: 0 0 0 3px rgba(104, 211, 145, 0.3);
}

/* Style pour le lien "Créer un compte" */
.border-white {
  border-color: rgba(255, 255, 255, 0.5);
}

.border-white:hover {
  background-color: white;
}

/* Responsive */
@media (max-width: 640px) {
  .max-w-md {
    max-width: 100%;
  }
  
  .p-8 {
    padding: 1.5rem;
  }
  
  .text-3xl {
    font-size: 1.75rem;
  }
  
  .space-y-6 > * + * {
    margin-top: 1rem;
  }
  
  .py-4 {
    padding-top: 1rem;
    padding-bottom: 1rem;
  }
  
  .py-3 {
    padding-top: 0.75rem;
    padding-bottom: 0.75rem;
  }
}
</style>