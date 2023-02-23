from backend.config import Config 

def test_defaut_config_has_t_running():
    config = Config()
    assert (config["runtime"]["t_running"] > 0) 

def test_defaut_config_has_t_between_sessions():
    config = Config()
    assert (config["runtime"]["t_between_sessions"] > 0)