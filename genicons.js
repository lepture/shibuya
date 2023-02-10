const fs = require('fs')
const path = require('path')

function buildIcons (iconsDir, output) {
  let css = ':root {\n'
  fs.readdirSync(iconsDir).forEach(name => {
    if (/\.svg$/.test(name)) {
      const key = name.replace(/\.svg$/, '')
      let svg = fs.readFileSync(path.resolve(iconsDir, name), 'utf8')
      svg = svg.replace(/#000/g, 'currentColor')
      const url = `url("data:image/svg+xml;utf8,${encodeSvgForCss(svg)}")`
      css += `  --i-${key}-url:${url};\n`
    }
  })
  css += '}\n'
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

const ICONS_SOURCE = path.resolve('static/icons')
const ICONS_OUTPUT = path.resolve('static/css/icons.css')

buildIcons(ICONS_SOURCE, ICONS_OUTPUT)
