<template>
  <!-- Image d'arrière-plan fixe (même que la page d'accueil) -->
  <div 
    class="fixed inset-0 bg-cover bg-center bg-no-repeat"
    style="background-image: url('https://images.unsplash.com/photo-1542601906990-b4d3fb778b09?ixlib=rb-4.0.3&auto=format&fit=crop&w=2000&q=80')"
  >
    <!-- Overlay sombre pour améliorer la lisibilité -->
    <div class="absolute inset-0 bg-black/40"></div>
  </div>
  
  <!-- Contenu par-dessus l'image -->
  <div class="relative z-10 min-h-screen flex flex-col">
    <!-- 🌱 SECTION 1 — Header Hero avec style verre -->
    <header class="relative py-16 px-4 overflow-hidden">
      <div class="max-w-4xl mx-auto text-center relative z-10">
        <div class="inline-flex items-center justify-center gap-3 mb-6">
          <div class="p-3 bg-gradient-to-r from-agri-green to-agri-green-dark rounded-2xl shadow-lg backdrop-blur-lg border border-white/20">
            <span class="text-2xl">🌱</span>
          </div>
          <h1 class="text-3xl md:text-4xl font-bold text-white">
            Bonnes Pratiques AgriCycle
          </h1>
        </div>
        <p class="text-lg md:text-xl text-white/90 max-w-2xl mx-auto leading-relaxed mb-8">
          Adopter les bons gestes pour protéger<br>
          votre santé, vos terres et l'environnement.
        </p>
      </div>
    </header>

    <!-- 🎥 SECTION 2 — Vidéo locale avec style verre -->
    <section class="py-12 px-4">
      <div class="max-w-4xl mx-auto">
        <div class="bg-white/10 backdrop-blur-lg rounded-2xl p-8 border border-white/20 shadow-2xl">
          <!-- Zone vidéo -->
          <div class="aspect-video bg-gray-900/50 rounded-2xl overflow-hidden relative border-2 border-white/20">
            <!-- Loading -->
            <div
              v-if="videoLoading && !videoError"
              class="absolute inset-0 flex items-center justify-center bg-gray-900/50"
            >
              <div class="animate-spin rounded-full h-12 w-12 border-4 border-agri-green-light border-t-transparent"></div>
              <span class="ml-3 text-white">Chargement de la vidéo...</span>
            </div>

            <!-- Error -->
            <div
              v-if="videoError"
              class="absolute inset-0 flex flex-col items-center justify-center bg-gray-900/50 text-center p-6"
            >
              <div class="text-6xl mb-4">⚠️</div>
              <p class="text-white font-semibold">{{ videoError }}</p>
              <p class="text-white/80 mt-2">Chemin: src/assets/videos/AgriCycle.mp4</p>
            </div>

            <!-- Video -->
            <video
              v-show="!videoError"
              :src="videoUrl"
              controls
              class="w-full h-full object-cover"
              preload="metadata"
              poster="https://images.unsplash.com/photo-1500382017468-9049fed747ef?auto=format&fit=crop&w=1200&q=80"
              @loadeddata="videoLoading = false"
              @error="handleVideoError"
            >
              Votre navigateur ne supporte pas la vidéo.
            </video>
          </div>
        </div>
      </div>
    </section>

    <!-- 🚜 SECTION 3 — Pour les AGRICULTEURS avec style verre -->
    <section class="py-16 px-4">
      <div class="max-w-6xl mx-auto">
        <div class="text-center mb-12">
          <div class="inline-flex items-center gap-3 mb-4">
            <span class="text-4xl">🚜</span>
            <h2 class="text-3xl font-bold text-white">
              Bonnes pratiques pour les agriculteurs
            </h2>
          </div>
          <p class="text-white/80 max-w-2xl mx-auto">
            Des gestes simples pour une utilisation responsable des produits phytosanitaires
          </p>
        </div>

        <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6 mb-16">
          <div class="agri-card bg-white/10 backdrop-blur-lg rounded-2xl p-6 border border-white/20 hover:shadow-2xl transition-all group">
            <div class="text-4xl mb-4 group-hover:scale-110 transition-transform">🧴</div>
            <h3 class="text-xl font-bold text-white mb-3">Utilisation des pesticides</h3>
            <ul class="space-y-2">
              <li class="flex items-start gap-2">
                <span class="text-agri-green-light mt-1 text-lg">✓</span>
                <span class="text-white/90">Lire attentivement l'étiquette</span>
              </li>
              <li class="flex items-start gap-2">
                <span class="text-agri-green-light mt-1 text-lg">✓</span>
                <span class="text-white/90">Respecter les doses recommandées</span>
              </li>
              <li class="flex items-start gap-2">
                <span class="text-agri-green-light mt-1 text-lg">✓</span>
                <span class="text-white/90">Porter les équipements de protection</span>
              </li>
              <li class="flex items-start gap-2">
                <span class="text-agri-green-light mt-1 text-lg">✓</span>
                <span class="text-white/90">Ne pas traiter par vent fort</span>
              </li>
            </ul>
          </div>

          <div class="agri-card bg-white/10 backdrop-blur-lg rounded-2xl p-6 border border-white/20 hover:shadow-2xl transition-all group">
            <div class="text-4xl mb-4 group-hover:scale-110 transition-transform">🧼</div>
            <h3 class="text-xl font-bold text-white mb-3">Nettoyage du matériel</h3>
            <ul class="space-y-2">
              <li class="flex items-start gap-2">
                <span class="text-agri-green-light mt-1 text-lg">✓</span>
                <span class="text-white/90">Nettoyer après chaque utilisation</span>
              </li>
              <li class="flex items-start gap-2">
                <span class="text-agri-green-light mt-1 text-lg">✓</span>
                <span class="text-white/90">Utiliser les zones de lavage désignées</span>
              </li>
              <li class="flex items-start gap-2">
                <span class="text-agri-green-light mt-1 text-lg">✓</span>
                <span class="text-white/90">Éviter la contamination des sols</span>
              </li>
              <li class="flex items-start gap-2">
                <span class="text-agri-green-light mt-1 text-lg">✓</span>
                <span class="text-white/90">Stockage dans local ventilé</span>
              </li>
            </ul>
          </div>

          <div class="agri-card bg-white/10 backdrop-blur-lg rounded-2xl p-6 border border-white/20 hover:shadow-2xl transition-all group">
            <div class="text-4xl mb-4 group-hover:scale-110 transition-transform">🏷️</div>
            <h3 class="text-xl font-bold text-white mb-3">Tri des emballages</h3>
            <ul class="space-y-2">
              <li class="flex items-start gap-2">
                <span class="text-agri-green-light mt-1 text-lg">✓</span>
                <span class="text-white/90">Séparer les plastiques et cartons</span>
              </li>
              <li class="flex items-start gap-2">
                <span class="text-agri-green-light mt-1 text-lg">✓</span>
                <span class="text-white/90">Vider complètement les contenants</span>
              </li>
              <li class="flex items-start gap-2">
                <span class="text-agri-green-light mt-1 text-lg">✓</span>
                <span class="text-white/90">Apporter aux points de collecte AgriCycle</span>
              </li>
              <li class="flex items-start gap-2">
                <span class="text-agri-green-light mt-1 text-lg">✓</span>
                <span class="text-white/90">Ne pas brûler les emballages</span>
              </li>
            </ul>
          </div>
        </div>

        <!-- Timeline des étapes de nettoyage avec style verre -->
        <div class="bg-white/10 backdrop-blur-lg rounded-3xl p-8 border border-white/20 shadow-2xl">
          <h3 class="text-2xl font-bold text-white mb-8 text-center">
            Étapes de nettoyage des bidons
          </h3>
          
          <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6">
            <div class="text-center group">
              <div class="w-16 h-16 bg-gradient-to-r from-agri-green to-agri-green-dark text-white text-2xl font-bold rounded-full flex items-center justify-center mx-auto mb-4 shadow-lg group-hover:scale-110 transition-transform">
                ①
              </div>
              <h4 class="text-lg font-semibold text-white mb-2">Rincer 4–5 fois</h4>
              <p class="text-white/80 text-sm">Vider le bidon et rincer abondamment à l'eau claire</p>
            </div>
            
            <div class="text-center group">
              <div class="w-16 h-16 bg-gradient-to-r from-agri-green to-agri-green-dark text-white text-2xl font-bold rounded-full flex items-center justify-center mx-auto mb-4 shadow-lg group-hover:scale-110 transition-transform">
                ②
              </div>
              <h4 class="text-lg font-semibold text-white mb-2">Eau dans pulvérisateur</h4>
              <p class="text-white/80 text-sm">Utiliser l'eau de rinçage pour traiter les cultures</p>
            </div>
            
            <div class="text-center group">
              <div class="w-16 h-16 bg-gradient-to-r from-agri-green to-agri-green-dark text-white text-2xl font-bold rounded-full flex items-center justify-center mx-auto mb-4 shadow-lg group-hover:scale-110 transition-transform">
                ③
              </div>
              <h4 class="text-lg font-semibold text-white mb-2">Percer le bidon</h4>
              <p class="text-white/80 text-sm">Empêcher toute réutilisation dangereuse</p>
            </div>
            
            <div class="text-center group">
              <div class="w-16 h-16 bg-gradient-to-r from-agri-green to-agri-green-dark text-white text-2xl font-bold rounded-full flex items-center justify-center mx-auto mb-4 shadow-lg group-hover:scale-110 transition-transform">
                ④
              </div>
              <h4 class="text-lg font-semibold text-white mb-2">Dépôt au centre</h4>
              <p class="text-white/80 text-sm">Apporter au centre AgriCycle pour recyclage</p>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- 🤝 SECTION 4 — Pour les BÉNÉFICIAIRES avec style verre -->
    <section class="py-16 px-4">
      <div class="max-w-6xl mx-auto">
        <div class="text-center mb-12">
          <div class="inline-flex items-center gap-3 mb-4">
            <span class="text-4xl">🤝</span>
            <h2 class="text-3xl font-bold text-white">
              Bonnes pratiques pour les bénéficiaires
            </h2>
          </div>
          <p class="text-white/80 max-w-2xl mx-auto">
            Participer activement à la collecte et au recyclage responsable
          </p>
        </div>

        <div class="grid grid-cols-1 lg:grid-cols-3 gap-6">
          <div class="agri-card bg-white/10 backdrop-blur-lg rounded-2xl p-6 border border-white/20 hover:shadow-2xl transition-all">
            <div class="flex items-center gap-3 mb-4">
              <div class="p-3 bg-white/20 rounded-xl">
                <span class="text-2xl text-agri-green-light">📦</span>
              </div>
              <h3 class="text-xl font-bold text-white">Collecte responsable</h3>
            </div>
            <ul class="space-y-3">
              <li class="flex items-start gap-2">
                <span class="text-agri-green-light mt-1 text-lg">•</span>
                <span class="text-white/90">Vérifier la propreté des bidons</span>
              </li>
              <li class="flex items-start gap-2">
                <span class="text-agri-green-light mt-1 text-lg">•</span>
                <span class="text-white/90">Porter des gants de protection</span>
              </li>
              <li class="flex items-start gap-2">
                <span class="text-agri-green-light mt-1 text-lg">•</span>
                <span class="text-white/90">Refuser les bidons non percés</span>
              </li>
              <li class="flex items-start gap-2">
                <span class="text-agri-green-light mt-1 text-lg">•</span>
                <span class="text-white/90">Compter et peser les emballages</span>
              </li>
            </ul>
          </div>

          <div class="agri-card bg-white/10 backdrop-blur-lg rounded-2xl p-6 border border-white/20 hover:shadow-2xl transition-all">
            <div class="flex items-center gap-3 mb-4">
              <div class="p-3 bg-white/20 rounded-xl">
                <span class="text-2xl text-agri-green-light">🏭</span>
              </div>
              <h3 class="text-xl font-bold text-white">Stockage sécurisé</h3>
            </div>
            <ul class="space-y-3">
              <li class="flex items-start gap-2">
                <span class="text-agri-green-light mt-1 text-lg">•</span>
                <span class="text-white/90">Zone dédiée et ventilée</span>
              </li>
              <li class="flex items-start gap-2">
                <span class="text-agri-green-light mt-1 text-lg">•</span>
                <span class="text-white/90">À l'abri des enfants et animaux</span>
              </li>
              <li class="flex items-start gap-2">
                <span class="text-agri-green-light mt-1 text-lg">•</span>
                <span class="text-white/90">Protégé des intempéries</span>
              </li>
              <li class="flex items-start gap-2">
                <span class="text-agri-green-light mt-1 text-lg">•</span>
                <span class="text-white/90">Signalisation claire des dangers</span>
              </li>
            </ul>
          </div>

          <div class="agri-card bg-white/10 backdrop-blur-lg rounded-2xl p-6 border border-white/20 hover:shadow-2xl transition-all">
            <div class="flex items-center gap-3 mb-4">
              <div class="p-3 bg-white/20 rounded-xl">
                <span class="text-2xl text-agri-green-light">♻️</span>
              </div>
              <h3 class="text-xl font-bold text-white">Recyclage efficient</h3>
            </div>
            <ul class="space-y-3">
              <li class="flex items-start gap-2">
                <span class="text-agri-green-light mt-1 text-lg">•</span>
                <span class="text-white/90">Séparation par type de plastique</span>
              </li>
              <li class="flex items-start gap-2">
                <span class="text-agri-green-light mt-1 text-lg">•</span>
                <span class="text-white/90">Traitement selon les normes</span>
              </li>
              <li class="flex items-start gap-2">
                <span class="text-agri-green-light mt-1 text-lg">•</span>
                <span class="text-white/90">Transformation en nouvelles ressources</span>
              </li>
              <li class="flex items-start gap-2">
                <span class="text-agri-green-light mt-1 text-lg">•</span>
                <span class="text-white/90">Valorisation des matériaux recyclés</span>
              </li>
            </ul>
          </div>
        </div>
      </div>
    </section>

    <!-- ❓ SECTION 5 — FAQ avec style verre -->
    <section class="py-16 px-4">
      <div class="max-w-3xl mx-auto">
        <div class="text-center mb-12">
          <h2 class="text-3xl font-bold text-white mb-4">Questions fréquentes</h2>
          <p class="text-white/80">Trouvez les réponses à vos interrogations</p>
        </div>
        
        <div class="space-y-4">
          <div 
            v-for="(faq, index) in faqs" 
            :key="index"
            class="agri-card bg-white/10 backdrop-blur-lg rounded-xl p-6 border border-white/20 hover:shadow-2xl transition-all cursor-pointer"
            @click="toggleFAQ(index)"
          >
            <div class="flex items-center justify-between">
              <h3 class="font-bold text-white">{{ faq.question }}</h3>
              <span class="text-2xl text-agri-green-light">{{ expandedFAQ === index ? '−' : '+' }}</span>
            </div>
            <div v-show="expandedFAQ === index" class="mt-4 text-white/90">
              {{ faq.answer }}
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- 🌿 SECTION 6 — Message d'engagement avec style verre -->
    <section class="py-16 px-4">
      <div class="max-w-4xl mx-auto">
        <div class="agri-card bg-white/10 backdrop-blur-lg rounded-3xl p-12 border border-white/20 shadow-2xl text-center">
          <div class="text-6xl mb-6 animate-pulse text-agri-green-light">🌿</div>
          <h2 class="text-3xl md:text-4xl font-bold text-white mb-6">
            Ensemble pour une agriculture durable
          </h2>
          <p class="text-xl text-white/90 mb-8 max-w-2xl mx-auto leading-relaxed">
            Chaque geste compte.<br>
            AgriCycle transforme les déchets en ressources utiles pour tous.
          </p>
          <div class="flex flex-col sm:flex-row gap-4 justify-center">
            <button 
              @click="scrollToTop"
              class="agri-btn px-8 py-3 text-lg font-semibold"
            >
              ✅ J'ai compris les bonnes pratiques
            </button>
            <a 
              href="/"
              class="agri-btn-light px-8 py-3 text-lg font-semibold text-center"
            >
              ← Retour à l'accueil
            </a>
          </div>
        </div>
      </div>
    </section>

    <!-- Footer avec style verre -->
    <footer class="relative z-10 py-6 px-4 mt-auto">
      <div class="max-w-6xl mx-auto px-4">
        <div class="flex flex-col md:flex-row justify-between items-center">
          <div class="text-white/80 text-sm mb-4 md:mb-0">
            © {{ new Date().getFullYear() }} AgriCycle — Agriculture durable ♻️🌱
          </div>
        </div>
      </div>
    </footer>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import agriVideo from '../../assets/videos/AgriCycle.mp4';

