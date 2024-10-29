import math

workload = { 
    'avg_replicas': 10,
    'max_memory' : 40
}



def get_memory_request(workload, proposed_replicas=None):
    replicas = workload['avg_replicas']
    max_memory_plus_buffer = workload['max_avg_memory'] * 1.2
    total_memory_capacity = max_memory_plus_buffer * replicas
    proposed_replicas = replicas if proposed_replicas is None else proposed_replicas
    proposed_replicas = max(proposed_replicas, 2)
    return round(total_memory_capacity/proposed_replicas, 3)


def algo_original_dcr(workload):
    recommendation = {
        'min_replicas' : workload['avg_replicas'],
        'memory_request': get_memory_request(workload)
    }
    return recommendation

def algo_that_changes_replicas_count(workload, min_replicas):    
    min_replicas = min_replicas  # TOFIX: simulate computing min replicas
    recommendation = {
        'min_replicas' : min_replicas,
        'memory_request': get_memory_request(workload, min_replicas)
    }
    return recommendation
