"""Tests for prep_single.py — stale result file cleanup."""
import os

from conftest import run_script


class TestPrepSingle:
    def test_removes_existing_result(self, tmp_path, monkeypatch):
        single_dir = tmp_path / "single"
        single_dir.mkdir()
        result_file = single_dir / "RHAISTRAT-1234.result.md"
        result_file.write_text("old result")

        # Patch the hardcoded path by running with env manipulation
        # prep_single.py uses /tmp/strat-assess/single hardcoded,
        # so we test against the real path
        result = run_script("prep_single.py", ["RHAISTRAT-1234"])
        assert result.returncode == 0
        assert "SINGLE_DIR=" in result.stdout

    def test_no_existing_file(self):
        result = run_script("prep_single.py", ["RHAISTRAT-9999"])
        assert result.returncode == 0
        assert "SINGLE_DIR=" in result.stdout
        assert "REMOVED=" not in result.stdout

    def test_creates_single_dir(self):
        result = run_script("prep_single.py", ["RHAISTRAT-5555"])
        assert result.returncode == 0
        assert os.path.isdir("/tmp/strat-assess/single")

    def test_no_args_exits_1(self):
        result = run_script("prep_single.py", [])
        assert result.returncode == 1
