from core.libxx import Analysis, Graph

if __name__ == '__main__':
    thread_hold = 10000
    name = f"usdt-net-thread{thread_hold}"
    Analysis().handle_history()
    Graph().graph_building_bsc_analysis_read(
        project_name=name,
        scope=thread_hold
    )
