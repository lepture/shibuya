function scrollParent (el) {
  let node = el.parentElement
  while (node && node !== document.body && node !== document.documentElement) {
    const overflowY = window.getComputedStyle(node).overflowY
    if ((overflowY === 'auto' || overflowY === 'scroll') && node.scrollHeight > node.clientHeight) {
      return node
    }
    node = node.parentElement
  }
  return null
}

// Scroll the sidebar box that contains `el` so that `el` is visible, if it
// is not already. Only the box is scrolled, never the page:
// scrollIntoView() and scrollIntoViewIfNeeded() also act on the page's own
// scroll position, and that can stop a smooth scroll the page is doing at the
// time (after clicking an "On this page" link, for example).
// `center` centres `el` in the box; otherwise it goes to the nearest edge.
export function scrollSidebarTo (el, center) {
  const box = scrollParent(el)
  if (!box) return

  const boxRect = box.getBoundingClientRect()
  const boxTop = boxRect.top + box.clientTop
  const top = Math.max(boxTop, 0)
  const bottom = Math.min(boxTop + box.clientHeight, window.innerHeight)
  const rect = el.getBoundingClientRect()
  if (rect.top >= top && rect.bottom <= bottom) return

  if (center) {
    box.scrollTop += (rect.top + rect.bottom) / 2 - (top + bottom) / 2
  } else if (rect.top < top) {
    box.scrollTop += rect.top - top
  } else {
    box.scrollTop += rect.bottom - bottom
  }
}
