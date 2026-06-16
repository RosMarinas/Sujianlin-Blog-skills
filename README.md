# cognitive-knowledge-network

`cognitive-knowledge-network` is a agent-compatible skill and local knowledge
package for navigating a compiled knowledge graph built from Su Jianlin's blog
corpus.

This public repository is intended to distribute the skill, schema,
documentation, and derived knowledge layers without bundling the original
`Data/` evidence corpus.

The omitted `Data/` directory is the original evidence layer: a locally
collected and organized archive of Su Jianlin blog materials, including source
markdown converted from original pages and related assets.

## Repository layout

- `SKILL.md`: skill entrypoint
- `skill/`: Python helpers and skill-local docs
- `schema.md`: page and graph contracts
- `wiki/`: derived knowledge pages
- `graph/`: structured derived graph content
- `purpose.md`: repository purpose and boundaries, if present
- `docs/`: design and workflow documentation, if present
- `probes/`: validation and diagnostic artifacts, if present

`Data/` is intentionally excluded from the public GitHub package.

## Licensing

This is a mixed-license repository.

### MIT-licensed layer

Unless a file says otherwise, the MIT License applies to the software and
engineering layer, including:

- `SKILL.md`
- `skill/`
- `visualize.py`
- `visualize.html`
- `schema.md`
- `README.md`
- `.gitignore`
- build, test, and packaging files
- `purpose.md` if added later
- `docs/` if added later

See [LICENSE](LICENSE).

### CC BY-NC-SA 4.0 content layer

Unless a file says otherwise, the following derived knowledge directories are
licensed under CC BY-NC-SA 4.0:

- `wiki/`
- `graph/`
- `probes/` if added later

These directories are not released under MIT.

See [LICENSE-content.md](LICENSE-content.md).

## Upstream provenance

This repository is built around content derived from the blog corpus of Su
Jianlin.

- Original author: Su Jianlin
- Original sites: `https://spaces.ac.cn/` and `https://kexue.fm/`

The `wiki/` and `graph/` directories are curated and structured by this
repository's maintainers. They contain maintainer-authored organization,
selection, and structured representation. However, they are still derived from
the upstream blog corpus and are therefore distributed under CC BY-NC-SA 4.0
rather than MIT.

Where upstream attribution is preserved in file metadata or page frontmatter,
that attribution should remain intact in downstream reuse.
