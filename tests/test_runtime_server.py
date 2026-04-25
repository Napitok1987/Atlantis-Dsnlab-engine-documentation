from pathlib import Path
import os
import shutil
import subprocess
import tempfile
import unittest


DOC_ROOT = Path(__file__).resolve().parents[1]
WORKSPACE_ROOT = DOC_ROOT.parent
BINARY = Path(os.environ.get("ATLANTIS_STANDARD_BINARY", str(WORKSPACE_ROOT / "DSNAtlantis-src/standard/standard")))
TMP_ROOT = DOC_ROOT / "tests/_runtime_tmp"
FIXTURE_ROOT = DOC_ROOT / "tests/fixtures/runtime_new_game_32"


def read_text(path: Path) -> str:
    data = path.read_bytes()
    try:
        return data.decode("utf-8")
    except UnicodeDecodeError:
        return data.decode("latin-1")


class RuntimeServerTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        if not BINARY.exists():
            raise unittest.SkipTest("standard binary is not built")
        if not (FIXTURE_ROOT / "game.in").exists() or not (FIXTURE_ROOT / "players.in").exists():
            raise unittest.SkipTest("runtime fixture is not available")
        TMP_ROOT.mkdir(exist_ok=True)

    def make_workdir(self, prefix: str) -> Path:
        workdir = Path(tempfile.mkdtemp(prefix=prefix, dir=TMP_ROOT))
        self.addCleanup(shutil.rmtree, workdir, ignore_errors=True)
        return workdir

    def run_binary(self, *args: str, cwd: Path, input_text: str | None = None, timeout: int = 10) -> subprocess.CompletedProcess[str]:
        return subprocess.run(
            [str(BINARY), *args],
            cwd=str(cwd),
            input=input_text,
            text=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            timeout=timeout,
            check=False,
        )

    def copy_fixture_game(self, workdir: Path) -> None:
        shutil.copy2(FIXTURE_ROOT / "game.in", workdir / "game.in")
        shutil.copy2(FIXTURE_ROOT / "players.in", workdir / "players.in")

    def parse_faction_num(self, players_text: str, player_name: str) -> str:
        lines = players_text.splitlines()
        for idx, line in enumerate(lines):
            if line.startswith("Faction: ") and idx + 1 < len(lines) and lines[idx + 1].startswith(f"Name: {player_name} ("):
                return line.split(": ", 1)[1]
        self.fail(f"Faction for {player_name!r} not found")

    def parse_template_unit_num(self, report_text: str) -> str:
        for line in report_text.splitlines():
            if line.startswith("unit "):
                return line.split()[1]
        self.fail("No unit line found in report template")

    def bootstrap_new_player(self, workdir: Path, player_name: str, email: str, password: str = "secret") -> tuple[str, str]:
        self.copy_fixture_game(workdir)
        with (workdir / "players.in").open("a", encoding="utf-8") as handle:
            handle.write("Faction: new\n")
            handle.write(f"Name: {player_name}\n")
            handle.write(f"Email: {email}\n")
            handle.write(f"Password: {password}\n")
            handle.write("SendTimes: 1\n")

        result = self.run_binary(
            "run",
            "ignored-game.in",
            "admin.txt",
            "orders.txt",
            "reports.txt",
            "ignored-game.out",
            "players.txt",
            "times.txt",
            cwd=workdir,
            timeout=20,
        )
        self.assertEqual(result.returncode, 0)

        players_out = read_text(workdir / "players.out")
        faction_num = self.parse_faction_num(players_out, player_name)
        report_text = read_text(workdir / f"report.{faction_num}")
        unit_num = self.parse_template_unit_num(report_text)
        return faction_num, unit_num

    def promote_outputs_to_next_turn_inputs(self, workdir: Path) -> None:
        shutil.copy2(workdir / "game.out", workdir / "game.in")
        shutil.copy2(workdir / "players.out", workdir / "players.in")

    def run_turn_with_orders(self, workdir: Path, faction_num: str, password: str, unit_num: str, order_lines: list[str]) -> str:
        (workdir / f"orders.{faction_num}").write_text(
            "\n".join([f"#atlantis {faction_num} {password}", f"unit {unit_num}", *order_lines, "#end"]) + "\n",
            encoding="utf-8",
        )
        result = self.run_binary(
            "run",
            "ignored-game.in",
            "admin.txt",
            "orders.txt",
            "reports.txt",
            "ignored-game.out",
            "players.txt",
            "times.txt",
            cwd=workdir,
            timeout=20,
        )
        self.assertEqual(result.returncode, 0)
        return read_text(workdir / f"report.{faction_num}")

    def bootstrap_forbid_scenario(self, workdir: Path) -> tuple[str, str, str, str]:
        self.copy_fixture_game(workdir)
        with (workdir / "players.in").open("a", encoding="utf-8") as handle:
            handle.write("Faction: new\n")
            handle.write("Name: Guard Fac\n")
            handle.write("Email: guardfac@player.com\n")
            handle.write("Password: guardpw\n")
            handle.write("SendTimes: 1\n")
            handle.write("Faction: new\n")
            handle.write("Name: Attack Fac\n")
            handle.write("Email: attackfac@player.com\n")
            handle.write("Password: attackpw\n")
            handle.write("SendTimes: 1\n")

        result = self.run_binary(
            "run",
            "ignored-game.in",
            "admin.txt",
            "orders.txt",
            "reports.txt",
            "ignored-game.out",
            "players.txt",
            "times.txt",
            cwd=workdir,
            timeout=20,
        )
        self.assertEqual(result.returncode, 0)

        players_out = read_text(workdir / "players.out")
        guard_fac = self.parse_faction_num(players_out, "Guard Fac")
        attack_fac = self.parse_faction_num(players_out, "Attack Fac")
        guard_unit = self.parse_template_unit_num(read_text(workdir / f"report.{guard_fac}"))
        attack_unit = self.parse_template_unit_num(read_text(workdir / f"report.{attack_fac}"))

        self.promote_outputs_to_next_turn_inputs(workdir)
        (workdir / f"orders.{guard_fac}").write_text(
            "\n".join(
                [
                    f"#atlantis {guard_fac} guardpw",
                    f"unit {guard_unit}",
                    "claim 200",
                    "study combat",
                    "#end",
                ]
            )
            + "\n",
            encoding="utf-8",
        )
        (workdir / f"orders.{attack_fac}").write_text(
            "\n".join(
                [
                    f"#atlantis {attack_fac} attackpw",
                    "#end",
                ]
            )
            + "\n",
            encoding="utf-8",
        )
        result = self.run_binary(
            "run",
            "ignored-game.in",
            "admin.txt",
            "orders.txt",
            "reports.txt",
            "ignored-game.out",
            "players.txt",
            "times.txt",
            cwd=workdir,
            timeout=20,
        )
        self.assertEqual(result.returncode, 0)

        self.promote_outputs_to_next_turn_inputs(workdir)
        (workdir / f"orders.{guard_fac}").write_text(
            "\n".join(
                [
                    f"#atlantis {guard_fac} guardpw",
                    f"unit {guard_unit}",
                    "move north",
                    "#end",
                ]
            )
            + "\n",
            encoding="utf-8",
        )
        (workdir / f"orders.{attack_fac}").write_text(
            "\n".join(
                [
                    f"#atlantis {attack_fac} attackpw",
                    f"unit {attack_unit}",
                    "move north",
                    "#end",
                ]
            )
            + "\n",
            encoding="utf-8",
        )
        result = self.run_binary(
            "run",
            "ignored-game.in",
            "admin.txt",
            "orders.txt",
            "reports.txt",
            "ignored-game.out",
            "players.txt",
            "times.txt",
            cwd=workdir,
            timeout=20,
        )
        self.assertEqual(result.returncode, 0)

        self.promote_outputs_to_next_turn_inputs(workdir)
        (workdir / f"orders.{guard_fac}").write_text(
            "\n".join(
                [
                    f"#atlantis {guard_fac} guardpw",
                    f"unit {guard_unit}",
                    "move south",
                    "#end",
                ]
            )
            + "\n",
            encoding="utf-8",
        )
        (workdir / f"orders.{attack_fac}").write_text(
            "\n".join(
                [
                    f"#atlantis {attack_fac} attackpw",
                    f"unit {attack_unit}",
                    "#end",
                ]
            )
            + "\n",
            encoding="utf-8",
        )
        result = self.run_binary(
            "run",
            "ignored-game.in",
            "admin.txt",
            "orders.txt",
            "reports.txt",
            "ignored-game.out",
            "players.txt",
            "times.txt",
            cwd=workdir,
            timeout=20,
        )
        self.assertEqual(result.returncode, 0)

        self.promote_outputs_to_next_turn_inputs(workdir)
        return guard_fac, attack_fac, guard_unit, attack_unit

    def bootstrap_object_forbid_scenario(self, workdir: Path) -> tuple[str, str, str, str]:
        self.copy_fixture_game(workdir)
        with (workdir / "players.in").open("a", encoding="utf-8") as handle:
            handle.write("Faction: new\n")
            handle.write("Name: Object Guard\n")
            handle.write("Email: objectguard@player.com\n")
            handle.write("Password: guardpw\n")
            handle.write("SendTimes: 1\n")
            handle.write("Faction: new\n")
            handle.write("Name: Object Attack\n")
            handle.write("Email: objectattack@player.com\n")
            handle.write("Password: attackpw\n")
            handle.write("SendTimes: 1\n")

        result = self.run_binary(
            "run",
            "ignored-game.in",
            "admin.txt",
            "orders.txt",
            "reports.txt",
            "ignored-game.out",
            "players.txt",
            "times.txt",
            cwd=workdir,
            timeout=20,
        )
        self.assertEqual(result.returncode, 0)

        players_out = read_text(workdir / "players.out")
        guard_fac = self.parse_faction_num(players_out, "Object Guard")
        attack_fac = self.parse_faction_num(players_out, "Object Attack")
        guard_unit = self.parse_template_unit_num(read_text(workdir / f"report.{guard_fac}"))
        attack_unit = self.parse_template_unit_num(read_text(workdir / f"report.{attack_fac}"))

        self.promote_outputs_to_next_turn_inputs(workdir)
        (workdir / f"orders.{guard_fac}").write_text(
            "\n".join(
                [
                    f"#atlantis {guard_fac} guardpw",
                    f"unit {guard_unit}",
                    "move north 1",
                    "#end",
                ]
            )
            + "\n",
            encoding="utf-8",
        )
        (workdir / f"orders.{attack_fac}").write_text(
            "\n".join(
                [
                    f"#atlantis {attack_fac} attackpw",
                    f"unit {attack_unit}",
                    "claim 200",
                    "study combat",
                    "#end",
                ]
            )
            + "\n",
            encoding="utf-8",
        )
        result = self.run_binary(
            "run",
            "ignored-game.in",
            "admin.txt",
            "orders.txt",
            "reports.txt",
            "ignored-game.out",
            "players.txt",
            "times.txt",
            cwd=workdir,
            timeout=20,
        )
        self.assertEqual(result.returncode, 0)

        self.promote_outputs_to_next_turn_inputs(workdir)
        (workdir / f"orders.{guard_fac}").write_text(
            "\n".join(
                [
                    f"#atlantis {guard_fac} guardpw",
                    f"unit {guard_unit}",
                    "#end",
                ]
            )
            + "\n",
            encoding="utf-8",
        )
        (workdir / f"orders.{attack_fac}").write_text(
            "\n".join(
                [
                    f"#atlantis {attack_fac} attackpw",
                    f"unit {attack_unit}",
                    "move north",
                    "#end",
                ]
            )
            + "\n",
            encoding="utf-8",
        )
        result = self.run_binary(
            "run",
            "ignored-game.in",
            "admin.txt",
            "orders.txt",
            "reports.txt",
            "ignored-game.out",
            "players.txt",
            "times.txt",
            cwd=workdir,
            timeout=20,
        )
        self.assertEqual(result.returncode, 0)

        self.promote_outputs_to_next_turn_inputs(workdir)
        return guard_fac, attack_fac, guard_unit, attack_unit

    def bootstrap_magic_object_battle_scenario(self, workdir: Path, attacker_turns: list[list[str]]) -> tuple[str, str, str, str]:
        self.copy_fixture_game(workdir)
        with (workdir / "players.in").open("a", encoding="utf-8") as handle:
            handle.write("Faction: new\n")
            handle.write("Name: Magic Guard\n")
            handle.write("Email: magicguard@player.com\n")
            handle.write("Password: guardpw\n")
            handle.write("SendTimes: 1\n")
            handle.write("Faction: new\n")
            handle.write("Name: Magic Attack\n")
            handle.write("Email: magicattack@player.com\n")
            handle.write("Password: attackpw\n")
            handle.write("SendTimes: 1\n")

        result = self.run_binary(
            "run",
            "ignored-game.in",
            "admin.txt",
            "orders.txt",
            "reports.txt",
            "ignored-game.out",
            "players.txt",
            "times.txt",
            cwd=workdir,
            timeout=20,
        )
        self.assertEqual(result.returncode, 0)

        players_out = read_text(workdir / "players.out")
        guard_fac = self.parse_faction_num(players_out, "Magic Guard")
        attack_fac = self.parse_faction_num(players_out, "Magic Attack")
        guard_unit = self.parse_template_unit_num(read_text(workdir / f"report.{guard_fac}"))
        attack_unit = self.parse_template_unit_num(read_text(workdir / f"report.{attack_fac}"))

        for idx, attack_lines in enumerate(attacker_turns):
            self.promote_outputs_to_next_turn_inputs(workdir)
            guard_lines = ["move north 1"] if idx == 0 else []
            (workdir / f"orders.{guard_fac}").write_text(
                "\n".join(
                    [
                        f"#atlantis {guard_fac} guardpw",
                        f"unit {guard_unit}",
                        *guard_lines,
                        "#end",
                    ]
                )
                + "\n",
                encoding="utf-8",
            )
            (workdir / f"orders.{attack_fac}").write_text(
                "\n".join(
                    [
                        f"#atlantis {attack_fac} attackpw",
                        f"unit {attack_unit}",
                        *attack_lines,
                        "#end",
                    ]
                )
                + "\n",
                encoding="utf-8",
            )
            result = self.run_binary(
                "run",
                "ignored-game.in",
                "admin.txt",
                "orders.txt",
                "reports.txt",
                "ignored-game.out",
                "players.txt",
                "times.txt",
                cwd=workdir,
                timeout=20,
            )
            self.assertEqual(result.returncode, 0)

        self.promote_outputs_to_next_turn_inputs(workdir)
        (workdir / f"orders.{guard_fac}").write_text(
            "\n".join(
                [
                    f"#atlantis {guard_fac} guardpw",
                    f"unit {guard_unit}",
                    "#end",
                ]
            )
            + "\n",
            encoding="utf-8",
        )
        (workdir / f"orders.{attack_fac}").write_text(
            "\n".join(
                [
                    f"#atlantis {attack_fac} attackpw",
                    f"unit {attack_unit}",
                    "move north",
                    "#end",
                ]
            )
            + "\n",
            encoding="utf-8",
        )
        result = self.run_binary(
            "run",
            "ignored-game.in",
            "admin.txt",
            "orders.txt",
            "reports.txt",
            "ignored-game.out",
            "players.txt",
            "times.txt",
            cwd=workdir,
            timeout=20,
        )
        self.assertEqual(result.returncode, 0)

        self.promote_outputs_to_next_turn_inputs(workdir)
        return guard_fac, attack_fac, guard_unit, attack_unit

    def bootstrap_magic_region_battle_scenario(self, workdir: Path, attacker_turns: list[list[str]]) -> tuple[str, str, str, str]:
        guard_fac, attack_fac, guard_unit, attack_unit = self.bootstrap_forbid_scenario(workdir)

        for attack_lines in attacker_turns:
            (workdir / f"orders.{guard_fac}").write_text(
                "\n".join(
                    [
                        f"#atlantis {guard_fac} guardpw",
                        f"unit {guard_unit}",
                        "#end",
                    ]
                )
                + "\n",
                encoding="utf-8",
            )
            (workdir / f"orders.{attack_fac}").write_text(
                "\n".join(
                    [
                        f"#atlantis {attack_fac} attackpw",
                        f"unit {attack_unit}",
                        *attack_lines,
                        "#end",
                    ]
                )
                + "\n",
                encoding="utf-8",
            )
            result = self.run_binary(
                "run",
                "ignored-game.in",
                "admin.txt",
                "orders.txt",
                "reports.txt",
                "ignored-game.out",
                "players.txt",
                "times.txt",
                cwd=workdir,
                timeout=20,
            )
            self.assertEqual(result.returncode, 0)
            self.promote_outputs_to_next_turn_inputs(workdir)

        return guard_fac, attack_fac, guard_unit, attack_unit

    def test_run_can_process_a_real_new_game_snapshot_with_new_player(self) -> None:
        workdir = self.make_workdir("run_e2e_")
        new_faction_num, _ = self.bootstrap_new_player(workdir, "New Player", "new@player.com")
        players_out = read_text(workdir / "players.out")
        self.assertIn("TurnNumber: 1", players_out)
        self.assertIn("GameStatus: Running", players_out)
        self.assertIn("Name: New Player (", players_out)

        report_text = read_text(workdir / f"report.{new_faction_num}")
        self.assertIn(f"New Player ({new_faction_num})", report_text)
        self.assertIn("leader [LEAD].", report_text)
        self.assertIn("Age = 1.", report_text)

    def test_second_turn_persistence_overwrites_game_and_report_outputs(self) -> None:
        workdir = self.make_workdir("run_persist_")
        faction_num, unit_num = self.bootstrap_new_player(workdir, "Persist Player", "persist@player.com")
        first_report = read_text(workdir / f"report.{faction_num}")
        self.assertIn("January, Year 1", first_report)
        self.assertIn("Age = 1.", first_report)

        self.promote_outputs_to_next_turn_inputs(workdir)
        (workdir / f"orders.{faction_num}").write_text(
            "\n".join(
                [
                    f"#atlantis {faction_num} secret",
                    f"unit {unit_num}",
                    "#end",
                ]
            )
            + "\n",
            encoding="utf-8",
        )

        result = self.run_binary(
            "run",
            "ignored-game.in",
            "admin.txt",
            "orders.txt",
            "reports.txt",
            "ignored-game.out",
            "players.txt",
            "times.txt",
            cwd=workdir,
            timeout=20,
        )
        self.assertEqual(result.returncode, 0)
        self.assertTrue((workdir / "game.out").exists())

        players_out = read_text(workdir / "players.out")
        self.assertIn("TurnNumber: 2", players_out)

        second_report = read_text(workdir / f"report.{faction_num}")
        self.assertIn("February, Year 1", second_report)
        self.assertIn("Age = 2.", second_report)
        self.assertNotEqual(first_report, second_report)

    def test_studying_force_turns_leader_into_mage_and_unlocks_magic_branch(self) -> None:
        workdir = self.make_workdir("study_force_")
        faction_num, unit_num = self.bootstrap_new_player(workdir, "Mage Player", "mage@player.com")
        self.promote_outputs_to_next_turn_inputs(workdir)

        report_text = self.run_turn_with_orders(workdir, faction_num, "secret", unit_num, ["claim 200", "study force"])
        self.assertIn("Mages: 1 (3)", report_text)
        self.assertIn(f"Unit ({unit_num}): Studies force.", report_text)
        self.assertIn("force [FORC] 1:", report_text)
        self.assertIn("Skills: force [FORC] 1 (30). Can Study: fire [FIRE],", report_text)
        self.assertIn("force shield [FSHI]", report_text)
        self.assertIn("energy shield [ESHI]", report_text)

    def test_quoted_multiword_magic_skill_names_work_in_study_and_combat(self) -> None:
        workdir = self.make_workdir("quoted_magic_skill_")
        faction_num, unit_num = self.bootstrap_new_player(workdir, "Quoted Mage", "quoted-mage@player.com")
        self.promote_outputs_to_next_turn_inputs(workdir)
        self.run_turn_with_orders(workdir, faction_num, "secret", unit_num, ["claim 200", "study force"])

        self.promote_outputs_to_next_turn_inputs(workdir)
        report_text = self.run_turn_with_orders(workdir, faction_num, "secret", unit_num, ["claim 200", 'study "force shield"'])
        self.assertIn("force shield [FSHI] 1 (30)", report_text)

        self.promote_outputs_to_next_turn_inputs(workdir)
        report_text = self.run_turn_with_orders(workdir, faction_num, "secret", unit_num, ['combat "force shield"'])
        self.assertIn("Combat spell set to force shield.", report_text)

    def test_clear_skies_cast_order_emits_runtime_event(self) -> None:
        workdir = self.make_workdir("clear_skies_cast_")
        faction_num, unit_num = self.bootstrap_new_player(workdir, "Weather Mage", "weather@player.com")
        self.promote_outputs_to_next_turn_inputs(workdir)
        self.run_turn_with_orders(workdir, faction_num, "secret", unit_num, ["claim 200", "study force"])

        self.promote_outputs_to_next_turn_inputs(workdir)
        self.run_turn_with_orders(workdir, faction_num, "secret", unit_num, ["claim 200", "study pattern"])

        self.promote_outputs_to_next_turn_inputs(workdir)
        self.run_turn_with_orders(workdir, faction_num, "secret", unit_num, ["claim 200", "study WEAT"])

        self.promote_outputs_to_next_turn_inputs(workdir)
        report_text = self.run_turn_with_orders(workdir, faction_num, "secret", unit_num, ["claim 200", "study CLEA"])
        self.assertIn("clear skies [CLEA] 1 (30)", report_text)

        self.promote_outputs_to_next_turn_inputs(workdir)
        report_text = self.run_turn_with_orders(workdir, faction_num, "secret", unit_num, ["cast CLEA"])
        self.assertIn("Casts Clear Skies.", report_text)
        self.assertNotIn("Errors during turn:", report_text)

    def test_move_from_nexus_updates_region(self) -> None:
        workdir = self.make_workdir("move_nexus_")
        faction_num, unit_num = self.bootstrap_new_player(workdir, "Move Player", "move@player.com")
        self.promote_outputs_to_next_turn_inputs(workdir)

        report_text = self.run_turn_with_orders(workdir, faction_num, "secret", unit_num, ["move north"])
        self.assertIn("Walks from nexus (0,0,nexus) in Unnamed to plain (0,12) in", report_text)
        self.assertIn("plain (0,12) in Dunkeld, contains Drense [city]", report_text)
        self.assertNotIn("nexus (0,0,nexus) in Unnamed.\n------------------------------------------------------------", report_text)

    def test_move_into_ocean_is_blocked_before_entry(self) -> None:
        workdir = self.make_workdir("move_ocean_")
        faction_num, unit_num = self.bootstrap_new_player(workdir, "Ocean Player", "ocean@player.com")
        self.promote_outputs_to_next_turn_inputs(workdir)
        self.run_turn_with_orders(workdir, faction_num, "secret", unit_num, ["move north"])

        self.promote_outputs_to_next_turn_inputs(workdir)
        report_text = self.run_turn_with_orders(workdir, faction_num, "secret", unit_num, ["move northeast"])
        self.assertIn("Discovers that ocean (1,11) in Atlantis Ocean is ocean.", report_text)
        self.assertIn("plain (0,12) in Dunkeld, contains Drense [city]", report_text)
        self.assertNotIn("ocean (1,11) in Atlantis Ocean.\n------------------------------------------------------------", report_text)

    def test_route_move_can_enter_object_by_numeric_id(self) -> None:
        workdir = self.make_workdir("move_enter_object_")
        faction_num, unit_num = self.bootstrap_new_player(workdir, "Object Player", "object@player.com")
        self.promote_outputs_to_next_turn_inputs(workdir)

        report_text = self.run_turn_with_orders(workdir, faction_num, "secret", unit_num, ["move north 1"])
        self.assertIn("Walks from nexus (0,0,nexus) in Unnamed to plain (0,12) in", report_text)
        self.assertIn("Enters Shaft [1].", report_text)
        self.assertIn("+ Shaft [1] : Shaft, contains an inner location.", report_text)
        shaft_block = report_text.split("+ Shaft [1] : Shaft, contains an inner location.", 1)[1].split("Orders Template", 1)[0]
        self.assertIn(f"* Unit ({unit_num}), Object Player ({faction_num})", shaft_block)

    def test_guard_requires_combat_ready_unit_at_runtime(self) -> None:
        workdir = self.make_workdir("guard_runtime_")
        faction_num, unit_num = self.bootstrap_new_player(workdir, "Guard Player", "guard@player.com")
        self.promote_outputs_to_next_turn_inputs(workdir)

        report_text = self.run_turn_with_orders(workdir, faction_num, "secret", unit_num, ["guard 1", "move north"])
        self.assertIn("Errors during turn:", report_text)
        self.assertIn("Must be combat ready to be on guard.", report_text)
        self.assertIn("Walks from nexus (0,0,nexus) in Unnamed to plain (0,12) in", report_text)
        city_block = report_text.split("plain (0,12) in Dunkeld", 1)[1].split("Orders Template", 1)[0]
        self.assertIn(f"* Unit ({unit_num}), Guard Player", city_block)
        self.assertNotIn(f"* Unit ({unit_num}), Guard Player ({faction_num}), on guard", city_block)

    def test_move_is_blocked_by_guard_based_forbid(self) -> None:
        workdir = self.make_workdir("forbid_move_")
        guard_fac, attack_fac, guard_unit, attack_unit = self.bootstrap_forbid_scenario(workdir)

        (workdir / f"orders.{guard_fac}").write_text(
            "\n".join(
                [
                    f"#atlantis {guard_fac} guardpw",
                    f"unit {guard_unit}",
                    f"declare {attack_fac} hostile",
                    "guard 1",
                    "#end",
                ]
            )
            + "\n",
            encoding="utf-8",
        )
        (workdir / f"orders.{attack_fac}").write_text(
            "\n".join(
                [
                    f"#atlantis {attack_fac} attackpw",
                    f"unit {attack_unit}",
                    "move south",
                    "#end",
                ]
            )
            + "\n",
            encoding="utf-8",
        )

        attack_report = self.run_turn_with_orders(workdir, attack_fac, "attackpw", attack_unit, ["move south"])
        guard_report = read_text(workdir / f"report.{guard_fac}")
        self.assertIn("Is forbidden entry to plain (0,14) in Dunkeld by Unit", attack_report)
        self.assertIn("plain (0,12) in Dunkeld, contains Drense [city]", attack_report)
        self.assertNotIn("plain (0,14) in Dunkeld, 698 peasants", attack_report)
        self.assertIn("* Unit (92), on guard, Guard Fac", guard_report)

    def test_advance_enters_guarded_region_and_triggers_battle(self) -> None:
        workdir = self.make_workdir("forbid_advance_")
        guard_fac, attack_fac, guard_unit, attack_unit = self.bootstrap_forbid_scenario(workdir)

        (workdir / f"orders.{guard_fac}").write_text(
            "\n".join(
                [
                    f"#atlantis {guard_fac} guardpw",
                    f"unit {guard_unit}",
                    f"declare {attack_fac} hostile",
                    "guard 1",
                    "#end",
                ]
            )
            + "\n",
            encoding="utf-8",
        )
        attack_report = self.run_turn_with_orders(workdir, attack_fac, "attackpw", attack_unit, ["advance south"])
        guard_report = read_text(workdir / f"report.{guard_fac}")
        self.assertIn("Battles during turn:", attack_report)
        self.assertIn(f"Unit ({attack_unit}) attacks Unit ({guard_unit}) in plain (0,14) in Dunkeld!", attack_report)
        self.assertIn("Walks from plain (0,12) in Dunkeld to plain (0,14) in", attack_report)
        self.assertIn("plain (0,14) in Dunkeld, 698 peasants", attack_report)
        self.assertIn("Attack Fac", attack_report)
        self.assertIn("your faction has been eliminated", guard_report)

    def test_region_advance_battle_reports_silver_spoils(self) -> None:
        workdir = self.make_workdir("battle_spoils_")
        guard_fac, attack_fac, guard_unit, attack_unit = self.bootstrap_forbid_scenario(workdir)

        (workdir / f"orders.{guard_fac}").write_text(
            "\n".join(
                [
                    f"#atlantis {guard_fac} guardpw",
                    f"unit {guard_unit}",
                    f"declare {attack_fac} hostile",
                    "guard 1",
                    "#end",
                ]
            )
            + "\n",
            encoding="utf-8",
        )
        attack_report = self.run_turn_with_orders(workdir, attack_fac, "attackpw", attack_unit, ["advance south"])
        battle_block = attack_report[attack_report.index("Battles during turn:"):attack_report.index("Events during turn:")]
        self.assertIn("Spoils: 65 silver [SILV].", battle_block)
        self.assertNotIn("No spoils.", battle_block)

    def test_advance_is_blocked_by_attackers_one_way_ally_attitude(self) -> None:
        workdir = self.make_workdir("forbid_ally_advance_")
        guard_fac, attack_fac, guard_unit, attack_unit = self.bootstrap_forbid_scenario(workdir)

        (workdir / f"orders.{guard_fac}").write_text(
            "\n".join(
                [
                    f"#atlantis {guard_fac} guardpw",
                    f"unit {guard_unit}",
                    f"declare {attack_fac} hostile",
                    "guard 1",
                    "#end",
                ]
            )
            + "\n",
            encoding="utf-8",
        )
        (workdir / f"orders.{attack_fac}").write_text(
            "\n".join(
                [
                    f"#atlantis {attack_fac} attackpw",
                    f"unit {attack_unit}",
                    f"declare {guard_fac} ally",
                    "advance south",
                    "#end",
                ]
            )
            + "\n",
            encoding="utf-8",
        )

        attack_report = self.run_turn_with_orders(workdir, attack_fac, "attackpw", attack_unit, [f"declare {guard_fac} ally", "advance south"])
        guard_report = read_text(workdir / f"report.{guard_fac}")
        self.assertIn("Can't ADVANCE: Dunkeld is guarded by Unit", attack_report)
        self.assertIn(f"Ally : Guard Fac ({guard_fac}).", attack_report)
        self.assertIn("plain (0,12) in Dunkeld, contains Drense [city]", attack_report)
        self.assertNotIn("plain (0,14) in Dunkeld, 698 peasants", attack_report)
        self.assertNotIn("Battles during turn:", attack_report)
        self.assertIn("* Unit (92), on guard, Guard Fac", guard_report)

    def test_move_is_refused_by_neutral_object_owner(self) -> None:
        workdir = self.make_workdir("object_forbid_move_")
        guard_fac, attack_fac, guard_unit, attack_unit = self.bootstrap_object_forbid_scenario(workdir)

        (workdir / f"orders.{guard_fac}").write_text(
            "\n".join(
                [
                    f"#atlantis {guard_fac} guardpw",
                    f"unit {guard_unit}",
                    "#end",
                ]
            )
            + "\n",
            encoding="utf-8",
        )
        attack_report = self.run_turn_with_orders(workdir, attack_fac, "attackpw", attack_unit, ["move 1"])
        self.assertIn("ENTER: Is refused entry.", attack_report)
        self.assertIn("plain (0,12) in Dunkeld, contains Drense [city]", attack_report)
        self.assertNotIn("Enters Shaft [1].", attack_report)

    def test_advance_against_neutral_object_owner_triggers_battle_before_entry(self) -> None:
        workdir = self.make_workdir("object_forbid_advance_")
        guard_fac, attack_fac, guard_unit, attack_unit = self.bootstrap_object_forbid_scenario(workdir)

        (workdir / f"orders.{guard_fac}").write_text(
            "\n".join(
                [
                    f"#atlantis {guard_fac} guardpw",
                    f"unit {guard_unit}",
                    "#end",
                ]
            )
            + "\n",
            encoding="utf-8",
        )
        attack_report = self.run_turn_with_orders(workdir, attack_fac, "attackpw", attack_unit, ["advance 1"])
        guard_report = read_text(workdir / f"report.{guard_fac}")
        self.assertIn("Battles during turn:", attack_report)
        self.assertIn(f"Unit ({attack_unit}) attacks Unit ({guard_unit}) in plain (0,12) in Dunkeld!", attack_report)
        self.assertIn("City Guard (10), behind", attack_report)
        self.assertNotIn("Enters Shaft [1].", attack_report)
        self.assertIn("your faction has been eliminated", attack_report)
        self.assertIn("your faction has been eliminated", guard_report)

    def test_object_entry_battle_reports_silver_spoils(self) -> None:
        workdir = self.make_workdir("object_battle_spoils_")
        guard_fac, attack_fac, guard_unit, attack_unit = self.bootstrap_object_forbid_scenario(workdir)

        (workdir / f"orders.{guard_fac}").write_text(
            "\n".join(
                [
                    f"#atlantis {guard_fac} guardpw",
                    f"unit {guard_unit}",
                    "#end",
                ]
            )
            + "\n",
            encoding="utf-8",
        )
        attack_report = self.run_turn_with_orders(workdir, attack_fac, "attackpw", attack_unit, ["advance 1"])
        battle_block = attack_report[attack_report.index("Battles during turn:"):attack_report.index("Events during turn:")]
        self.assertIn("Spoils: 75 silver [SILV].", battle_block)
        self.assertNotIn("No spoils.", battle_block)

    def test_city_guard_joins_object_entry_battle_but_not_region_advance_battle(self) -> None:
        region_workdir = self.make_workdir("region_battle_guard_")
        region_guard_fac, region_attack_fac, region_guard_unit, region_attack_unit = self.bootstrap_forbid_scenario(region_workdir)
        (region_workdir / f"orders.{region_guard_fac}").write_text(
            "\n".join(
                [
                    f"#atlantis {region_guard_fac} guardpw",
                    f"unit {region_guard_unit}",
                    f"declare {region_attack_fac} hostile",
                    "guard 1",
                    "#end",
                ]
            )
            + "\n",
            encoding="utf-8",
        )
        region_attack_report = self.run_turn_with_orders(region_workdir, region_attack_fac, "attackpw", region_attack_unit, ["advance south"])

        object_workdir = self.make_workdir("object_battle_guard_")
        object_guard_fac, object_attack_fac, object_guard_unit, object_attack_unit = self.bootstrap_object_forbid_scenario(object_workdir)
        (object_workdir / f"orders.{object_guard_fac}").write_text(
            "\n".join(
                [
                    f"#atlantis {object_guard_fac} guardpw",
                    f"unit {object_guard_unit}",
                    "#end",
                ]
            )
            + "\n",
            encoding="utf-8",
        )
        object_attack_report = self.run_turn_with_orders(object_workdir, object_attack_fac, "attackpw", object_attack_unit, ["advance 1"])

        self.assertNotIn("City Guard (10), behind", region_attack_report)
        self.assertIn("City Guard (10), behind", object_attack_report)

    def test_force_shield_combat_spell_is_cast_in_runtime_battle(self) -> None:
        workdir = self.make_workdir("force_shield_battle_")
        guard_fac, attack_fac, guard_unit, attack_unit = self.bootstrap_magic_object_battle_scenario(
            workdir,
            [
                ["claim 200", "study force"],
                ["claim 200", "study FSHI"],
            ],
        )

        (workdir / f"orders.{guard_fac}").write_text(
            "\n".join(
                [
                    f"#atlantis {guard_fac} guardpw",
                    f"unit {guard_unit}",
                    "#end",
                ]
            )
            + "\n",
            encoding="utf-8",
        )
        attack_report = self.run_turn_with_orders(workdir, attack_fac, "attackpw", attack_unit, ["combat FSHI", "advance 1"])
        battle_block = attack_report[attack_report.index("Battles during turn:"):attack_report.index("Events during turn:")]
        self.assertIn("Combat spell set to force shield.", attack_report)
        self.assertIn(f"Unit ({attack_unit}) casts Force Shield.", battle_block)
        self.assertIn("City Guard (10), behind", battle_block)

    def test_fire_combat_spell_emits_fireball_line_in_battle_log(self) -> None:
        workdir = self.make_workdir("fire_battle_")
        guard_fac, attack_fac, guard_unit, attack_unit = self.bootstrap_magic_object_battle_scenario(
            workdir,
            [
                ["claim 200", "study force"],
                ["claim 200", "study FIRE"],
            ],
        )

        (workdir / f"orders.{guard_fac}").write_text(
            "\n".join(
                [
                    f"#atlantis {guard_fac} guardpw",
                    f"unit {guard_unit}",
                    "#end",
                ]
            )
            + "\n",
            encoding="utf-8",
        )
        attack_report = self.run_turn_with_orders(workdir, attack_fac, "attackpw", attack_unit, ["combat FIRE", "advance 1"])
        battle_block = attack_report[attack_report.index("Battles during turn:"):attack_report.index("Events during turn:")]
        self.assertIn("Combat spell set to fire.", attack_report)
        self.assertIn("shoots a Fireball", battle_block)

    def test_clear_skies_combat_spell_is_cast_in_runtime_battle(self) -> None:
        workdir = self.make_workdir("clear_skies_battle_")
        guard_fac, attack_fac, guard_unit, attack_unit = self.bootstrap_magic_object_battle_scenario(
            workdir,
            [
                ["claim 200", "study force"],
                ["claim 200", "study pattern"],
                ["claim 200", "study WEAT"],
                ["claim 200", "study CLEA"],
            ],
        )

        (workdir / f"orders.{guard_fac}").write_text(
            "\n".join(
                [
                    f"#atlantis {guard_fac} guardpw",
                    f"unit {guard_unit}",
                    "#end",
                ]
            )
            + "\n",
            encoding="utf-8",
        )
        attack_report = self.run_turn_with_orders(workdir, attack_fac, "attackpw", attack_unit, ["combat CLEA", "advance 1"])
        battle_block = attack_report[attack_report.index("Battles during turn:"):attack_report.index("Events during turn:")]
        self.assertIn("Combat spell set to clear skies.", attack_report)
        self.assertIn(f"Unit ({attack_unit}) casts Clear Skies.", battle_block)

    def test_summon_storm_combat_spell_emits_debuff_line_in_battle_log(self) -> None:
        workdir = self.make_workdir("summon_storm_battle_")
        guard_fac, attack_fac, guard_unit, attack_unit = self.bootstrap_magic_region_battle_scenario(
            workdir,
            [
                ["claim 200", "study force"],
                ["claim 200", "study pattern"],
                ["claim 200", "study WEAT"],
                ["claim 200", "study SSTO"],
            ],
        )

        (workdir / f"orders.{guard_fac}").write_text(
            "\n".join(
                [
                    f"#atlantis {guard_fac} guardpw",
                    f"unit {guard_unit}",
                    f"declare {attack_fac} hostile",
                    "guard 1",
                    "#end",
                ]
            )
            + "\n",
            encoding="utf-8",
        )
        attack_report = self.run_turn_with_orders(workdir, attack_fac, "attackpw", attack_unit, ["combat SSTO", "advance south"])
        battle_block = attack_report[attack_report.index("Battles during turn:"):attack_report.index("Events during turn:")]
        self.assertIn("Combat spell set to summon storm.", attack_report)
        self.assertIn("summons a terrible storm", battle_block)
        self.assertIn("reducing the effectiveness of", battle_block)

if __name__ == "__main__":
    unittest.main()
