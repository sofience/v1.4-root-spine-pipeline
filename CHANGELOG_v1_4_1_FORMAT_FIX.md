# Changelog — v1.4.1 Format Fix

## Added

- `.gitattributes`
- `.editorconfig`
- `scripts/validate_ai_readable.py`
- `docs/V1_4_1_FORMAT_FIX_NOTES.md`
- `PATCH_APPLY_GUIDE.md`
- `PATCH_CHECKSUMS.sha256`

## Changed

- Rewrote `README.md` with normal LF line breaks.
- Rewrote `00_AI_ENTRYPOINT.md` with normal LF line breaks.
- Rewrote `llms.txt` with normal LF line breaks.
- Rewrote `SDELTA_ACCESS_PROTOCOL.yaml` as valid block YAML.
- Rewrote `SDELTA_MODULE_ROUTING.yaml` as valid block YAML.
- Rewrote `/pipeline/*.yaml` as valid block YAML.
- Rewrote `/pipeline/*.md` with normal Markdown line breaks.
- Added compact `SERIES_INDEX.json`.
- Added compact `SERIES_DOI_MAP.json`.

## Preserved

- Minimal root route: `01 -> 03 -> 47 -> 62`
- Operational diagnostic route: `47 -> 62 -> 39 -> 65 -> 64 -> 56`
- Zenodo as canonical citation layer
- GitHub as AI-readable ingestion layer