// --------------------
// VIDEO
// --------------------
const videoUrl = ref(null);
const videoLoading = ref(true);
const videoError = ref(null);

onMounted(() => {
  videoUrl.value = agriVideo;
  videoLoading.value = true;
});

function handleVideoError(e) {
  videoLoading.value = false;
  videoError.value = "Impossible de charger la vidéo locale.";
  console.error("Erreur vidéo :", e);
}

// --------------------
// FAQ
// --------------------
const faqs = ref([
  {
    question: "Où puis-je déposer mes bidons vides ?",
    answer: "Vous pouvez déposer vos bidons vides dans l'un de nos centres de collecte AgriCycle."
  },
  {
    question: "Faut-il rincer les bidons avant de les déposer ?",
    answer: "Oui, 4 à 5 rinçages à l'eau claire sont obligatoires."
  },
  {
    question: "Pourquoi percer les bidons ?",
    answer: "Pour éviter toute réutilisation dangereuse."
  },
  {
    question: "Quels types d'emballages sont acceptés ?",
    answer: "Bidons plastiques, cartons, sachets et fûts métalliques."
  }
]);

const expandedFAQ = ref(null);

function toggleFAQ(index) {
  expandedFAQ.value = expandedFAQ.value === index ? null : index;
}

function scrollToTop() {
  window.scrollTo({ top: 0, behavior: 'smooth' });
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

/* Structure flex pour le footer en bas */
.flex-col {
  display: flex;
  flex-direction: column;
}

.flex-1 {
  flex: 1;
}

.min-h-screen {
  min-height: 100vh;
}

/* Couleurs personnalisées */
.text-agri-green-light {
  color: #68d391;
}

.bg-agri-green {
  background-color: #48bb78;
}

.bg-agri-green-dark {
  background-color: #2f855a;
}

.from-agri-green {
  --tw-gradient-from: #48bb78;
}

.to-agri-green-dark {
  --tw-gradient-to: #2f855a;
}

/* Styles pour les boutons (copiés de la page d'accueil) */
.agri-btn {
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

.agri-btn:hover {
  transform: translateY(-3px);
  box-shadow: 0 15px 35px rgba(72, 187, 120, 0.4);
  background: linear-gradient(135deg, #5cc489 0%, #3a9a6b 100%);
}

.agri-btn-light {
  border: 2px solid white;
  color: white;
  border-radius: 12px;
  transition: all 0.3s ease;
  background: transparent;
  font-weight: 600;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  box-shadow: 0 8px 20px rgba(255, 255, 255, 0.1);
}

.agri-btn-light:hover {
  background: white;
  color: #2f855a;
  transform: translateY(-3px);
  box-shadow: 0 15px 35px rgba(255, 255, 255, 0.2);
}

/* Styles pour les cartes avec effet de verre (copiés de la page d'accueil) */
.agri-card {
  transition: transform 0.4s ease, box-shadow 0.4s ease;
  border: 1px solid rgba(255, 255, 255, 0.2);
  backdrop-filter: blur(8px);
  -webkit-backdrop-filter: blur(8px);
}

.agri-card:hover {
  transform: translateY(-8px);
  box-shadow: 0 20px 40px rgba(0, 0, 0, 0.3);
  background: rgba(255, 255, 255, 0.15) !important;
}

/* Effet de texte avec ombre pour mieux ressortir */
.text-white {
  text-shadow: 0 2px 4px rgba(0, 0, 0, 0.3);
}

.font-bold {
  text-shadow: 0 2px 4px rgba(0, 0, 0, 0.4);
}

/* Style du footer */
footer {
  backdrop-filter: blur(10px);
  -webkit-backdrop-filter: blur(10px);
  background: rgba(0, 0, 0, 0.2);
  border-top: 1px solid rgba(255, 255, 255, 0.1);
}

/* Animation pulse */
.animate-pulse {
  animation: pulse 2s infinite;
}

@keyframes pulse {
  0%, 100% {
    transform: scale(1);
  }
  50% {
    transform: scale(1.1);
  }
}

/* Group hover effect */
.group:hover .group-hover\:scale-110 {
  transform: scale(1.1);
}

/* Pour les écrans mobiles */
@media (max-width: 768px) {
  .fixed {
    background-attachment: scroll;
  }
  
  .text-3xl {
    font-size: 1.875rem;
  }
  
  .text-4xl {
    font-size: 2.25rem;
  }
  
  .agri-card {
    padding: 1.5rem;
  }
  
  footer {
    text-align: center;
    padding: 1.5rem 1rem;
  }
  
  footer .flex-col {
    gap: 1rem;
  }
}
</style>