const COLOR_MODES = ['auto', 'light', 'dark']
const el = document.querySelector('.js-theme')

function rotateColorMode () {
  let index = getModeIndex()
  index += 1
  if (!COLOR_MODES[index]) {
    index = 0
  }
  const mode = COLOR_MODES[index]
  setColorMode(mode)
  sessionStorage['_theme'] = mode
  updateLabel(mode)
}

function getModeIndex () {
  return COLOR_MODES.indexOf(document.documentElement.getAttribute('data-color-mode') || 'auto')
}

function updateLabel (mode) {
  const label = el.getAttribute('data-aria-' + mode)
  el.setAttribute('aria-label', label)
}

if (el) {
  el.addEventListener('click', rotateColorMode)
  updateLabel(COLOR_MODES[getModeIndex()] || 'auto')
}
