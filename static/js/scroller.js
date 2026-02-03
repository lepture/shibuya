let PREVIOUS_SCROLLY = 0
let SCROLL_MARGIN_TOP = 200

let allSections = []
const backToTop = document.querySelector('.back-to-top')

function measureScrollMarginTop () {
  const element = document.querySelector('.yue > section')
  if (element) {
    const style = window.getComputedStyle(element)
    SCROLL_MARGIN_TOP = parseInt(style.scrollMarginTop, 10) || 0
  }
}

function isInSection (section) {
  const rect = section.getBoundingClientRect()
  return rect.top <= SCROLL_MARGIN_TOP && rect.bottom >= SCROLL_MARGIN_TOP
}

function clearActiveAnchors () {
  document.querySelectorAll('.localtoc li.active').forEach(entry => {
    entry.classList.remove('active')
  })
}

function setActiveAnchor (id) {
  const anchor = document.querySelector(`.localtoc a[href="#${id}"]`)
  if (!anchor) return

  const parent = anchor.parentNode
  if (parent.classList.contains('active')) return

  clearActiveAnchors()
  parent.classList.add('active')
}

function trackLocalToc () {
  let activeId
  for (let i = 0; i < allSections.length; i++) {
    if (isInSection(allSections[i])) {
      activeId = allSections[i].id
    }
  }
  if (activeId) {
    setActiveAnchor(activeId)
  }
}

function onScroll () {
  const scrollHeight = document.documentElement.scrollHeight
  if (allSections.length && (window.innerHeight + Math.round(window.scrollY)) >= scrollHeight) {
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

if (document.querySelector('.localtoc')) {
  window.addEventListener('scroll', onScroll)
  window.addEventListener('DOMContentLoaded', () => {
    allSections = document.querySelectorAll('.yue > section section[id]')
    measureScrollMarginTop()
    trackLocalToc()
  })
  window.addEventListener('resize', measureScrollMarginTop)
}
