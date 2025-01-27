import subprocess
import pytest


class TestCLITool:
    @staticmethod
    def run_cli_tool(args):
        result = subprocess.run(
            ["python3", "tool.py"] + args,
            capture_output=True,
            text=True
        )
        return result

    def test_run_command_with_no_options(self):
        result = self.run_cli_tool(["run"])
        assert result.returncode == 0

    def test_run_command_with_verbose_option(self):
        result = self.run_cli_tool(["run", "-v"])
        assert result.returncode == 0

    def test_run_command_with_output_option(self):
        result = self.run_cli_tool(["run", "-o", "file.txt"])
        assert result.returncode == 0

    def test_run_command_with_both_options(self):
        result = self.run_cli_tool(["run", "-v", "-o", "file.txt"])
        assert result.returncode == 0

    def test_run_command_with_long_verbose_option(self):
        result = self.run_cli_tool(["run", "--verbose"])
        assert result.returncode == 0

    def test_run_command_with_long_output_option(self):
        result = self.run_cli_tool(["run", "--output", "file.txt"])
        assert result.returncode == 0

    def test_run_command_with_missing_value_for_output(self):
        result = self.run_cli_tool(["run", "-o"])
        assert result.returncode == 0

    def test_unknown_command(self):
        result = self.run_cli_tool(["unknown_command"])
        assert result.returncode == 0

    def test_unknown_option(self):
        result = self.run_cli_tool(["run", "--unknown"])
        assert result.returncode == 0
