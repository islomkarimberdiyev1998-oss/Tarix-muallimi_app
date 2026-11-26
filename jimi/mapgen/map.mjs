// usage: node map.mjs spec.json  -> writes spec.out (SVG)
// spec: {out, bbox:[lon0,lat0,lon1,lat1], w, h, marks:[{n, lon, lat}]}
import fs from 'fs';
import {geoMercator, geoPath, geoGraticule10} from 'd3-geo';
import {feature, mesh} from 'topojson-client';
const here = new URL('.', import.meta.url).pathname;
const topo = JSON.parse(fs.readFileSync(here + 'node_modules/world-atlas/countries-50m.json'));
const land = feature(topo, topo.objects.land);
const borders = mesh(topo, topo.objects.countries, (a, b) => a !== b);
const s = JSON.parse(fs.readFileSync(process.argv[2]));
const W = s.w || 600, H = s.h || 470;
const [x0, y0, x1, y1] = s.bbox;
const box = {type: 'MultiPoint', coordinates: [[x0, y0], [x1, y1], [x0, y1], [x1, y0]]};
const proj = geoMercator().fitExtent([[0, 0], [W, H]], box).clipExtent([[0, 0], [W, H]]);
const path = geoPath(proj).digits(1);
let svg = `<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 ${W} ${H}">
<rect width="${W}" height="${H}" fill="#e8eef3"/>
<path d="${path(land)}" fill="#fff" stroke="#222" stroke-width="1.1" stroke-linejoin="round"/>
<path d="${path(borders)}" fill="none" stroke="#555" stroke-width="0.7" stroke-linejoin="round"/>
<rect width="${W}" height="${H}" fill="none" stroke="#222" stroke-width="2"/>
<g font-family="Georgia,serif" font-weight="bold" font-size="25" text-anchor="middle">`;
for (const m of s.marks) {
  const [x, y] = proj([m.lon, m.lat]);
  if (x < 0 || y < 0 || x > W || y > H) throw new Error('mark outside map: ' + JSON.stringify(m));
  svg += `<circle cx="${x.toFixed(1)}" cy="${y.toFixed(1)}" r="19" fill="#fff" stroke="#c0392b" stroke-width="3"/><text x="${x.toFixed(1)}" y="${(y + 9).toFixed(1)}" fill="#c0392b">${m.n}</text>`;
}
svg += '</g></svg>\n';
fs.writeFileSync(s.out, svg);
