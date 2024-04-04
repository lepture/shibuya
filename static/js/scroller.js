let PREVIOUS_SCROLLY = 0
let SCROLL_MARGIN_TOP = 200
const allSections = document.querySelectorAll('.yue > section section[id]')

function measureScrollMarginTop () {
  const element = document.querySelector('.yue > section')
  SCROLL_MARGIN_TOP = element.computedStyleMap().get('scroll-margin-top').value
}

function isInSection (section) {
  const rect = section.getBoundingClientRect()
  return rect.top <= SCROLL_MARGIN_TOP && rect.bottom >= SCROLL_MARGIN_TOP
}

function setActiveAnchor (id) {
  document.querySelectorAll('.localtoc li.active').forEach(entry => {
    entry.classList.remove('active')
  })
  document.querySelector(`.localtoc a[href="#${id}"]`).parentNode.classList.add('active')
}

function trackLocalToc () {
  let currentSection
  for (let i = 0; i < allSections.length; i++) {
    currentSection = allSections[i]
    if (isInSection(currentSection)) {
      setActiveAnchor(currentSection.id)
      break
    }
  }
}

function onScroll () {
  if ((window.innerHeight + Math.round(window.scrollY)) >= document.body.offsetHeight) {
    const lastSection = allSections[allSections.length - 1]
    setActiveAnchor(lastSection.id)
  } else {
    trackLocalToc()

    if (window.scrollY < PREVIOUS_SCROLLY) {
      // scroll back to top
    } else {
    }
    PREVIOUS_SCROLLY = window.scrollY
  }
}

window.addEventListener('scroll', onScroll)
window.addEventListener('DOMContentLoaded', () => {
  measureScrollMarginTop()
  trackLocalToc()
})
window.addEventListener('resize', measureScrollMarginTop)
