const fs = require('fs')
const path = require('path')

function buildIcons (prefix) {
  const iconsDir = path.resolve(`static/${prefix}`)
  const output = path.resolve(`static/css/icons/${prefix}.css`)

  const icons = []
  let css = ':root {\n'
  fs.readdirSync(iconsDir).forEach(name => {
    if (/\.svg$/.test(name)) {
      const key = name.replace(/\.svg$/, '')
      icons.push(key)
      let svg = fs.readFileSync(path.resolve(iconsDir, name), 'utf8')
      svg = svg.replace(/#000/g, 'currentColor')
      const url = `url("data:image/svg+xml;utf8,${encodeSvgForCss(svg)}")`
      css += `  --${prefix}-${key}-url:${url};\n`
    }
  })
  css += '}\n'
  icons.forEach(key => {
    css += `.i-${prefix}.${key}{--icon-url:var(--${prefix}-${key}-url)}\n`
  })
  fs.writeFileSync(output, css)
}

function encodeSvgForCss(svg) {
  let useSvg = svg.startsWith('<svg>') ? svg.replace('<svg>', '<svg >') : svg;
  if (!useSvg.includes(' xmlns:xlink=') && useSvg.includes(' xlink:')) {
    useSvg = useSvg.replace(
      '<svg ',
      '<svg xmlns:xlink="http://www.w3.org/1999/xlink" '
    );
  }
  if (!useSvg.includes(' xmlns=')) {
    useSvg = useSvg.replace(
      '<svg ',
      '<svg xmlns="http://www.w3.org/2000/svg" '
    );
  }
  return useSvg.trim()
    .replace(/"/g, "'")
    .replace(/%/g, '%25')
    .replace(/#/g, '%23')
    .replace(/{/g, '%7B')
    .replace(/}/g, '%7D')
    .replace(/</g, '%3C')
    .replace(/>/g, '%3E');
}

buildIcons('lucide')
