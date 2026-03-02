<template>
  <div class="relative min-h-screen flex flex-col">
    <!-- Image d'arrière-plan fixe -->
    <div 
      class="fixed inset-0 bg-cover bg-center bg-no-repeat"
      style="background-image: url('https://images.unsplash.com/photo-1542601906990-b4d3fb778b09?ixlib=rb-4.0.3&auto=format&fit=crop&w=2000&q=80')"
    >
      <!-- Overlay sombre pour améliorer la lisibilité -->
      <div class="absolute inset-0 bg-black/40"></div>
    </div>
    
    <!-- Contenu par-dessus l'image -->
    <div class="relative z-10 flex-1">
      <!-- Hero Section -->
      <main class="max-w-6xl mx-auto px-4 py-8 pt-20">
        <div class="flex justify-center">
          <!-- Carte principale centrée -->
          <div class="bg-white/10 backdrop-blur-lg p-10 rounded-2xl shadow-2xl border border-white/20 w-full max-w-lg">
            <!-- Titre centré -->
            <div class="text-center mb-8">
              <h1 class="text-4xl lg:text-5xl font-bold text-white leading-tight mb-4">
                AgriCycle 
              </h1>
              <p class="text-white/90 text-lg font-medium">
                Une application agricole simple et moderne pour :
              </p>
            </div>
            
            <!-- Liste des fonctionnalités -->
            <div class="space-y-4 mb-8">
              <div class="flex items-center">
                <span class="text-agri-green-light text-2xl mr-4 flex-shrink-0">✓</span>
                <span class="text-white font-medium text-lg">Gérer vos cultures et récoltes</span>
              </div>
              <div class="flex items-center">
                <span class="text-agri-green-light text-2xl mr-4 flex-shrink-0">✓</span>
                <span class="text-white font-medium text-lg">Optimiser l'utilisation des ressources</span>
              </div>
              <div class="flex items-center">
                <span class="text-agri-green-light text-2xl mr-4 flex-shrink-0">✓</span>
                <span class="text-white font-medium text-lg">Suivre les bonnes pratiques agricoles</span>
              </div>
              <div class="flex items-center">
                <span class="text-agri-green-light text-2xl mr-4 flex-shrink-0">✓</span>
                <span class="text-white font-medium text-lg">Connecter producteurs et bénéficiaires</span>
              </div>
            </div>
            
            <!-- Boutons d'action centrés -->
            <div class="flex flex-col sm:flex-row gap-4 justify-center mb-8">
              <router-link 
                to="/login" 
                class="agri-btn text-center py-3 px-6 text-lg font-semibold flex-1 sm:flex-none"
              >
                Se connecter
              </router-link>
              <router-link 
                to="/register" 
                class="agri-btn-light text-center py-3 px-6 text-lg font-semibold flex-1 sm:flex-none"
              >
                S'inscrire
              </router-link>
            </div>
            
            <!-- Lien vers les bonnes pratiques centré -->
            <div class="text-center">
              <router-link 
                to="/good-practices" 
                class="inline-flex items-center justify-center text-white hover:text-agri-green-light font-medium"
              >
                Voir les bonnes pratiques
                <svg class="w-5 h-5 ml-2" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M14 5l7 7m0 0l-7 7m7-7H3" />
                </svg>
              </router-link>
            </div>
          </div>
        </div>
        
        <!-- Section "Pourquoi AgriCycle" -->
        <div class="mt-16">
          <h2 class="text-3xl font-bold text-white text-center mb-8">
            Pourquoi choisir AgriCycle ?
          </h2>
          
          <div class="grid md:grid-cols-3 gap-6">
            <div class="agri-card p-8 text-center hover:shadow-2xl transition-all bg-white/10 backdrop-blur-lg">
              <h3 class="font-bold text-xl mb-4 text-white">Économie circulaire</h3>
              <p class="text-white/90">
                Réduction du gaspillage alimentaire et optimisation des ressources
              </p>
            </div>
            
            <div class="agri-card p-8 text-center hover:shadow-2xl transition-all bg-white/10 backdrop-blur-lg">
              <h3 class="font-bold text-xl mb-4 text-white">Simplicité</h3>
              <p class="text-white/90">
                Interface intuitive pour les professionnels agricoles
              </p>
            </div>
            
            <div class="agri-card p-8 text-center hover:shadow-2xl transition-all bg-white/10 backdrop-blur-lg">
              <h3 class="font-bold text-xl mb-4 text-white">Communauté</h3>
              <p class="text-white/90">
                Mise en relation agriculteurs, distributeurs, consommateurs
              </p>
            </div>
          </div>
        </div>
        
        <!-- Section CTA -->
        <div class="mt-16">
          <div class="agri-card p-8 text-center hover:shadow-2xl transition-all bg-white/10 backdrop-blur-lg">
            <p class="text-2xl font-bold text-white mb-4">
              Rejoignez la révolution agricole durable
            </p>
            <p class="text-white/90 text-lg mb-8">
              Des centaines d'agriculteurs font déjà confiance à AgriCycle
            </p>
            <router-link 
              to="/register" 
              class="agri-btn inline-flex items-center py-4 px-10 text-xl font-bold"
            >
              Commencer maintenant
              <svg class="w-6 h-6 ml-3" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17 8l4 4m0 0l-4 4m4-4H3" />
              </svg>
            </router-link>
          </div>
        </div>
      </main>
    </div>

    <!-- Footer -->
    <footer >
      <div class="max-w-6xl mx-auto px-4">
        <div class="flex flex-col md:flex-row justify-between items-center">
          <!-- Copyright -->
          <div class="text-white/80 text-sm mb-4 md:mb-0">
            © {{ new Date().getFullYear() }} AgriCycle — Agriculture durable ♻️🌱
          </div>
        </div>
      </div>
    </footer>
  </div>
</template>

<script setup>
// Pas besoin d'import spécifique pour l'image
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

/* Couleurs personnalisées pour le texte blanc */
.text-agri-green-light {
  color: #68d391; /* Version plus claire du vert AgriCycle */
}

/* Styles pour les boutons */
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

/* Styles pour les cartes avec effet de verre */
.agri-card {
  transition: transform 0.4s ease, box-shadow 0.4s ease;
  border: 1px solid rgba(255, 255, 255, 0.2);
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
}

/* Pour les écrans mobiles, ajuster les effets */
@media (max-width: 768px) {
  .fixed {
    background-attachment: scroll;
  }
  
  .grid-cols-2, .grid-cols-3 {
    grid-template-columns: 1fr;
  }
  
  .text-5xl {
    font-size: 2.5rem;
  }
  
  .text-4xl {
    font-size: 2rem;
  }
  
  .text-3xl {
    font-size: 1.75rem;
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