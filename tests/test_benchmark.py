from compositional_emergence.benchmark import cases, confusion


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
