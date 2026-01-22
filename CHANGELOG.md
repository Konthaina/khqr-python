# Changelog

## 0.1.7
- Documentation update and improvements
- Add English and Khmer README files
- Improve usage examples for Static and Dynamic KHQR
- Clarify currency handling (KHR / USD) and QR generation
- Add link to CHANGELOG in README

## 0.1.6
- Fix CI failure caused by Ruff lint rule (UP037)
- Remove quoted return type annotations (Python 3.9+ compatible)
- Ensure CI passes on Python 3.9–3.13
- No functional changes to KHQR generation

## 0.1.5
- Fix currency handling for KHR and USD
- `set_currency(Currency.KHR)` now correctly outputs Tag 53 = 116
- Support currency input as Enum (`Currency.KHR`, `Currency.USD`)
  and string values (`"KHR"`, `"USD"`, `"116"`, `"840"`)
- Improve static QR behavior (stable output when no amount)

## 0.1.4
- Improve static QR generation logic
- Static QR now omits timestamp when amount is not set
- Point of Initiation Method (Tag 01) auto-switch:
  - `11` for static (no amount)
  - `12` for dynamic (with amount)

## 0.1.3
- Add static QR support
- Auto-detect static vs dynamic QR based on amount
- Minor refactoring and code cleanup

## 0.1.2
- Configure PyPI Trusted Publishing (OIDC)
- Add GitHub Actions workflow for automated release
- Improve packaging and metadata

## 0.1.1
- CI fixes and test stabilization
- Ruff, mypy, and pytest configuration improvements
- Minor internal refactors (no behavior change)

## 0.1.0
- Initial release
- KHQR payload generator (NBC KHQR v2.7-style TLV)
- CRC-16/CCITT-FALSE verification
- Simple TLV decode helper
- Basic CLI support
