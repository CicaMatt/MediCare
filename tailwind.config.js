/** @type {import('tailwindcss').Config} */
const defaultTheme = require('tailwindcss/defaultTheme')

module.exports = {
  content: ['./flaskDir/templates/*.html'],
  theme: {
    extend: {fontFamily: {
      sans: ["Inter", ...defaultTheme.fontFamily.sans],
      },
      colors: {
      'navbarreg': '#B5CBE8',
      'blu400':`#63B3DE`,
      'formpers':  '#f5f6f7',
      'prova': '#03396c',
    },
    },

  },
  plugins: [],

}