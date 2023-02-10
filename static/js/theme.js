const defaultToDark = window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches


function setTheme (value) {
  const root = document.documentElement
  let toAdd = value
  let toRemove

  if (value === 'dark') {
    toRemove = 'light'
  } else if (value === 'light') {
    toRemove = 'dark'
  } else {
    toAdd = defaultToDark ? 'dark' : 'light'
    toRemove = defaultToDark ? 'light' : 'dark'
  }
  root.classList.remove(toRemove)
  root.classList.add(toAdd)
  sessionStorage['_theme'] = value
  root.dataset['theme'] = value || 'system'
}

const theme = sessionStorage['_theme'] || ''
setTheme(theme)

const el = document.getElementById('theme-select')
if (el) {
  el.value = theme
  el.addEventListener('change', () => {
    setTheme(el.value)
  })
}
