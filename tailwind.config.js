/** @type {import('tailwindcss').Config} */
export default {
  content: ['./index.html', './src/**/*.{vue,js}'],
  safelist: [
    'badge-day-1','badge-day-2','badge-day-3','badge-day-4',
    'badge-day-5','badge-day-6','badge-day-7','badge-day-8','badge-day-9',
  ],
  theme: {
    extend: {
      colors: {
        yamabuki: {
          50:  '#FFFBF0',
          100: '#FFF3CC',
          200: '#FFE080',
          300: '#FFD04A',
          400: '#F6AD3C',
          500: '#E8961A',
          600: '#C97A0A',
          700: '#A66005',
          800: '#7A4505',
          900: '#3D2203',
        },
        kaki: {
          50:  '#FFF1EE',
          100: '#FFE0D8',
          200: '#FFC0AE',
          300: '#FF9278',
          400: '#F06A4A',
          500: '#E55125',
          600: '#C93D14',
          700: '#A42E0D',
          800: '#7A2209',
          900: '#3D1104',
        },
        fuji: {
          50:  '#F5F3FF',
          100: '#EDE9FD',
          200: '#DDD6FB',
          300: '#C3B6F5',
          400: '#A893E8',
          500: '#8E77AD',
          600: '#7358A0',
          700: '#5A3E88',
          800: '#3E2965',
          900: '#241540',
        },
        ivory: {
          50:  '#FEFDFB',
          100: '#FAF1E4',
          200: '#F2EFE9',
          300: '#E8E0D5',
          400: '#D5C9B8',
          500: '#B8A898',
          600: '#8C7B68',
          700: '#655849',
          800: '#3D3228',
          900: '#3D1B0E',
        },
      },
      fontFamily: {
        heading: ['Fredoka', 'sans-serif'],
        body: ['Nunito', '-apple-system', 'BlinkMacSystemFont', 'Segoe UI', 'sans-serif'],
      },
      maxWidth: {
        container: '1100px',
      },
      borderRadius: {
        'card-sm': '12px',
        'card-md': '18px',
        'card-lg': '28px',
        'card-xl': '40px',
      },
      boxShadow: {
        'card-sm':     '0 2px 8px rgba(61,27,14,.07)',
        'card-md':     '0 8px 24px rgba(246,173,60,.18)',
        'card-lg':     '0 20px 50px rgba(246,173,60,.22)',
        'card-kaki':   '0 12px 30px rgba(229,81,37,.28)',
      },
      transitionTimingFunction: {
        custom: 'cubic-bezier(.22,.61,.36,1)',
      },
      keyframes: {
        'fade-in-up': {
          from: { opacity: '0', transform: 'translateY(24px)' },
          to:   { opacity: '1', transform: 'translateY(0)' },
        },
        float: {
          '0%,100%': { transform: 'translateY(0) scale(1)' },
          '50%':     { transform: 'translateY(-22px) scale(1.04)' },
        },
        'pulse-dot': {
          '0%,100%': { transform: 'scale(1)', opacity: '1' },
          '50%':     { transform: 'scale(1.4)', opacity: '0.6' },
        },
      },
      animation: {
        'fade-in-up':   'fade-in-up 0.8s cubic-bezier(.22,.61,.36,1) both',
        'fade-in-up-1': 'fade-in-up 0.9s cubic-bezier(.22,.61,.36,1) 0.1s both',
        'fade-in-up-2': 'fade-in-up 1.0s cubic-bezier(.22,.61,.36,1) 0.2s both',
        'fade-in-up-3': 'fade-in-up 1.1s cubic-bezier(.22,.61,.36,1) 0.3s both',
        float:          'float 10s ease-in-out infinite',
        'float-d':      'float 10s ease-in-out -5s infinite',
        'pulse-dot':    'pulse-dot 2s ease-in-out infinite',
      },
    },
  },
  plugins: [],
}
