import unittest
from marllib import marl
from marllib.envs.base_env.mpe import REGISTRY as MPE_REGISTRY

'''
MAPPO test case
available scenario train 
one per iteration
'''

ENV = 'mpe'

class TestMPEEnv(unittest.TestCase):

    def test_mpe_scenarios_from_marllib_api(self):
        mappo = marl.algos.mappo(hyperparam_source=ENV)
        for scenario in MPE_REGISTRY.keys():
            print(scenario)
            env = marl.make_env(environment_name=ENV, map_name=scenario)
            model = marl.build_model(env, mappo, {"core_arch": "mlp", "encode_layer": "256-256"})
            mappo.fit(env, model, stop={'training_iteration': 5}, local_mode=True, num_gpus=1,
                      num_workers=1, share_policy='group', checkpoint_end=False)


if __name__ == "__main__":
    import pytest
    import sys

    sys.exit(pytest.main(["-v", __file__]))