/** @type {import('tailwindcss').Config} */
export default {
  content: ["./index.html", "./src/**/*.{js,ts,jsx,tsx,vue}"],
  theme: {
    extend: {
      colors: {
        "agri-bg": "#f7f4ec",
        "agri-text": "#243021",
        "agri-green": "#4CAF50",
        "agri-green-dark": "#388E3C",
        "agri-brown": "#8B4513",
        "agri-beige": "#f7f4ec",
        "agri-card": "#ffffff",
      },
      borderRadius: {
        xl2: "0.75rem",
      },
      boxShadow: {
        card: "0 4px 6px -1px rgb(0 0 0 / 0.1)",
      },
    },
  },
  plugins: [],
};
