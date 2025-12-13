/**
 * @param {HTMLButtonElement} button
 */
function bindButtonEvent(button) {
  button.addEventListener('click', () => {
    const element = button.querySelector('i')
    element.setAttribute('data-icon', 'loader')
    const url = button.getAttribute('data-url')
    if (url) {
      copySource(element, url)
    } else {
      copyMarkdown(element)
    }
  })
}

/**
 * @param {HTMLElement} element
 * @param {String} url
 */
function copySource(element, url) {
  fetch(url).then(resp => {
    return resp.text()
  }).then((text) => {
    return navigator.clipboard.writeText(text)
  }).then(() => {
    element.setAttribute('data-icon', 'check')
    setTimeout(() => {
      element.setAttribute('data-icon', 'copy')
    }, 500)
  })
}

/**
 * @param {HTMLElement} element
 */
function copyMarkdown (element) {
  import("https://esm.sh/turndown").then((module) => {
    const turndown = new module.default({
      headingStyle: 'atx',
      bulletListMarker: '-',
      codeBlockStyle: 'fenced',
    })
    turndown.addRule('highlight', {
      filter: (node) => {
        return (
          node.nodeName === 'DIV' &&
          node.classList.contains('highlight')
        )
      },
      replacement: function (_, node) {
        const lang = extractLanguage(node.parentNode.className)
        let text = '```'
        if (lang) {
          text += lang
        }
        return text + '\n' + node.textContent.trim() + '\n```'
      },
    })
    turndown.addRule('literal-block-wrapper', {
      filter: (node) => {
        return (
          node.nodeName === 'DIV' &&
          node.classList.contains('literal-block-wrapper') &&
          node.querySelector('.highlight')
        )
      },
      replacement: function (_, node) {
        const highlight = node.querySelector('.highlight')
        const lang = extractLanguage(highlight.parentNode.className)
        let text = '```'
        if (lang) {
          const caption = node.querySelector('.caption-text')
          text += lang
          if (caption) {
            text += ' "' + caption.textContent.trim() + '"'
          }
        }
        return text + '\n' + highlight.textContent + '\n```'
      },
    })
    return turndown
  }).then((turndown) => {
    const content = document.querySelector('.yue').cloneNode(true)
    const markdown = turndown.turndown(cleanContent(content))
    return navigator.clipboard.writeText(markdown)
  }).then(() => {
    element.setAttribute('data-icon', 'check')
    setTimeout(() => {
      element.setAttribute('data-icon', 'copy')
    }, 500)
  })
}

/**
 * @param {HTMLElement} element
 */
function cleanContent (element) {
  element.querySelectorAll('.headerlink').forEach(el => {
    el.remove()
  })
  element.querySelectorAll('.copybtn').forEach(el => {
    el.remove()
  })
  element.querySelectorAll('span.linenos').forEach(el => {
    el.remove()
  })
  return element.innerHTML
}

/**
 * @param {String} className
 */
function extractLanguage (className) {
  const m = className.match(/highlight-(\S+)/)
  if (m) {
    return m[1]
  }
}

/** @type {NodeListOf<HTMLButtonElement>} */
const copyButtons = document.querySelectorAll('.js-copy')
for (let i = 0; i < copyButtons.length; i++) {
  bindButtonEvent(copyButtons[i])
}
