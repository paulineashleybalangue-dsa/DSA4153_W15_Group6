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
| 3 | Earthquakes with magnitude `6.0` were misclassified as `"Moderate"` instead of `"Strong"`.| `quakewatch.py`, `MAG_BINS`: the second bin boundary was set to `6.05` instead of `5.95`, placing `6.0` below the `"Strong"` threshold.| Changed the second bin boundary in `MAG_BINS` from `6.05` to `5.95`.| `test_group_magnitude_boundaries`| [TILO] |
| 4 | Events east of Mindanao were assigned to a distant northern Luzon city. | `quakewatch.py`, `nearest\_city()`: event longitude was passed as latitude and event latitude as longitude to `haversine\_km()`. | Passed event latitude first and longitude second, matching the function signature and the city coordinate order. | `test\_nearest\_city\_of\_known\_events` | [FERNANDEZ] |
| 5 | Running the pipeline twice appended the same earthquakes again. | `quakewatch.py`, `load_new()`: the watermark helper existed but was never used; every run fetched from `FIRST_DAY`. | Used `watermark()` and requested data beginning one millisecond after the latest saved event. The first run still starts at `FIRST_DAY`; later runs fetch only new events. | `test_second_load_adds_nothing`; `test_ids_stay_unique_after_two_loads`; `test_group_incremental_acquisition_uses_fake_api`; `test_run_twice_gives_the_same_numbers` | [ESPIRITU] |
| 6 | | | | | |

## Our own tests (in `tests/test_group.py`)

| Test name | Tool used (`parametrize`, fake API, `caplog`) | What it proves | Fails on the broken code? | Written by |
| --- | --- | --- | --- | --- |
| `test_group_features_uses_depth_km` | `loaded` fixture | Confirms that the feature stage uses `depth_km` correctly to generate non-null `depth_class` values. | Yes | [BALANGUE] |
| `test_group_manila_time_conversion` | `loaded` fixture | Confirms that earthquake timestamps are correctly converted to Manila local time (UTC+8). | Yes | [CUBOL] |
| `test\_group\_magnitude\_boundaries` | `pytest.mark.parametrize` | Checks magnitude classification boundaries, including 5.0, 5.9, 6.0, 6.9, 7.0, and 8.0. | Yes | [TILO] |
| `test\_group\_mindanao\_event\_nearest\_city` | `loaded` fixture | Confirms that the Mindanao earthquake event is assigned to the correct nearest city (`C10`). | Yes | [FERNANDEZ] |
| `test_group_incremental_acquisition_uses_fake_api` | `monkeypatch` fake API response | Confirms that incremental acquisition starts one millisecond after the latest saved watermark. | Yes | [ESPIRITU] |

## Logging we added

| Where (function) | Level | Message | Why this level |
| --- | --- | --- | --- |
| | | | |
| | | | |
| | | | |

## One thing we learned about debugging

(two or three sentences)
