/** @type {import('tailwindcss').Config} */
module.exports = {
  darkMode: ['class'],
  content: ["./src/shibuya/theme/**/*.html"],
  theme: {
    extend: {
      typography: {
        DEFAULT: {
          css: {
            '--tw-prose-body': 'var(--sy-c-text)',
            '--tw-prose-headings': 'var(--sy-c-heading)',
            '--tw-prose-bold': 'var(--sy-c-bold)',
            a: {
              'text-decoration': 'none',
              'border-bottom': '1px solid rgba(var(--sy-rc-link), 0.8)',
            },
            'a:hover': {
              'border-bottom': '2px solid var(--sy-c-link)',
            },
          }
        }
      }
    },
  },
  plugins: [
    require('@tailwindcss/typography'),
  ],
}
