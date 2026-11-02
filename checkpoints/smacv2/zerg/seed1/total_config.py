exp_config = {
    'env': {
        'manager': {
            'episode_num': float("inf"),
            'max_retry': 5,
            'step_timeout': None,
            'auto_reset': True,
            'reset_timeout': 6000,
            'retry_type': 'renew',
            'retry_waiting_time': 0.1,
            'shared_memory': False,
            'copy_on_get': True,
            'context': 'fork',
            'wait_num': float("inf"),
            'step_wait_timeout': None,
            'connect_timeout': 60,
            'reset_inplace': False,
            'cfg_type': 'SyncSubprocessEnvManagerDict',
            'type': 'subprocess'
        },
        'stop_value': 10000000000,
        'n_evaluator_episode': 32,
        'type': 'smac2',
        'import_names': ['dizoo.smac2.envs.smac2'],
        'map_name': '10gen_zerg',
        'difficulty': '7',
        'agent_num': 10,
        'collector_env_num': 8,
        'evaluator_env_num': 8,
        'obs_alone': False,
        'obs_last_action': True
    },
    'policy': {
        'model': {
            'agent_num': 10,
            'obs_shape': 304,
            'global_obs_shape': 290,
            'action_shape': 16,
            'self_feature_range': [300, 304],
            'ally_feature_range': [84, 300],
            'hidden_size_list': [64],
            'attention_size': 32,
            'mixer': True,
            'lstm_type': 'gru',
            'dueling': True
        },
        'learn': {
            'learner': {
                'train_iterations': 1000000000,
                'dataloader': {
                    'num_workers': 0
                },
                'log_policy': True,
                'hook': {
                    'load_ckpt_before_run': '',
                    'log_show_after_iter': 100,
                    'save_ckpt_after_iter': 999999999,
                    'save_ckpt_after_run': True
                },
                'cfg_type': 'BaseLearnerDict'
            },
            'resume_training': False,
            'update_per_collect': 20,
            'batch_size': 32,
            'learning_rate': 0.0005,
            'clip_value': 5,
            'target_update_theta': 0.01,
            'discount_factor': 0.99,
            'double_q': True,
            'lambda_delta_q': 1.0,
            'episode_buffer': True
        },
        'collect': {
            'collector': {
                'deepcopy_obs': False,
                'transform_obs': False,
                'collect_print_freq': 100,
                'get_train_sample': True,
                'reward_shaping': False,
                'cfg_type': 'EpisodeSerialCollectorDict',
                'type': 'episode'
            },
            'unroll_len': 10,
            'n_episode': 32,
            'env_num': 8
        },
        'eval': {
            'evaluator': {
                'eval_freq': 50000,
                'render': {
                    'render_freq': -1,
                    'mode': 'train_iter'
                },
                'figure_path': None,
                'cfg_type': 'InteractionSerialEvaluatorDict',
                'eval_mode': 'envstep',
                'stop_value': 10000000000,
                'n_episode': 32
            },
            'env_num': 8
        },
        'other': {
            'replay_buffer': {
                'type': 'naive',
                'replay_buffer_size': 15000,
                'deepcopy': False,
                'enable_track_used_data': False,
                'periodic_thruput_seconds': 60,
                'cfg_type': 'NaiveReplayBufferDict'
            },
            'eps': {
                'type': 'linear',
                'start': 1.0,
                'end': 0.05,
                'decay': 50000
            },
            'commander': {
                'cfg_type': 'BaseSerialCommanderDict'
            }
        },
        'on_policy': False,
        'cuda': False,
        'multi_gpu': False,
        'bp_update_sync': True,
        'traj_len_inf': False,
        'type': 'caqmix_command',
        'priority': False,
        'priority_IS_weight': False,
        'cfg_type': 'CAQMIXCommandModePolicyDict',
        'multi_agent': True
    },
    'exp_name': 'SMAC2_zerg_caqmix_seed1',
    'seed': 1
}
