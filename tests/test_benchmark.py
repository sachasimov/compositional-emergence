import pytest
from compositional_emergence.benchmark import cases, confusion, fixture_expectation_met


def test_frozen_panel_separates_known_labels_from_unlabelled_diagnostics():
    panel = cases()
    assert len({c["id"] for c in panel}) == len(panel)
    assert sum(c["label"] is not None for c in panel) == 11
    assert all(c["label"] is None for c in panel if c["split"] == "diagnostic")
    assert all(c["initial"].shape == (32, 32) for c in panel)


def test_metrics_account_for_errors_and_undefined_denominators():
    assert confusion([], "assay")["precision"] is None
    rows = [{"label": label, "assay": pred, "status": "ok"}
            for label, pred in [(True, True), (True, False), (False, True), (False, False)]]
    rows.append({"label": True, "status": "error"})
    result = confusion(rows, "assay")
    assert [result[k] for k in ["tp", "fp", "tn", "fn", "n_errors"]] == [1, 1, 1, 1, 1]
    assert result["accuracy"] == 0.5


@pytest.mark.parametrize("wrong", [{"period": 2, "displacement": [1, 1]},
                                  {"period": 4, "displacement": [-1, 1]}])
def test_wrong_recurrence_signature_cannot_pass(wrong):
    row = {"label": True, "status": "ok", "assay": True,
           "expected_recurrence": {"period": 4, "displacement": [1, 1]},
           "recurrence": wrong}
    assert not fixture_expectation_met(row)
    row["recurrence"] = row["expected_recurrence"]
    assert fixture_expectation_met(row)
