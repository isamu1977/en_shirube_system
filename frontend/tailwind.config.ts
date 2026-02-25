import type { Config } from "tailwindcss";

export default {
  content: ["./src/**/*.{html,js,svelte,ts}"],

  theme: {
    extend: {
      colors: {
        'brand': {
          offwhite: '#FAF9F6',
          charcoal: '#2D2926',
          gold: '#C5A365',    // muted gold
          rose: '#D2A19B',    // dusty rose
          light: '#F5F2EC',   // slightly warmer off-white for sections
        }
      },
      fontFamily: {
        serif: ['"Noto Serif JP"', '"Yu Mincho"', 'serif'],
        sans: ['"Inter"', 'sans-serif'],
      },
      animation: {
        'fade-in-up': 'fadeInUp 0.8s ease-out forwards',
      },
      keyframes: {
        fadeInUp: {
          '0%': { opacity: '0', transform: 'translateY(20px)' },
          '100%': { opacity: '1', transform: 'translateY(0)' },
        }
      }
    }
  },

  plugins: []
} satisfies Config;
