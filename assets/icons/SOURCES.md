# Icon sources

These tiles adapt existing brand artwork to the 48px dark rounded tile used by
the profile. Synergy and OpenManage use vendor artwork with a product label. VMware tiles
use distinct product artwork rather than the VMware wordmark.

- Rancher, Helm and Dell: [Simple Icons](https://github.com/simple-icons/simple-icons), CC0. Original paths preserved, tile backgrounds and colors added.
- Harvester: [Harvester Dashboard icon](https://github.com/harvester/dashboard/blob/master/pkg/harvester-manager/icon.svg), Apache-2.0. Original path preserved, color and tile background added.
- HPE: [Grommet Icons](https://github.com/grommet/grommet-icons/blob/master/public/img/hpe.svg), Apache-2.0. Original path preserved, tile background and Synergy label added.

Brand names and logos remain the property of their respective owners.
The Apache-2.0 license for adapted Apache artwork is included in LICENSE-APACHE-2.0.txt.

- Linux, Kubernetes, Docker, Ansible, Terraform, Bash, AWS and Cloudflare: [Skill Icons](https://github.com/tandpfun/skill-icons), MIT. Original SVGs retained locally, license in LICENSE-SKILL-ICONS.txt.
- vCenter, vSphere and Aria: [VMware icon bundle](https://github.com/imtrinity94/VMware-Latest-IconSet-Bundle-2024), original product artwork embedded unchanged in dark tiles. VMware trademarks and artwork remain their owners' property; the mirror does not provide an open-source license for them.

Regenerate the single eight-column grid with `python3 scripts/generate_icon_grid.py`.
Tiles are 48px with an 8px gap. All SVG IDs are namespaced to prevent gradient
collisions between icons. No runtime or third-party package is required.
