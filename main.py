from service.mission_service import *

if __name__ == '__main__':
    all_missions = create_all_missions()
    all_missions_sorted = sorted(all_missions, key=lambda m: m.mission_fit_score)
    final_missions = reduce(
        lambda l, n:
        l + [n] if n.assigned_aircraft not in map(lambda m: m.assigned_aircraft, l)
                   and n.target_city not in map(lambda m: m.target_city, l)
                   and n.assigned_pilot not in map(lambda m: m.assigned_pilot, l)
        else l, all_missions_sorted[::-1], [])
    write_missions_to_csv(final_missions, 'csvs/missions.csv')
    print(final_missions)