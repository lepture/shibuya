const defaultToDark = window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches

// set default theme
const root = document.documentElement

function toggleTheme () {
  const isDark = root.classList.contains('dark')
  const toRemove = isDark ? 'dark' : 'light'
  root.classList.remove(toRemove)

  const theme = isDark ? 'light' : 'dark'
  setTheme(theme)
  sessionStorage['_theme'] = theme
}

const el = document.querySelector('.js-theme')

function setTheme (theme) {
  root.classList.add(theme)
  const label = el.getAttribute('data-aria-' + theme)
  el.setAttribute('aria-label', label)
}

if (el) {
  const defaultTheme = defaultToDark ? 'dark': 'light'
  const theme = sessionStorage['_theme'] || defaultTheme
  setTheme(theme)
  el.addEventListener('click', toggleTheme)
}
