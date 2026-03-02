import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'

export default defineConfig({
  plugins: [vue()],
  base: './',  // ← CHANGEZ CE CI !!! (utilisation de chemins relatifs)
  build: {
    outDir: 'dist',
    sourcemap: false,
    minify: true
  }
})