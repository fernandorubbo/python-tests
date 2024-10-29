import unittest
from hpa_rec_memory_max import *

class TestGetMemoryRequest(unittest.TestCase):

    def test_same_replicas_count(self):
        workload = {'avg_replicas': 10, 'max_avg_memory' : 40}
        proposed_replicas = 10 
        self.assertEqual(get_memory_request(workload), 48)
        self.assertEqual(get_memory_request(workload, proposed_replicas), 48)

    def test_decrease_replicas_count(self):
        workload = {'avg_replicas': 10, 'max_avg_memory' : 40}
        proposed_replicas = 9 
        self.assertEqual(get_memory_request(workload, proposed_replicas), 53.333)
        workload = {'avg_replicas': 23, 'max_avg_memory' : 40}
        proposed_replicas = 22 
        self.assertEqual(get_memory_request(workload, proposed_replicas), 50.182)
        workload = {'avg_replicas': 23, 'max_avg_memory' : 40}
        proposed_replicas = 10 
        self.assertEqual(get_memory_request(workload, proposed_replicas), 110.4)

    def test_decrease_replicas_count_below_2(self):
        workload = {'avg_replicas': 10, 'max_avg_memory' : 40}
        proposed_replicas = 2 
        self.assertEqual(get_memory_request(workload, proposed_replicas), 240)
        workload = {'avg_replicas': 10, 'max_avg_memory' : 40}
        proposed_replicas = 1 
        self.assertEqual(get_memory_request(workload, proposed_replicas), 240)
        workload = {'avg_replicas': 10, 'max_avg_memory' : 40}
        proposed_replicas = 0 
        self.assertEqual(get_memory_request(workload, proposed_replicas), 240)        

    def test_increase_replica_count(self):
        workload = {'avg_replicas': 10, 'max_avg_memory' : 40}
        proposed_replicas = 11 
        self.assertEqual(get_memory_request(workload, proposed_replicas), 43.636)
        workload = {'avg_replicas': 10, 'max_avg_memory' : 40}
        proposed_replicas = 20 
        self.assertEqual(get_memory_request(workload, proposed_replicas), 24)
        workload = {'avg_replicas': 10, 'max_avg_memory' : 40}
        proposed_replicas = 30 
        self.assertEqual(get_memory_request(workload, proposed_replicas), 16)

    def test_algo_original_dcr(self):
        workload = {'avg_replicas': 10, 'max_avg_memory' : 40}
        self.assertEqual(algo_original_dcr(workload), {'min_replicas': 10, 'memory_request': 48})

    def test_algo_that_changes_replicas_count(self):
        workload = {'avg_replicas': 10, 'max_avg_memory' : 40}
        # TOFIX
        self.assertEqual(algo_that_changes_replicas_count(workload, 5), {'min_replicas': 5, 'memory_request': 96})



if __name__ == '__main__':
    unittest.main()