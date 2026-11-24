# Repair log

Study group: Group 6  
Members:
- BALANGUE, PAULINE ASHLEY  
- CUBOL, MARY BELLE
- TILO, MIKAELA STEFANIE
- FERNANDEZ, COLEEN DIAN
- ESPIRITU, MEGHAN ISABELLE
- ALANO, ROLANDO BANJO

## Defects

| # | Symptom (what was wrong for the user) | Cause (file, function, line; why it was wrong) | Fix (what you changed) | Test that now guards it | Fixed by |
| --- | --- | --- | --- | --- | --- |
| 1 | `features_stage()` stopped with a `KeyError` before the dashboard was written. | `quakewatch.py`, `features_stage()`: the code accessed `t["depth"]`, but the acquired and integrated data use the column `depth_km`. | Changed the depth-class calculation to use `t["depth_km"]`. | `test_features_stage_runs`; `test_depth_classes`; | [BALANGUE] |
| 2 | The strongest event was shown at 14:37 Manila time instead of 22:37. | `quakewatch.py`, `features_stage()`: `tz_localize(None).tz_localize("Asia/Manila")` relabeled UTC clock values as Manila time instead of converting the instant. | Used `t["time"].dt.tz_convert("Asia/Manila")` to convert the timezone correctly. | `test_strongest_event_is_at_night_in_manila` | [CUBOL] |
| 3 | | | | | |
| 4 | | | | | |
| 5 | | | | | |
| 6 | | | | | |

## Our own tests (in `tests/test_group.py`)

| Test name | Tool used (`parametrize`, fake API, `caplog`) | What it proves | Fails on the broken code? | Written by |
| --- | --- | --- | --- | --- |
| `test_group_features_uses_depth_km` | `loaded` fixture | Confirms that the feature stage uses `depth_km` correctly to generate non-null `depth_class` values. | Yes | [BALANGUE] |
| | | | | |
| | | | | |

## Logging we added

| Where (function) | Level | Message | Why this level |
| --- | --- | --- | --- |
| | | | |
| | | | |
| | | | |

## One thing we learned about debugging

(two or three sentences)
