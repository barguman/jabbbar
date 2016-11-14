from zabbbana.teams import Team
from . import jordan

DEFAULT_TEAM_ID = "Creativedash"
test_team = Team(jordan, DEFAULT_TEAM_ID)


def test_list_players():
    # List all the players who are part of the instanciated team
    response        = test_team.list_players()
    assert isinstance(response, list)

    # List all the players who are part of another team
    response        = test_team.list_players(team_id="ueno")
    assert isinstance(response, list)


def test_list_shots():
    # List all the shots published by the instanciated team
    response        = test_team.list_shots()
    assert isinstance(response, list)

    # List all the shots published by another team
    response        = test_team.list_shots(team_id="ueno")
    assert isinstance(response, list)