let PREVIOUS_SCROLLY = 0
let SCROLL_MARGIN_TOP = 200

const allSections = document.querySelectorAll('.yue > section section[id]')
const backToTop = document.querySelector('.back-to-top')

function measureScrollMarginTop () {
  const element = document.querySelector('.yue > section')
  if (element) {
    SCROLL_MARGIN_TOP = element.computedStyleMap().get('scroll-margin-top').value
  }
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
    if (lastSection) {
      setActiveAnchor(lastSection.id)
    }
  } else {
    trackLocalToc()
  }

  if (backToTop) {
    if (window.scrollY && window.scrollY < PREVIOUS_SCROLLY) {
      backToTop.setAttribute('data-visible', 'true')
    } else if (backToTop.hasAttribute('data-visible')) {
      backToTop.removeAttribute('data-visible')
    }
    PREVIOUS_SCROLLY = window.scrollY
  }
}

if (backToTop) {
  backToTop.addEventListener('click', () => {
    window.scrollTo(0, 0)
  })
}

window.addEventListener('scroll', onScroll)
window.addEventListener('DOMContentLoaded', () => {
  measureScrollMarginTop()
  trackLocalToc()
})
window.addEventListener('resize', measureScrollMarginTop)
