#!/usr/bin/env python3
"""Pack the profile's local infrastructure icons into one Skill Icons-sized grid."""
from pathlib import Path
import re
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
ICONS = ROOT / 'assets/icons'
ORDER = (
    'linux', 'kubernetes', 'docker', 'ansible', 'terraform', 'bash', 'aws', 'cloudflare',
    'rancher', 'harvester', 'helm', 'hpe-synergy', 'dell-openmanage',
    'vcenter', 'vsphere', 'aria',
)
ET.register_namespace('', 'http://www.w3.org/2000/svg')


def main():
    height = ((len(ORDER) + 7) // 8) * 56 - 8
    grid = ET.Element('{http://www.w3.org/2000/svg}svg', { 'width': '440', 'height': str(height),
        'viewBox': f'0 0 440 {height}', 'role': 'img',
    })
    ET.SubElement(grid, 'title').text = 'Infrastructure and operations: ' + ', '.join(ORDER)
    for index, name in enumerate(ORDER):
        icon = ET.parse(ICONS / f'{name}.svg').getroot()
        icon.set('x', str((index % 8) * 56))
        icon.set('y', str((index // 8) * 56))
        icon.set('width', '48')
        icon.set('height', '48')
        # SVG identifiers share a document scope, including nested SVGs.
        ids = {node.attrib['id']: f'{name}-{node.attrib["id"]}'
               for node in icon.iter() if 'id' in node.attrib}
        for node in icon.iter():
            for key, value in list(node.attrib.items()):
                if key == 'id':
                    node.set(key, ids[value])
                else:
                    value = re.sub(r'url\(#([^)]*)\)', lambda m: f'url(#{ids[m[1]]})', value)
                    if key.endswith('href') and value.startswith('#'):
                        value = '#' + ids[value[1:]]
                    node.set(key, value)
        grid.append(icon)
    ET.ElementTree(grid).write(ICONS / 'infrastructure.svg', encoding='utf-8', xml_declaration=False)


if __name__ == '__main__':
    main()
