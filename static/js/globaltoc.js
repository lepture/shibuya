function addToggleToc () {
  const globaltoc = document.querySelector(".globaltoc")
  if (!globaltoc) {
    return
  }
  const depth = parseInt(globaltoc.getAttribute('data-expand-depth'), 10)

  const shouldExpand = (el) => {
    if (!depth) {
      return false
    }
    let level = 0
    while (el.parentNode && el.parentNode !== globaltoc) {
      el = el.parentNode
      if (el.nodeName === 'UL') {
        level += 1
      }
    }
    return depth >= level
  }

  const sublist = globaltoc.querySelectorAll('li > ul')

  sublist.forEach(el => {
    const list = el.parentNode
    if (list.classList.contains('current') || shouldExpand(list)) {
      list.classList.add('_expand')
      el.style.maxHeight = el.scrollHeight + "px"
    } else {
      list.classList.add('_collapse')
      el.style.maxHeight = "0px"
    }
    const button = createToggleButton(el)
    list.appendChild(button)
  })
}

function propagateDelta (list, delta) {
  let ul = list.parentNode
  while (ul && ul.nodeName === 'UL' && ul.parentNode && ul.parentNode.nodeName === 'LI') {
    const current = parseFloat(ul.style.maxHeight) || 0
    ul.style.maxHeight = Math.max(0, current + delta) + 'px'
    ul = ul.parentNode.parentNode
  }
}

function createToggleButton (el) {
  const button = document.createElement("button")
  button.innerHTML = '<i class="i-lucide chevron-right"></i>'

  const list = el.parentNode
  const link = el.previousSibling
  const title = link.textContent

  const updateArialLabel = () => {
    if (list.classList.contains("_expand")) {
      button.setAttribute("aria-label", "Collapse " + title)
    } else {
      button.setAttribute("aria-label", "Expand " + title)
    }
  }
  updateArialLabel()

  const toggleExpand = (e) => {
    e.preventDefault()
    const oldHeight = parseFloat(el.style.maxHeight) || 0
    if (list.classList.contains("_expand")) {
      list.classList.remove("_expand")
      list.classList.add("_collapse")
      el.style.maxHeight = "0px"
    } else {
      list.classList.remove("_collapse")
      list.classList.add("_expand")
      el.style.maxHeight = el.scrollHeight + "px"
    }
    propagateDelta(list, (parseFloat(el.style.maxHeight) || 0) - oldHeight)
    updateArialLabel()
  }

  if (link.getAttribute("href") === "#") {
    link.addEventListener("click", toggleExpand)
  }
  button.addEventListener("click", toggleExpand)
  return button
}

const currentLink = document.querySelector('.globaltoc a.current')
if (currentLink && currentLink.scrollIntoViewIfNeeded) {
  currentLink.scrollIntoViewIfNeeded()
}

addToggleToc()
